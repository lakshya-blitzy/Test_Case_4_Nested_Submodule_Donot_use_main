#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on list and sequence unpacking assignment, including starred (``*``) splat targets.

Each ``test_*`` method explores a facet of Python's structured assignment:
binding an entire list to a single name, parallel one-to-one unpacking,
extended unpacking in which a starred ``*`` target absorbs the surplus
items (or an empty list when there are too few), unpacking that keeps a
nested sublist intact, and swapping two names in a single statement. Every
test leaves a ``__`` blank (imported from :mod:`runner.koan`) for the
learner to fill in with the expected value.

Source: koans.txt:L6 (entry ``koans.about_list_assignments.AboutListAssignments``); :class:`AboutListAssignments` at koans/about_list_assignments.py:L24 (tests span koans/about_list_assignments.py:L30-L61).
"""

#
# Based on AboutArrayAssignments in the Ruby Koans
#

from runner.koan import *

class AboutListAssignments(Koan):
    """Koan exercises on assigning to and unpacking Python lists and sequences.

    Source: koans/about_list_assignments.py:L24 (class definition); test methods span koans/about_list_assignments.py:L30-L61.
    """

    def test_non_parallel_assignment(self):
        names = ["John", "Smith"]
        self.assertEqual(__, names)

    def test_parallel_assignments(self):
        first_name, last_name = ["John", "Smith"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_extra_values(self):
        title, *first_names, last_name = ["Sir", "Ricky", "Bobby", "Worthington"]
        self.assertEqual(__, title)
        self.assertEqual(__, first_names)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_fewer_values(self):
        title, *first_names, last_name = ["Mr", "Bond"]
        self.assertEqual(__, title)
        self.assertEqual(__, first_names)
        self.assertEqual(__, last_name)

    def test_parallel_assignments_with_sublists(self):
        first_name, last_name = [["Willie", "Rae"], "Johnson"]
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

    def test_swapping_with_parallel_assignment(self):
        first_name = "Roy"
        last_name = "Rob"
        first_name, last_name = last_name, first_name
        self.assertEqual(__, first_name)
        self.assertEqual(__, last_name)

