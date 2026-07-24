#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Unit tests for ``runner.helper`` — the ``cls_name`` class-name introspection helper.
'''

import unittest

from runner import helper

class TestHelper(unittest.TestCase):
    '''
    Verify that ``runner.helper.cls_name(obj)`` returns the correct class name
    for various object types.
    '''

    def test_that_get_class_name_works_with_a_string_instance(self):
        '''
        Verify ``cls_name(str())`` returns ``"str"``.
        '''
        self.assertEqual("str", helper.cls_name(str()))

    def test_that_get_class_name_works_with_a_4(self):
        '''
        Verify ``cls_name(4)`` returns ``"int"``.
        '''
        self.assertEquals("int", helper.cls_name(4))

    def test_that_get_class_name_works_with_a_tuple(self):
        '''
        Verify ``cls_name((3, "pie", []))`` returns ``"tuple"``.
        '''
        self.assertEquals("tuple", helper.cls_name((3,"pie", [])))
