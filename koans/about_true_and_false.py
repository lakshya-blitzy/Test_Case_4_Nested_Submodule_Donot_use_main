#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Explore how Python values are treated as true or false in a boolean context.

Demonstrates that ``True``, non-zero numbers, and non-empty collections are
truthy, while ``False``, ``None``, ``0``, empty collections, and the empty
string are treated as false when used in a conditional such as ``if``.

Source: koans.txt:L12 (entry ``koans.about_true_and_false.AboutTrueAndFalse``); :class:`AboutTrueAndFalse` at koans/about_true_and_false.py:L17 (tests span koans/about_true_and_false.py:L28-L57).
"""

from runner.koan import *


class AboutTrueAndFalse(Koan):
    """Koan lesson on which Python values are treated as true or false.

    Source: koans/about_true_and_false.py:L17 (class definition); test methods span koans/about_true_and_false.py:L28-L57.
    """
    def truth_value(self, condition):
        if condition:
            return 'true stuff'
        else:
            return 'false stuff'

    def test_true_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(True))

    def test_false_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(False))

    def test_none_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(None))

    def test_zero_is_treated_as_false(self):
        self.assertEqual(__, self.truth_value(0))

    def test_empty_collections_are_treated_as_false(self):
        self.assertEqual(__, self.truth_value([]))
        self.assertEqual(__, self.truth_value(()))
        self.assertEqual(__, self.truth_value({}))
        self.assertEqual(__, self.truth_value(set()))

    def test_blank_strings_are_treated_as_false(self):
        self.assertEqual(__, self.truth_value(""))

    def test_everything_else_is_treated_as_true(self):
        self.assertEqual(__, self.truth_value(1))
        self.assertEqual(__, self.truth_value([0]))
        self.assertEqual(__, self.truth_value((0,)))
        self.assertEqual(
            __,
            self.truth_value("Python is named after Monty Python"))
        self.assertEqual(__, self.truth_value(' '))
        self.assertEqual(__, self.truth_value('0'))
