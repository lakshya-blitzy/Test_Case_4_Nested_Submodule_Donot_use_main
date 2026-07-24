#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fixture module providing a :class:`Dog` class for the koan lessons.

This is a minimal support/fixture module used by the koan curriculum. Its
:class:`Dog` is a deliberate twin of the ``Dog`` defined in :mod:`koans.joes`:
the two classes share the same name but live in different modules, so the
scope and module koans (see ``koans/about_scope.py`` and
``koans/about_modules.py``) can demonstrate that identically-named classes in
different namespaces are distinct objects. :meth:`Dog.identify` returns the
literal ``"jims dog"``, which lets the lessons tell the twins apart.

Source: koans/jims.py:L20 (``Dog``) and koans/jims.py:L33 (``identify`` returns "jims dog");
companion koans/joes.py:L18; consumers koans/about_modules.py:L31,L33 and
koans/about_scope.py:L22,L30.
"""

class Dog:
    """Minimal fixture dog whose :meth:`identify` returns ``"jims dog"``.

    Source: koans/jims.py:L33 (``identify``); consumers koans/about_scope.py:L22
    (``jims.Dog()``) and koans/about_modules.py:L31.
    """

    def identify(self):
        """Return this dog's identity string, ``"jims dog"``.

        Source: koans/jims.py:L33 (the ``return`` below); consumers
        koans/about_modules.py:L33 and koans/about_scope.py:L26,L30.
        """
        return "jims dog"
