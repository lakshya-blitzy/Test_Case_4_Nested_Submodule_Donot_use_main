#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Small introspection helper for the runner engine.

This module provides a single utility, :func:`cls_name`, that looks up the
short class name of an arbitrary object. The ``Sensei`` reporter groups and
labels koan output by the class that owns each test, so it relies on this
helper to turn a live test instance into a printable class name.

Source: runner/helper.py:L17 (``cls_name`` definition); consumer
runner/sensei.py:L89-L95 (``Sensei.startTest`` groups and labels koan output by class name via ``helper.cls_name``).
'''


def cls_name(obj):
    '''
    Return the class name of ``obj`` -- i.e. ``obj.__class__.__name__``.

    Accepts any object and returns its type's short name (the class name
    only, without any enclosing module path) as a ``str``. For example,
    ``cls_name(4)`` returns ``"int"`` and ``cls_name("x")`` returns
    ``"str"``.

    :param obj: any Python object whose class name is required.
    :returns: the short class name of ``obj`` as a ``str``.

    Source: runner/helper.py:L17, L31 (definition and return); consumer runner/sensei.py:L89-L95.
    '''
    return obj.__class__.__name__