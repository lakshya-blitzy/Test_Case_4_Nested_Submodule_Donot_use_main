#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Custom :class:`unittest.TestResult` reporter for the Python Koans runner.

Defines :class:`Sensei`, the result object that renders colored, tutorial-style
feedback to the terminal as the koans (test cases) are run. Importing this
module initializes the vendored ``libs.colorama`` package so that ANSI color
codes work across platforms; the ``init()`` call executes at import time.

Source: runner/sensei.py:14-15
"""

import unittest
import re
import sys
import os
import glob

from . import helper
from .mockable_test_result import MockableTestResult
from runner import path_to_enlightenment

from libs.colorama import init, Fore, Style
init() # init colorama

class Sensei(MockableTestResult):
    """Colored, progress-tracking reporter used while a koan ``TestSuite`` runs.

    ``Sensei`` is a :class:`MockableTestResult` subclass (which itself subclasses
    :class:`unittest.TestResult`), so it acts as the result object plugged into
    the standard ``unittest`` machinery. As tests execute it prints a
    ``"Thinking <ClassName>"`` heading once per lesson, records and announces
    successes only while the current lesson is still passing, and funnels errors
    into the failure list (see :meth:`addError`) so that errors and failures form
    a single, correctly ordered sequence. When the run finishes, :meth:`learn`
    prints the progress summary, the remaining work, and a closing Zen message.

    Progress is tracked with two counters: ``pass_count`` (individual koans
    passed) and ``lesson_pass_count`` (lessons started/passed). Consistent with
    ``README.rst``, a run that still has failures ends with ``sys.exit(-1)``.
    """

    def __init__(self, stream):
        """Initialize the reporter and eagerly load the full koan suite.

        Sets up base :class:`unittest.TestResult` state, stores the output
        ``stream``, resets the previous-class tracker, and loads every koan into
        ``self.tests`` via :func:`path_to_enlightenment.koans`. The progress
        counters and the lazy lesson-file cache start empty.

        :param stream: Output stream (a ``WritelnDecorator``) that the reporter
            writes all tutorial feedback to.
        """
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.prevTestClassName = None
        self.tests = path_to_enlightenment.koans()
        self.pass_count = 0
        self.lesson_pass_count  = 0
        self.all_lessons = None

    def startTest(self, test):
        """Announce a new lesson before its first test runs.

        Runs before each test. When the test's class name (obtained via
        :func:`helper.cls_name`) differs from the previously seen class *and*
        no failures have occurred yet, prints a blank line followed by a
        ``"Thinking <ClassName>"`` heading. The lesson tally
        (``lesson_pass_count``) is then incremented unless the class is
        ``AboutAsserts`` or ``AboutExtraCredit``, which are excluded from the
        count.

        Source: runner/sensei.py:30-37
        """
        MockableTestResult.startTest(self, test)

        if helper.cls_name(test) != self.prevTestClassName:
            self.prevTestClassName = helper.cls_name(test)
            if not self.failures:
                self.stream.writeln()
                self.stream.writeln("{0}{1}Thinking {2}".format(
                    Fore.RESET, Style.NORMAL, helper.cls_name(test)))
                if helper.cls_name(test) not in ['AboutAsserts', 'AboutExtraCredit']:
                    self.lesson_pass_count += 1

    def addSuccess(self, test):
        """Record and announce a passing koan.

        Acts only while :meth:`passesCount` is true (the current lesson has not
        already failed): registers the success with the base class, prints a
        green ``"<testMethodName> has expanded your awareness."`` line, and
        increments ``pass_count``.

        Source: runner/sensei.py:39-46
        """
        if self.passesCount():
            MockableTestResult.addSuccess(self, test)
            self.stream.writeln( \
                "  {0}{1}{2} has expanded your awareness.{3}{4}" \
                .format(Fore.GREEN, Style.BRIGHT, test._testMethodName, \
                Fore.RESET, Style.NORMAL))
            self.pass_count += 1

    def addError(self, test, err):
        """Handle an errored test by recording it as a failure.

        Delegates to :meth:`addFailure` so that errors and failures share one
        ordered sequence; keeping two separate lists would disrupt the error
        ordering (see the comment below).
        """
        # Having 1 list for errors and 1 list for failures would mess with
        # the error sequence
        self.addFailure(test, err)

    def passesCount(self):
        """Return whether a subsequent success should still be counted.

        Returns ``True`` unless at least one failure exists whose first failing
        class differs from ``prevTestClassName``. In effect, once a lesson has
        failed, later passes belonging to a different class are no longer
        counted.

        Source: runner/sensei.py:53-54
        """
        return not (self.failures and helper.cls_name(self.failures[0][0]) != self.prevTestClassName)

    def addFailure(self, test, err):
        """Record a failure using the base ``unittest`` bookkeeping.

        Delegates to :meth:`MockableTestResult.addFailure`.
        """
        MockableTestResult.addFailure(self, test, err)

    def sortFailures(self, testClassName):
        r"""Return this class's failures ordered by source line number.

        Scans ``self.failures`` for entries whose class name equals
        ``testClassName``, extracts the numeric source line from each traceback
        via the ``(?<= line )\d+`` regex, and builds ``(lineno, test, err)``
        tuples. Returns them sorted ascending by line number, or ``None`` when
        no failure matches or none exposes a numeric line.

        :param testClassName: Class name whose failures should be collected.
        Source: runner/sensei.py:59-71
        """
        table = list()
        for test, err in self.failures:
            if helper.cls_name(test) ==  testClassName:
                m = re.search("(?<= line )\d+" ,err)
                if m:
                    tup = (int(m.group(0)), test, err)
                    table.append(tup)

        if table:
            return sorted(table)
        else:
            return None

    def firstFailure(self):
        """Return the earliest-line failure of the first failing class.

        Returns the ``(test, err)`` pair for the lowest-line-number failure of
        the class of ``self.failures[0]`` (via :meth:`sortFailures`), or
        ``None`` when there are no failures.

        Source: runner/sensei.py:73-81
        """
        if not self.failures: return None

        table = self.sortFailures(helper.cls_name(self.failures[0][0]))

        if table:
            return (table[0][1], table[0][2])
        else:
            return None

    def learn(self):
        """Print the end-of-run report and finish the session.

        Emits the error report (:meth:`errorReport`), two blank lines, the
        progress summary (:meth:`report_progress`), the remaining work
        (:meth:`report_remaining`, only when failures exist), a blank line, and
        a Zen message (:meth:`say_something_zenlike`).

        .. important::
            If any failures remain this calls ``sys.exit(-1)``, terminating the
            process. Only on a completely clean run does it fall through to
            print the magenta ``"That was the last one, well done!"`` banner and
            the pointer to ``about_extra_credit.py``.

        Source: runner/sensei.py:83-102
        """
        self.errorReport()

        self.stream.writeln("")
        self.stream.writeln("")
        self.stream.writeln(self.report_progress())
        if self.failures:
          self.stream.writeln(self.report_remaining())
        self.stream.writeln("")
        self.stream.writeln(self.say_something_zenlike())

        if self.failures: sys.exit(-1)
        self.stream.writeln(
            "\n{0}**************************************************" \
            .format(Fore.RESET))
        self.stream.writeln("\n{0}That was the last one, well done!" \
            .format(Fore.MAGENTA))
        self.stream.writeln(
            "\nIf you want more, take a look at about_extra_credit.py{0}{1}" \
            .format(Fore.RESET, Style.NORMAL))

    def errorReport(self):
        """Print the detailed report for the first outstanding failure.

        When :meth:`firstFailure` returns a problem, prints the red
        ``"<testMethodName> has damaged your karma."`` line, the
        ``"You have not yet reached enlightenment ..."`` message, the scraped
        assertion error (:meth:`scrapeAssertionError`), and a
        ``"Please meditate on the following code:"`` section containing the
        scraped stack dump (:meth:`scrapeInterestingStackDump`). Returns
        immediately (printing nothing) when there is no failure.

        Source: runner/sensei.py:104-119
        """
        problem = self.firstFailure()
        if not problem: return
        test, err = problem
        self.stream.writeln("  {0}{1}{2} has damaged your "
          "karma.".format(Fore.RED, Style.BRIGHT, test._testMethodName))

        self.stream.writeln("\n{0}{1}You have not yet reached enlightenment ..." \
            .format(Fore.RESET, Style.NORMAL))
        self.stream.writeln("{0}{1}{2}".format(Fore.RED, \
            Style.BRIGHT, self.scrapeAssertionError(err)))
        self.stream.writeln("")
        self.stream.writeln("{0}{1}Please meditate on the following code:" \
            .format(Fore.RESET, Style.NORMAL))
        self.stream.writeln("{0}{1}{2}{3}{4}".format(Fore.YELLOW, Style.BRIGHT, \
            self.scrapeInterestingStackDump(err), Fore.RESET, Style.NORMAL))

    def scrapeAssertionError(self, err):
        """Extract the human-readable assertion message from a traceback.

        Returns ``""`` when ``err`` is falsy. Otherwise walks the traceback
        text and returns the cleaned assertion message: the lines following the
        first unindented header line, each stripped and re-indented by two
        spaces.

        :param err: Formatted traceback text (or ``None``).
        :returns: The cleaned assertion message, or ``""``.
        Source: runner/sensei.py:121-133
        """
        if not err: return ""

        error_text = ""
        count = 0
        for line in err.splitlines():
            m = re.search("^[^^ ].*$",line)
            if m and m.group(0):
                count+=1

            if count>1:
                error_text += ("  " + line.strip()).rstrip() + '\n'
        return error_text.strip('\n')

    def scrapeInterestingStackDump(self, err):
        r"""Return a focused, colorized excerpt of a koan traceback.

        Returns ``""`` when ``err`` is falsy. Otherwise keeps only
        ``"File ..."`` lines together with their indented source lines, filters
        to frames whose path contains ``koans``, then colorizes ``about_*.py``
        file names and ``line N`` references for display.

        :param err: Formatted traceback text (or ``None``).
        :returns: The focused, colorized traceback excerpt, or ``""``.
        Source: runner/sensei.py:135-167
        """
        if not err:
            return ""

        lines = err.splitlines()

        sep = '@@@@@SEP@@@@@'

        stack_text = ""
        for line in lines:
            m = re.search("^  File .*$",line)
            if m and m.group(0):
                stack_text += '\n' + line

            m = re.search("^    \w(\w)+.*$",line)
            if m and m.group(0):
                stack_text += sep + line

        lines = stack_text.splitlines()

        stack_text = ""
        for line in lines:
            m = re.search("^.*[/\\\\]koans[/\\\\].*$",line)
            if m and m.group(0):
                stack_text += line + '\n'


        stack_text = stack_text.replace(sep, '\n').strip('\n')
        stack_text = re.sub(r'(about_\w+.py)',
                r"{0}\1{1}".format(Fore.BLUE, Fore.YELLOW), stack_text)
        stack_text = re.sub(r'(line \d+)',
                r"{0}\1{1}".format(Fore.BLUE, Fore.YELLOW), stack_text)
        return stack_text

    def report_progress(self):
        """Return the one-line progress summary.

        Formats ``"You have completed {pass_count} ({percent} %) koans and
        {lesson_pass_count} (out of {total_lessons}) lessons."`` where
        ``percent`` is ``pass_count * 100 // total_koans()``.

        Source: runner/sensei.py:169-175
        """
        return "You have completed {0} ({2} %) koans and " \
                "{1} (out of {3}) lessons.".format(
                self.pass_count,
                self.lesson_pass_count,
                self.pass_count*100//self.total_koans(),
                self.total_lessons())

    def report_remaining(self):
        """Return the one-line "work remaining" summary.

        Formats ``"You are now {koans_remaining} koans and {lessons_remaining}
        lessons away from reaching enlightenment."`` where the remaining values
        are the totals minus the current ``pass_count`` and
        ``lesson_pass_count``.

        Source: runner/sensei.py:177-184
        """
        koans_remaining = self.total_koans() - self.pass_count
        lessons_remaining = self.total_lessons() - self.lesson_pass_count

        return "You are now {0} koans and {1} lessons away from " \
            "reaching enlightenment.".format(
                koans_remaining,
                lessons_remaining)

    # Hat's tip to Tim Peters for the zen statements from The 'Zen
    # of Python' (http://www.python.org/dev/peps/pep-0020/)
    #
    # Also a hat's tip to Ara T. Howard for the zen statements from his
    # metakoans Ruby Quiz (http://rubyquiz.com/quiz67.html) and
    # Edgecase's later permutation in the Ruby Koans
    def say_something_zenlike(self):
        """Return a cyan-colored Zen message describing the run's state.

        When failures exist, returns one of 37 rotating "Zen of Python"
        statements selected by ``pass_count % 37``. When there are no failures,
        returns the ``"Nobody ever expects the Spanish Inquisition."`` line
        instead. The statements are attributed to Tim Peters' Zen of Python and
        Ara T. Howard's metakoans (see the comment above this method); the final
        ``"The temple is collapsing! Run!!!"`` return is an intentionally
        unreachable safeguard.

        Source: runner/sensei.py:192-249
        """
        if self.failures:
            turn = self.pass_count % 37

            zenness = "";
            if turn == 0:
                zenness = "Beautiful is better than ugly."
            elif turn == 1 or turn == 2:
                zenness = "Explicit is better than implicit."
            elif turn == 3 or turn == 4:
                zenness = "Simple is better than complex."
            elif turn == 5 or turn == 6:
                zenness = "Complex is better than complicated."
            elif turn == 7 or turn == 8:
                zenness = "Flat is better than nested."
            elif turn == 9 or turn == 10:
                zenness = "Sparse is better than dense."
            elif turn == 11 or turn == 12:
                zenness = "Readability counts."
            elif turn == 13 or turn == 14:
                zenness = "Special cases aren't special enough to " \
                          "break the rules."
            elif turn == 15 or turn == 16:
                zenness = "Although practicality beats purity."
            elif turn == 17 or turn == 18:
                zenness = "Errors should never pass silently."
            elif turn == 19 or turn == 20:
                zenness = "Unless explicitly silenced."
            elif turn == 21 or turn == 22:
                zenness = "In the face of ambiguity, refuse the " \
                          "temptation to guess."
            elif turn == 23 or turn == 24:
                zenness = "There should be one-- and preferably only " \
                          "one --obvious way to do it."
            elif turn == 25 or turn == 26:
                zenness = "Although that way may not be obvious at " \
                          "first unless you're Dutch."
            elif turn == 27 or turn == 28:
                zenness = "Now is better than never."
            elif turn == 29 or turn == 30:
                zenness = "Although never is often better than right " \
                          "now."
            elif turn == 31 or turn == 32:
                zenness = "If the implementation is hard to explain, " \
                          "it's a bad idea."
            elif turn == 33 or turn == 34:
                zenness = "If the implementation is easy to explain, " \
                          "it may be a good idea."
            else:
                zenness = "Namespaces are one honking great idea -- " \
                          "let's do more of those!"
            return "{0}{1}{2}{3}".format(Fore.CYAN, zenness, Fore.RESET, Style.NORMAL);
        else:
            return "{0}Nobody ever expects the Spanish Inquisition." \
                .format(Fore.CYAN)

        # Hopefully this will never ever happen!
        return "The temple is collapsing! Run!!!"

    def total_lessons(self):
        """Return the number of lesson files, or ``0`` when none are found.

        Delegates discovery to :meth:`filter_all_lessons`.

        Source: runner/sensei.py:251-256
        """
        all_lessons = self.filter_all_lessons()
        if all_lessons:
          return len(all_lessons)
        else:
          return 0

    def total_koans(self):
        """Return the total number of koan test cases in the loaded suite.

        Equivalent to ``self.tests.countTestCases()``.

        Source: runner/sensei.py:258-259
        """
        return self.tests.countTestCases()

    def filter_all_lessons(self):
        """Lazily discover and cache the lesson files.

        Globs ``about*.py`` in the sibling ``../koans/`` directory (resolved
        relative to this file), excluding ``about_extra_credit``. The result is
        cached in ``self.all_lessons`` and returned on subsequent calls.

        Source: runner/sensei.py:261-269
        """
        cur_dir = os.path.split(os.path.realpath(__file__))[0]
        if not self.all_lessons:
            self.all_lessons = glob.glob('{0}/../koans/about*.py'.format(cur_dir))
            self.all_lessons = list(filter(lambda filename:
                                      "about_extra_credit" not in filename,
                                      self.all_lessons))

        return self.all_lessons
