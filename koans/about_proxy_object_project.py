#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The Proxy Object project koan.

This module is the *Proxy Object* project of the Python Koans path to
enlightenment. The learner is asked to complete the :class:`Proxy` class
(started as a stub below) so that it wraps an arbitrary target object,
transparently forwards every attribute access to that wrapped object, and
records the name of each message (attribute) sent through it.

Two koan test cases are registered from this module in ``koans.txt``:

* :class:`AboutProxyObjectProject` -- the specification the learner must
  satisfy; its tests fail until :class:`Proxy` is completed.
* :class:`TelevisionTest` -- already-passing tests exercising the
  :class:`Television` fixture used by the proxy exercise.

The :class:`Television` support fixture defined below is complete and needs
no changes.

Source: koans/about_proxy_object_project.py:L4-L17 (project description).
"""

# Project: Create a Proxy Class
#
# In this assignment, create a proxy class (one is started for you
# below).  You should be able to initialize the proxy object with any
# object.  Any attributes called on the proxy object should be forwarded
# to the target object.  As each attribute call is sent, the proxy should
# record the name of the attribute sent.
#
# The proxy class is started for you.  You will need to add a method
# missing handler and any other supporting methods.  The specification
# of the Proxy class is given in the AboutProxyObjectProject koan.

# Note: This is a bit trickier than its Ruby Koans counterpart, but you
# can do it!

from runner.koan import *

class Proxy:
    """Recording proxy that forwards attribute access to a wrapped object.

    This is the class the learner must complete for the Proxy Object project.
    A :class:`Proxy` is initialized with any ``target_object`` and is expected
    to:

    * forward every attribute read, assignment and method call to the wrapped
      object, and
    * record the name of each attribute (message) accessed so the call history
      can later be queried.

    The full behavioural contract the finished class must satisfy is expressed
    by :class:`AboutProxyObjectProject` (``messages``, ``was_called``,
    ``number_of_times_called`` and graceful handling of invalid messages).

    .. note::
       This is an intentionally unfinished learner exercise. The body below
       only stores the wrapped object in ``self._obj``; the attribute
       forwarding and message-recording behaviour is left for the learner to
       implement.

    Source: koans/about_proxy_object_project.py:L4-L14 (project description).
    """

    def __init__(self, target_object):
        # WRITE CODE HERE

        #initialize '_obj' attribute last. Trust me on this!
        self._obj = target_object

    # WRITE CODE HERE

# The proxy object should pass the following Koan:
#
class AboutProxyObjectProject(Koan):
    """Koan specifying the required behaviour of :class:`Proxy`.

    These tests define the contract a completed :class:`Proxy` must fulfil and
    therefore fail until the learner implements it. Collectively they require
    the proxy to:

    * wrap a target object while remaining an instance of :class:`Proxy`;
    * transparently forward attribute reads, writes and method calls to the
      wrapped object;
    * expose ``messages()`` returning the ordered list of accessed attribute
      names;
    * expose ``was_called(name)`` reporting whether a message was ever sent;
    * expose ``number_of_times_called(name)`` returning the call count for a
      message; and
    * raise :class:`AttributeError` for messages the wrapped object does not
      understand.
    """

    def test_proxy_method_returns_wrapped_object(self):
        # NOTE: The Television class is defined below
        tv = Proxy(Television())

        self.assertTrue(isinstance(tv, Proxy))

    def test_tv_methods_still_perform_their_function(self):
        tv = Proxy(Television())

        tv.channel = 10
        tv.power()

        self.assertEqual(10, tv.channel)
        self.assertTrue(tv.is_on())

    def test_proxy_records_messages_sent_to_tv(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 10

        self.assertEqual(['power', 'channel'], tv.messages())

    def test_proxy_handles_invalid_messages(self):
        tv = Proxy(Television())

        with self.assertRaises(AttributeError):
            tv.no_such_method()


    def test_proxy_reports_methods_have_been_called(self):
        tv = Proxy(Television())

        tv.power()
        tv.power()

        self.assertTrue(tv.was_called('power'))
        self.assertFalse(tv.was_called('channel'))

    def test_proxy_counts_method_calls(self):
        tv = Proxy(Television())

        tv.power()
        tv.channel = 48
        tv.power()

        self.assertEqual(2, tv.number_of_times_called('power'))
        self.assertEqual(1, tv.number_of_times_called('channel'))
        self.assertEqual(0, tv.number_of_times_called('is_on'))

    def test_proxy_can_record_more_than_just_tv_objects(self):
        proxy = Proxy("Py Ohio 2010")

        result = proxy.upper()

        self.assertEqual("PY OHIO 2010", result)

        result = proxy.split()

        self.assertEqual(["Py", "Ohio", "2010"], result)
        self.assertEqual(['upper', 'split'], proxy.messages())

# ====================================================================
# The following code is to support the testing of the Proxy class.  No
# changes should be necessary to anything below this comment.

# Example class using in the proxy testing above.
class Television:
    """Support fixture with a ``channel`` property and a ``power()`` toggle.

    A minimal, complete example object used as the wrapped target in the proxy
    tests. It exposes a read/write ``channel`` property, a ``power()`` method
    that toggles the set between on and off, and ``is_on()`` reporting the
    current power state. No changes to this class are required.
    """

    def __init__(self):
        self._channel = None
        self._power = None

    @property
    def channel(self):
        return self._channel

    @channel.setter
    def channel(self, value):
        self._channel = value

    def power(self):
        if self._power == 'on':
            self._power = 'off'
        else:
            self._power = 'on'

    def is_on(self):
        return self._power == 'on'

# Tests for the Television class.  All of theses tests should pass.
class TelevisionTest(Koan):
    """Passing tests that verify the :class:`Television` support fixture."""

    def test_it_turns_on(self):
        tv = Television()

        tv.power()
        self.assertTrue(tv.is_on())

    def test_it_also_turns_off(self):
        tv = Television()

        tv.power()
        tv.power()

        self.assertFalse(tv.is_on())

    def test_edge_case_on_off(self):
        tv = Television()

        tv.power()
        tv.power()
        tv.power()

        self.assertTrue(tv.is_on())

        tv.power()

        self.assertFalse(tv.is_on())

    def test_can_set_the_channel(self):
        tv = Television()

        tv.channel = 11
        self.assertEqual(11, tv.channel)
