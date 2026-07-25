#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for ``runner.path_to_enlightenment`` — koan-name filtering
(``filter_koan_names``) and ``unittest.TestSuite`` construction
(``koans_suite``).

Source: runner/path_to_enlightenment.py:L17 (``filter_koan_names``) and L42
(``koans_suite``) — the functions these tests exercise.
'''

import io
import unittest

from runner import path_to_enlightenment as pte


class TestFilterKoanNames(unittest.TestCase):
    '''
    Verify ``filter_koan_names`` strips surrounding whitespace and drops
    blank lines and ``#`` comment lines.

    Source: runner/path_to_enlightenment.py:L17-L28 (``filter_koan_names`` implementation).
    '''

    def test_empty_input_produces_empty_output(self):
        '''
        Empty input yields no koan names.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L37 (assertion);
        subject runner/path_to_enlightenment.py:L17.
        '''
        infile = io.StringIO('')
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_names_yielded_match_names_in_file(self):
        '''
        Ordinary newline-delimited names are yielded unchanged and in order.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L53 (assertion);
        subject runner/path_to_enlightenment.py:L22-L27 (yields each non-blank line in order).
        '''
        names = [
          'this.is.a.test',
          'this.is.only.a.test',
          ]
        infile = io.StringIO('\n'.join(names))
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(names, received)
        return

    def test_whitespace_is_stripped(self):
        '''
        Leading and trailing whitespace is stripped from each yielded name.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L77 (assertion);
        subject runner/path_to_enlightenment.py:L23 (``line.strip()``).
        '''
        names = [
          'this.is.a.test',
          '    white.space.should.be.stripped',
          'this.is.only.a.test',
          'white.space.should.be.stripped    ',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = [
          'this.is.a.test',
          'white.space.should.be.stripped',
          'this.is.only.a.test',
          'white.space.should.be.stripped',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def test_commented_out_names_are_excluded(self):
        '''
        Lines that are ``#`` comments (including indented comments) are
        excluded.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L100 (assertion);
        subject runner/path_to_enlightenment.py:L24-L25 (skips ``#`` comment lines).
        '''
        names = [
          'this.is.a.test',
          '#this.is.a.comment',
          'this.is.only.a.test',
          '    #    this.is.also a.comment    ',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = [
          'this.is.a.test',
          'this.is.only.a.test',
          ]
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return

    def all_blank_or_comment_lines_produce_empty_output(self):
        '''
        Input consisting only of blank, whitespace, and comment lines yields
        nothing. (Intentionally not prefixed ``test_`` so ``unittest`` does not
        auto-run it.)

        Source: runner/runner_tests/test_path_to_enlightenment.py:L121 (assertion);
        subject runner/path_to_enlightenment.py:L23-L27.
        '''
        names = [
          ' ',
          '# This is a comment.',
          '\t',
          '    # This is also a comment.',
          ]
        infile = io.StringIO('\n'.join(names))
        expected = []
        received = list(pte.filter_koan_names(infile))
        self.assertListEqual(expected, received)
        return


class TestKoansSuite(unittest.TestCase):
    '''
    Verify ``koans_suite`` builds a ``unittest.TestSuite`` from
    fully-qualified names.

    Source: runner/path_to_enlightenment.py:L42-L53 (``koans_suite`` implementation).
    '''

    def test_empty_input_produces_empty_testsuite(self):
        '''
        ``koans_suite([])`` returns an empty ``unittest.TestSuite``.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L142, L145 (assertions);
        subject runner/path_to_enlightenment.py:L42, L47.
        '''
        names = []
        suite = pte.koans_suite(names)
        self.assertTrue(isinstance(suite, unittest.TestSuite))
        expected = []
        received = list(suite)
        self.assertListEqual(expected, received)
        return

    def test_testcase_names_appear_in_testsuite(self):
        '''
        ``koans_suite`` loads the named cases so the suite contains
        ``AboutAsserts``, ``AboutNone``, and ``AboutStrings``.

        Source: runner/runner_tests/test_path_to_enlightenment.py:L169 (assertion);
        subject runner/path_to_enlightenment.py:L51 (``loadTestsFromName``).
        '''
        names = [
          'koans.about_asserts.AboutAsserts',
          'koans.about_none.AboutNone',
          'koans.about_strings.AboutStrings',
          ]
        suite = pte.koans_suite(names)
        self.assertTrue(isinstance(suite, unittest.TestSuite))
        expected = [
          'AboutAsserts',
          'AboutNone',
          'AboutStrings',
          ]
        received = sorted(set(test.__class__.__name__ for test in suite))
        self.assertListEqual(expected, received)
        return
