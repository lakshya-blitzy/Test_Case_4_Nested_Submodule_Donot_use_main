#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on ``lambda`` anonymous functions and assigning them to variables.

Works through creating an anonymous function with a ``lambda`` expression and
binding it to a name to call it explicitly, returning a ``lambda`` from an
enclosing method (closing over that method's arguments), and invoking such a
returned ``lambda`` immediately without assigning it to a variable.

Source: koans.txt:L20 (entry ``koans.about_lambdas.AboutLambdas``); :class:`AboutLambdas` at koans/about_lambdas.py:L21 (tests span koans/about_lambdas.py:L27-L44).
"""

#
# Based slightly on the lambdas section of AboutBlocks in the Ruby Koans
#

from runner.koan import *

class AboutLambdas(Koan):
    """Koan exercises on ``lambda`` anonymous functions and binding them to variables.

    Source: koans/about_lambdas.py:L21 (class definition); test methods span koans/about_lambdas.py:L27-L44.
    """

    def test_lambdas_can_be_assigned_to_variables_and_called_explicitly(self):
        add_one = lambda n: n + 1
        self.assertEqual(__, add_one(10))

    # ------------------------------------------------------------------

    def make_order(self, order):
        return lambda qty: str(qty) + " " + order + "s"

    def test_accessing_lambda_via_assignment(self):
        sausages = self.make_order('sausage')
        eggs = self.make_order('egg')

        self.assertEqual(__, sausages(3))
        self.assertEqual(__, eggs(2))

    def test_accessing_lambda_without_assignment(self):
        self.assertEqual(__, self.make_order('spam')(39823))
