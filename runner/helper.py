#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cls_name(obj):
    """Return the runtime class name of ``obj`` as a string.

    A tiny introspection helper used throughout the runner (notably by
    ``Sensei``) to detect test-class transitions and to group failures by
    their originating koan class.

    Args:
        obj: Any Python object whose class name is wanted.

    Returns:
        str: ``obj.__class__.__name__``, e.g. ``"AboutAsserts"`` for an
        instance of the ``AboutAsserts`` test case, or ``"str"`` for a
        string.

    Source: runner/helper.py:L4
    """
    return obj.__class__.__name__