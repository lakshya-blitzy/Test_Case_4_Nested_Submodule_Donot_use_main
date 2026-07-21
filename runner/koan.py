#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Exercise-facing scaffold shared by every Python Koans lesson.

Each koan lesson pulls this module's public names into its namespace with a
star-import (``from runner.koan import *``) and subclasses :class:`Koan` to
define its exercises. ``Source: runner/koan.py:10``

The exported surface is declared by ``__all__`` and is intentionally composed
of unusually named symbols -- ``__``, ``___``, ``____``, ``_____`` and
``Koan``. A leading underscore normally signals "private" scope, but for these
names that convention is deliberately waived (see the naming note immediately
below this docstring): they are *learner placeholders* and are meant to be
imported. Within the lessons the learner substitutes real values for the
``__``/``____``/``_____`` placeholders so that the intentionally failing tests
begin to pass.

Placeholders exported by this module and the role each one plays:

* ``__`` -- a fill-in *string* sentinel (``"-=> FILL ME IN! <=-"``) marking a
  value the learner must supply, e.g. ``self.assertEqual(__, expression)``.
* ``____`` -- a true/false *string* sentinel (``"-=> TRUE OR FALSE? <=-"``)
  used where the learner must decide whether an expression is truthy or falsy,
  e.g. ``self.assertEqual(____, some_condition)``.
* ``_____`` -- a *numeric* sentinel (``0``) used where the learner must supply
  a number, e.g. ``self.assertEqual(_____, some_number)``.
* ``___`` -- a placeholder :class:`Exception` subclass used where a lesson must
  expect a specific exception, e.g. ``self.assertRaises(___, ...)``.
* ``Koan`` -- the base :class:`unittest.TestCase` subclass that every lesson
  (``class AboutXxx(Koan)``) inherits from.

``Source: runner/koan.py:12-23``
"""

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    """Placeholder exception type supplied by the learner.

    Used in lessons where the exercise must expect a specific exception, for
    example ``with self.assertRaises(___):`` or ``self.assertRaises(___, ...)``.
    The learner replaces ``___`` with the real exception class that the code
    under contemplation is expected to raise. ``Source: runner/koan.py:14-15``
    """
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    """Base test-case class inherited by every koan lesson.

    Each lesson defines ``class AboutXxx(Koan)`` and thereby gains the full
    :class:`unittest.TestCase` assertion API within the Python Koans runner.
    ``Koan`` adds no behaviour of its own beyond :class:`unittest.TestCase`; it
    exists to give the curriculum a single, well-named base class.
    ``Source: runner/koan.py:22-23``
    """
    pass
