#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Triangle Project support module for the Python Koans curriculum.

Declares the intentionally-unimplemented ``triangle(a, b, c)`` classifier
stub and the ``TriangleError`` exception exercised by
``about_triangle_project.py`` and ``about_triangle_project2.py``. Learners
implement ``triangle`` themselves; it ships as a ``pass`` stub and is
deliberately left unsolved. Source: koans/triangle.py:L19.
"""

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    pass

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
