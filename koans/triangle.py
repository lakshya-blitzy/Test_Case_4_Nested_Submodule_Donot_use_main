#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Triangle Project module: the learner-implemented :func:`triangle` side-length
classifier together with its companion :class:`TriangleError`.

:func:`triangle` reports the type of a triangle -- ``'equilateral'``,
``'isosceles'`` or ``'scalene'`` -- from the lengths of its three sides. Its
body is intentionally left unimplemented for the student to complete, so this
module ships as an unsolved exercise. The koans that drive it live in
``about_triangle_project.py`` and ``about_triangle_project2.py``.

Source: koans/triangle.py:L17-L31 (Triangle Project contract comment) and koans/triangle.py:L32 (``triangle`` definition); consumers koans/about_triangle_project.py:L28-L63 (``AboutTriangleProject``) and koans/about_triangle_project2.py:L22-L51 (``AboutTriangleProject2``).
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
    """
    Classify a triangle from the lengths of its three sides.

    Given the side lengths ``a``, ``b`` and ``c``, return the type of triangle
    they form:

    * ``'equilateral'`` -- if all three sides are equal;
    * ``'isosceles'``   -- if exactly two sides are equal;
    * ``'scalene'``     -- if no sides are equal.

    :param a: length of the first side of the triangle.
    :param b: length of the second side of the triangle.
    :param c: length of the third side of the triangle.
    :returns: one of ``'equilateral'``, ``'isosceles'`` or ``'scalene'``.

    .. note::
       This is a learner exercise: the body is intentionally left as ``pass``
       for the student to implement, so the function returns ``None`` until the
       classification logic has been written.

    Source: koans/triangle.py:L32 (``triangle`` definition) and koans/triangle.py:L56 (learner ``pass`` stub); consumer koans/about_triangle_project.py:L38-L63 (classification tests calling ``triangle``).
    """
    # DELETE 'PASS' AND WRITE THIS CODE
    pass

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    """Exception raised for an invalid triangle; used by the part-2 koan.

    Source: koans/triangle.py:L59 (``TriangleError`` definition); consumer
    koans/about_triangle_project2.py:L36-L51 (``triangle`` raises it for invalid inputs).
    """
    pass
