#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Test harness for the runner engine — the ``runner/`` package that powers the
koans — as distinct from the koan lessons themselves (``koans/about_*.py``).

Aggregate every runner-layer unit test found in the
``runner/runner_tests/test_*.py`` modules into a single
``unittest.TestSuite`` (assembled by ``suite()``) and run it with a verbose
``TextTestRunner``. Invoke the harness directly from the repository root::

    python _runner_tests.py

This is also the command Travis CI executes for the project
(Source: .travis.yml:L7). The process exits non-zero when any runner test
fails, so it doubles as a continuous-integration gate
(Source: _runner_tests.py:L54).
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
    Build and return the aggregate suite of runner-engine unit tests.

    Load every runner-layer ``TestCase`` — ``TestMountain``, ``TestSensei``,
    ``TestHelper``, ``TestFilterKoanNames`` and ``TestKoansSuite`` — in that
    order via ``unittest.TestLoader().loadTestsFromTestCase`` and collect them
    into one ``unittest.TestSuite``, which is returned to the caller.

    Source: _runner_tests.py:L43-L49 (the five ``loadTestsFromTestCase`` calls
    that assemble the suite and the ``return`` that hands it back).
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
