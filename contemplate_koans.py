#!/usr/bin/env python
'''
Command-line entry point for Python Koans -- the script a learner runs to
"walk the path" toward enlightenment.

Usage:
    ``python3 contemplate_koans.py``
        Run all koans, in the order declared by the curriculum manifest.
    ``python3 contemplate_koans.py <name>``
        Run a single lesson (``TestCase``), e.g. ``about_strings``, or a single
        test such as ``about_strings.AboutStrings.test_...``.
    `Source: contemplate_koans.py:L61`, `Source: Contributor Notes.txt:L8-L12`.

This is the Python 3 edition. Running it under Python 2 prints an error and
does not run the koans; running it under a Python older than 3.7 prints a
compatibility warning but continues anyway.
`Source: contemplate_koans.py:L38-L54`.

Once the version gate passes, the runner engine is imported lazily and started
via ``runner.mountain.Mountain().walk_the_path(sys.argv)``.
`Source: contemplate_koans.py:L59-L61`.
'''

#
# Acknowledgment:
#
# Python Koans is a port of Ruby Koans originally written by Jim Weirich
# and Joe O'brien of Edgecase. There are some differences and tweaks specific
# to the Python language, but a great deal of it has been copied wholesale.
# So thanks guys!
#

import sys

if __name__ == '__main__':
    # Python 2 guard: this is the Python 3 edition, so refuse to run under
    # Python 2 and point the learner at the correct interpreter.
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
              "running it with Python 2!\n\n"
              "Did you accidentally use the wrong Python script? \nTry:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
        # Soft warning for Python < 3.7 (the koans target 3.7+); continue anyway.
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

        # Import the orchestrator lazily -- only after the version checks pass --
        # then walk the path with the CLI args. The deferred import is intentional
        # so the version messages still appear even on very old interpreters.
        from runner.mountain import Mountain

        Mountain().walk_the_path(sys.argv)
