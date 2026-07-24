#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Provide the ``Dog`` fixture that illustrates module namespacing in the koans.

This support module is a deliberate twin of ``koans/jims.py``: both modules
define a class named ``Dog`` whose ``identify`` method returns a
module-specific string. The scope and modules lessons
(``koans/about_scope.py`` and ``koans/about_modules.py``) import both modules
so learners can observe that two identically named classes living in different
modules are distinct objects.

Source: koans/joes.py:L18 (``Dog``) and koans/joes.py:L30 (``identify`` returns "joes dog");
companion koans/jims.py:L20 (whose ``Dog.identify`` returns "jims dog");
consumers koans/about_modules.py:L32,L34 and koans/about_scope.py:L25,L30.
"""

class Dog:
    """Minimal fixture dog whose ``identify`` returns ``"joes dog"``.

    Source: koans/joes.py:L30 (``identify``); consumers koans/about_scope.py:L25
    (``joes.Dog()``) and koans/about_modules.py:L32.
    """
    def identify(self):
        """Return this dog's identity string, ``"joes dog"``.

        Source: koans/joes.py:L30 (the ``return`` below); consumers
        koans/about_modules.py:L34 and koans/about_scope.py:L27,L30.
        """
        return "joes dog"
