#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Triangle project koan, part 1: classify a triangle by its side lengths.

Exercises the learner-implemented ``triangle(a, b, c)`` function defined in
:mod:`koans.triangle`.  Each ``test_*`` method supplies three side lengths and
asserts that ``triangle`` returns the correct classification string:

* ``'equilateral'`` -- all three sides are equal,
* ``'isosceles'``   -- exactly two sides are equal,
* ``'scalene'``     -- no two sides are equal.

The tests fail until the learner replaces the stub body of ``triangle`` with a
working implementation; part 2 (error handling) lives in
``about_triangle_project2.py``.

Source: koans/triangle.py:L19
"""

from runner.koan import *

# You need to write the triangle method in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject(Koan):
    """Koan verifying that :func:`triangle` returns the correct classification.

    Checks that ``triangle(a, b, c)`` yields ``'equilateral'`` for
    equal-sided inputs, ``'isosceles'`` for inputs with exactly two equal
    sides, and ``'scalene'`` for inputs with no two sides equal.
    """

    def test_equilateral_triangles_have_equal_sides(self):
        """A triangle with all three sides equal is ``'equilateral'``."""
        self.assertEqual('equilateral', triangle(2, 2, 2))
        self.assertEqual('equilateral', triangle(10, 10, 10))

    def test_isosceles_triangles_have_exactly_two_sides_equal(self):
        """A triangle with exactly two sides equal is ``'isosceles'``."""
        self.assertEqual('isosceles', triangle(3, 4, 4))
        self.assertEqual('isosceles', triangle(4, 3, 4))
        self.assertEqual('isosceles', triangle(4, 4, 3))
        self.assertEqual('isosceles', triangle(10, 10, 2))

    def test_scalene_triangles_have_no_equal_sides(self):
        """A triangle with no two sides equal is ``'scalene'``."""
        self.assertEqual('scalene', triangle(3, 4, 5))
        self.assertEqual('scalene', triangle(10, 11, 12))
        self.assertEqual('scalene', triangle(5, 4, 2))
