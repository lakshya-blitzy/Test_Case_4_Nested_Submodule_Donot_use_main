#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cls_name(obj):
    '''
    Returns the class name of ``obj`` -- a shortcut for
    ``obj.__class__.__name__``.

    Small introspection helper used by ``Sensei`` to recognise and group
    koan ``TestCase`` classes as a run progresses. ``obj`` may be any
    object; its unqualified class name is returned as a ``str``.

    Source: runner/helper.py:L4-L15
    '''
    return obj.__class__.__name__