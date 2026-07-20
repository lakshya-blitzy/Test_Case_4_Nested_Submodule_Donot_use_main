#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Support/fixture module used by the scope and module koans: defines a ``Dog`` whose ``identify()`` returns ``"jims dog"``. Paired with ``joes.py`` (an identically-shaped ``Dog``) so ``about_scope.py`` and ``about_modules.py`` can show that module namespaces disambiguate same-named classes."""

class Dog:
    def identify(self):
        return "jims dog"
