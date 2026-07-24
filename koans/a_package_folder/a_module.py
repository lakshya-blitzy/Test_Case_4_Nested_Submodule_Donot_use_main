#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Sample module inside a package, imported by the AboutPackages koan to demonstrate relative and absolute imports.

Source: koans/a_package_folder/a_module.py:L11 (``Duck``); consumers
koans/about_packages.py:L29 (relative import) and koans/about_packages.py:L58
(absolute import).
"""

class Duck:
    """Minimal example class exposing a read-only ``name`` property.

    Source: koans/a_package_folder/a_module.py:L25 (``name`` returns "Donald");
    consumers koans/about_packages.py:L32 (``duck.name``) and koans/about_packages.py:L60
    (``Duck.__module__``).
    """
    @property
    def name(self):
        """Return the duck's name, the constant string 'Donald'.

        Source: koans/a_package_folder/a_module.py:L25 (the ``return`` below);
        consumer koans/about_packages.py:L32.
        """
        return "Donald"