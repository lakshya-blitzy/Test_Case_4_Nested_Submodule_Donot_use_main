#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on monkey patching.

Monkey patching is the practice of adding or replacing attributes and
methods on an existing class at runtime.  This lesson demonstrates
patching a plain, user-defined class (:class:`AboutMonkeyPatching.Dog`)
to teach it a new trick, explains why most built-in classes (such as
:class:`int`) cannot be monkey patched, and shows that user-defined
subclasses of those built-ins (:class:`AboutMonkeyPatching.MyInt`) can
be patched freely.
"""

#
# Related to AboutOpenClasses in the Ruby Koans
#

from runner.koan import *

class AboutMonkeyPatching(Koan):
    """Koan exploring runtime monkey patching of Python classes."""

    class Dog:
        """Simple class that gains a ``wag()`` method via monkey patching."""

        def bark(self):
            return "WOOF"

    def test_as_defined_dogs_do_bark(self):
        fido = self.Dog()
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    # Add a new method to an existing class.
    def test_after_patching_dogs_can_both_wag_and_bark(self):
        def wag(self): return "HAPPY"
        self.Dog.wag = wag

        fido = self.Dog()
        self.assertEqual(__, fido.wag())
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    def test_most_built_in_classes_cannot_be_monkey_patched(self):
        try:
            int.is_even = lambda self: (self % 2) == 0
        except Exception as ex:
            err_msg = ex.args[0]

        self.assertRegex(err_msg, __)

    # ------------------------------------------------------------------

    class MyInt(int):
        """``int`` subclass: subclasses of built-ins CAN be patched."""
        pass

    def test_subclasses_of_built_in_classes_can_be_be_monkey_patched(self):
        self.MyInt.is_even = lambda self: (self % 2) == 0

        self.assertEqual(__, self.MyInt(1).is_even())
        self.assertEqual(__, self.MyInt(2).is_even())
