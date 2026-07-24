#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sample module inside a package, imported by the AboutPackages koan to demonstrate relative and absolute imports."""

class Duck:
    """Minimal example class exposing a read-only ``name`` property."""
    @property
    def name(self):
        """Return the duck's name, the constant string 'Donald'."""
        return "Donald"