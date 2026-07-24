#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Patchable test-seam subclass of ``unittest.TestResult`` for the runner engine.

The runner's own tests need to mock the test-result type in order to verify how
``Sensei`` records successes and failures.  Mocking ``unittest.TestResult``
directly is not safe, though: it confuses ``unittest`` itself and breaks the
machinery the runner depends on (Source: runner/mockable_test_result.py:L21-L22).
Subclassing it here gives those tests a dedicated, safe class to patch instead.

For that reason ``Sensei`` extends ``MockableTestResult`` rather than
``unittest.TestResult`` directly (Source: runner/sensei.py:L17), so test helpers
can patch methods such as ``addSuccess`` on this seam without mocking the
standard library out of existence.
'''

import unittest

# Needed to stop unittest.TestResult itself getting Mocked out of existence,
# which is a problem when testing the helper classes! (It confuses the runner)

class MockableTestResult(unittest.TestResult):
    '''
    Thin, behavior-free subclass of ``unittest.TestResult``.

    This class adds no behavior of its own; it exists purely as a mockable
    seam.  Test helpers can patch or replace ``MockableTestResult`` (and its
    inherited methods) without mocking ``unittest.TestResult`` out of
    existence, which would otherwise confuse ``unittest`` and the runner.

    Source: runner/mockable_test_result.py:L24
    '''
    pass