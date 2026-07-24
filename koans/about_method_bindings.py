#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lessons on Python method binding and the descriptor protocol.

This module defines :class:`AboutMethodBindings`, the lesson exploring how a
plain function becomes a *bound* method when accessed through an instance, how
the attribute sets of functions and bound methods differ (as revealed by
:func:`dir`), how arbitrary attributes may be attached to functions and to
inner functions, and how the descriptor protocol customises attribute access.
The nested :class:`AboutMethodBindings.BoundClass` implements ``__get__`` to
show attribute-binding resolution, while
:class:`AboutMethodBindings.SuperColor` implements ``__set__`` to intercept
attribute assignment. The module-level :func:`function` and :func:`function2`
fixtures, together with the top-level :class:`Class`, supply the callables the
koan inspects.

Source: koans.txt (``koans.about_method_bindings.AboutMethodBindings``).
"""

from runner.koan import *

def function():
    """Return ``"pineapple"``; a plain module-level function fixture for the koan."""
    return "pineapple"

def function2():
    """Return ``"tractor"``; a fixture used to demonstrate attaching inner functions."""
    return "tractor"

class Class:
    """Simple fixture class whose :meth:`method` demonstrates method binding."""
    def method(self):
        return "parrot"

class AboutMethodBindings(Koan):
    """
    Koan test cases about method binding and the descriptor protocol.

    Each ``test_*`` method inspects how Python turns functions into bound
    methods, contrasts the attributes carried by functions versus bound
    methods, attaches attributes to callables and inner functions, and
    exercises the nested descriptors declared as the ``binding`` and ``color``
    class attributes -- :class:`BoundClass` (which implements ``__get__``) and
    :class:`SuperColor` (which implements ``__set__``).
    """
    def test_methods_are_bound_to_an_object(self):
        obj = Class()
        self.assertEqual(__, obj.method.__self__ == obj)

    def test_methods_are_also_bound_to_a_function(self):
        obj = Class()
        self.assertEqual(__, obj.method())
        self.assertEqual(__, obj.method.__func__(obj))

    def test_functions_have_attributes(self):
        obj = Class()
        self.assertEqual(__, len(dir(function)))
        self.assertEqual(__, dir(function) == dir(obj.method.__func__))

    def test_methods_have_different_attributes(self):
        obj = Class()
        self.assertEqual(__, len(dir(obj.method)))

    def test_setting_attributes_on_an_unbound_function(self):
        function.cherries = 3
        self.assertEqual(__, function.cherries)

    def test_setting_attributes_on_a_bound_method_directly(self):
        obj = Class()
        with self.assertRaises(___): obj.method.cherries = 3

    def test_setting_attributes_on_methods_by_accessing_the_inner_function(self):
        obj = Class()
        obj.method.__func__.cherries = 3
        self.assertEqual(__, obj.method.cherries)

    def test_functions_can_have_inner_functions(self):
        function2.get_fruit = function
        self.assertEqual(__, function2.get_fruit())

    def test_inner_functions_are_unbound(self):
        function2.get_fruit = function
        with self.assertRaises(___): cls = function2.get_fruit.__self__

    # ------------------------------------------------------------------

    class BoundClass:
        """A descriptor implementing ``__get__`` to show how attribute binding is resolved."""
        def __get__(self, obj, cls):
            return (self, obj, cls)

    binding = BoundClass()

    def test_get_descriptor_resolves_attribute_binding(self):
        bound_obj, binding_owner, owner_type = self.binding
        # Look at BoundClass.__get__():
        #   bound_obj = self
        #   binding_owner = obj
        #   owner_type = cls

        self.assertEqual(__, bound_obj.__class__.__name__)
        self.assertEqual(__, binding_owner.__class__.__name__)
        self.assertEqual(AboutMethodBindings, owner_type)

    # ------------------------------------------------------------------

    class SuperColor:
        """A descriptor implementing ``__set__`` to intercept attribute assignment."""
        def __init__(self):
            self.choice = None

        def __set__(self, obj, val):
            self.choice = val

    color = SuperColor()

    def test_set_descriptor_changes_behavior_of_attribute_assignment(self):
        self.assertEqual(None, self.color.choice)
        self.color = 'purple'
        self.assertEqual(__, self.color.choice)

