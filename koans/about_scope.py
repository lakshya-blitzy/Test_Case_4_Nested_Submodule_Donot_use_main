#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on Python variable scope and name resolution.

Explores how names are looked up and bound across the module, class, and
function scopes: module-level globals, the ``global`` and ``nonlocal``
statements, bare-name resolution, and the fact that class names are *not*
resolved against the enclosing class scope.  The ``Dog`` classes exercised
by these tests are defined in the sibling modules ``jims`` and ``joes``.

Source: koans/jims.py:L20 (``Dog``) and koans/joes.py:L18 (``Dog``).
"""

from runner.koan import *

from . import jims
from . import joes

counter = 0 # Global

class AboutScope(Koan):
    """
    Koan exploring how Python resolves names across module, class, and
    function scopes.

    Demonstrates that bare class names are not looked up in the enclosing
    class scope, the distinction between the ``global`` and ``nonlocal``
    statements, that constants are a naming convention only, and that a
    ``global`` binding may be introduced part way through a class body.

    Source: koans/about_scope.py:L23-L150 (the ``AboutScope`` koan).
    """
    #
    # NOTE:
    #   Look in jims.py and joes.py to see definitions of Dog used
    #   for this set of tests
    #

    def test_dog_is_not_available_in_the_current_scope(self):
        with self.assertRaises(___): fido = Dog()

    def test_you_can_reference_nested_classes_using_the_scope_operator(self):
        fido = jims.Dog()
        # name 'jims' module name is taken from jims.py filename

        rover = joes.Dog()
        self.assertEqual(__, fido.identify())
        self.assertEqual(__, rover.identify())

        self.assertEqual(__, type(fido) == type(rover))
        self.assertEqual(__, jims.Dog == joes.Dog)

    # ------------------------------------------------------------------

    class str:
        """Local class that intentionally shadows the builtin ``str`` inside the class namespace.

        The shadowing is the lesson: this nested class is reachable only
        through the class namespace -- as ``AboutScope.str`` or, from an
        instance, ``self.str`` -- and is a distinct object from the builtin
        ``str``.  A bare, unqualified ``str`` used inside a method does *not*
        search the enclosing class namespace; it resolves through the ordinary
        local -> enclosing -> global -> builtins lookup and therefore refers to
        the builtin ``str``.  Hence ``AboutScope.str`` and ``self.str`` name
        this local class, whereas a bare ``str`` names the builtin.

        Source: koans/about_scope.py:L57-L75 (this nested ``str`` class),
        demonstrated by koans/about_scope.py:L77-L78 (``AboutScope.str`` is
        this class, bare ``str`` is the builtin), koans/about_scope.py:L80-L81
        (``self.str`` is this class) and koans/about_scope.py:L83-L84 (bare
        ``str`` is the builtin).
        """
        pass

    def test_bare_bones_class_names_do_not_assume_the_current_scope(self):
        self.assertEqual(__, AboutScope.str == str)

    def test_nested_string_is_not_the_same_as_the_system_string(self):
        self.assertEqual(__, self.str == type("HI"))

    def test_str_without_self_prefix_stays_in_the_global_scope(self):
        self.assertEqual(__, str == type("HI"))

    # ------------------------------------------------------------------

    PI = 3.1416

    def test_constants_are_defined_with_an_initial_uppercase_letter(self):
        self.assertAlmostEqual(_____, self.PI)
        # Note, floating point numbers in python are not precise.
        # assertAlmostEqual will check that it is 'close enough'

    def test_constants_are_assumed_by_convention_only(self):
        self.PI = "rhubarb"
        self.assertEqual(_____, self.PI)
        # There aren't any real constants in python. Its up to the developer
        # to keep to the convention and not modify them.

    # ------------------------------------------------------------------

    def increment_using_local_counter(self, counter):
        counter = counter + 1

    def increment_using_global_counter(self):
        global counter
        counter = counter + 1

    def test_incrementing_with_local_counter(self):
        global counter
        start = counter
        self.increment_using_local_counter(start)
        self.assertEqual(__, counter == start + 1)

    def test_incrementing_with_global_counter(self):
        global counter
        start = counter
        self.increment_using_global_counter()
        self.assertEqual(__, counter == start + 1)

    # ------------------------------------------------------------------

    def local_access(self):
        stuff = 'eels'
        def from_the_league():
            stuff = 'this is a local shop for local people'
            return stuff
        return from_the_league()

    def nonlocal_access(self):
        stuff = 'eels'
        def from_the_boosh():
            nonlocal stuff
            return stuff
        return from_the_boosh()

    def test_getting_something_locally(self):
        self.assertEqual(__, self.local_access())

    def test_getting_something_nonlocally(self):
        self.assertEqual(__, self.nonlocal_access())

    # ------------------------------------------------------------------

    global deadly_bingo
    deadly_bingo = [4, 8, 15, 16, 23, 42]

    def test_global_attributes_can_be_created_in_the_middle_of_a_class(self):
        self.assertEqual(__, deadly_bingo[5])
