#!/usr/bin/env python
"""Command-line entry point for Python Koans.

Python Koans is an interactive tutorial for learning the Python language by
making a suite of deliberately failing ``unittest`` tests pass, one lesson at
a time. Executing this module begins that journey: it hands control to the
``runner`` package, which runs the selected koans through a custom
``unittest`` result reporter (``Sensei``) and, once a koan fails, focuses the
final report on the first outstanding failure so the learner knows which
lesson to fix next.

Launch flow:

When run as the main program (``__name__ == '__main__'``) the module performs
a Python-version guard before doing any real work:

- If ``sys.version_info < (3, 0)`` -- that is, the script was started with a
  Python 2 interpreter -- it prints a message explaining that this is the
  Python 3 edition of Python Koans and that the user should re-run it with
  ``python3 contemplate_koans.py``, then exits without running any koans.
  Source: contemplate_koans.py:57-61.
- Otherwise, if ``sys.version_info < (3, 7)``, it prints a compatibility
  WARNING (this edition was designed for Python 3.7 or greater) but still
  proceeds. Source: contemplate_koans.py:63-72.
- For supported interpreters it imports ``Mountain`` from ``runner.mountain``
  and calls ``Mountain().walk_the_path(sys.argv)``, forwarding the full
  argument vector so that an optional koan name supplied on the command line
  (for example ``about_asserts``) selects a single lesson instead of the whole
  suite. Source: contemplate_koans.py:74-76.

Usage:

- ``python contemplate_koans.py`` runs the complete set of koans.
- ``python contemplate_koans.py about_asserts`` runs a single named koan.

The convenience launchers ``run.sh`` (Unix/macOS) and ``run.bat`` (Windows)
run the default full suite -- they invoke ``contemplate_koans.py`` with no
arguments and do not forward a koan name -- so selecting a single koan
requires invoking ``python contemplate_koans.py <koan_name>`` directly.

This module defines no functions or classes of its own; all behavior is
delegated to the ``runner`` package (see ``runner/mountain.py``).
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
