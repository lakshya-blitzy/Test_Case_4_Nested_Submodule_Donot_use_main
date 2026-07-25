#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Triangle project, part 2: verify that ``triangle()`` rejects illegal side lengths.

This koan drives the error-handling half of the learner-implemented
``triangle()`` classifier function.  Where part 1 (``about_triangle_project.py``)
checks that a well-formed triangle is classified correctly, part 2
confirms that ``triangle()`` raises ``TriangleError`` when the supplied
sides cannot describe a real triangle -- that is, when a side is not
positive or when the sum of two sides does not exceed the third.

Source: koans/triangle.py:L59 (``TriangleError``).
"""

from runner.koan import *

# You need to finish implementing triangle() in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject2(Koan):
    """
    Koan asserting that ``triangle()`` raises ``TriangleError`` for illegal sides.

    Each assertion passes side lengths that cannot describe a valid
    triangle -- either because a side is non-positive or because the
    sides violate the triangle inequality (the sum of any two sides must
    exceed the third) -- and expects ``TriangleError`` to be raised.

    Source: koans/triangle.py:L59 (``TriangleError``).
    """

    # The first assignment did not talk about how to handle errors.
    # Let's handle that part now.
    def test_illegal_triangles_throw_exceptions(self):
        """Assert ``triangle()`` rejects illegal side lengths.

        Source: koans/triangle.py:L59 (``TriangleError``); koans/about_triangle_project2.py:L36-L51 (asserts illegal sides raise it).
        """
        # All sides should be greater than 0
        with self.assertRaises(TriangleError):
            triangle(0, 0, 0)
        with self.assertRaises(TriangleError):
            triangle(3, 4, -5)

        # The sum of any two sides should be greater than the third one
        with self.assertRaises(TriangleError):
            triangle(1, 1, 3)
        with self.assertRaises(TriangleError):
            triangle(2, 5, 2)


