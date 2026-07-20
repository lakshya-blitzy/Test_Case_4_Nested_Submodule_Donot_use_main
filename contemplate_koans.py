#!/usr/bin/env python
"""Command-line entry point for the Python 3 edition of Python Koans.

Run this module directly under Python 3 to walk the koans::

    python3 contemplate_koans.py                 # walk the full path
    python3 contemplate_koans.py about_asserts   # run a single lesson

When executed as ``__main__`` it first guards on the interpreter version
(rejecting Python 2 outright and warning below Python 3.7), then constructs
``runner.mountain.Mountain`` and calls ``walk_the_path(sys.argv)`` to run the
selected koans and render the learner's progress. Importing the module has no
side effects.

Source: contemplate_koans.py:L31-L61
"""

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thanks guys!
#

import sys

# The koans launcher runs only when this file is executed directly
# (e.g. ``python3 contemplate_koans.py``); importing it has no side effects.
if __name__ == '__main__':
    # A Python 2 interpreter cannot run this Python 3 port: print guidance to
    # re-run under ``python3`` and intentionally do not start the runner.
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
              "running it with Python 2!\n\n"
              "Did you accidentally use the wrong Python script? \nTry:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
        # Python 3 execution path.
        # On Python 3 older than 3.7, warn that Koans targets 3.7+ but still
        # continue on a best-effort basis ("let's see how far we get").
        if sys.version_info < (3, 7):
            print("\n" +
                  "********************************************************\n" +
                  "WARNING:\n" +
                  "This version of Python Koans was designed for " +
                  "Python 3.7 or greater.\n" +
                  "Your version of Python is older, so you may run into " +
                  "problems!\n\n" +
                  "But let's see how far we get...\n" +
                  "********************************************************\n")

        # The runner import is deferred until after the version guard so a
        # Python 2 user still sees the friendly message above.
        # Source: runner/mountain.py:L11
        from runner.mountain import Mountain

        # Forward the full process argv so an optional koan/lesson name can be
        # selected on the command line (e.g. ``... about_asserts``).
        Mountain().walk_the_path(sys.argv)
