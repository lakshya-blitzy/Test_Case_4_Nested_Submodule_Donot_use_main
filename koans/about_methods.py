#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson exploring Python methods and functions.

Works through how Python treats callables: calling conventions and the
wrong-argument ``TypeError``, positional and default arguments and ``*args``
collection, the distinction between methods (which receive ``self``) and
module-level global functions, method redefinition and aliasing, one-line
method bodies, the docstring placed at the beginning of a function, and the
name mangling applied to ``__``-prefixed methods on the nested
:class:`AboutMethods.Dog` fixture.

Source: koans.txt:L10 (entry ``koans.about_methods.AboutMethods``);
``my_global_function`` at koans/about_methods.py:L27, ``AboutMethods`` at
koans/about_methods.py:L35, and the nested ``Dog`` fixture at
koans/about_methods.py:L169.
"""

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *

def my_global_function(a,b):
    """Return the sum ``a + b`` (a module-level function used to contrast global functions with methods.)

    Source: koans/about_methods.py:L27 (definition); consumed by
    ``test_calling_a_global_function`` at koans/about_methods.py:L50.
    """
    return a + b

class AboutMethods(Koan):
    """Koan cases contrasting Python methods with module-level functions.

    The lessons here cover calling conventions and the wrong-argument-count
    ``TypeError``, default and variable (``*args``) arguments, the difference
    between methods bound through ``self`` and global functions, method
    redefinition and aliasing, one-line method bodies, function docstrings,
    and the name mangling applied to ``__``-prefixed attributes on the nested
    :class:`Dog` fixture.

    Source: koans/about_methods.py:L35 (class definition); lesson methods run
    from koans/about_methods.py:L50 through L202, with the nested ``Dog``
    fixture at koans/about_methods.py:L169.
    """

    def test_calling_a_global_function(self):
        self.assertEqual(__, my_global_function(2,3))

    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except TypeError as exception:
            msg = exception.args[0]

        # Note, the text comparison works for Python 3.2
        # It has changed in the past and may change in the future
        self.assertRegex(msg,
            r'my_global_function\(\) missing 2 required positional arguments')

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        # Note, watch out for parenthesis. They need slashes in front!
        self.assertRegex(msg, __)

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(__, self.pointless_method(1, 2))
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        self.assertEqual(__, self.method_with_defaults(1))
        self.assertEqual(__, self.method_with_defaults(1, 2))

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        self.assertEqual(__, self.method_with_var_args())
        self.assertEqual(('one',), self.method_with_var_args('one'))
        self.assertEqual(__, self.method_with_var_args('one', 'two'))

    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, function_with_the_same_name(3,4))

    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(__, self.function_with_the_same_name(3,4))

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        self.assertEqual(__, self.another_method_with_the_same_name())

    def test_that_overlapped_method_is_still_there(self):
        self.assertEqual(__, self.link_to_overlapped_method())

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(__, self.empty_method())

    def test_pass_does_nothing_at_all(self):
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(____, "Still got to this line" != None)

    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        self.assertEqual(__, self.one_line_method())

    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertRegex(self.method_with_documentation.__doc__, __)

    # ------------------------------------------------------------------

    class Dog:
        """Fixture demonstrating Python's method-visibility conventions.

        Exposes a public ``name`` method, a ``_tail`` method whose single
        leading underscore marks it as *private by convention* only, and a
        ``__password`` method whose double leading underscore triggers name
        mangling (it becomes reachable only as ``_Dog__password``).

        Source: koans/about_methods.py:L169 (nested class); ``name`` at L182,
        ``_tail`` at L185, ``__password`` at L189; consumed by tests at
        koans/about_methods.py:L192, L196, L202.
        """

        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual(__, rover.name())

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # This is a little rude, but legal
        self.assertEqual(__, rover._tail())

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        rover = self.Dog()
        with self.assertRaises(___): password = rover.__password()

        # But this still is!
        self.assertEqual(__, rover._Dog__password())

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection
