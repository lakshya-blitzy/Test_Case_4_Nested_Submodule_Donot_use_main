#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Python Koans' own test-runner engine.

The ``runner`` package implements the layered runtime pipeline that
powers the Python Koans: launch -> coordinate -> build-suite ->
execute -> report.

Pipeline components:

- ``mountain.Mountain`` is the runner-level coordinator: it wires the
  output stream, the koan suite, and the reporter together, then walks
  the path (Source: runner/mountain.py:L24).
- ``path_to_enlightenment`` builds the ordered ``unittest`` suite from
  the ``koans.txt`` manifest
  (Source: runner/path_to_enlightenment.py:L14).
- ``sensei.Sensei`` is the custom ``unittest`` result/reporter that
  captures the first failing koan, counts progress, and prints
  colorized, Zen-flavored output (Source: runner/sensei.py:L32).

Supporting modules:

- ``koan`` -- the ``Koan`` base ``TestCase`` plus the learner-facing
  placeholder sentinels.
- ``writeln_decorator`` -- a thin ``stdout`` wrapper that adds a
  ``writeln`` method.
- ``helper`` -- small introspection helpers used by the reporter.
- ``mockable_test_result`` -- a mockable seam over
  ``unittest.TestResult`` that eases unit-testing the reporter.
'''

# Namespace: runner

