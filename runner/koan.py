#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
The koan exercise surface: the sentinel placeholders and the ``Koan``
base ``TestCase`` that every ``about_*`` lesson builds on.

The learner replaces the sentinel values defined below with real answers
to make each koan pass; the sentinels and ``Koan`` are re-exported via
``__all__`` so a lesson can ``from runner.koan import *``.

Source: runner/koan.py:L21-L67
'''

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

# The four sentinels below are intentional placeholders: every koan ships
# with one of these obviously-wrong values, and the learner edits the koan
# to replace the sentinel with whatever makes the assertion pass (so an
# un-edited koan fails loudly). They are described here by PURPOSE only --
# no koan answers are given:
#   ``__``    -- a fill-me-in placeholder *string*.
#   ``___``   -- a placeholder *Exception* subclass (for koans expecting a raise).
#   ``____``  -- a true/false placeholder.
#   ``_____`` -- a numeric placeholder (its sentinel value is ``0``).
# All four, plus ``Koan``, are re-exported via ``__all__`` above.
# Source: runner/koan.py:L21-L53
__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    '''
    Exception sentinel for koans that expect an error to be raised.

    Koans that assert a particular exception occurs use ``___`` as the
    deliberately-wrong placeholder; the learner replaces it with the real
    exception type to make the koan pass (so an un-edited koan fails
    loudly). Subclassing ``Exception`` lets ``___`` stand in anywhere an
    exception class is expected, while the empty ``pass`` body adds no
    behaviour of its own.

    Source: runner/koan.py:L36-L49
    '''
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    '''
    Base class for every koan lesson.

    All ``about_*`` lessons define ``TestCase`` classes that inherit from
    ``Koan`` (which itself extends ``unittest.TestCase``), so the runner
    can discover and execute them uniformly. The body is intentionally
    empty -- ``Koan`` exists only to give the lessons a shared base type.

    Source: runner/koan.py:L56-L67
    '''
    pass
