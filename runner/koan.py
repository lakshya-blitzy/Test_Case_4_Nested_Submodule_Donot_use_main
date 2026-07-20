#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Base test-case scaffold and fill-in placeholder markers for the koans.

This module exports a deliberately "private-looking" API (see ``__all__``)
whose names use leading underscores by design so that they read naturally
inside exercise code:

* ``__``    -> the string ``"-=> FILL ME IN! <=-"`` (fill-in-the-blank marker)
* ``____``  -> the string ``"-=> TRUE OR FALSE? <=-"`` (boolean prompt marker)
* ``_____`` -> the integer ``0`` (numeric fill-in marker)
* ``___``   -> a custom ``Exception`` subclass used as a placeholder to raise
* ``Koan``  -> the ``unittest.TestCase`` base class every ``about_*`` koan extends

Leading-underscore names normally imply private scope; this module makes an
intentional exception so learners can write ``self.assertEqual(__, value)``.

Source: runner/koan.py:L7-L22
"""

import unittest
import re

# Starting a classname or attribute with an underscore normally implies Private scope.
# However, we are making an exception for __ and ___.

__all__ = [ "__", "___", "____", "_____", "Koan" ]

__ = "-=> FILL ME IN! <=-"

class ___(Exception):
    """Placeholder exception type used where a koan must fill in an error class.

    Named with three underscores intentionally (an exported pseudo-private
    name) so it reads as a blank to be completed. Adds no behavior beyond
    ``Exception``.

    Source: runner/koan.py:L14
    """
    pass

____ = "-=> TRUE OR FALSE? <=-"

_____ = 0


class Koan(unittest.TestCase):
    """Base ``unittest.TestCase`` for every koan exercise (``about_*`` files).

    A behavior-free subclass of ``unittest.TestCase`` that gives all koans a
    common, project-branded base type. It adds no assertions or fixtures of
    its own; each koan subclass supplies the lessons to meditate on.

    Source: runner/koan.py:L22
    """
    pass
