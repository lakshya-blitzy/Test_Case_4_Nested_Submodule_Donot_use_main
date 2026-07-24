#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Unit tests for ``runner.sensei.Sensei`` -- the koans' custom ``unittest`` result/reporter.

Covers success counting, failure sorting and first-failure selection,
assertion/stack-trace scraping, Zen-message rotation, and koan/lesson
counting.

Source: runner/runner_tests/test_sensei.py:L128-L413 (the ``TestSensei`` suite); subject runner/sensei.py:L32 (``Sensei``).
"""

import unittest
import re

from libs.mock import *

from runner.sensei import Sensei
from runner.writeln_decorator import WritelnDecorator
from runner.mockable_test_result import MockableTestResult

class AboutParrots:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L22-L27 (``AboutParrots`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutLumberjacks:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L28-L33 (``AboutLumberjacks`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutTennis:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L34-L39 (``AboutTennis`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutTheKnightsWhoSayNi:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L40-L45 (``AboutTheKnightsWhoSayNi`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutMrGumby:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L46-L51 (``AboutMrGumby`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutMessiahs:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L52-L57 (``AboutMessiahs`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutGiantFeet:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L58-L63 (``AboutGiantFeet`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutTrebuchets:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L64-L69 (``AboutTrebuchets`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass
class AboutFreemasons:
    """Dummy stand-in for a koan test class, used to populate ``Sensei`` failure records in these tests.

    Source: runner/runner_tests/test_sensei.py:L70-L75 (``AboutFreemasons`` koan-class stand-in); consumers runner/sensei.py:L157-L181 (``sortFailures``) and runner/sensei.py:L183-L200 (``firstFailure``), which process the ``self.failures`` records these stand-ins populate.
    """
    pass

error_assertion_with_message = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 43, in test_durability
    self.assertEqual("Steel","Lard", "Another fine mess you've got me into Stanley...")
AssertionError: Another fine mess you've got me into Stanley..."""

error_assertion_equals = """

Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_exploding_trousers.py", line 49, in test_math
    self.assertEqual(4,99)
AssertionError: 4 != 99
"""

error_assertion_true = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_armories.py", line 25, in test_weoponary
    self.assertTrue("Pen" > "Sword")
AssertionError

"""

error_mess = """
Traceback (most recent call last):
  File "contemplate_koans.py", line 5, in <module>
    from runner.mountain import Mountain
  File "/Users/Greg/hg/python_koans/runner/mountain.py", line 7, in <module>
    import path_to_enlightenment
  File "/Users/Greg/hg/python_koans/runner/path_to_enlightenment.py", line 8, in <module>
    from koans import *
  File "/Users/Greg/hg/python_koans/koans/about_asserts.py", line 20
    self.assertTrue(eoe"Pen" > "Sword", "nhnth")
                           ^
SyntaxError: invalid syntax"""

error_with_list = """Traceback (most recent call last):
  File "/Users/Greg/hg/python_koans/koans/about_armories.py", line 84, in test_weoponary
    self.assertEqual([1, 9], [1, 2])
AssertionError: Lists differ: [1, 9] != [1, 2]

First differing element 1:
9
2

- [1, 9]
?     ^

+ [1, 2]
?     ^

"""


class TestSensei(unittest.TestCase):
    """Exercise ``Sensei`` (the custom reporter) with a mocked ``WritelnDecorator(Mock())`` stream, verifying counting, failure sorting/selection, scraping, Zen-message rotation, and totals.

    Source: runner/runner_tests/test_sensei.py:L128-L413 (the 26 ``Sensei`` tests); subject runner/sensei.py:L32 (``Sensei``).
    """

    def setUp(self):
        """Construct a fresh ``Sensei`` wrapping a mocked ``WritelnDecorator(Mock())`` stream before each test.

        Source: runner/runner_tests/test_sensei.py:L134-L139 (constructs the ``Sensei`` fixture); subject runner/sensei.py:L52-L73 (``Sensei.__init__``).
        """
        self.sensei = Sensei(WritelnDecorator(Mock()))

    def test_that_it_successes_only_count_if_passes_are_currently_allowed(self):
        """``addSuccess`` consults ``passesCount()`` to decide whether a success should be counted.

        Source: runner/runner_tests/test_sensei.py:L141-L149 (test body); subject runner/sensei.py:L98-L115 (``addSuccess``) and runner/sensei.py:L131-L143 (``passesCount``).
        """
        with patch('runner.mockable_test_result.MockableTestResult.addSuccess', Mock()):
            self.sensei.passesCount = Mock()
            self.sensei.addSuccess(Mock())
            self.assertTrue(self.sensei.passesCount.called)

    def test_that_it_increases_the_passes_on_every_success(self):
        """``addSuccess`` increments ``pass_count`` by one on each recorded success.

        Source: runner/runner_tests/test_sensei.py:L151-L159 (test body); subject runner/sensei.py:L98-L115 (``addSuccess``).
        """
        with patch('runner.mockable_test_result.MockableTestResult.addSuccess', Mock()):
            pass_count = self.sensei.pass_count
            self.sensei.addSuccess(Mock())
            self.assertEqual(pass_count + 1, self.sensei.pass_count)

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_no_failures(self):
        """``sortFailures`` returns ``None`` when there are no failures.

        Source: runner/runner_tests/test_sensei.py:L161-L167 (test body); subject runner/sensei.py:L157-L181 (``sortFailures``).
        """
        self.sensei.failures = []
        self.assertEqual(None, self.sensei.sortFailures("AboutLife"))

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_no_relevent_failures(self):
        """``sortFailures`` returns ``None`` when no recorded failure belongs to the requested class.

        Source: runner/runner_tests/test_sensei.py:L169-L179 (test body); subject runner/sensei.py:L157-L181 (``sortFailures``).
        """
        self.sensei.failures = [
            (AboutTheKnightsWhoSayNi(),"File 'about_the_knights_whn_say_ni.py', line 24"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 43"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 844")
        ]
        self.assertEqual(None, self.sensei.sortFailures("AboutLife"))

    def test_that_nothing_is_returned_as_sorted_result_if_there_are_3_shuffled_results(self):
        """``sortFailures`` returns only the requested class's failures, sorted ascending by parsed source line number (``2``, ``30``, ``299``).

        Source: runner/runner_tests/test_sensei.py:L181-L200 (test body); subject runner/sensei.py:L157-L181 (``sortFailures``).
        """
        self.sensei.failures = [
            (AboutTennis(),"File 'about_tennis.py', line 299"),
            (AboutTheKnightsWhoSayNi(),"File 'about_the_knights_whn_say_ni.py', line 24"),
            (AboutTennis(),"File 'about_tennis.py', line 30"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 43"),
            (AboutTennis(),"File 'about_tennis.py', line 2"),
            (AboutMrGumby(),"File 'about_mr_gumby.py', line odd"),
            (AboutMessiahs(),"File 'about_messiahs.py', line 844")
        ]

        results = self.sensei.sortFailures("AboutTennis")
        self.assertEqual(3, len(results))
        self.assertEqual(2, results[0][0])
        self.assertEqual(30, results[1][0])
        self.assertEqual(299, results[2][0])

    def test_that_it_will_choose_not_find_anything_with_non_standard_error_trace_string(self):
        """``sortFailures`` returns ``None`` when the traceback's line number cannot be parsed (``line MISSING``).

        Source: runner/runner_tests/test_sensei.py:L202-L210 (test body); subject runner/sensei.py:L157-L181 (``sortFailures``).
        """
        self.sensei.failures = [
            (AboutMrGumby(),"File 'about_mr_gumby.py', line MISSING"),
        ]
        self.assertEqual(None, self.sensei.sortFailures("AboutMrGumby"))


    def test_that_it_will_choose_correct_first_result_with_lines_9_and_27(self):
        """``firstFailure`` selects the failure with the lowest parsed line number (``line 9``), ignoring the unparseable ``line 73v``.

        Source: runner/runner_tests/test_sensei.py:L213-L223 (test body); subject runner/sensei.py:L183-L200 (``firstFailure``).
        """
        self.sensei.failures = [
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 27"),
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 9"),
            (AboutTrebuchets(),"File 'about_trebuchets.py', line 73v")
        ]
        self.assertEqual("File 'about_trebuchets.py', line 9", self.sensei.firstFailure()[1])

    def test_that_it_will_choose_correct_first_result_with_multiline_test_classes(self):
        """``firstFailure`` picks the lowest-line failure of the FIRST failing class (``about_giant_feet.py`` ``line 44``).

        Source: runner/runner_tests/test_sensei.py:L225-L236 (test body); subject runner/sensei.py:L183-L200 (``firstFailure``).
        """
        self.sensei.failures = [
            (AboutGiantFeet(),"File 'about_giant_feet.py', line 999"),
            (AboutGiantFeet(),"File 'about_giant_feet.py', line 44"),
            (AboutFreemasons(),"File 'about_freemasons.py', line 1"),
            (AboutFreemasons(),"File 'about_freemasons.py', line 11")
        ]
        self.assertEqual("File 'about_giant_feet.py', line 44", self.sensei.firstFailure()[1])

    def test_that_error_report_features_a_stack_dump(self):
        """``errorReport`` invokes ``scrapeInterestingStackDump`` to render the focused stack dump for the first failure.

        Source: runner/runner_tests/test_sensei.py:L238-L247 (test body); subject runner/sensei.py:L236-L264 (``errorReport``) and runner/sensei.py:L290-L333 (``scrapeInterestingStackDump``).
        """
        self.sensei.scrapeInterestingStackDump = Mock()
        self.sensei.firstFailure = Mock()
        self.sensei.firstFailure.return_value = (Mock(), "FAILED")
        self.sensei.errorReport()
        self.assertTrue(self.sensei.scrapeInterestingStackDump.called)

    def test_that_scraping_the_assertion_error_with_nothing_gives_you_a_blank_back(self):
        """``scrapeAssertionError(None)`` returns an empty string.

        Source: runner/runner_tests/test_sensei.py:L249-L254 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("", self.sensei.scrapeAssertionError(None))

    def test_that_scraping_the_assertion_error_with_messaged_assert(self):
        """``scrapeAssertionError`` extracts the ``AssertionError`` line (with its custom message), indented two spaces, from ``error_assertion_with_message``.

        Source: runner/runner_tests/test_sensei.py:L256-L262 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("  AssertionError: Another fine mess you've got me into Stanley...",
            self.sensei.scrapeAssertionError(error_assertion_with_message))

    def test_that_scraping_the_assertion_error_with_assert_equals(self):
        """``scrapeAssertionError`` extracts the equality failure (``4 != 99``) from ``error_assertion_equals``.

        Source: runner/runner_tests/test_sensei.py:L264-L270 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("  AssertionError: 4 != 99",
            self.sensei.scrapeAssertionError(error_assertion_equals))

    def test_that_scraping_the_assertion_error_with_assert_true(self):
        """``scrapeAssertionError`` extracts a bare ``AssertionError`` (no message) from ``error_assertion_true``.

        Source: runner/runner_tests/test_sensei.py:L272-L278 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("  AssertionError",
            self.sensei.scrapeAssertionError(error_assertion_true))

    def test_that_scraping_the_assertion_error_with_syntax_error(self):
        """``scrapeAssertionError`` extracts ``SyntaxError: invalid syntax`` from the ``error_mess`` traceback.

        Source: runner/runner_tests/test_sensei.py:L280-L286 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("  SyntaxError: invalid syntax",
            self.sensei.scrapeAssertionError(error_mess))

    def test_that_scraping_the_assertion_error_with_list_error(self):
        """``scrapeAssertionError`` extracts and two-space-indents the full multi-line list-diff ``AssertionError`` from ``error_with_list``.

        Source: runner/runner_tests/test_sensei.py:L288-L304 (test body); subject runner/sensei.py:L266-L288 (``scrapeAssertionError``).
        """
        self.assertEqual("""  AssertionError: Lists differ: [1, 9] != [1, 2]

  First differing element 1:
  9
  2

  - [1, 9]
  ?     ^

  + [1, 2]
  ?     ^""",
            self.sensei.scrapeAssertionError(error_with_list))

    def test_that_scraping_a_non_existent_stack_dump_gives_you_nothing(self):
        """``scrapeInterestingStackDump(None)`` returns an empty string.

        Source: runner/runner_tests/test_sensei.py:L306-L311 (test body); subject runner/sensei.py:L290-L333 (``scrapeInterestingStackDump``).
        """
        self.assertEqual("", self.sensei.scrapeInterestingStackDump(None))

    def test_that_if_there_are_no_failures_say_the_final_zenlike_remark(self):
        """With no failures, ``say_something_zenlike`` returns the completion line containing ``Spanish Inquisition``.

        Source: runner/runner_tests/test_sensei.py:L313-L322 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.failures = None
        words = self.sensei.say_something_zenlike()

        m = re.search("Spanish Inquisition", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_are_0_successes_it_will_say_the_first_zen_of_python_koans(self):
        """At ``pass_count`` 0, ``say_something_zenlike`` returns the first Zen line (``Beautiful is better than ugly``).

        Source: runner/runner_tests/test_sensei.py:L324-L333 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.pass_count = 0
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()
        m = re.search("Beautiful is better than ugly", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_is_1_success_it_will_say_the_second_zen_of_python_koans(self):
        """At ``pass_count`` 1, ``say_something_zenlike`` returns the second Zen line (``Explicit is better than implicit``).

        Source: runner/runner_tests/test_sensei.py:L335-L344 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.pass_count = 1
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()
        m = re.search("Explicit is better than implicit", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_are_10_successes_it_will_say_the_sixth_zen_of_python_koans(self):
        """At ``pass_count`` 10, ``say_something_zenlike`` returns ``Sparse is better than dense``.

        Source: runner/runner_tests/test_sensei.py:L346-L355 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.pass_count = 10
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()
        m = re.search("Sparse is better than dense", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_are_36_successes_it_will_say_the_final_zen_of_python_koans(self):
        """At ``pass_count`` 36, ``say_something_zenlike`` returns the final Zen line (``Namespaces are one honking great idea``).

        Source: runner/runner_tests/test_sensei.py:L357-L366 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.pass_count = 36
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()
        m = re.search("Namespaces are one honking great idea", words)
        self.assertTrue(m and m.group(0))

    def test_that_if_there_are_37_successes_it_will_say_the_first_zen_of_python_koans_again(self):
        """The Zen rotation wraps: at ``pass_count`` 37 (``% 37 == 0``) it returns the first Zen line again.

        Source: runner/runner_tests/test_sensei.py:L368-L377 (test body); subject runner/sensei.py:L376-L444 (``say_something_zenlike``).
        """
        self.sensei.pass_count = 37
        self.sensei.failures = Mock()
        words = self.sensei.say_something_zenlike()
        m = re.search("Beautiful is better than ugly", words)
        self.assertTrue(m and m.group(0))

    def test_that_total_lessons_return_7_if_there_are_7_lessons(self):
        """``total_lessons`` returns the count of discovered lessons (7) from ``filter_all_lessons``.

        Source: runner/runner_tests/test_sensei.py:L379-L386 (test body); subject runner/sensei.py:L446-L459 (``total_lessons``).
        """
        self.sensei.filter_all_lessons = Mock()
        self.sensei.filter_all_lessons.return_value = [1,2,3,4,5,6,7]
        self.assertEqual(7, self.sensei.total_lessons())

    def test_that_total_lessons_return_0_if_all_lessons_is_none(self):
        """``total_lessons`` returns ``0`` when ``filter_all_lessons`` yields ``None``.

        Source: runner/runner_tests/test_sensei.py:L388-L395 (test body); subject runner/sensei.py:L446-L459 (``total_lessons``).
        """
        self.sensei.filter_all_lessons = Mock()
        self.sensei.filter_all_lessons.return_value = None
        self.assertEqual(0, self.sensei.total_lessons())

    def test_total_koans_return_43_if_there_are_43_test_cases(self):
        """``total_koans`` returns the suite's test-case count (43) via ``tests.countTestCases()``.

        Source: runner/runner_tests/test_sensei.py:L397-L404 (test body); subject runner/sensei.py:L461-L470 (``total_koans``).
        """
        self.sensei.tests.countTestCases = Mock()
        self.sensei.tests.countTestCases.return_value = 43
        self.assertEqual(43, self.sensei.total_koans())

    def test_filter_all_lessons_will_discover_test_classes_if_none_have_been_discovered_yet(self):
        """``filter_all_lessons`` discovers and caches the lesson list (more than 10) when ``all_lessons`` has not been populated.

        Source: runner/runner_tests/test_sensei.py:L406-L413 (test body); subject runner/sensei.py:L472-L491 (``filter_all_lessons``).
        """
        self.sensei.all_lessons = 0
        self.assertTrue(len(self.sensei.filter_all_lessons()) > 10)
        self.assertTrue(len(self.sensei.all_lessons) > 10)
