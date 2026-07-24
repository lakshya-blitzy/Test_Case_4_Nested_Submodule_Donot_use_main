#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutSandwichCode in the Ruby Koans
#

"""
Koan lesson on the ``with`` statement and context managers.

Contrasts the repetitive try/finally "sandwich code" pattern used to
acquire and release a resource (such as opening and closing a file)
with Python's context managers -- objects implementing the
``__enter__``/``__exit__`` protocol that the ``with`` statement drives
automatically.

Source: koans.txt:L23 (entry ``koans.about_with_statements.AboutWithStatements``); :class:`AboutWithStatements` at koans/about_with_statements.py:L24 (tests span koans/about_with_statements.py:L43-L132); fixture data example_file.txt:L1-L4.
"""

from runner.koan import *

import re # For regular expression string comparisons

class AboutWithStatements(Koan):
    """
    Koan exercises that contrast try/finally "sandwich code" with the
    ``with`` statement and a custom file context manager.

    Source: koans/about_with_statements.py:L24 (class definition); test methods span koans/about_with_statements.py:L43-L132; nested fixtures ``FileContextManager`` at koans/about_with_statements.py:L88.
    """

    def count_lines(self, file_name):
        try:
            file = open(file_name)
            try:
                return len(file.readlines())
            finally:
                file.close()
        except IOError:
            # should never happen
            self.fail()

    def test_counting_lines(self):
        self.assertEqual(__, self.count_lines("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line(self, file_name):
        try:
            file = open(file_name)
            try:
                for line in file.readlines():
                    match = re.search('e', line)
                    if match:
                        return line
            finally:
                file.close()
        except IOError:
            # should never happen
            self.fail()

    def test_finding_lines(self):
        self.assertEqual(__, self.find_line("example_file.txt"))

    ## ------------------------------------------------------------------
    ## THINK ABOUT IT:
    ##
    ## The count_lines and find_line are similar, and yet different.
    ## They both follow the pattern of "sandwich code".
    ##
    ## Sandwich code is code that comes in three parts: (1) the top slice
    ## of bread, (2) the meat, and (3) the bottom slice of bread.
    ## The bread part of the sandwich almost always goes together, but
    ## the meat part changes all the time.
    ##
    ## Because the changing part of the sandwich code is in the middle,
    ## abstracting the top and bottom bread slices to a library can be
    ## difficult in many languages.
    ##
    ## (Aside for C++ programmers: The idiom of capturing allocated
    ## pointers in a smart pointer constructor is an attempt to deal with
    ## the problem of sandwich code for resource allocation.)
    ##
    ## Python solves the problem using Context Managers. Consider the
    ## following code:
    ##

    class FileContextManager():
        """A context manager that opens a file on ``__enter__`` and closes it on ``__exit__``.

        Source: koans/about_with_statements.py:L88 (fixture); exercised by koans/about_with_statements.py:L107.
        """

        def __init__(self, file_name):
            self._file_name = file_name
            self._file = None

        def __enter__(self):
            self._file = open(self._file_name)
            return self._file

        def __exit__(self, cls, value, tb):
            self._file.close()

    # Now we write:

    def count_lines2(self, file_name):
        with self.FileContextManager(file_name) as file:
            return len(file.readlines())

    def test_counting_lines2(self):
        self.assertEqual(__, self.count_lines2("example_file.txt"))

    # ------------------------------------------------------------------

    def find_line2(self, file_name):
        # Using the context manager self.FileContextManager, rewrite this
        # function to return the first line containing the letter 'e'.
        return None

    def test_finding_lines2(self):
        self.assertNotEqual(None, self.find_line2("example_file.txt"))
        self.assertEqual('test\n', self.find_line2("example_file.txt"))

    # ------------------------------------------------------------------

    def count_lines3(self, file_name):
        with open(file_name) as file:
            return len(file.readlines())

    def test_open_already_has_its_own_built_in_context_manager(self):
        self.assertEqual(__, self.count_lines3("example_file.txt"))
