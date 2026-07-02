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
    '''
    A ``unittest`` result that turns a koans run into colorized,
    learner-facing feedback and a final "report card".

    ``Sensei`` extends ``MockableTestResult`` (itself a
    ``unittest.TestResult``). As the suite runs it records passes and
    failures, prints a "Thinking <Lesson>" banner for each new lesson,
    tracks how many koans and lessons have been cleared, and -- at the
    end of the run via ``learn()`` -- reports progress, points the
    learner at the first failing koan to "meditate on", and offers a
    Zen-of-Python aphorism.

    Source: runner/sensei.py:L17-L456
    '''
    def __init__(self, stream):
        '''
        Initialize the reporter's counters and state.

        Retains the output ``stream``, resets the "current lesson"
        tracker ``prevTestClassName`` and the pass counters, and loads
        the full ordered suite via ``path_to_enlightenment.koans()`` so
        the totals used by ``report_progress`` and ``report_remaining``
        can be computed later.

        Source: runner/sensei.py:L32-L50
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
        Hook called as each test begins.

        Delegates to the base ``MockableTestResult.startTest`` and, when
        ``test`` belongs to a different class than the previous one,
        prints a ``Thinking <ClassName>`` banner. Advances the lesson
        counter for each newly seen lesson, except for ``AboutAsserts``
        and ``AboutExtraCredit`` which are not counted as lessons.

        Source: runner/sensei.py:L52-L73
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
        Record a passing koan.

        Guarded by ``passesCount()`` so a pass is only counted while
        still on the current lesson; on success it delegates to the base
        ``addSuccess``, prints the "has expanded your awareness" line,
        and increments the koan pass count.

        Source: runner/sensei.py:L75-L92
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
        Treat an error exactly like a failure.

        Funnels ``err`` into ``addFailure`` so errors and failures share
        a single ordered list; keeping them together preserves the
        failure sequence the report logic relies on.

        Source: runner/sensei.py:L94-L106
        '''
        # Having 1 list for errors and 1 list for failures would mess with
        # the error sequence
        self.addFailure(test, err)

    def passesCount(self):
        '''
        Return ``True`` while it is still valid to count successes.

        Guards ``addSuccess``: returns ``False`` once a failure has been
        recorded for a *different* lesson than the one currently
        running, so passes from later lessons are not tallied past the
        first failure.

        Source: runner/sensei.py:L108-L119
        '''
        return not (self.failures and helper.cls_name(self.failures[0][0]) != self.prevTestClassName)

    def addFailure(self, test, err):
        '''
        Record a failing koan by delegating to
        ``MockableTestResult.addFailure``.

        Source: runner/sensei.py:L121-L128
        '''
        MockableTestResult.addFailure(self, test, err)

    def sortFailures(self, testClassName):
        '''
        Collect and order the failures for a single lesson.

        Scans the recorded failures for those belonging to
        ``testClassName``, parses the failing source-line number out of
        each traceback, and returns the matches sorted by line number as
        ``(line, test, err)`` tuples -- or ``None`` when the lesson has
        no failures.

        Source: runner/sensei.py:L130-L153
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
        Return the earliest failure (by source line) in the current
        lesson.

        Sorts the current lesson's failures via ``sortFailures`` and
        returns the first as a ``(test, err)`` pair, or ``None`` when
        there are no failures.

        Source: runner/sensei.py:L155-L173
        '''
        if not self.failures: return None

        table = self.sortFailures(helper.cls_name(self.failures[0][0]))

        if table:
            return (table[0][1], table[0][2])
        else:
            return None

    def learn(self):
        '''
        Print the end-of-run report and finish the session.

        Emits the error report (first failing koan), the progress line,
        the "koans/lessons remaining" line (while failures remain), and
        a Zen aphorism. If any failures remain it exits the process with
        a non-zero status (``sys.exit(-1)``); otherwise it prints the
        completion message pointing the learner at
        ``about_extra_credit.py``.

        Source: runner/sensei.py:L175-L206
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
        Describe the first failing koan for the learner to "meditate on".

        Looks up ``firstFailure()`` and, when one exists, prints the
        failing koan's name, the scraped assertion message
        (``scrapeAssertionError``), and the relevant, colorized stack
        excerpt (``scrapeInterestingStackDump``). Does nothing when there
        are no failures.

        Source: runner/sensei.py:L208-L234
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
        Extract the tidied assertion-message lines from a traceback
        string.

        Walks the lines of ``err`` and keeps the message body (the lines
        after the first non-indented marker line), trimming and
        re-joining them; returns an empty string when ``err`` is falsy.

        Source: runner/sensei.py:L236-L258
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

        From the traceback string ``err`` it keeps only the stack frames
        that point at files under ``koans/`` and then highlights the
        ``about_*.py`` filename and ``line N`` references with color;
        returns an empty string when ``err`` is falsy.

        Source: runner/sensei.py:L260-L302
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
        Return the one-line progress summary.

        Formats "You have completed X (P %) koans and Y (out of Z)
        lessons." from the current pass counts and the totals from
        ``total_koans`` and ``total_lessons``.

        Source: runner/sensei.py:L304-L319
        '''
        return "You have completed {0} ({2} %) koans and " \
                "{1} (out of {3}) lessons.".format(
                self.pass_count,
                self.lesson_pass_count,
                self.pass_count*100//self.total_koans(),
                self.total_lessons())

    def report_remaining(self):
        '''
        Return the one-line "work remaining" summary.

        Formats "You are now N koans and M lessons away from reaching
        enlightenment." from the difference between the totals and the
        current pass counts.

        Source: runner/sensei.py:L321-L337
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
        Return a line of encouragement for the current run.

        While failures remain, returns one of the rotating "Zen of
        Python" aphorisms (selected from the koan pass count); once
        everything passes, returns the closing line.

        Source: runner/sensei.py:L345-L411
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
        Return the number of lessons in the curriculum.

        Counts the entries returned by ``filter_all_lessons`` (the
        ``about*.py`` files, excluding extra credit); the runtime value
        is 37. Returns ``0`` when no lessons are found.

        Source: runner/sensei.py:L413-L427
        '''
        all_lessons = self.filter_all_lessons()
        if all_lessons:
          return len(all_lessons)
        else:
          return 0

    def total_koans(self):
        '''
        Return the total number of koans (test cases) in the loaded
        suite, via ``self.tests.countTestCases()``; the runtime value
        is 304.

        Source: runner/sensei.py:L429-L437
        '''
        return self.tests.countTestCases()

    def filter_all_lessons(self):
        '''
        Find and cache the lesson files on disk.

        Globs ``koans/about*.py`` relative to this package, drops the
        ``about_extra_credit`` lesson, memoizes the result on ``self``
        and returns it; the runtime count is 37 lessons.

        Source: runner/sensei.py:L439-L456
        '''
        cur_dir = os.path.split(os.path.realpath(__file__))[0]
        if not self.all_lessons:
            self.all_lessons = glob.glob('{0}/../koans/about*.py'.format(cur_dir))
            self.all_lessons = list(filter(lambda filename:
                                      "about_extra_credit" not in filename,
                                      self.all_lessons))

        return self.all_lessons
