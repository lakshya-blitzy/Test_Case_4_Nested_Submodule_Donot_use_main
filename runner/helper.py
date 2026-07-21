#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Introspection helpers for the Python Koans runner framework.

This module provides small, dependency-free utility functions used by the
koan test runner. Its single helper, :func:`cls_name`, is consumed by
``runner/sensei.py`` to detect when the test run advances to a new koan
(i.e. a new ``unittest`` test class) so the reporter can print a fresh
"Thinking <ClassName>" heading (Source: runner/sensei.py:30-35).
"""

def cls_name(obj):
    """Return the name of an object's class as a string.

    Returns ``obj.__class__.__name__`` for an instance of any type, for
    example ``cls_name("x") == "str"``, ``cls_name(4) == "int"`` and
    ``cls_name((1, 2)) == "tuple"``.

    Used by :class:`~runner.sensei.Sensei` to detect when execution moves to
    a new koan/test class, at which point the reporter prints a new
    "Thinking <ClassName>" heading (Source: runner/sensei.py:30-35).

    :param obj: any Python object.
    :returns: the name of the object's class.
    :rtype: str
    """
    return obj.__class__.__name__