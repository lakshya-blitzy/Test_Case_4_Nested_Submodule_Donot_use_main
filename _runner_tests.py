#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Aggregator entry point for the runner engine's own self-tests.

These are the unit tests that verify the koans *runner* itself (the
orchestration and reporting engine under ``runner/``), as distinct from
the fill-in-the-blank koan exercises a learner solves.

The module assembles a single ``unittest.TestSuite`` from the runner
test cases ``TestMountain``, ``TestSensei``, ``TestHelper``,
``TestFilterKoanNames`` and ``TestKoansSuite``, imported from the
``runner.runner_tests`` package.  `Source: _runner_tests.py:L32-L36`

This module is the command Continuous Integration uses to verify the
runner: Travis runs ``python _runner_tests.py``.  `Source: .travis.yml:L6-L7`

Running the module executes the assembled suite with a ``TextTestRunner``
at ``verbosity=2`` and exits with a non-zero status if any test fails.
`Source: _runner_tests.py:L58-L60`

Known caveat (documented, not fixed): on Python 3.12 this command fails
because the runner self-tests use the removed ``assertEquals`` alias.
`Source: runner/runner_tests/test_helper.py:L14-L17`  This is a code-level
compatibility matter recorded here as a caveat only; see the deployment guide.
'''

import sys
import unittest

from runner.runner_tests.test_mountain import TestMountain
from runner.runner_tests.test_sensei import TestSensei
from runner.runner_tests.test_helper import TestHelper
from runner.runner_tests.test_path_to_enlightenment import TestFilterKoanNames
from runner.runner_tests.test_path_to_enlightenment import TestKoansSuite


def suite():
    '''
    Builds and returns the runner self-test ``unittest.TestSuite``.

    Aggregates every runner self-test ``TestCase`` — ``TestMountain``,
    ``TestSensei``, ``TestHelper``, ``TestFilterKoanNames`` and
    ``TestKoansSuite`` — each loaded via
    ``unittest.TestLoader().loadTestsFromTestCase(...)``.
    `Source: _runner_tests.py:L49-L55`
    '''
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
