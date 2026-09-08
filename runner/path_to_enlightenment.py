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

    Source: runner/path_to_enlightenment.py:L33-L39
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

    Source: runner/path_to_enlightenment.py:L58-L61
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
        unittest.TestSuite: A suite populated in the supplied-name order, so
        the manifest/``TestCase`` order is preserved as each named case's
        tests are added. The loader's ``sortTestMethodsUsing`` is set to
        ``None`` to disable the loader's own re-sorting of method names;
        within each ``TestCase`` the methods are then enumerated in
        ``unittest``'s default discovery order (the alphabetical order
        returned by ``dir()``) rather than source-definition order.

    Source: runner/path_to_enlightenment.py:L83-L89
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

    Source: runner/path_to_enlightenment.py:L108-L109
    '''
    names = names_from_file(filename)
    return koans_suite(names)
