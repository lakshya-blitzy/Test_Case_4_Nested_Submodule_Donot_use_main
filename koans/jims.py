#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Support/fixture module used by the scope and module koans: defines a ``Dog`` whose ``identify()`` method returns this module's own distinguishing label. Paired with ``joes.py`` (an identically-shaped ``Dog`` living in a separate module namespace) so ``about_scope.py`` and ``about_modules.py`` can show that module namespaces disambiguate same-named classes.

Source: koans/jims.py:L9-L11
"""

class Dog:
    def identify(self):
        return "jims dog"
