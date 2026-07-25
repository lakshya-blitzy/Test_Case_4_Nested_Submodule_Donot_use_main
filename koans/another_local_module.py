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
that a wildcard import does not bind such names into the importing namespace,
so referencing the bare name ``_SecretSquirrel`` after
``from .another_local_module import *`` raises ``NameError``. The class itself
is not private, though -- it can still be reached by qualified access
(``another_local_module._SecretSquirrel``) or by importing it explicitly by
name.

Source: koans/another_local_module.py:L29 (``Goose``), koans/another_local_module.py:L44
(``Hamster``), koans/another_local_module.py:L59 (``_SecretSquirrel``); consumer
koans/about_modules.py:L33 (``import *``) and koans/about_modules.py:L76-L84 (uses
``Goose``/``Hamster`` and shows bare ``_SecretSquirrel`` raising ``NameError``).
"""

class Goose:
    """Fixture class exposing a ``name`` property that returns ``"Mr Stabby"``.

    Source: koans/another_local_module.py:L42 (``name`` returns "Mr Stabby");
    consumer koans/about_modules.py:L79 (``goose.name``).
    """
    @property
    def name(self):
        """Return the fixed name ``"Mr Stabby"``.

        Source: koans/another_local_module.py:L42 (the ``return`` below);
        consumer koans/about_modules.py:L79 (``goose.name``).
        """
        return "Mr Stabby"

class Hamster:
    """Fixture class exposing a ``name`` property that returns ``"Phil"``.

    Source: koans/another_local_module.py:L57 (``name`` returns "Phil");
    consumer koans/about_modules.py:L80 (``hamster.name``).
    """
    @property
    def name(self):
        """Return the fixed name ``"Phil"``.

        Source: koans/another_local_module.py:L57 (the ``return`` below);
        consumer koans/about_modules.py:L80 (``hamster.name``).
        """
        return "Phil"

class _SecretSquirrel:
    """
    Underscore-prefixed fixture class exposing a ``name`` property that
    returns ``"Mr Anonymous"``.

    The leading underscore keeps this class out of
    ``from .another_local_module import *`` wildcard imports (the module
    defines no ``__all__``), so the bare name is not bound by a wildcard
    import. It is not truly private, though: it remains reachable via
    qualified access or an explicit
    ``from .another_local_module import _SecretSquirrel``.

    Source: koans/another_local_module.py:L81 (``name`` returns "Mr Anonymous");
    consumer koans/about_modules.py:L83-L84 (bare ``_SecretSquirrel()`` after
    ``import *`` raises ``NameError``).
    """
    @property
    def name(self):
        """Return the fixed name ``"Mr Anonymous"``.

        Source: koans/another_local_module.py:L81 (the ``return`` below).
        """
        return "Mr Anonymous"