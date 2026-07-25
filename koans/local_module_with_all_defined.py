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

Source: koans/local_module_with_all_defined.py:L22-L25 (``__all__``),
koans/local_module_with_all_defined.py:L27 (``Goat``),
koans/local_module_with_all_defined.py:L42 (``_Velociraptor``),
koans/local_module_with_all_defined.py:L57 (``SecretDuck``); consumer
koans/about_modules.py:L34 (``import *``) and koans/about_modules.py:L101-L110
(``Goat``/``_Velociraptor`` resolve, bare ``SecretDuck`` raises ``NameError``).
"""

__all__ = (
    'Goat',
    '_Velociraptor'
)

class Goat:
    """Publicly named fixture listed in ``__all__``; ``name`` returns ``"George"``.

    Source: koans/local_module_with_all_defined.py:L40 (``name`` returns "George");
    consumer koans/about_modules.py:L101-L102 (``goat.name``).
    """
    @property
    def name(self):
        """Return this fixture's fixed name, ``"George"``.

        Source: koans/local_module_with_all_defined.py:L40 (the ``return`` below);
        consumer koans/about_modules.py:L102 (``goat.name``).
        """
        return "George"

class _Velociraptor:
    """Underscore-prefixed fixture force-exported by ``__all__`` despite its leading underscore; ``name`` returns ``"Cuddles"``.

    Source: koans/local_module_with_all_defined.py:L55 (``name`` returns "Cuddles");
    consumer koans/about_modules.py:L105-L106 (``_Velociraptor()`` resolves via ``__all__``, ``lizard.name``).
    """
    @property
    def name(self):
        """Return this fixture's fixed name, ``"Cuddles"``.

        Source: koans/local_module_with_all_defined.py:L55 (the ``return`` below);
        consumer koans/about_modules.py:L106 (``lizard.name``).
        """
        return "Cuddles"

class SecretDuck:
    """Fixture deliberately omitted from ``__all__`` so wildcard import cannot see it; ``name`` returns ``"None of your business"``.

    Source: koans/local_module_with_all_defined.py:L70 (``name`` returns
    "None of your business"); consumer koans/about_modules.py:L109-L110 (bare
    ``SecretDuck()`` after ``import *`` raises ``NameError``).
    """
    @property
    def name(self):
        """Return this fixture's fixed name, ``"None of your business"``.

        Source: koans/local_module_with_all_defined.py:L70 (the ``return`` below).
        """
        return "None of your business"
