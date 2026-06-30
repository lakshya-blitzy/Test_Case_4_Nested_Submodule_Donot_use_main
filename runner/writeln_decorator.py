#!/usr/bin/env python
# encoding: utf-8

import sys
import os

# Taken from legacy python unittest
class WritelnDecorator:
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        """Wrap and retain the given file-like ``stream``.

        Source: runner/writeln_decorator.py:L10-L11"""
        self.stream = stream

    def __getattr__(self, attr):
        """Delegate unknown attribute access transparently to the wrapped
        ``stream`` (so the decorator behaves like the stream it wraps).

        Source: runner/writeln_decorator.py:L13-L14"""
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        """Write the optional ``arg`` (when given) followed by a newline.

        On text-mode streams the newline is translated to a
        carriage-return/newline pair (CRLF) as needed.

        Source: runner/writeln_decorator.py:L16-L18"""
        if arg: self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed

