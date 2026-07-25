#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Koan lesson on deleting objects with ``del`` and its deletion hooks.

Demonstrates deleting list slices and whole names, removing instance and
class attributes, defining deletable managed attributes with both the
four-argument ``property()`` built-in and the ``@property``/``@name.deleter``
decorator form, and intercepting deletions by overriding ``__delattr__``.

Source: koans.txt:L36 (entry ``koans.about_deleting_objects.AboutDeletingObjects``); :class:`AboutDeletingObjects` at koans/about_deleting_objects.py:L17 (tests span koans/about_deleting_objects.py:L23-L160).
"""

from runner.koan import *

class AboutDeletingObjects(Koan):
    """The koan on deleting objects, attributes, and properties.

    Source: koans/about_deleting_objects.py:L17 (class definition); test methods span koans/about_deleting_objects.py:L23-L160; nested fixtures ``ClosingSale`` at koans/about_deleting_objects.py:L38, ``ClintEastwood`` at koans/about_deleting_objects.py:L77, ``Prisoner`` at koans/about_deleting_objects.py:L112, ``MoreOrganisedClosingSale`` at koans/about_deleting_objects.py:L143.
    """

    def test_del_can_remove_slices(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums[1]
        del lottery_nums[2:4]

        self.assertEqual(___, lottery_nums)

    def test_del_can_remove_entire_lists(self):
        lottery_nums = [4, 8, 15, 16, 23, 42]
        del lottery_nums

        with self.assertRaises(___): win = lottery_nums

    # ====================================================================

    class ClosingSale:
        """Fixture with attributes and methods used to demonstrate attribute deletion.

        Source: koans/about_deleting_objects.py:L38 (fixture); exercised by koans/about_deleting_objects.py:L57.
        """

        def __init__(self):
            self.hamsters = 7
            self.zebras = 84

        def cameras(self):
            return 34

        def toilet_brushes(self):
            return 48

        def jellies(self):
            return 5

    def test_del_can_remove_attributes(self):
        crazy_discounts = self.ClosingSale()
        del self.ClosingSale.toilet_brushes
        del crazy_discounts.hamsters

        try:
            still_available = crazy_discounts.toilet_brushes()
        except AttributeError as e:
            err_msg1 = e.args[0]

        try:
            still_available = crazy_discounts.hamsters
        except AttributeError as e:
            err_msg2 = e.args[0]

        self.assertRegex(err_msg1, __)
        self.assertRegex(err_msg2, __)

    # ====================================================================

    class ClintEastwood:
        """Uses a four-argument ``property`` (including a deleter and doc string) to show property deletion.

        Source: koans/about_deleting_objects.py:L77 (fixture); exercised by koans/about_deleting_objects.py:L101.
        """

        def __init__(self):
            self._name = None

        def get_name(self):
            try:
                return self._name
            except:
                return "The man with no name"

        def set_name(self, name):
            self._name = name

        def del_name(self):
            del self._name

        name = property(get_name, set_name, del_name, \
            "Mr Eastwood's current alias")

    def test_del_works_with_properties(self):
        cowboy = self.ClintEastwood()
        cowboy.name = 'Senor Ninguno'
        self.assertEqual('Senor Ninguno', cowboy.name)

        del cowboy.name
        self.assertEqual(__, cowboy.name)


    # ====================================================================

    class Prisoner:
        """Uses the ``@property``/``@name.deleter`` decorator form of a deletable property.

        Source: koans/about_deleting_objects.py:L112 (fixture); exercised by koans/about_deleting_objects.py:L133.
        """

        def __init__(self):
            self._name = None

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, name):
            self._name = name

        @name.deleter
        def name(self):
            self._name = 'Number Six'

    def test_another_way_to_make_a_deletable_property(self):
        citizen = self.Prisoner()
        citizen.name = "Patrick"
        self.assertEqual('Patrick', citizen.name)

        del citizen.name
        self.assertEqual(__, citizen.name)

    # ====================================================================

    class MoreOrganisedClosingSale(ClosingSale):
        """Overrides ``__delattr__`` to intercept deletions.

        Source: koans/about_deleting_objects.py:L143 (fixture); exercised by koans/about_deleting_objects.py:L156.
        """

        def __init__(self):
            self.last_deletion = None
            super().__init__()

        def __delattr__(self, attr_name):
            self.last_deletion = attr_name

    def tests_del_can_be_overriden(self):
        sale = self.MoreOrganisedClosingSale()
        self.assertEqual(__, sale.jellies())
        del sale.jellies
        self.assertEqual(__, sale.last_deletion)
