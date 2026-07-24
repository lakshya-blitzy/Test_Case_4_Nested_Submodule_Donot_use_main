#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The Sensei: the koans' custom ``unittest`` result / observer / reporter.

This module defines :class:`Sensei`, the object that watches a learner
walk "the path" through the koans. Acting as a ``unittest`` result, it
observes every test-start, success, failure, and error callback; it
captures the *first* failing koan (with a focused, learner-friendly
traceback); it tracks how many koans and lessons have been completed;
and it prints colorized, Zen-flavored progress to the console.

For cross-platform colorized terminal output it integrates the vendored
Colorama library (``from libs.colorama import init, Fore, Style``).
Source: runner/sensei.py:L14
'''

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
    '''
    A custom ``unittest`` result object that doubles as the koans' reporter.

    ``Sensei`` subclasses ``MockableTestResult`` (itself a subclass of
    ``unittest.TestResult``) so it can act as the result collector while a
    koan suite is run. It observes the ``startTest`` / ``addSuccess`` /
    ``addFailure`` / ``addError`` callbacks, keeps a single ordered list of
    failures, and counts how many koans have passed and how many lessons
    have been reached (the lesson count deliberately excludes
    ``AboutAsserts`` and ``AboutExtraCredit``).

    Once the run finishes, :meth:`learn` renders the report through the
    injected ``WritelnDecorator`` stream: the first failing koan, a
    progress line, the remaining work, and a rotating "Zen of Python"
    message.

    Source: runner/sensei.py:L17
    '''

    def __init__(self, stream):
        '''
        Initialize the result/reporter around the given output ``stream``.

        Chains up to ``unittest.TestResult.__init__`` to set up the standard
        result bookkeeping, stores the ``WritelnDecorator`` ``stream`` used
        for all console output, and seeds the reporter state: the
        last-seen koan class name (``prevTestClassName``), the full koan
        suite used for totals (``self.tests`` built from
        ``path_to_enlightenment.koans()``), the ``pass_count`` and
        ``lesson_pass_count`` counters, and the lazily-populated
        ``all_lessons`` cache.
        '''
        unittest.TestResult.__init__(self)
        self.stream = stream
        self.prevTestClassName = None
        self.tests = path_to_enlightenment.koans()
        self.pass_count = 0
        self.lesson_pass_count  = 0
        self.all_lessons = None

    def startTest(self, test):
        '''
        Announce entry into a koan class before ``test`` runs.

        Called by ``unittest`` ahead of every test. When the run moves into
        a new koan class and no failures have been recorded yet, it prints a
        colored ``Thinking <ClassName>`` heading. It also advances
        ``lesson_pass_count`` when the new class is a lesson, excluding the
        non-lesson classes ``AboutAsserts`` and ``AboutExtraCredit``.
        '''
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
        '''
        Record a passing koan and celebrate it on the stream.

        When :meth:`passesCount` reports that successes should still be
        counted, the success is recorded via ``MockableTestResult`` and a
        green ``<method> has expanded your awareness.`` line is printed;
        ``pass_count`` is then incremented.
        '''
        if self.passesCount():
            MockableTestResult.addSuccess(self, test)
            self.stream.writeln( \
                "  {0}{1}{2} has expanded your awareness.{3}{4}" \
                .format(Fore.GREEN, Style.BRIGHT, test._testMethodName, \
                Fore.RESET, Style.NORMAL))
            self.pass_count += 1

    def addError(self, test, err):
        '''
        Treat an errored koan exactly like a failing one.

        Errors are routed through :meth:`addFailure` so that errors and
        failures share a single ordered list, preserving the sequence in
        which they occurred.
        '''
        # Having 1 list for errors and 1 list for failures would mess with
        # the error sequence
        self.addFailure(test, err)

    def passesCount(self):
        '''
        Report whether further successes should still be counted.

        Returns ``True`` while the learner is still within the same koan
        class as (or ahead of) the first failure, and ``False`` once the
        first failure belongs to a different class than the one currently
        being processed -- so passes recorded "past" the first failing
        lesson do not inflate the score.
        '''
        return not (self.failures and helper.cls_name(self.failures[0][0]) != self.prevTestClassName)

    def addFailure(self, test, err):
        '''
        Record a failing koan by delegating to ``MockableTestResult``.

        This appends the ``(test, err)`` pair to the standard ``failures``
        list; :meth:`addError` also funnels through here so a single ordered
        list captures both failures and errors.
        '''
        MockableTestResult.addFailure(self, test, err)

    def sortFailures(self, testClassName):
        r'''
        Return the failures for ``testClassName`` ordered by source line.

        Scans the ``failures`` list for entries whose class matches
        ``testClassName``, parses the offending source line number out of
        each traceback with ``re.search("(?<= line )\d+", err)``, and
        returns a list of ``(line_number, test, err)`` tuples sorted
        ascending by line number. Returns ``None`` when no matching,
        line-numbered failure can be found.
        '''
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
        '''
        Return the earliest failure of the first failing koan class.

        Uses :meth:`sortFailures` on the class of the first recorded failure
        and returns its lowest-source-line entry as a ``(test, err)`` pair,
        or ``None`` when there are no failures (or none are sortable).
        '''
        if not self.failures: return None

        table = self.sortFailures(helper.cls_name(self.failures[0][0]))

        if table:
            return (table[0][1], table[0][2])
        else:
            return None

    def learn(self):
        '''
        Render the end-of-run report and finish the walk.

        Prints the error report for the first failing koan, a blank
        separator, the progress line, and -- when failures remain -- the
        remaining-work line, followed by a Zen message. If any failures
        remain the process exits with a non-zero status via
        ``sys.exit(-1)`` (surfaced to the shell as exit code 255); on a
        clean run it instead prints the colored completion banner pointing
        the learner at ``about_extra_credit.py``.
        '''
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
        '''
        Print a focused report for the first failing koan.

        Looks up :meth:`firstFailure` and, when one exists, prints
        ``<method> has damaged your karma.``, the "You have not yet reached
        enlightenment ..." message, the cleaned assertion text from
        :meth:`scrapeAssertionError`, and -- under "Please meditate on the
        following code:" -- the focused, colorized stack dump from
        :meth:`scrapeInterestingStackDump`. Returns early when there is no
        failure to report.
        '''
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
        '''
        Extract just the assertion message from a traceback string.

        Walks the lines of ``err`` and returns only the human-readable
        error text (for example the ``AssertionError: ...`` message and any
        following diff), each line indented two spaces. Returns ``""`` when
        ``err`` is falsy.
        '''
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
        '''
        Extract and colorize the koan-relevant frames of a traceback.

        Keeps only the stack frames whose file paths contain ``koans`` --
        hiding the runner's own frames -- and then colorizes the
        ``about_*.py`` filenames and ``line <n>`` references so the learner
        can spot the exact spot to meditate on. Returns ``""`` when ``err``
        is falsy.
        '''
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
        '''
        Return the progress summary string.

        Describes how many koans have been completed (with the percentage
        of :meth:`total_koans`) and how many lessons have been completed
        (out of :meth:`total_lessons`).
        '''
        return "You have completed {0} ({2} %) koans and " \
                "{1} (out of {3}) lessons.".format(
                self.pass_count,
                self.lesson_pass_count,
                self.pass_count*100//self.total_koans(),
                self.total_lessons())

    def report_remaining(self):
        '''
        Return the remaining-work summary string.

        Reports how many koans and lessons still stand between the learner
        and enlightenment, computed as the totals minus the counts already
        passed.
        '''
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
        '''
        Return a Zen message appropriate to the current progress.

        While failures remain, returns one line from the "Zen of Python"
        rotation, selected by ``self.pass_count % 37`` (a 37-message
        cycle), so the message advances as the learner solves more koans.
        On a clean run it instead returns the cyan "Nobody ever expects the
        Spanish Inquisition." completion line.
        '''
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
        '''
        Return the number of discovered lesson files.

        Delegates to :meth:`filter_all_lessons` and returns the count of
        lesson files found, or ``0`` when none are discovered.
        '''
        all_lessons = self.filter_all_lessons()
        if all_lessons:
          return len(all_lessons)
        else:
          return 0

    def total_koans(self):
        '''
        Return the total number of koans (test cases) in the suite.

        This is ``self.tests.countTestCases()`` over the full suite built in
        :meth:`__init__` from ``path_to_enlightenment.koans()``.
        '''
        return self.tests.countTestCases()

    def filter_all_lessons(self):
        '''
        Discover and cache the lesson files, excluding extra credit.

        Globs the ``../koans/about*.py`` files relative to this module,
        drops ``about_extra_credit`` (which is not counted as a lesson),
        and caches the result in ``self.all_lessons`` so the (potentially
        expensive) filesystem scan happens only once. Returns the cached
        list on subsequent calls.
        '''
        cur_dir = os.path.split(os.path.realpath(__file__))[0]
        if not self.all_lessons:
            self.all_lessons = glob.glob('{0}/../koans/about*.py'.format(cur_dir))
            self.all_lessons = list(filter(lambda filename:
                                      "about_extra_credit" not in filename,
                                      self.all_lessons))

        return self.all_lessons
