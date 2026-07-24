#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan exploring the semantics of Python's ``None`` singleton.

Demonstrates that ``None`` is a first-class object, that it is the one
universal instance shared throughout the interpreter (identity
comparisons with ``is`` always succeed), that it is distinct from other
falsy values such as ``0`` and ``False``, and which exception is raised
when a nonexistent method is called on it.
"""

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):
    """Koan exercises on the object nature and identity semantics of ``None``."""

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        self.assertEqual(__, isinstance(None, object))

    def test_none_is_universal(self):
        "There is only one None"
        self.assertEqual(____, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute

        self.assertEqual(__, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], __)

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        self.assertEqual(__, None is not 0)
        self.assertEqual(__, None is not False)
