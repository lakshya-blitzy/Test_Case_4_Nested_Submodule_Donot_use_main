#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import sys

from . import path_to_enlightenment
from .sensei import Sensei
from .writeln_decorator import WritelnDecorator

class Mountain:
    """Top-level orchestrator that runs the koans with the custom ``Sensei``.

    Instantiated by the ``contemplate_koans.py`` launcher. On construction it
    wires together the three collaborators of the runner engine:

    * a ``WritelnDecorator`` around ``sys.stdout`` for convenient line output,
    * the full koan ``TestSuite`` loaded via ``path_to_enlightenment.koans()``, and
    * a ``Sensei`` result renderer bound to that stream.

    Calling :meth:`walk_the_path` then executes the suite through the
    ``Sensei`` and renders the learner's progress.

    Source: runner/mountain.py:L11-L15
    """
    def __init__(self):
        """Build the output stream, load the koan suite, and create the ``Sensei``."""
        self.stream = WritelnDecorator(sys.stdout)
        self.tests = path_to_enlightenment.koans()
        self.lesson = Sensei(self.stream)

    def walk_the_path(self, args=None):
        """Run the koans tests with a custom runner output.

        When invoked with command-line arguments selecting a single lesson
        (``len(args) >= 2``), reloads ``self.tests`` to just that koan module
        (``"koans." + args[1]``); otherwise runs the full suite. The suite is
        executed against the ``Sensei`` result, then ``Sensei.learn()`` renders
        the final report (and may exit the process on failure).

        Args:
            args (list|None): Argument vector (e.g. ``sys.argv``); when a
                second element is present it names the koan module to run.

        Returns:
            Sensei: The result renderer after the run, exposing ``pass_count``,
            ``lesson_pass_count``, and the collected failures.

        Source: runner/mountain.py:L17-L25
        """

        if args and len(args) >=2:
            self.tests = unittest.TestLoader().loadTestsFromName("koans." + args[1])

        self.tests(self.lesson)
        self.lesson.learn()
        return self.lesson
