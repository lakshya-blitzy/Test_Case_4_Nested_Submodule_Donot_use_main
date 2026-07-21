"""Sniffer autotest configuration for Python Koans.

Configures Sniffer, an autotest tool that watches the project's files and
automatically re-runs the koans whenever a watched file changes, giving a fast
edit/save/test feedback loop while you work through the lessons.
Source: scent.py:1,4.

Sniffer is enabled by installing it (``pip install sniffer``) and then running
the ``sniffer`` command from the project root; it is "controlled by
``scent.py``" as documented in the README's "Sniffer Support" section. The
module-level ``watch_paths`` list tells Sniffer which directories to monitor:
``'.'`` (the project root) and ``'koans/'`` (the lesson directory).
Source: scent.py:4.

Two Sniffer hooks are registered below:

* ``py_files()`` -- a ``@file_validator`` selecting which file changes count.
* ``execute_koans()`` -- a ``@runnable`` that launches the koans on a change.
"""

from sniffer.api import *
import os

watch_paths = ['.', 'koans/']

@file_validator
def py_files(filename):
    """Sniffer ``@file_validator`` hook: accept only non-hidden Python files.

    Returns ``True`` only when ``filename`` ends in ``.py`` and its basename
    does not start with a dot, so that solely changes to visible Python source
    files trigger a koans re-run. Source: scent.py:6-8.
    """
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

@runnable
def execute_koans(*args):
    """Sniffer ``@runnable`` hook: re-run the koans on a watched-file change.

    Ignores its hook arguments and synchronously launches the koans via
    ``os.system('python3 -B contemplate_koans.py')``; the ``-B`` flag
    suppresses ``.pyc`` bytecode cache generation. Source: scent.py:10-12.
    """
    os.system('python3 -B contemplate_koans.py')
