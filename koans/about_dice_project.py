#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The Dice project koan.

The learner implements :meth:`DiceSet.roll`, which must populate a
:class:`DiceSet` with ``n`` random dice values, each an integer in the
range 1..6.  The :class:`AboutDiceProject` koan verifies that behavior.
"""

from runner.koan import *

import random

class DiceSet:
    """
    A set of dice values produced by rolling.

    ``DiceSet`` exposes the result of the most recent roll through its
    read-only :attr:`values` property.  The learner implements
    :meth:`roll` so that it generates ``n`` random integers, each in the
    range 1..6, and stores them for retrieval via :attr:`values`.

    :meth:`roll` is intentionally left unimplemented (its body is a
    ``pass``) for the learner to complete.
    """
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        pass

class AboutDiceProject(Koan):
    """
    Koan specifying the expected behavior of :class:`DiceSet`.

    These tests assert that a dice set can be created, that rolling ``n``
    dice yields a list of ``n`` integers between 1 and 6, that the stored
    values do not change until the set is explicitly rolled again, that
    consecutive rolls produce differing values, and that the set can be
    rolled with varying numbers of dice.
    """
    def test_can_create_a_dice_set(self):
        dice = DiceSet()
        self.assertTrue(dice)

    def test_rolling_the_dice_returns_a_set_of_integers_between_1_and_6(self):
        dice = DiceSet()

        dice.roll(5)
        self.assertTrue(isinstance(dice.values, list), "should be a list")
        self.assertEqual(5, len(dice.values))
        for value in dice.values:
            self.assertTrue(value >= 1 and value <= 6, "value " + str(value) + " must be between 1 and 6")

    def test_dice_values_do_not_change_unless_explicitly_rolled(self):
        dice = DiceSet()
        dice.roll(5)
        first_time = dice.values
        second_time = dice.values
        self.assertEqual(first_time, second_time)

    def test_dice_values_should_change_between_rolls(self):
        dice = DiceSet()

        dice.roll(5)
        first_time = dice.values

        dice.roll(5)
        second_time = dice.values

        self.assertNotEqual(first_time, second_time, \
            "Two rolls should not be equal")

        # THINK ABOUT IT:
        #
        # If the rolls are random, then it is possible (although not
        # likely) that two consecutive rolls are equal.  What would be a
        # better way to test this?

    def test_you_can_roll_different_numbers_of_dice(self):
        dice = DiceSet()

        dice.roll(3)
        self.assertEqual(3, len(dice.values))

        dice.roll(1)
        self.assertEqual(1, len(dice.values))
