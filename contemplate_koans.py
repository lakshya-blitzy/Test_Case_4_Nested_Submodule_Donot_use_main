#!/usr/bin/env python

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
    # This is the Python 3 port of the koans: reject Python 2 outright and
    # point the user at the correct interpreter instead of running the suite.
    if sys.version_info < (3, 0):
        print("\nThis is the Python 3 version of Python Koans, but you are " +
              "running it with Python 2!\n\n"
              "Did you accidentally use the wrong Python script? \nTry:\n\n" +
              "    python3 contemplate_koans.py\n")
    else:
        # 3.7 is the minimum version the koans were designed for; on older 3.x
        # we only warn (and still attempt the run) rather than hard-stop.
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

        # Hand control to the test runner. sys.argv is forwarded so an optional
        # koan name (e.g. "about_strings") can target a single lesson.
        Mountain().walk_the_path(sys.argv)
