#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan exercises for function-based decorators.

Demonstrates two decorators implemented as plain functions:
``addcowbell`` attaches an attribute to the wrapped function without
changing its behavior, while ``xmltag`` wraps the decorated function so
its return value is surrounded by XML-style tag markup.
"""

from runner.koan import *


class AboutDecoratingWithFunctions(Koan):
    """
    Koan exploring decorators defined as functions.

    Pairs each decorator with a method it decorates: ``addcowbell`` tags
    ``mediocre_song`` with a ``wow_factor`` attribute, and ``xmltag`` wraps
    ``render_tag`` so its return value is enclosed in XML-style tag markup.
    """

    def addcowbell(fn):
        fn.wow_factor = 'COWBELL BABY!'
        return fn

    @addcowbell
    def mediocre_song(self):
        return "o/~ We all live in a broken submarine o/~"

    def test_decorators_can_modify_a_function(self):
        self.assertRegex(self.mediocre_song(), __)
        self.assertEqual(__, self.mediocre_song.wow_factor)

    # ------------------------------------------------------------------

    def xmltag(fn):
        def func(*args):
            return '<' + fn(*args) + '/>'
        return func

    @xmltag
    def render_tag(self, name):
        return name

    def test_decorators_can_change_a_function_output(self):
        self.assertEqual(__, self.render_tag('llama'))
