#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fixture classes for the module and wildcard-import koans.

Defines three small classes -- :class:`Goose`, :class:`Hamster`, and
:class:`_SecretSquirrel` -- each exposing a single read-only ``name``
property. ``koans/about_modules.py`` imports this module with
``from .another_local_module import *`` to explore how Python modules and
wildcard imports behave.

Because the module defines no ``__all__``, a wildcard import binds only the
non-underscore names (:class:`Goose` and :class:`Hamster`).
:class:`_SecretSquirrel` is deliberately underscore-prefixed to demonstrate
that such names are hidden from ``from .another_local_module import *`` and
remain inaccessible unless imported explicitly.

Source: koans/about_modules.py:L11, L43-L51
"""

class Goose:
    """Fixture class exposing a ``name`` property that returns ``"Mr Stabby"``."""
    @property
    def name(self):
        """Return the fixed name ``"Mr Stabby"``."""
        return "Mr Stabby"

class Hamster:
    """Fixture class exposing a ``name`` property that returns ``"Phil"``."""
    @property
    def name(self):
        """Return the fixed name ``"Phil"``."""
        return "Phil"

class _SecretSquirrel:
    """
    Underscore-prefixed fixture class exposing a ``name`` property that
    returns ``"Mr Anonymous"``.

    The leading underscore keeps this class out of
    ``from .another_local_module import *`` wildcard imports (the module
    defines no ``__all__``), so it stays private and must be imported
    explicitly to be used.
    """
    @property
    def name(self):
        """Return the fixed name ``"Mr Anonymous"``."""
        return "Mr Anonymous"