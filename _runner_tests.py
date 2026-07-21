#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Self-test entry point for the Python Koans ``runner/`` framework.

This module is the test harness for the *runner itself* -- the machinery that
discovers, loads, runs, and reports on the koan lessons -- and NOT for the koan
lessons under ``koans/``. It aggregates the runner's own unit tests (defined in
the ``runner.runner_tests`` package) into a single ``unittest.TestSuite`` and
executes them with ``unittest.TextTestRunner``.

Continuous Integration runs this module directly: the Travis build step invokes
``python _runner_tests.py`` (Source: .travis.yml:7). When executed as a script,
the process exits with a non-zero status if any test fails and zero when every
test passes, via ``sys.exit(not res.wasSuccessful())``
(Source: _runner_tests.py:26); this makes the run usable as a CI pass/fail gate.

Usage:
    python _runner_tests.py
"""

import sys
import unittest

from runner.runner_tests.test_mountain import TestMountain
from runner.runner_tests.test_sensei import TestSensei
from runner.runner_tests.test_helper import TestHelper
from runner.runner_tests.test_path_to_enlightenment import TestFilterKoanNames
from runner.runner_tests.test_path_to_enlightenment import TestKoansSuite


def suite():
    """Build and return the runner framework's aggregated test suite.

    Constructs a fresh ``unittest.TestSuite`` and populates it, in source
    order, with every test case that exercises the runner framework:
    ``TestMountain``, ``TestSensei``, ``TestHelper``, ``TestFilterKoanNames``,
    and ``TestKoansSuite`` (all imported from the ``runner.runner_tests``
    package). Each case is added via
    ``unittest.TestLoader().loadTestsFromTestCase(...)`` so that all of its
    ``test_*`` methods are collected. (Source: _runner_tests.py:14-21)

    Returns:
        unittest.TestSuite: A newly built suite containing the runner's own
        unit tests, ready to be executed by a runner such as
        ``unittest.TextTestRunner``.
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
    sys.exit(not res.wasSuccessful())
