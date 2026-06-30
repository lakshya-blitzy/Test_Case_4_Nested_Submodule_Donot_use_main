#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    '''
    Orchestrates a single koans session -- the small engine that
    ``contemplate_koans.py`` hands control to in order to "walk the path".

    A ``Mountain`` wires together the output stream, the ordered suite of
    koans and the ``Sensei`` reporter, then runs the suite (either the
    full curriculum or a single named lesson) and prints the progress
    summary.

    Source: runner/mountain.py:L11-L25
    '''
    def __init__(self):
        '''
        Wire up a session's collaborators.

        Builds the line-oriented output stream by wrapping ``sys.stdout``
        in a ``WritelnDecorator``, loads the default ordered koans suite
        via ``path_to_enlightenment.koans()``, and creates the ``Sensei``
        reporter bound to that stream.

        Source: runner/mountain.py:L12-L15
        '''
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        '''
        Run the koans tests with a custom runner output. Returns the
        ``Sensei`` that observed the run.

        When ``args`` has at least two elements -- i.e. a lesson name was
        given on the command line, as in ``contemplate_koans.py
        about_strings`` -- the run is narrowed to that single lesson via
        ``unittest.TestLoader().loadTestsFromName("koans." + args[1])``;
        otherwise the full ordered suite loaded in ``__init__`` runs. The
        selected suite is executed against the ``Sensei`` result, then
        ``lesson.learn()`` prints the final report card. Returns the
        ``Sensei`` instance (``self.lesson``).

        Source: runner/mountain.py:L17-L25
        '''

        if args and len(args) >=2:
            self.tests = unittest.TestLoader().loadTestsFromName("koans." + args[1])

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
