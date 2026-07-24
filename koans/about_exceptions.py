#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on raising and handling exceptions in Python.

This module defines :class:`AboutExceptions`, the koan that teaches Python's
exception model: how built-in exceptions inherit from ``Exception`` through a
shared method-resolution order, how the ``try`` / ``except`` / ``else`` /
``finally`` control-flow clauses behave, and how to define, raise, and catch a
custom exception class (the nested :class:`AboutExceptions.MySpecialError`).

Source: koans.txt (entry ``koans.about_exceptions.AboutExceptions``).
"""

from runner.koan import *

class AboutExceptions(Koan):
    """
    Koan test cases exploring Python's exception-handling model.

    Each ``test_*`` method demonstrates a distinct facet of exceptions: the
    inheritance chain that links :class:`MySpecialError` up through
    ``RuntimeError``, ``Exception``, and ``BaseException``; the ``try`` /
    ``except`` clause for trapping errors; raising and catching a specific
    custom error type; and the ``else`` and ``finally`` clauses. Several tests
    intentionally leave a ``__`` blank (or call ``self.fail``) so that they
    fail until the learner supplies the correct value.
    """

    class MySpecialError(RuntimeError):
        """Custom ``RuntimeError`` subclass used to demonstrate raising and catching a specific error type."""
        pass

    def test_exceptions_inherit_from_exception(self):
        mro = self.MySpecialError.mro()
        self.assertEqual(__, mro[1].__name__)
        self.assertEqual(__, mro[2].__name__)
        self.assertEqual(__, mro[3].__name__)
        self.assertEqual(__, mro[4].__name__)

    def test_try_clause(self):
        result = None
        try:
            self.fail("Oops")
        except Exception as ex:
            result = 'exception handled'

            ex2 = ex

        self.assertEqual(__, result)

        self.assertEqual(__, isinstance(ex2, Exception))
        self.assertEqual(__, isinstance(ex2, RuntimeError))

        self.assertTrue(issubclass(RuntimeError, Exception), \
            "RuntimeError is a subclass of Exception")

        self.assertEqual(__, ex2.args[0])

    def test_raising_a_specific_error(self):
        result = None
        try:
            raise self.MySpecialError("My Message")
        except self.MySpecialError as ex:
            result = 'exception handled'
            msg = ex.args[0]

        self.assertEqual(__, result)
        self.assertEqual(__, msg)

    def test_else_clause(self):
        result = None
        try:
            pass
        except RuntimeError:
            result = 'it broke'
            pass
        else:
            result = 'no damage done'

        self.assertEqual(__, result)


    def test_finally_clause(self):
        result = None
        try:
            self.fail("Oops")
        except:
            # no code here
            pass
        finally:
            result = 'always run'

        self.assertEqual(__, result)
