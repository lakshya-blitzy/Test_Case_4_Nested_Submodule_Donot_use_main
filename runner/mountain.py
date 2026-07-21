#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Runner-level coordinator that runs the Python Koans lessons.

This module defines ``Mountain``, the thin coordinator that wires the loaded
koan test suite to the ``Sensei`` reporter and runs it. ``Mountain`` is the
object the command-line entry point instantiates and drives: at launch,
``contemplate_koans.py`` imports this class, constructs a single instance, and
calls ``walk_the_path(sys.argv)`` on it -- so this module is effectively the
top of the runner framework's call stack.

Source: contemplate_koans.py:32-34
"""

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    """Coordinate a single koan run: load, run, and report.

    A ``Mountain`` owns the three collaborators needed to run the koans and
    present the outcome to the learner:

    * ``stream`` -- a ``WritelnDecorator`` wrapping ``sys.stdout`` that adds a
      line-oriented ``writeln`` method for the reporter's output.
    * ``tests`` -- the loaded koan suite (a ``unittest``-compatible callable),
      by default every lesson listed in ``koans.txt``.
    * ``lesson`` -- a ``Sensei`` reporter (a custom ``unittest.TestResult``)
      that both collects the test results and renders them to ``stream``.

    It is deliberately minimal: it is not a CLI argument parser and not a
    resource manager. It simply loads the suite, runs it through the ``Sensei``,
    and reports the result. This mirrors the runner API reference in README.rst.
    """

    def __init__(self):
        """Construct a runner with its output stream, suite, and reporter.

        Building a ``Mountain`` wires together the three collaborators later
        used by ``walk_the_path``:

        1. Wrap ``sys.stdout`` in a ``WritelnDecorator`` and store it as
           ``self.stream``.
        2. Load the default koan suite via ``path_to_enlightenment.koans()``
           and store it as ``self.tests``.
        3. Create a ``Sensei`` reporter bound to that stream and store it as
           ``self.lesson``.

        Source: runner/mountain.py:56-58
        """
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        """Run the koans tests with a custom runner output.

        When ``args`` is truthy and has at least two elements, the default
        suite loaded in ``__init__`` is replaced by a single named lesson,
        loaded via ``unittest.TestLoader().loadTestsFromName("koans." +
        args[1])`` -- so ``python contemplate_koans.py about_asserts`` runs only
        that koan. Otherwise the full default suite is used.
        (Source: runner/mountain.py:83-84)

        The selected suite is then run through the ``Sensei`` reporter
        (``self.tests(self.lesson)``); ``self.lesson.learn()`` renders the
        outcome (printing the progress report and calling ``sys.exit(-1)`` when
        koans remain unsolved); and the ``Sensei`` result object is returned.
        (Source: runner/mountain.py:86-88)

        :param args: Optional ``argv``-like sequence, typically ``sys.argv``.
            When it contains at least two elements, ``args[1]`` names a single
            ``koans.<name>`` lesson to run in place of the full suite.
        :returns: The ``Sensei`` lesson/result object after the suite has been
            run and reported.
        """

        if args and len(args) >=2:
            self.tests = unittest.TestLoader().loadTestsFromName("koans." + args[1])

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
