#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Patchable ``unittest.TestResult`` subclass seam for testing.

This module defines :class:`MockableTestResult`, a thin subclass of
:class:`unittest.TestResult` that exists purely as a *mocking seam* for the
runner's own unit tests.

The runner's tests need to replace or patch the test-result type in order to
verify reporting behaviour (for example the ``Sensei`` reporter defined in
``runner/sensei.py``). Patching :class:`unittest.TestResult` directly would
mock the standard-library base class "out of existence" and confuse the
runner. Interposing this trivial subclass gives the tests a dedicated
attachment point: they can patch ``MockableTestResult`` (or individual result
methods such as ``addSuccess``) without disturbing
:class:`unittest.TestResult` itself.

Source: runner/mockable_test_result.py:6-7
"""

import unittest

# Needed to stop unittest.TestResult itself getting Mocked out of existence,
# which is a problem when testing the helper classes! (It confuses the runner)

class MockableTestResult(unittest.TestResult):
    """Empty, patchable direct subclass of :class:`unittest.TestResult`.

    ``MockableTestResult`` intentionally adds no behaviour of its own; it is a
    dedicated seam that exists solely so that tests can patch it. The
    ``Sensei`` reporter subclasses ``MockableTestResult`` rather than
    :class:`unittest.TestResult` directly (see ``runner/sensei.py``), which
    lets the runner's unit tests patch
    ``runner.mockable_test_result.MockableTestResult.addSuccess`` (and similar
    result methods) without mocking the standard-library base class out of
    existence.

    Source: runner/sensei.py:17, runner/runner_tests/test_sensei.py:89,95
    """
    pass