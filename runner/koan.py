#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Exercise-facing scaffold for the koans.

This module defines the ``Koan`` base class that every ``About*`` lesson
extends, together with the intentional "fill in the blank" placeholders a
learner replaces while walking the Path to Enlightenment.

Starting a class name or attribute with an underscore normally implies
private scope; the blanks below are the deliberate exceptions to that
convention. Their all-underscore names make the spots a learner must
complete stand out visually inside each koan.

The placeholders are documented here for reference; their values are
intentional and must not be changed:

- ``__`` = ``"-=> FILL ME IN! <=-"`` -- the blank a learner replaces with
  the correct value (Source: runner/koan.py:L12).
- ``____`` = ``"-=> TRUE OR FALSE? <=-"`` -- a boolean-answer blank
  (Source: runner/koan.py:L17).
- ``_____`` = ``0`` -- a numeric-answer blank (Source: runner/koan.py:L19).
- ``___`` -- an ``Exception`` subclass used as an "answer placeholder"
  wherever a koan expects the learner to supply the expected exception
  type (Source: runner/koan.py:L14).
'''

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    '''Intentional placeholder exception: the "fill me in" stand-in used wherever a koan expects the learner to supply the expected exception type. (Source: runner/koan.py:L14)'''
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    '''
    Base ``unittest.TestCase`` subclass that every ``About*`` lesson extends.

    Subclassing ``unittest.TestCase`` gives each koan the standard assertion
    methods (for example ``assertEqual`` and ``assertTrue``) that the lessons
    use to check the learner's answers. (Source: runner/koan.py:L22)
    '''
    pass
