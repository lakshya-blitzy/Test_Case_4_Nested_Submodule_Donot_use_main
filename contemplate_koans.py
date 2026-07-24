#!/usr/bin/env python

"""Command-line entry point for Python Koans -- the start of the path to enlightenment.

Launch the koan runner from the shell. Before running, this script performs a
Python version gate: it refuses to run under Python 2, printing guidance to
re-invoke the suite with ``python3 contemplate_koans.py``
(Source: contemplate_koans.py:L40-L44), and it prints a compatibility warning when
the running interpreter is older than Python 3.7, the version the koans were
designed for (Source: contemplate_koans.py:L46-L55).

On a supported interpreter the module constructs a ``Mountain`` and calls
``walk_the_path(sys.argv)``, forwarding the full argument vector. ``Mountain``
builds the koan test suite and runs it under the custom ``Sensei`` reporter,
which prints the first failing koan, your progress along the path, and a
closing Zen aphorism (Source: contemplate_koans.py:L57-L59).

Usage::

    python contemplate_koans.py                # run the full path
    python contemplate_koans.py about_asserts  # one lesson, by short name

Exit status: a run that still contains a failing koan exits non-zero (255),
while a fully completed path -- every koan solved -- exits 0. Both codes are
surfaced by the ``Sensei`` reporter.
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

if __name__ == '__main__':
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
              "running it with Python 2!\n\n"
              "Did you accidentally use the wrong Python script? \nTry:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
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

        from runner.mountain import Mountain

        Mountain().walk_the_path(sys.argv)
