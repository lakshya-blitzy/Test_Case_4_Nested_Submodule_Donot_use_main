#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Runner-level coordinator for the Python Koans.

``Mountain`` is the thin layer that wires a koans run together: it builds
the ordered test suite via ``path_to_enlightenment``, wraps ``sys.stdout``
in a ``WritelnDecorator``, and binds a custom ``Sensei`` result/reporter to
that stream, then walks (runs) the path.

It is the object the command-line entry point drives --
``contemplate_koans.py`` launches the whole experience with
``Mountain().walk_the_path(sys.argv)`` (Source: contemplate_koans.py:L57-L59).
'''

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    '''
    Runner-level coordinator for a single koans run.

    Builds the koan ``unittest`` suite and runs it under the custom
    ``Sensei`` result/reporter, optionally narrowing the run to a single
    named lesson supplied on the command line.

    Source: runner/mountain.py:L24
    '''

    def __init__(self):
        '''
        Set up the coordinator for a run.

        Wraps ``sys.stdout`` in a ``WritelnDecorator`` (``self.stream``),
        builds the default koan suite via ``path_to_enlightenment.koans()``
        (``self.tests``), and creates a ``Sensei`` result bound to that
        stream (``self.lesson``).

        Source: runner/mountain.py:L35-L48
        '''
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        "Run the koans tests with a custom runner output."

        if args and len(args) >=2:
            self.tests = unittest.TestLoader().loadTestsFromName("koans." + args[1])

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
