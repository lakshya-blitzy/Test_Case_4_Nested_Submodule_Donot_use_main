#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Functions to load the test cases ("koans") that make up the
Path to Enlightenment.
'''

import io
import unittest


# The path to enlightenment starts with the following:
KOANS_FILENAME = 'koans.txt'


def filter_koan_names(lines):
    '''
    Strips leading and trailing whitespace, then filters out blank
    lines and comment lines.

    Args:
        lines: An iterable of raw text lines (e.g. an open file object or a
            list of strings).

    Yields:
        str: Each non-blank, non-comment line with surrounding whitespace
        stripped, in the original input order. Lines whose stripped form
        starts with ``#`` are treated as comments and skipped.

    Source: runner/path_to_enlightenment.py:L17-L28
    '''
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            continue
        if line:
            yield line
    return


def names_from_file(filename):
    '''
    Opens the given ``filename`` and yields the fully-qualified names
    of TestCases found inside (one per line).

    Args:
        filename (str): Path to a curriculum manifest such as ``koans.txt``.

    Yields:
        str: Fully-qualified ``TestCase`` names (one per non-comment line),
        produced by delegating to ``filter_koan_names``. The file is opened
        UTF-8 text-mode inside a context manager and closed when iteration
        completes.

    Source: runner/path_to_enlightenment.py:L31-L39
    '''
    with io.open(filename, 'rt', encoding='utf8') as names_file:
        for name in filter_koan_names(names_file):
            yield name
    return


def koans_suite(names):
    '''
    Returns a ``TestSuite`` loaded with all tests found in the given
    ``names``, preserving the order in which they are found.

    Args:
        names: An iterable of fully-qualified ``TestCase`` names to load.

    Returns:
        unittest.TestSuite: A suite populated in supplied-name order. The
        loader's ``sortTestMethodsUsing`` is set to ``None`` so test methods
        run in definition order rather than being alphabetized.

    Source: runner/path_to_enlightenment.py:L42-L53
    '''
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None
    for name in names:
        tests = loader.loadTestsFromName(name)
        suite.addTests(tests)
    return suite


def koans(filename=KOANS_FILENAME):
    '''
    Returns a ``TestSuite`` loaded with all the koans (``TestCase``s)
    listed in ``filename``.

    Args:
        filename (str): Manifest to read; defaults to ``KOANS_FILENAME``
            (``'koans.txt'``).

    Returns:
        unittest.TestSuite: The fully assembled koan suite, composed by
        reading the manifest via ``names_from_file`` and building the suite
        via ``koans_suite``.

    Source: runner/path_to_enlightenment.py:L56-L62
    '''
    names = names_from_file(filename)
    return koans_suite(names)
