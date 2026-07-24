#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide the ``Dog`` fixture that illustrates module namespacing in the koans.

This support module is a deliberate twin of ``koans/jims.py``: both modules
define a class named ``Dog`` whose ``identify`` method returns a
module-specific string. The scope and modules lessons
(``koans/about_scope.py`` and ``koans/about_modules.py``) import both modules
so learners can observe that two identically named classes living in different
modules are distinct objects.

Source: koans/jims.py (companion fixture whose ``Dog.identify`` returns
``"jims dog"``).
"""

class Dog:
    """Minimal fixture dog whose ``identify`` returns ``"joes dog"``."""
    def identify(self):
        """Return this dog's identity string, ``"joes dog"``."""
        return "joes dog"
