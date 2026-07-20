#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Aggregate regression test runner for the ``runner/`` engine infrastructure.

Unlike the koans curriculum under ``koans/`` -- the fill-in-the-blank learning
exercises students edit -- this module exercises the *runner engine itself*:
the machinery in ``runner/`` that discovers, executes, and scores those koans.
It gathers the engine's unit test cases into a single ``unittest.TestSuite``:

* ``TestMountain``        -- runner/runner_tests/test_mountain.py
* ``TestSensei``          -- runner/runner_tests/test_sensei.py
* ``TestHelper``          -- runner/runner_tests/test_helper.py
* ``TestFilterKoanNames`` -- runner/runner_tests/test_path_to_enlightenment.py
* ``TestKoansSuite``      -- runner/runner_tests/test_path_to_enlightenment.py

Run the suite from the repository root::

    python _runner_tests.py

This is the exact command continuous integration invokes
(Source: .travis.yml:L7). When executed as a script the process exit code
mirrors the outcome -- ``0`` when every test passes and ``1`` when any test
fails or errors -- so CI (and shell callers) can gate on the result.
"""

import sys
import unittest

from runner.runner_tests.test_mountain import TestMountain
from runner.runner_tests.test_sensei import TestSensei
from runner.runner_tests.test_helper import TestHelper
from runner.runner_tests.test_path_to_enlightenment import TestFilterKoanNames
from runner.runner_tests.test_path_to_enlightenment import TestKoansSuite


def suite():
    """Build the aggregate suite of runner-engine regression tests.

    Assembles the five runner test cases -- ``TestMountain``, ``TestSensei``,
    ``TestHelper``, ``TestFilterKoanNames`` and ``TestKoansSuite`` -- into one
    suite, preserving their source order. Each case is loaded with a fresh
    ``unittest.TestLoader`` via ``loadTestsFromTestCase`` and appended with
    ``addTests`` (Source: _runner_tests.py:L14-L21).

    Returns:
        unittest.TestSuite: A suite containing every runner-engine test case,
        ready to be executed by a runner such as ``unittest.TextTestRunner``.
    """
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMountain))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSensei))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestHelper))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestFilterKoanNames))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestKoansSuite))
    return suite


if __name__ == '__main__':
    res = unittest.TextTestRunner(verbosity=2).run(suite())
    # Exit code mirrors the outcome: 0 when every test passed, 1 otherwise (CI-friendly).
    sys.exit(not res.wasSuccessful())
