#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for ``runner.helper`` — the ``cls_name`` class-name introspection helper.

Source: runner/helper.py:L17 (the ``cls_name`` function these tests exercise).
'''

import unittest

from runner import helper

class TestHelper(unittest.TestCase):
    '''
    Verify that ``runner.helper.cls_name(obj)`` returns the correct class name
    for various object types.

    Source: runner/helper.py:L17 (``cls_name`` definition under test).
    '''

    def test_that_get_class_name_works_with_a_string_instance(self):
        '''
        Verify ``cls_name(str())`` returns ``"str"``.

        Source: runner/runner_tests/test_helper.py:L28 (assertion); subject runner/helper.py:L17.
        '''
        self.assertEqual("str", helper.cls_name(str()))

    def test_that_get_class_name_works_with_a_4(self):
        '''
        Verify ``cls_name(4)`` returns ``"int"``.

        Source: runner/runner_tests/test_helper.py:L36 (assertion); subject runner/helper.py:L17.
        '''
        self.assertEqual("int", helper.cls_name(4))

    def test_that_get_class_name_works_with_a_tuple(self):
        '''
        Verify ``cls_name((3, "pie", []))`` returns ``"tuple"``.

        Source: runner/runner_tests/test_helper.py:L44 (assertion); subject runner/helper.py:L17.
        '''
        self.assertEqual("tuple", helper.cls_name((3,"pie", [])))
