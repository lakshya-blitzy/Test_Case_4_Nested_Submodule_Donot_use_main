#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Support/fixture module for the module-import koans: defines the ``Duck`` class (with a private ``_password`` and a read-only ``name`` property) imported by ``about_modules.py`` to demonstrate importing classes and attribute visibility.

Source: koans/local_module.py:L9-L15
"""

class Duck:
    def __init__(self):
        self._password = 'password' # Genius!

    @property
    def name(self):
        return "Daffy"
