#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Greed dice-game scoring project koan.

This koan presents the classic *Greed* scoring exercise. The learner is
expected to implement the module-level :func:`score` function so that it
computes the Greed score for a single roll of the dice, following the rules
described in the comment block below. The :class:`AboutScoringProject` koan
then verifies that implementation against a series of expected-score
assertions.

The scoring exercise is intentionally left unimplemented (``score`` is a
learner stub); the koan fails until the learner fills it in.

Source: koans.txt:L21 (entry ``koans.about_scoring_project.AboutScoringProject``); :func:`score` at koans/about_scoring_project.py:L50; :class:`AboutScoringProject` at koans/about_scoring_project.py:L81 (tests span koans/about_scoring_project.py:L93-L161); Greed scoring rules at koans/GREEDS_RULES.txt:L12-L19.
"""

from runner.koan import *

# Greed is a dice game where you roll up to five dice to accumulate
# points.  The following "score" function will be used to calculate the
# score of a single roll of the dice.
#
# A greed roll is scored as follows:
#
# * A set of three ones is 1000 points
#
# * A set of three numbers (other than ones) is worth 100 times the
#   number. (e.g. three fives is 500 points).
#
# * A one (that is not part of a set of three) is worth 100 points.
#
# * A five (that is not part of a set of three) is worth 50 points.
#
# * Everything else is worth 0 points.
#
#
# Examples:
#
# score([1,1,1,5,1]) => 1150 points
# score([2,3,4,6,2]) => 0 points
# score([3,4,5,3,3]) => 350 points
# score([1,5,1,2,4]) => 250 points
#
# More scoring examples are given in the tests below:
#
# Your goal is to write the score method.

def score(dice):
    """Return the total Greed score for a single roll of the dice.

    Given an iterable of individual die values from one roll, compute and
    return the roll's Greed score according to the rules documented in the
    comment block above and in ``koans/GREEDS_RULES.txt``:

    * Three 1s score 1000 points.
    * Three of any other number ``n`` score ``n * 100`` points
      (for example, three 5s score 500).
    * Each remaining 1 that is not part of a triple scores 100 points.
    * Each remaining 5 that is not part of a triple scores 50 points.
    * All other dice score 0 points.

    A single die is only ever counted once within a roll (a 5 contributes to
    a triple *or* as an individual 50, never both).

    :param dice: An iterable of integer die values (typically 1 through 6)
        produced by a single roll. An empty iterable scores 0.
    :returns: The total Greed score for ``dice`` as an ``int``.

    .. note::
       This is a learner exercise. The body is intentionally left as ``pass``
       so that :class:`AboutScoringProject` fails until the method is
       implemented. Do not treat the current ``None`` return as the contract.

    Source: koans/about_scoring_project.py:L50 (learner-implemented function under test); Greed scoring rules at koans/GREEDS_RULES.txt:L12-L19.
    """
    # You need to write this method
    pass

class AboutScoringProject(Koan):
    """Koan that verifies the learner's :func:`score` implementation.

    Each ``test_*`` method asserts the expected Greed score for a specific
    roll of the dice, collectively covering empty rolls, single 1s and 5s,
    triples, mixed rolls, and the "a die counts once" rule. Every assertion
    fails until the module-level :func:`score` function is correctly
    implemented per the Greed scoring rules.

    Source: koans/about_scoring_project.py:L81 (class definition); test methods span koans/about_scoring_project.py:L93-L161.
    """

    def test_score_of_an_empty_list_is_zero(self):
        """Verify that scoring an empty roll yields 0 points.

        Source: koans/about_scoring_project.py:L93.
        """
        self.assertEqual(0, score([]))

    def test_score_of_a_single_roll_of_5_is_50(self):
        """Verify that a lone 5 scores 50 points.

        Source: koans/about_scoring_project.py:L100; koans/GREEDS_RULES.txt:L19.
        """
        self.assertEqual(50, score([5]))

    def test_score_of_a_single_roll_of_1_is_100(self):
        """Verify that a lone 1 scores 100 points.

        Source: koans/about_scoring_project.py:L107; koans/GREEDS_RULES.txt:L18.
        """
        self.assertEqual(100, score([1]))

    def test_score_of_multiple_1s_and_5s_is_the_sum_of_individual_scores(self):
        """Verify that loose 1s and 5s score as the sum of their values.

        Source: koans/about_scoring_project.py:L114; koans/GREEDS_RULES.txt:L18-L19.
        """
        self.assertEqual(300, score([1,5,5,1]))

    def test_score_of_single_2s_3s_4s_and_6s_are_zero(self):
        """Verify that non-scoring singles (2, 3, 4, 6) contribute 0 points.

        Source: koans/about_scoring_project.py:L121.
        """
        self.assertEqual(0, score([2,3,4,6]))

    def test_score_of_a_triple_1_is_1000(self):
        """Verify that three 1s score 1000 points.

        Source: koans/about_scoring_project.py:L128; koans/GREEDS_RULES.txt:L12.
        """
        self.assertEqual(1000, score([1,1,1]))

    def test_score_of_other_triples_is_100x(self):
        """Verify that a triple of n (other than 1) scores n * 100 points.

        Source: koans/about_scoring_project.py:L135; koans/GREEDS_RULES.txt:L13-L17.
        """
        self.assertEqual(200, score([2,2,2]))
        self.assertEqual(300, score([3,3,3]))
        self.assertEqual(400, score([4,4,4]))
        self.assertEqual(500, score([5,5,5]))
        self.assertEqual(600, score([6,6,6]))

    def test_score_of_mixed_is_sum(self):
        """Verify that mixed rolls sum triple and single contributions.

        Source: koans/about_scoring_project.py:L146; koans/GREEDS_RULES.txt:L12-L19.
        """
        self.assertEqual(250, score([2,5,2,2,3]))
        self.assertEqual(550, score([5,5,5,5]))
        self.assertEqual(1150, score([1,1,1,5,1]))

    def test_ones_not_left_out(self):
        """Verify that a lone 1 is still scored alongside a scoring triple of 2s (three 2s score 200).

        Source: koans/about_scoring_project.py:L155; koans/GREEDS_RULES.txt:L17-L18.
        """
        self.assertEqual(300, score([1,2,2,2]))
        self.assertEqual(350, score([1,5,2,2,2]))
