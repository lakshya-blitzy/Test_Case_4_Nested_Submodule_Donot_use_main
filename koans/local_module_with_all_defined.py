#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Fixture module demonstrating how a module's ``__all__`` declaration
controls ``from local_module_with_all_defined import *`` behavior.

The explicit ``__all__ = ('Goat', '_Velociraptor')`` tuple defines the
public export surface for wildcard imports: it forces the
underscore-prefixed ``_Velociraptor`` to be exported (even though names
beginning with an underscore are normally hidden from ``import *``), while
deliberately omitting ``SecretDuck`` from the exported names.
"""

__all__ = (
    'Goat',
    '_Velociraptor'
)

class Goat:
    """Publicly named fixture listed in ``__all__``; ``name`` returns ``"George"``."""
    @property
    def name(self):
        """Return this fixture's fixed name, ``"George"``."""
        return "George"

class _Velociraptor:
    """Underscore-prefixed fixture force-exported by ``__all__`` despite its leading underscore; ``name`` returns ``"Cuddles"``."""
    @property
    def name(self):
        """Return this fixture's fixed name, ``"Cuddles"``."""
        return "Cuddles"

class SecretDuck:
    """Fixture deliberately omitted from ``__all__`` so wildcard import cannot see it; ``name`` returns ``"None of your business"``."""
    @property
    def name(self):
        """Return this fixture's fixed name, ``"None of your business"``."""
        return "None of your business"
