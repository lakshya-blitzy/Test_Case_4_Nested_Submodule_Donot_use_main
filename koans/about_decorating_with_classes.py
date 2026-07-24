#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan exercises on class-based decorators.

Demonstrates building decorators as classes: composing a callable with
``functools.partial``, using a callable descriptor class (``doubleit``) as a
method decorator, using a parametrized decorator class (``documenter``) that
rewrites ``__doc__``, and chaining multiple decorators on a single method.

Source: koans.txt:L28 (entry
``koans.about_decorating_with_classes.AboutDecoratingWithClasses``);
AboutDecoratingWithClasses at koans/about_decorating_with_classes.py:L23,
the ``doubleit`` descriptor decorator at L62, and the ``documenter``
parametrized decorator at L106.
"""

from runner.koan import *

import functools

class AboutDecoratingWithClasses(Koan):
    """Koan lesson exploring decorators implemented as classes.

    Source: koans/about_decorating_with_classes.py:L23 (class definition);
    ``functools.partial`` lessons at L37, L47, L53; the ``doubleit`` descriptor
    at L62 and ``documenter`` at L106; decorator chaining tested at L155.
    """

    def maximum(self, a, b):
        if a>b:
            return a
        else:
            return b

    def test_partial_that_wrappers_no_args(self):
        """
        Before we can understand this type of decorator we need to consider
        the partial.
        """
        max = functools.partial(self.maximum)

        self.assertEqual(__, max(7,23))
        self.assertEqual(__, max(10,-10))

    def test_partial_that_wrappers_first_arg(self):
        max0 = functools.partial(self.maximum, 0)

        self.assertEqual(__, max0(-4))
        self.assertEqual(__, max0(5))

    def test_partial_that_wrappers_all_args(self):
        always99 = functools.partial(self.maximum, 99, 20)
        always20 = functools.partial(self.maximum, 9, 20)

        self.assertEqual(__, always99())
        self.assertEqual(__, always20())

    # ------------------------------------------------------------------

    class doubleit:
        def __init__(self, fn):
            self.fn = fn

        def __call__(self, *args):
            return self.fn(*args) + ', ' + self.fn(*args)

        def __get__(self, obj, cls=None):
            if not obj:
                # Decorating an unbound function
                return self
            else:
                # Decorating a bound method
                return functools.partial(self, obj)

    @doubleit
    def foo(self):
        return "foo"

    @doubleit
    def parrot(self, text):
        return text.upper()

    def test_decorator_with_no_arguments(self):
        # To clarify: the decorator above the function has no arguments, even
        # if the decorated function does

        self.assertEqual(__, self.foo())
        self.assertEqual(__, self.parrot('pieces of eight'))

    # ------------------------------------------------------------------

    def sound_check(self):
        #Note: no decorator
        return "Testing..."

    def test_what_a_decorator_is_doing_to_a_function(self):
        #wrap the function with the decorator
        self.sound_check = self.doubleit(self.sound_check)

        self.assertEqual(__, self.sound_check())

    # ------------------------------------------------------------------

    class documenter:
        """Parametrized decorator class that wraps a function and sets its ``__doc__``, appending to any existing docstring.

        Source: koans/about_decorating_with_classes.py:L106 (class);
        ``__init__`` at L115, ``__call__`` at L118; applied at L128
        (``count_badly``), L135 (``idler``), and in the chain at L149-L152
        (``homer``); consumed by tests at L140-L145 and L155-L157.
        """

        def __init__(self, *args):
            self.fn_doc = args[0]

        def __call__(self, fn):
            def decorated_function(*args):
                return fn(*args)

            if fn.__doc__:
                decorated_function.__doc__ = fn.__doc__ + ": " + self.fn_doc
            else:
                decorated_function.__doc__ = self.fn_doc
            return decorated_function

    @documenter("Increments a value by one. Kind of.")
    def count_badly(self, num):
        num += 1
        if num==3:
            return 5
        else:
            return num
    @documenter("Does nothing")
    def idler(self, num):
        "Idler"
        pass

    def test_decorator_with_an_argument(self):
        self.assertEqual(__, self.count_badly(2))
        self.assertEqual(__, self.count_badly.__doc__)

    def test_documentor_which_already_has_a_docstring(self):
        self.assertEqual(__, self.idler.__doc__)

    # ------------------------------------------------------------------

    @documenter("DOH!")
    @doubleit
    @doubleit
    def homer(self):
        return "D'oh"

    def test_we_can_chain_decorators(self):
        self.assertEqual(__, self.homer())
        self.assertEqual(__, self.homer.__doc__)

