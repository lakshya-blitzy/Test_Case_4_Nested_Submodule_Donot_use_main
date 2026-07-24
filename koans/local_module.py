#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Local fixture module providing a ``Duck`` class for the module-import koans.

The koan lessons that explore Python's import system (for example,
``koans/about_modules.py``) import this module to demonstrate importing a
module, importing a name with ``from ... import``, and reaching an
underscore-prefixed attribute through a class instance.
"""


class Duck:
    """A fixture object with a private ``_password`` and a read-only ``name``.

    The read-only ``name`` property returns the string ``"Daffy"``. This
    ``Duck`` is distinct from the one in
    ``koans/a_package_folder/a_module.py``, whose ``name`` is ``"Donald"``.
    """

    def __init__(self):
        """Initialize the duck with a private ``_password`` attribute."""
        self._password = 'password' # Genius!

    @property
    def name(self):
        """Return the duck's name, ``"Daffy"``."""
        return "Daffy"
