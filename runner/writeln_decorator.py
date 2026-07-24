#!/usr/bin/env python
# encoding: utf-8

"""
stdout/stream decorator for the Python Koans runner engine.

Provides ``WritelnDecorator``, a small wrapper around a file-like object
that adds a convenience ``writeln`` method -- a line-writing helper taken
from legacy Python ``unittest``. Wrapping a stream this way lets the runner
emit a whole line of output without repeating the trailing-newline
boilerplate on every ``write`` call.

Both ``Mountain`` and ``Sensei`` write all koan output through a
``WritelnDecorator`` wrapped around ``sys.stdout`` (Source: runner/mountain.py:L13).
"""

import sys
import os

# Taken from legacy python unittest
class WritelnDecorator:
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        """Store the wrapped file-like ``stream``.

        The decorator keeps a reference to ``stream`` and delegates every
        write and attribute lookup to it, so the wrapper behaves like the
        underlying object while adding the ``writeln`` convenience method.
        """
        self.stream = stream

    def __getattr__(self, attr):
        """Delegate unknown attributes to the wrapped ``stream``.

        Any attribute that is not defined on the decorator itself (for
        example ``write`` or ``flush``) is looked up on the underlying
        ``stream``, so the decorator transparently behaves like the stream
        it wraps.
        """
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        """Write ``arg`` (when truthy) followed by a trailing newline.

        ``arg`` is written to the stream only when it is truthy; a trailing
        newline (``'\\n'``) is then always written afterwards, so calling
        ``writeln`` with no argument simply emits a blank line. Text-mode
        streams translate the newline to ``\\r\\n`` where needed.
        """
        if arg: self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed

