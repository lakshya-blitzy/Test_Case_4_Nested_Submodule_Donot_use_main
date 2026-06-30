'''
Sniffer ("scent") configuration that enables *continuous testing* of the
Python Koans.

Sniffer watches the project for file changes and automatically reruns the
koans whenever a watched file is modified, mirroring the "Sniffer Support"
section of the project ``README``. Sniffer is an external, optional developer
tool -- it is installed separately with ``pip install sniffer`` (for example,
``python3 -m pip install sniffer``) and is **not** a runtime dependency of the
koans application, which runs on the Python standard library alone. The
wildcard import ``from sniffer.api import *`` is required because it exposes
the ``@file_validator`` and ``@runnable`` decorators that Sniffer looks for in
this configuration module.

This module defines three pieces of configuration that Sniffer consumes:

``watch_paths``
    The directories Sniffer monitors for changes: the project root (``.``)
    and the ``koans/`` directory. ``Source: scent.py:L4``

``py_files`` (decorated with ``@file_validator``)
    Restricts which file changes trigger a rerun. It reacts only to files
    ending in ``.py`` whose basename does not start with ``.`` -- that is,
    real Python sources rather than hidden or temporary files.
    ``Source: scent.py:L6-L8``

``execute_koans`` (decorated with ``@runnable``)
    The action Sniffer runs on each trigger. It shells out via ``os.system``
    to run ``python3 -B contemplate_koans.py``; the ``-B`` flag suppresses
    the writing of ``.pyc`` bytecode files. ``Source: scent.py:L10-L12``
'''

from sniffer.api import *
import os

# Directories Sniffer watches for changes: the project root and the koans/ folder.
watch_paths = ['.', 'koans/']

# File filter: react only to non-hidden Python (.py) files.
@file_validator
def py_files(filename):
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

# Action run on each change: execute all koans (-B suppresses .pyc bytecode).
@runnable
def execute_koans(*args):
    os.system('python3 -B contemplate_koans.py')
