#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on single inheritance -- subclassing, overriding, and ``super()``.

Works through how a subclass inherits attributes and behavior from its parent,
adds new behavior of its own, overrides an inherited method, and reuses the
parent implementation cooperatively through ``super()``. It closes by
contrasting a subclass whose ``__init__`` forgets to call the base initializer
with one that correctly delegates via ``super().__init__``, using the nested
:class:`AboutInheritance.Dog` fixture family (``Chihuahua``, ``BullDog``,
``GreatDane``, ``Pug``, and ``Greyhound``).

Source: koans.txt:L29 (entry ``koans.about_inheritance.AboutInheritance``); :class:`AboutInheritance` at koans/about_inheritance.py:L20 (tests span koans/about_inheritance.py:L62-L146).
"""

from runner.koan import *

class AboutInheritance(Koan):
    """
    Koan test cases about single inheritance and ``super()``.

    Each ``test_*`` method exercises one of the nested ``Dog`` fixture classes
    to illustrate a facet of inheritance: ancestry and ``issubclass`` checks,
    behavior inherited from and added on top of the parent, method overriding,
    cooperative calls to the parent implementation through ``super()``, and the
    fact that a base ``__init__`` is not invoked automatically unless the
    subclass calls it explicitly.

    Source: koans/about_inheritance.py:L20 (class definition); test methods span koans/about_inheritance.py:L62-L146; nested fixtures ``Dog`` at koans/about_inheritance.py:L34, ``Chihuahua`` at koans/about_inheritance.py:L50, ``BullDog`` at koans/about_inheritance.py:L91, ``GreatDane`` at koans/about_inheritance.py:L107, ``Pug`` at koans/about_inheritance.py:L122, ``Greyhound`` at koans/about_inheritance.py:L131.
    """

    class Dog:
        """Base fixture class: a dog with a ``name`` property and a ``bark()`` that returns ``"WOOF"``.

        Source: koans/about_inheritance.py:L34 (fixture); exercised by koans/about_inheritance.py:L62, koans/about_inheritance.py:L75, koans/about_inheritance.py:L82.
        """

        def __init__(self, name):
            self._name = name

        @property
        def name(self):
            return self._name

        def bark(self):
            return "WOOF"

    class Chihuahua(Dog):
        """Subclass that adds a ``wag()`` behavior and overrides ``bark()`` to return ``"yip"``.

        Source: koans/about_inheritance.py:L50 (fixture); exercised by koans/about_inheritance.py:L62, koans/about_inheritance.py:L65, koans/about_inheritance.py:L71, koans/about_inheritance.py:L75, koans/about_inheritance.py:L82.
        """

        def wag(self):
            return "happy"

        def bark(self):
            return "yip"

    def test_subclasses_have_the_parent_as_an_ancestor(self):
        self.assertEqual(__, issubclass(self.Chihuahua, self.Dog))

    def test_all_classes_in_python_3_ultimately_inherit_from_object_class(self):
        self.assertEqual(__, issubclass(self.Chihuahua, object))

        # Note: This isn't the case in Python 2. In that version you have
        # to inherit from a built in class or object explicitly

    def test_instances_inherit_behavior_from_parent_class(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.name)

    def test_subclasses_add_new_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.wag())

        fido = self.Dog("Fido")
        with self.assertRaises(___): fido.wag()

    def test_subclasses_can_modify_existing_behavior(self):
        chico = self.Chihuahua("Chico")
        self.assertEqual(__, chico.bark())

        fido = self.Dog("Fido")
        self.assertEqual(__, fido.bark())

    # ------------------------------------------------------------------

    class BullDog(Dog):
        """Subclass that extends ``bark()`` by appending to the parent result via ``super()``.

        Source: koans/about_inheritance.py:L91 (fixture); exercised by koans/about_inheritance.py:L101.
        """

        def bark(self):
            return super().bark() + ", GRR"
            # Note, super() is much simpler to use in Python 3!

    def test_subclasses_can_invoke_parent_behavior_via_super(self):
        ralph = self.BullDog("Ralph")
        self.assertEqual(__, ralph.bark())

    # ------------------------------------------------------------------

    class GreatDane(Dog):
        """Subclass that calls the parent ``bark()`` from a different method, ``growl()``.

        Source: koans/about_inheritance.py:L107 (fixture); exercised by koans/about_inheritance.py:L116.
        """

        def growl(self):
            return super().bark() + ", GROWL"

    def test_super_works_across_methods(self):
        george = self.GreatDane("George")
        self.assertEqual(__, george.growl())

    # ---------------------------------------------------------

    class Pug(Dog):
        """Subclass whose ``__init__`` intentionally does not call the base initializer.

        Source: koans/about_inheritance.py:L122 (fixture); exercised by koans/about_inheritance.py:L140.
        """

        def __init__(self, name):
            pass

    class Greyhound(Dog):
        """Subclass whose ``__init__`` correctly calls the base initializer via ``super()``.

        Source: koans/about_inheritance.py:L131 (fixture); exercised by koans/about_inheritance.py:L144.
        """

        def __init__(self, name):
            super().__init__(name)

    def test_base_init_does_not_get_called_automatically(self):
        snoopy = self.Pug("Snoopy")
        with self.assertRaises(___): name = snoopy.name

    def test_base_init_has_to_be_called_explicitly(self):
        boxer = self.Greyhound("Boxer")
        self.assertEqual(__, boxer.name)
