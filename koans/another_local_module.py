#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Support/fixture module for the module-import koans: defines the ``Goose``, ``Hamster`` and private ``_SecretSquirrel`` classes imported via ``from .another_local_module import *`` in ``about_modules.py`` to demonstrate that underscore-prefixed names are excluded from wildcard imports.

Source: koans/another_local_module.py:L9-L22
"""

class Goose:
    @property
    def name(self):
        return "Mr Stabby"

class Hamster:
    @property
    def name(self):
        return "Phil"

class _SecretSquirrel:
    @property
    def name(self):
        return "Mr Anonymous"