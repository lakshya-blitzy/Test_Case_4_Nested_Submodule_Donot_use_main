#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

# Needed to stop unittest.TestResult itself getting Mocked out of existence,
# which is a problem when testing the helper classes! (It confuses the runner)

class MockableTestResult(unittest.TestResult):
    """An empty ``unittest.TestResult`` subclass used purely as a mocking seam.

    ``Sensei`` subclasses this class instead of ``unittest.TestResult``
    directly so that unit tests can mock/replace the base result behavior
    without mocking ``unittest.TestResult`` itself. Mocking the standard
    ``TestResult`` out of existence breaks the test runner; introducing this
    thin, behavior-free subclass provides a safe, dedicated override point.

    Inherits all standard ``TestResult`` state and behavior unchanged; it
    adds no fields or methods of its own.

    Source: runner/mockable_test_result.py:L9
    """
    pass