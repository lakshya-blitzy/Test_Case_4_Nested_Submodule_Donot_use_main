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

Source: koans/joes.py (companion fixture module)
"""

class Dog:
    """Minimal fixture dog whose :meth:`identify` returns ``"jims dog"``."""

    def identify(self):
        """Return this dog's identity string, ``"jims dog"``."""
        return "jims dog"
