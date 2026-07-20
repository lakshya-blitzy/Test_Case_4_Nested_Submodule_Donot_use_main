#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Support/fixture module for the module-import koans: defines ``Goat``, private ``_Velociraptor`` and ``SecretDuck``, and an ``__all__`` list that intentionally exports a private name while omitting ``SecretDuck`` — used by ``about_modules.py`` to show how ``from module import *`` honours ``__all__``."""

__all__ = (
    'Goat',
    '_Velociraptor'
)

class Goat:
    @property
    def name(self):
        return "George"

class _Velociraptor:
    @property
    def name(self):
        return "Cuddles"

class SecretDuck:
    @property
    def name(self):
        return "None of your business"
