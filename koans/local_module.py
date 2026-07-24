#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Local fixture module providing a ``Duck`` class for the module-import koans.

The koan lessons that explore Python's import system (for example,
``koans/about_modules.py``) import this module to demonstrate importing a
module, importing a name with ``from ... import``, and reaching an
underscore-prefixed attribute through a class instance.

Source: koans/local_module.py:L18 (``Duck``); consumers koans/about_modules.py:L17-L26
(import the module and the ``Duck`` name) and koans/about_modules.py:L53-L57
(reach the private ``_password`` through an instance).
"""


class Duck:
    """A fixture object with a private ``_password`` and a read-only ``name``.

    The read-only ``name`` property returns the string ``"Daffy"``. This
    ``Duck`` is distinct from the one in
    ``koans/a_package_folder/a_module.py``, whose ``name`` is ``"Donald"``.

    Source: koans/local_module.py:L36 (``_password``) and koans/local_module.py:L45
    (``name`` returns "Daffy"); consumers koans/about_modules.py:L26 (``duck.name``)
    and koans/about_modules.py:L57 (``duck._password``).
    """

    def __init__(self):
        """Initialize the duck with a private ``_password`` attribute.

        Source: koans/local_module.py:L36 (sets ``_password``); consumer
        koans/about_modules.py:L57 (``duck._password``).
        """
        self._password = 'password' # Genius!

    @property
    def name(self):
        """Return the duck's name, ``"Daffy"``.

        Source: koans/local_module.py:L45 (the ``return`` below); consumers
        koans/about_modules.py:L20,L26 (``duck.name``).
        """
        return "Daffy"
