"""Sniffer "scent" configuration for the Python Koans project.

This is the *scent file* read by the third-party ``sniffer`` tool (installed
with ``python3 -m pip install sniffer``). While ``sniffer`` runs, it
continuously watches the paths listed in ``watch_paths`` and, whenever a file
accepted by :func:`py_files` changes, it automatically re-runs the koans via
:func:`execute_koans` -- providing a continuous edit/test feedback loop so the
suite need not be launched by hand after every change.

Two Sniffer hooks are defined:

* :func:`py_files` -- a ``@file_validator`` selecting which files to watch.
* :func:`execute_koans` -- a ``@runnable`` that reruns the koans on change.

This complements the "Sniffer Support" section of ``README.rst``, which notes
that "Sniffer is controlled by ``scent.py``".

Source: scent.py:L1-L12
"""
from sniffer.api import *
import os

# Directories Sniffer monitors for changes: the repository root and koans/.
watch_paths = ['.', 'koans/']

@file_validator
def py_files(filename):
    """Return ``True`` for non-hidden Python source files.

    Registered with Sniffer through the ``@file_validator`` decorator, this
    predicate tells Sniffer which watched files should trigger a rerun: a file
    is accepted only when its name ends in ``.py`` and its basename does not
    start with a dot (``.``), so hidden files and dotfiles are ignored.

    :param filename: Path of the changed file offered by Sniffer.
    :type filename: str
    :returns: ``True`` if ``filename`` is a non-hidden ``.py`` file, ``False``
        otherwise.
    :rtype: bool

    Source: scent.py:L6-L8
    """
    return filename.endswith('.py') and not os.path.basename(filename).startswith('.')

@runnable
def execute_koans(*args):
    """Re-run the koans suite when a watched file changes.

    Registered with Sniffer through the ``@runnable`` decorator, this callback
    is invoked by Sniffer each time a file accepted by :func:`py_files`
    changes. Any callback arguments Sniffer passes are ignored (hence
    ``*args``); the function simply shells out to
    ``python3 -B contemplate_koans.py`` -- the same command used to launch the
    koans manually, where the ``-B`` flag suppresses writing ``.pyc`` bytecode
    files. It returns ``None`` implicitly.

    :param args: Positional callback arguments supplied by Sniffer; unused.
    :returns: ``None``.
    :rtype: NoneType

    Source: scent.py:L10-L12
    """
    os.system('python3 -B contemplate_koans.py')
