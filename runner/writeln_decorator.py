#!/usr/bin/env python
# encoding: utf-8

import sys
import os

# Taken from legacy python unittest
class WritelnDecorator:
    """Used to decorate file-like objects with a handy 'writeln' method.

    A transparent wrapper (adapted from the legacy ``unittest`` utility) that
    stores the wrapped stream as ``self.stream`` and delegates every unknown
    attribute to it via ``__getattr__``. Wrapped streams therefore remain
    fully usable while gaining a convenient ``writeln`` helper. Newline
    translation (line feed to carriage-return/line-feed) remains the
    responsibility of the wrapped stream.

    Source: runner/writeln_decorator.py:L8
    """
    def __init__(self,stream):
        """Store the wrapped stream for later attribute delegation.

        Args:
            stream: The file-like object to wrap. It is saved as
                ``self.stream`` and every unknown attribute access is
                forwarded to it by ``__getattr__``.

        Source: runner/writeln_decorator.py:L10
        """
        self.stream = stream

    def __getattr__(self, attr):
        """Delegate unknown attribute lookups to the wrapped stream.

        Invoked only when normal attribute resolution fails, so attributes
        set on the decorator itself (such as ``self.stream``) are returned
        directly and never routed here. This delegation is what allows the
        ``self.write(...)`` calls inside ``writeln`` to transparently reach
        the wrapped stream's ``write`` method.

        Args:
            attr: Name of the attribute requested on the decorator.

        Returns:
            The attribute of the same name resolved on the wrapped stream.

        Source: runner/writeln_decorator.py:L13
        """
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        """Write ``arg`` (only when truthy), then always write a trailing newline.

        Args:
            arg: Optional text to write before the newline. When ``None`` or
                otherwise falsy, only the newline is written.

        Returns:
            None. All output is delegated to the wrapped stream's ``write``
            method (resolved through ``__getattr__``).

        Source: runner/writeln_decorator.py:L16
        """
        if arg: self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed

