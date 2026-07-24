#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for ``runner.mountain.Mountain`` — the runner-level coordinator
that wires together the suite builder and the ``Sensei`` reporter.

Source: runner/mountain.py:L11 (the ``Mountain`` class these tests exercise).
'''

import unittest
from libs.mock import *

from runner.mountain import Mountain

class TestMountain(unittest.TestCase):
    '''
    Exercise ``Mountain`` with the output ``stream`` and the lesson's ``learn``
    method mocked out, so ``walk_the_path`` can run without real console output.

    Source: runner/mountain.py:L11 (``Mountain`` definition under test).
    '''

    def setUp(self):
        '''
        Construct a fresh ``Mountain`` fixture before each test.

        Source: runner/mountain.py:L12 (``Mountain.__init__``).
        '''
        self.mountain = Mountain()

    def test_it_gets_test_results(self):
        '''
        Verify that, with ``stream.writeln`` and the lesson's ``learn`` patched
        out, calling ``walk_the_path()`` drives the run to completion and invokes
        ``lesson.learn()``.

        Source: runner/mountain.py:L17 (``walk_the_path`` under test) and L24
        (the ``self.lesson.learn()`` call this asserts was invoked).
        '''
        with patch_object(self.mountain.stream, 'writeln', Mock()):
            with patch_object(self.mountain.lesson, 'learn', Mock()):
                self.mountain.walk_the_path()
                self.assertTrue(self.mountain.lesson.learn.called)
