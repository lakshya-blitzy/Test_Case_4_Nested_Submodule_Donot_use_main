#!/usr/bin/env python
# encoding: utf-8
"""Provides :class:`WritelnDecorator`, a small file-like stream wrapper (adapted from legacy Python ``unittest``) that adds a ``writeln`` convenience method to any writable stream."""

import sys
import os

# Taken from legacy python unittest
class WritelnDecorator:
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        """Wrap a file-like object, storing it as ``self.stream`` for delegation.

        :param stream: the underlying writable stream (for example
            ``sys.stdout``) that this decorator wraps. For instance
            ``runner/mountain.py`` constructs ``WritelnDecorator(sys.stdout)``
            to route koan output through this wrapper.
        """
        self.stream = stream

    def __getattr__(self, attr):
        """Delegate any undefined attribute to the wrapped stream.

        Attributes not defined on the decorator itself are resolved on the
        wrapped object via ``getattr(self.stream, attr)``, so the decorator
        transparently exposes the stream's own members (such as ``write`` and
        ``flush``). Following standard ``__getattr__`` semantics, this is only
        invoked for attributes missing on the instance, and a failed lookup
        propagates the wrapped stream's ``AttributeError``.

        :param attr: name of the attribute to resolve on the wrapped stream.
        :returns: the corresponding attribute obtained from ``self.stream``.
        """
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        """Write ``arg`` (only when truthy) followed by a trailing newline.

        The optional ``arg`` is written to the stream only if it is truthy, and
        a trailing ``'\\n'`` is then always written. As a result ``writeln()``
        emits a blank line while ``writeln("text")`` emits ``"text\\n"``.
        Text-mode streams translate ``\\n`` to ``\\r\\n`` as needed, as noted by
        the inline comment on the trailing write.

        :param arg: optional string to write before the newline.
        """
        if arg: self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed

