#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Introductory koan on assertions -- the first lesson on the Path to Enlightenment.

This module defines :class:`AboutAsserts`, the opening exercise in the koan
curriculum. It teaches how ``unittest``-style assertions (``assertTrue``,
``assertEqual``, and assertion failure messages) work together with Python's
native ``assert`` statement to reveal truth about running code, and it
introduces the ``__`` fill-in-the-blank convention (imported from
:mod:`runner.koan`) that the learner replaces with the correct value to make a
failing koan pass.

Source: koans.txt:L2 (first entry ``koans.about_asserts.AboutAsserts``); koans/about_asserts.py:L20 (``AboutAsserts``) and koans/about_asserts.py:L44 (intentional failing assertion).
"""

from runner.koan import *

class AboutAsserts(Koan):
    """
    Koan lesson introducing assertions and the fill-in-the-blank workflow.

    Each test method demonstrates a different assertion technique -- namely
    ``assertTrue``, ``assertEqual``, assertion failure messages, and Python's
    native ``assert`` statement. Several tests intentionally fail (for example
    by asserting ``False`` or by leaving a ``__`` blank in place) until the
    learner corrects the value or condition so that the assertion holds.

    Source: koans/about_asserts.py:L35-L100 (the lesson's test methods);
    intentional failures at koans/about_asserts.py:L44 and koans/about_asserts.py:L81;
    fill-in ``__`` blanks at koans/about_asserts.py:L56, L62, L70, L100.
    """

    def test_assert_truth(self):
        """
        We shall contemplate truth by testing reality, via asserts.
        """

        # Confused? This video should help:
        #
        #   http://bit.ly/about_asserts

        self.assertTrue(False) # This should be True

    def test_assert_with_message(self):
        """
        Enlightenment may be more easily achieved with appropriate messages.
        """
        self.assertTrue(False, "This should be True -- Please fix this")

    def test_fill_in_values(self):
        """
        Sometimes we will ask you to fill in the values
        """
        self.assertEqual(__, 1 + 1)

    def test_assert_equality(self):
        """
        To understand reality, we must compare our expectations against reality.
        """
        expected_value = __
        actual_value = 1 + 1
        self.assertTrue(expected_value == actual_value)

    def test_a_better_way_of_asserting_equality(self):
        """
        Some ways of asserting equality are better than others.
        """
        expected_value = __
        actual_value = 1 + 1

        self.assertEqual(expected_value, actual_value)

    def test_that_unittest_asserts_work_the_same_way_as_python_asserts(self):
        """
        Understand what lies within.
        """

        # This throws an AssertionError exception
        assert False

    def test_that_sometimes_we_need_to_know_the_class_type(self):
        """
        What is in a class name?
        """

        # Sometimes we will ask you what the class type of an object is.
        #
        # For example, contemplate the text string "navel". What is its class type?
        # The koans runner will include this feedback for this koan:
        #
        #   AssertionError: '-=> FILL ME IN! <=-' != <type 'str'>
        #
        # So "navel".__class__ is equal to <type 'str'>? No not quite. This
        # is just what it displays. The answer is simply str.
        #
        # See for yourself:

        self.assertEqual(__, "navel".__class__) # It's str, not <type 'str'>

        # Need an illustration? More reading can be found here:
        #
        #   https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

