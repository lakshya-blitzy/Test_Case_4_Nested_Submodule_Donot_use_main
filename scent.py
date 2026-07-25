'''
Sniffer configuration for Python Koans.

Sniffer provides continuous, auto-rerun test execution: whenever a
watched ``.py`` file changes on disk, the koans are re-run
automatically, giving a fast red/green feedback loop while filling in
the blanks.

Activate it by installing ``sniffer`` together with an operating-system
filesystem-event backend (``pyinotify`` on Linux, ``pywin32`` on
Windows or ``MacFSEvents`` on macOS) and running the ``sniffer``
command from the project root, as described in ``README.rst`` (see the
"Sniffer Support" section).

The module-level ``watch_paths = ['.', 'koans/']`` lists the directories
Sniffer monitors for changes.

Source: scent.py:L24 (``watch_paths``); scent.py:L27-L37
(``py_files`` file-validator); scent.py:L40-L54 (``execute_koans`` runnable).
'''
from sniffer.api import *
import os

watch_paths = ['.', 'koans/']

@file_validator
def py_files(filename):
    '''
    Returns ``True`` for non-hidden Python source files.

    Sniffer file-validator hook: accepts only filenames ending in
    ``.py`` whose basename does not start with ``.``, so the koans are
    re-run only when a real (non-hidden) Python source file changes.

    Source: scent.py:L27-L37 (this ``py_files`` file-validator).
    '''
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

@runnable
def execute_koans(*args):
    '''
    Re-runs the koans whenever a watched file changes.

    Sniffer runnable hook invoked on each detected change. It
    synchronously runs ``python3 -B contemplate_koans.py`` (the ``-B``
    flag suppresses ``.pyc`` bytecode caching, so no stale bytecode is
    written during the watch loop).

    The ``*args`` parameter receives the change metadata Sniffer passes
    to runnable hooks; it is intentionally unused here.

    Source: scent.py:L40-L54 (this ``execute_koans`` runnable); it runs contemplate_koans.py:L57-L59 (the ``Mountain().walk_the_path`` entry point).
    '''
    os.system('python3 -B contemplate_koans.py')
