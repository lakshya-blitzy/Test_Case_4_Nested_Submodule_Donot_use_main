#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    """Stateful, lesson-aware ``unittest`` result renderer for the koans.

    ``Sensei`` is the runner's reporting engine. It extends
    ``MockableTestResult`` (a thin ``unittest.TestResult`` subclass) but calls
    ``unittest.TestResult.__init__`` directly, and overrides the result
    lifecycle to print colored, koan-styled progress to a wrapped stream using
    ``libs.colorama``. It tracks how many koans (``pass_count``) and lessons
    (``lesson_pass_count``) the learner has completed, loads the full koan
    suite via ``path_to_enlightenment.koans()``, and — on the first failure —
    stops the learner at the koan that "damaged their karma," printing a Zen
    aphorism to meditate on.

    Attributes:
        stream: The (``WritelnDecorator``-wrapped) output stream.
        prevTestClassName (str|None): Name of the most recently seen test class,
            used to detect lesson transitions.
        tests: The loaded ``unittest.TestSuite`` of all koans.
        pass_count (int): Number of individual koans passed so far.
        lesson_pass_count (int): Number of lessons (koan classes) entered/passed.
        all_lessons (list|None): Lazily-populated cache of discovered lesson files.

    Source: runner/sensei.py:L17-L269
    """

    def __init__(self, stream):
        """Initialize the result renderer.

        Calls ``unittest.TestResult.__init__``, stores the output ``stream``,
        resets ``prevTestClassName``, loads the koan suite via
        ``path_to_enlightenment.koans()``, and zeroes ``pass_count`` /
        ``lesson_pass_count`` (``all_lessons`` starts unset).

        Args:
            stream: The output stream to write colored progress to.

        Source: runner/sensei.py:L18
        """
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.prevTestClassName = None
        self.tests = path_to_enlightenment.koans()
        self.pass_count = 0
        self.lesson_pass_count  = 0
        self.all_lessons = None

    def startTest(self, test):
        """Hook run before each test to announce lesson transitions.

        Delegates to ``MockableTestResult.startTest``; when the test's class
        name (via ``helper.cls_name``) differs from the previous one and there
        are no failures yet, prints a blank line and a colored
        ``Thinking <ClassName>`` banner and increments ``lesson_pass_count``
        (except for the ``AboutAsserts`` and ``AboutExtraCredit`` classes).

        Args:
            test: The test about to run.

        Side effects:
            Colored terminal output; mutates ``prevTestClassName`` and
            ``lesson_pass_count``.

        Source: runner/sensei.py:L27
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
        """Record a passing koan when passes are currently allowed.

        When ``passesCount()`` is true, delegates to
        ``MockableTestResult.addSuccess``, prints a bright-green
        ``<method> has expanded your awareness.`` line, and increments
        ``pass_count``.

        Args:
            test: The test that passed.

        Source: runner/sensei.py:L39
        """
        if self.passesCount():
            MockableTestResult.addSuccess(self, test)
            self.stream.writeln( \
                "  {0}{1}{2} has expanded your awareness.{3}{4}" \
                .format(Fore.GREEN, Style.BRIGHT, test._testMethodName, \
                Fore.RESET, Style.NORMAL))
            self.pass_count += 1

    def addError(self, test, err):
        """Treat errors identically to failures by forwarding to ``addFailure``.

        Args:
            test: The failing test.
            err: The ``sys.exc_info()``-style error tuple/string.

        Source: runner/sensei.py:L48
        """
        # Having 1 list for errors and 1 list for failures would mess with
        # the error sequence
        self.addFailure(test, err)

    def passesCount(self):
        """Report whether successes should still be counted.

        Returns:
            bool: ``True`` while passes should still be counted; ``False`` once
            a failure exists whose originating class differs from
            ``prevTestClassName`` (i.e., the learner has moved past the koan
            that broke).

        Source: runner/sensei.py:L53
        """
        return not (self.failures and helper.cls_name(self.failures[0][0]) != self.prevTestClassName)

    def addFailure(self, test, err):
        """Record a failing koan by delegating to ``MockableTestResult.addFailure``.

        Args:
            test: The failing test.
            err: The error info.

        Source: runner/sensei.py:L56
        """
        MockableTestResult.addFailure(self, test, err)

    def sortFailures(self, testClassName):
        """Collect and order the failures for a given test class.

        Gathers failures belonging to ``testClassName`` as
        ``(line_number, test, err)`` tuples (the line number is parsed from the
        traceback via the ``(?<= line )\\d+`` regex) and returns them sorted
        ascending by line number.

        Args:
            testClassName (str): The class name whose failures to collect.

        Returns:
            list[tuple] | None: The sorted ``(line_number, test, err)`` tuples,
            or ``None`` if none match.

        Source: runner/sensei.py:L59
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
        """Return the earliest failure for the first failing class.

        Returns:
            tuple | None: The ``(test, err)`` pair with the lowest source line
            for the first failing class, or ``None`` when there are no failures.

        Source: runner/sensei.py:L73
        """
        if not self.failures: return None

        table = self.sortFailures(helper.cls_name(self.failures[0][0]))

        if table:
            return (table[0][1], table[0][2])
        else:
            return None

    def learn(self):
        """Render the end-of-run report and terminate the walk.

        Emits the first-failure error report, the progress line, the
        remaining-work line (only when failures exist), and a Zen aphorism.
        Exits the process with ``sys.exit(-1)`` when any failure exists;
        otherwise prints the completion/congratulations banner.

        Side effects:
            Writes to the stream; may terminate the process via ``sys.exit``.

        Source: runner/sensei.py:L83
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
        """Print the detailed report for the first failure.

        Prints a red ``<method> has damaged your karma.`` line, the
        ``not yet reached enlightenment`` message, the scraped assertion error,
        and a ``meditate on the following code:`` block containing the scraped
        stack dump. Returns early (no output) if there is no failure.

        Source: runner/sensei.py:L104
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
        """Extract the human-readable assertion-failure message.

        Skips the first matching header line of the traceback string, then
        indents and trims the subsequent lines.

        Args:
            err (str): The traceback/error string to scrape.

        Returns:
            str: The cleaned assertion message (``''`` when ``err`` is falsy).

        Source: runner/sensei.py:L121
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
        """Extract and colorize the koans-relevant frames of a traceback.

        Keeps only the koans-relevant stack frames, colorizes ``about_*.py``
        filenames and ``line N`` references, and returns the formatted,
        koan-filtered stack text.

        Args:
            err (str): The traceback/error string to scrape.

        Returns:
            str: The formatted stack text (``''`` when ``err`` is falsy).

        Source: runner/sensei.py:L135
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
        """Summarize how far the learner has progressed.

        Returns:
            str: A summary reporting completed koans, percent complete
            (``pass_count * 100 // total_koans()``), and lessons completed out
            of ``total_lessons()``.

        Source: runner/sensei.py:L169
        """
        return "You have completed {0} ({2} %) koans and " \
                "{1} (out of {3}) lessons.".format(
                self.pass_count,
                self.lesson_pass_count,
                self.pass_count*100//self.total_koans(),
                self.total_lessons())

    def report_remaining(self):
        """Describe how much work remains before enlightenment.

        Returns:
            str: A message stating how many koans and lessons remain (totals
            minus the current counts).

        Source: runner/sensei.py:L177
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
        """Return a Zen aphorism appropriate to the current progress.

        When failures exist, chooses a line from the Zen of Python keyed by
        ``pass_count % 37`` (cyan-colored); when none exist, returns the
        celebratory ``Nobody ever expects the Spanish Inquisition.`` line.

        Returns:
            str: The selected Zen aphorism.

        Source: runner/sensei.py:L192
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
        """Count the discoverable lessons.

        Returns:
            int: ``len(filter_all_lessons())``, or ``0`` when none are found.

        Source: runner/sensei.py:L251
        """
        all_lessons = self.filter_all_lessons()
        if all_lessons:
          return len(all_lessons)
        else:
          return 0

    def total_koans(self):
        """Count the total number of koan test cases.

        Returns:
            int: ``self.tests.countTestCases()``.

        Source: runner/sensei.py:L258
        """
        return self.tests.countTestCases()

    def filter_all_lessons(self):
        """Lazily discover and cache the lesson files.

        Globs ``../koans/about*.py`` relative to this module and excludes
        ``about_extra_credit``; the result is cached on ``self.all_lessons``.

        Returns:
            list[str]: The discovered lesson file paths.

        Source: runner/sensei.py:L261
        """
        cur_dir = os.path.split(os.path.realpath(__file__))[0]
        if not self.all_lessons:
            self.all_lessons = glob.glob('{0}/../koans/about*.py'.format(cur_dir))
            self.all_lessons = list(filter(lambda filename:
                                      "about_extra_credit" not in filename,
                                      self.all_lessons))

        return self.all_lessons
