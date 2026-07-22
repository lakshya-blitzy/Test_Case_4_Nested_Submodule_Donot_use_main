============
Python Koans
============

.. image:: https://travis-ci.org/gregmalcolm/python_koans.png?branch=master
   :target: http://travis-ci.org/gregmalcolm/python_koans

.. image:: https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod
    :target: https://gitpod.io/#https://github.com/gregmalcolm/python_koans
    
.. image:: https://www.eclipse.org/che/contribute.svg
    :target: https://workspaces.openshift.com/f?url=https://gitpod.io/#https://github.com/gregmalcolm/python_koans

One click installation:
-----------------------

.. image:: https://www.eclipse.org/che/contribute.svg
    :target: https://workspaces.openshift.com/f?url=https://gitpod.io/#https://github.com/gregmalcolm/python_koans
|   or
.. image:: https://gitpod.io/button/open-in-gitpod.svg
    :target: https://gitpod.io/#https://gitpod.io/#https://github.com/gregmalcolm/python_koans

|

Python Koans is a port of Edgecase's "Ruby Koans" which can be found
at http://rubykoans.com/.

.. image:: https://user-images.githubusercontent.com/2614930/28401740-ec6214b2-6cd0-11e7-8afd-30ed3102bfd6.png

Python Koans is an interactive tutorial for learning the Python programming
language by making tests pass.

Most tests are *fixed* by filling the missing parts of assert functions. Eg:

.. code-block:: python

    self.assertEqual(__, 1+2)

which can be fixed by replacing the __ part with the appropriate code:

.. code-block:: python

    self.assertEqual(3, 1+2)

Occasionally you will encounter some failing tests that are already filled out.
In these cases you will need to finish implementing some code to progress. For
example, there is an exercise for writing some code that will tell you if a
triangle is equilateral, isosceles or scalene.

As well as being a great way to learn some Python, it is also a good way to get
a taste of Test Driven Development (TDD).


.. contents:: Table of Contents
   :depth: 2
   :backlinks: top


Downloading Python Koans
------------------------

Python Koans is available on GitHub:

* https://github.com/gregmalcolm/python_koans

You can clone with Git or download the source as a zip/gz/bz2.


Cloning with Git Submodules
---------------------------

This repository embeds other repositories as **Git submodules**, so a plain
``git clone`` leaves the submodule directories empty. The parent repository
(this repo) declares the submodule ``Submodule_01_Do_not_use_15Jun`` -- a
collection of GitHub ``.gitignore`` templates -- in its ``.gitmodules``
manifest (Source: .gitmodules:1-3). That submodule in turn declares a nested
submodule, ``Submodule_02_Do_not_use_15Jun`` -- a Node.js/Express app
(Source: Submodule_01_Do_not_use_15Jun/.gitmodules:1-3).

Per the documentation scope for this project, *every* submodule is treated as
a first-class part of the project. To fetch the parent and all nested
submodules in a single step, clone recursively:

.. code-block:: sh

    git clone --recurse-submodules --branch blitzy-d8650f2e-6762-4465-a4d2-f314ea37d85b https://github.com/lakshya-blitzy/Test_Case_4_Nested_Submodule_Donot_use_main.git

If you have already cloned without ``--recurse-submodules``, initialise and
pull the submodules afterwards with:

.. code-block:: sh

    git submodule update --init --recursive

See the `Repository Map / Submodules`_ section below for a diagram of the full
three-level chain and links into each submodule's own documentation.


Installing Python Koans
-----------------------

Aside from downloading or checking out the latest version of Python Koans, you
need to install the Python interpreter.

At this time of writing, we support Python 3. The policy is to try to keep
current with the latest production version.

You should be able to work with newer Python versions, but older ones will
likely give you problems.

You can download Python from here:

* https://www.python.org/downloads/

After installing Python make sure the folder containing the python executable
is in the system path. In other words, you need to be able to run Python from a
command console. It will either be ``python3`` or for Windows it will be ``python.exe``.

If you have problems, this may help:

* https://www.python.org/about/gettingstarted/

Windows users may also want to update the line in the batch file ``run.bat`` to
set the python path (Source: run.bat:8)::

    SET PYTHON_PATH=C:\Python311


Getting Started
---------------

Jake Hebbert has created a couple of screencasts available here:

https://www.youtube.com/watch?v=e2WXgXEjbHY&list=PL5Up_u-XkWgNcunP_UrTJG_3EXgbK2BQJ&index=1

Or if you prefer to read:

From a \*nix terminal or Windows command prompt run::

.. code-block:: sh

    python contemplate_koans.py

or:

.. code-block:: sh

    python3 contemplate_koans.py

In my case I'm using Python 3 with Windows, so I fire up my command
shell (cmd.exe) and run this:

.. image:: https://user-images.githubusercontent.com/2614930/28401747-f723ff00-6cd0-11e7-9b9a-a6993b753cf6.png

Apparently a test failed::

    AssertionError: False is not True

It also tells me exactly where the problem is, it's an assert on line 12
of ``.\\koans\\about_asserts.py``. This one is easy, just change ``False`` to ``True`` to
make the test pass.

Sooner or later you will likely encounter tests where you are not sure what the
expected value should be. For example:

.. code-block:: python

    class Dog:
        pass

    def test_objects_are_objects(self):
        fido = self.Dog()
        self.assertEqual(__, isinstance(fido, object))

This is where the Python Command Line can come in handy. In this case I can
fire up the command line, recreate the scenario and run queries:

.. image:: https://user-images.githubusercontent.com/2614930/28401750-f9dcb296-6cd0-11e7-98eb-c20318eada33.png

API / Module Reference
----------------------

Beyond the koan lessons themselves, Python Koans ships a small test-runner
framework in the ``runner/`` package together with a command-line entry
point. This section documents that public surface. Every module and function
below now carries a PEP 257 docstring -- the language-appropriate equivalent
of "JSDoc on all functions" for this Python repository -- so the same
reference is available from a terminal via ``pydoc`` (for example
``pydoc runner.mountain``) or the built-in ``help()`` function.

Command-line entry point: contemplate_koans.py
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The script you run to begin the koans. When executed as the main program it
first performs a Python-version guard: it refuses to run under Python 2 and
prints a WARNING (but still proceeds) for interpreters older than Python 3.7
(Source: contemplate_koans.py:56-72). On a supported interpreter it imports
``Mountain`` and calls ``Mountain().walk_the_path(sys.argv)``, forwarding the
full argument vector so an optional koan name selects a single lesson
(Source: contemplate_koans.py:74-76).

* ``python contemplate_koans.py`` -- run the complete suite of koans.
* ``python contemplate_koans.py about_asserts`` -- run a single named koan
  (Source: contemplate_koans.py:33-34).

Run coordinator: runner.mountain.Mountain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The thin coordinator that loads, runs, and reports a single koan run
(Source: runner/mountain.py:23). It owns two members:

``__init__(self)``
    Wires the three collaborators used during a run: a
    ``WritelnDecorator(sys.stdout)`` output stream, the default suite loaded
    via ``path_to_enlightenment.koans()``, and a ``Sensei`` reporter bound to
    that stream (Source: runner/mountain.py:56-58).

``walk_the_path(self, args=None)``
    Runs the selected suite through the ``Sensei`` reporter, calls ``learn()``
    to render the outcome, and returns the reporter.

    :param args: an ``argv``-like sequence (typically ``sys.argv``); when it
        has at least two elements, ``args[1]`` names a single ``koans.<name>``
        lesson loaded in place of the full default suite
        (Source: runner/mountain.py:83-84).
    :returns: the ``Sensei`` reporter, after the suite has been run and
        ``learn()`` has rendered the result (Source: runner/mountain.py:86-88).

Suite loader: runner.path_to_enlightenment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Loads the ordered koan curriculum. The module constant
``KOANS_FILENAME = 'koans.txt'`` names the default manifest
(Source: runner/path_to_enlightenment.py:14).

* ``filter_koan_names(lines)`` -- generator that strips whitespace and yields
  only non-blank, non-comment names
  (Source: runner/path_to_enlightenment.py:17-28).
* ``names_from_file(filename)`` -- opens a UTF-8 file and yields the
  fully-qualified ``TestCase`` names inside, one per line
  (Source: runner/path_to_enlightenment.py:31-39).
* ``koans_suite(names)`` -- builds an order-preserving ``unittest.TestSuite``
  (it sets ``loader.sortTestMethodsUsing = None`` to keep source order)
  (Source: runner/path_to_enlightenment.py:42-53).
* ``koans(filename=KOANS_FILENAME)`` -- composes the helpers above to return
  the full default suite (Source: runner/path_to_enlightenment.py:56-62).

Tutorial reporter: runner.sensei.Sensei
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A custom ``unittest.TestResult`` reporter (a subclass of
``MockableTestResult``) that renders colored, tutorial-style feedback
(Source: runner/sensei.py:27). Importing the module initialises the vendored
``libs.colorama`` so ANSI colors work across platforms
(Source: runner/sensei.py:24-25). As the suite runs it prints a
``Thinking <ClassName>`` heading once per lesson
(Source: runner/sensei.py:66-88) and tracks two counters, ``pass_count`` and
``lesson_pass_count`` (Source: runner/sensei.py:62-63). When the run
finishes, ``learn()`` prints the progress summary and a rotating Zen message
(Source: runner/sensei.py:360) and calls ``sys.exit(-1)`` if any failures
remain (Source: runner/sensei.py:185-211).

Lesson scaffold: runner.koan
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The exercise-facing scaffold that every lesson imports via
``from runner.koan import *``. Its ``__all__`` exports five learner
placeholders (Source: runner/koan.py:41):

* ``__`` -- fill-in string sentinel ``"-=> FILL ME IN! <=-"``
  (Source: runner/koan.py:43).
* ``___`` -- a placeholder ``Exception`` subclass for ``assertRaises``
  lessons (Source: runner/koan.py:45).
* ``____`` -- true/false string sentinel ``"-=> TRUE OR FALSE? <=-"``
  (Source: runner/koan.py:55).
* ``_____`` -- numeric sentinel ``0`` (Source: runner/koan.py:57).
* ``Koan`` -- the ``unittest.TestCase`` subclass that every lesson
  (``class AboutXxx(Koan)``) inherits from (Source: runner/koan.py:60).

Test seam: runner.mockable_test_result.MockableTestResult
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

An empty, patchable ``unittest.TestResult`` subclass. It adds no behavior of
its own; it exists purely as a mocking seam so the runner's own unit tests
can patch it (and ``Sensei`` subclasses it) without mocking the
standard-library base class out of existence
(Source: runner/mockable_test_result.py:26-40).

Stream wrapper: runner.writeln_decorator.WritelnDecorator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Wraps a writable stream (Source: runner/writeln_decorator.py:15). It
delegates any undefined attribute to the wrapped stream through
``__getattr__`` (Source: runner/writeln_decorator.py:27-40) and adds a
``writeln(arg=None)`` method that writes ``arg`` (only when truthy) followed
by a trailing newline (Source: runner/writeln_decorator.py:42-54).

Class-name helper: runner.helper.cls_name
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

``cls_name(obj)`` returns ``obj.__class__.__name__`` -- the name of an
object's class as a string. ``Sensei`` uses it to detect when execution
advances to a new koan/test class (Source: runner/helper.py:12-27).

Curriculum manifest: koans.txt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ordered curriculum manifest: 39 fully-qualified koan ``TestCase`` names,
loaded and run in the order listed. Lines beginning with ``#`` are ignored
(Source: koans.txt:1-40).

Runner class relationships (diagram D-4)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: mermaid

    classDiagram
        class TestResult
        class MockableTestResult
        class Sensei
        class Mountain
        class Koan
        TestResult <|-- MockableTestResult
        MockableTestResult <|-- Sensei
        Mountain --> Sensei : reports via
        Mountain --> Koan : loads

Launch / Running the Koans
--------------------------

Python Koans is a local command-line program; "deployment" here means the
different ways to launch the koan runner. All of them ultimately execute
``contemplate_koans.py``.

Unix / macOS
    Run ``./run.sh``, which executes ``python3 -B contemplate_koans.py`` (the
    ``-B`` flag disables ``.pyc`` bytecode caching) (Source: run.sh:3). You
    can equally run ``python3 contemplate_koans.py`` directly.

Windows
    Run ``run.bat``, an interactive launcher. Point it at your interpreter by
    editing the ``SET PYTHON_PATH=C:\Python311`` line to match your install
    (Source: run.bat:8); it then runs ``python.exe -B contemplate_koans.py``
    (Source: run.bat:5) and, after each run, prompts ``Test again? y or n``
    so you can loop without restarting (Source: run.bat:39).

Gitpod (one click)
    The badges at the top of this README open the project in a ready-to-code
    Gitpod workspace. ``.gitpod.yml`` declares the start task
    ``python contemplate_koans.py`` (Source: .gitpod.yml:5); the workspace
    image is built from ``.gitpod.Dockerfile``
    (``FROM gitpod/workspace-full:latest``, then
    ``pip3 install pytest==4.4.2 pytest-testdox mock``)
    (Source: .gitpod.Dockerfile:7-11).

Continuous integration
    Travis CI runs the project on Python 3.9 and executes
    ``python _runner_tests.py`` -- the runner framework's own self-test
    suite, not the koans (Source: .travis.yml:3-7). The config also carries
    commented ``contemplate_koans.py`` sample lines from a fork -- one runs
    the full suite and the other lists lesson names (Source: .travis.yml:8-9).
    Note, however, that the current CLI runs either the full suite or exactly
    one named lesson: ``walk_the_path`` consumes only ``args[1]``
    (Source: runner/mountain.py:83-84), so the second name in the sample
    ``about_asserts about_none`` line is ignored rather than run as a subset.

    The self-test suite targets Python 3.9 and passes on any Python 3 release
    older than 3.12. On Python 3.12 and newer it reports two errors because
    ``unittest.TestCase.assertEquals`` -- still used by
    ``runner/runner_tests/test_helper.py`` (Source:
    runner/runner_tests/test_helper.py:14) -- was removed from ``unittest`` in
    Python 3.12. Run the self-tests under Python 3.9 (as CI does); the koan
    curriculum (``python contemplate_koans.py``) is unaffected and runs on any
    supported Python 3 interpreter.

For a fast edit/save/test loop while working through the lessons, see the
`Sniffer Support`_ section below; Sniffer re-runs the koans automatically on
file changes and is controlled by ``scent.py``, whose ``execute_koans`` hook
launches ``python3 -B contemplate_koans.py`` (Source: scent.py:36-44).

Sniffer Support
---------------

Sniffer allows you to run the tests continuously. If you modify any files files
in the koans directory, it will rerun the tests.

To set this up, you need to install sniffer:

.. code-block:: sh

    python3 -m pip install sniffer

You should also run one of these libraries depending on your system. This will
automatically trigger sniffer when a file changes, otherwise sniffer will have
to poll to see if the files have changed.

On Linux:

.. code-block:: sh

    python3 -m pip install pyinotify

On Windows:

.. code-block:: sh

    python3 -m pip install pywin32

    Also available here:

    https://github.com/mhammond/pywin32/releases

On macOS:

.. code-block:: sh

    python3 -m pip install MacFSEvents

Once it is set up, you just run:

.. code-block:: sh

    sniffer

Just modify one of the koans files and you'll see that the tests are triggered
automatically. Sniffer is controlled by ``scent.py``.

Inline Code Explanations
------------------------

The parent repository's runner framework and entry points are documented
inline with PEP 257 docstrings -- the Python-language equivalent of adding
JSDoc to every JavaScript function. You can read these explanations without
leaving the terminal:

.. code-block:: sh

    python -c "import runner.mountain; help(runner.mountain.Mountain)"
    pydoc runner.sensei

End-to-end, a koan run flows through the framework like this:

1. ``contemplate_koans.py`` guards the Python version, then constructs a
   ``Mountain`` and calls ``walk_the_path(sys.argv)``
   (Source: contemplate_koans.py:74-76).
2. ``Mountain.__init__`` builds the output stream, the default suite, and the
   ``Sensei`` reporter (Source: runner/mountain.py:56-58); ``walk_the_path``
   optionally swaps in a single named koan, then runs the suite and calls
   ``learn()`` (Source: runner/mountain.py:83-88).
3. ``path_to_enlightenment.koans()`` builds the suite by reading the ordered
   ``koans.txt`` manifest (Source: runner/path_to_enlightenment.py:56-62).
4. ``Sensei`` reports each result as the suite runs and, at the end, prints
   the progress summary and exits non-zero while any koan remains unsolved
   (Source: runner/sensei.py:185-211).

Repository Map / Submodules
---------------------------

Python Koans is the top of a three-level nested Git-submodule chain, and this
documentation effort treats **every** submodule as a first-class part of the
project -- no submodule is skipped, despite the ``Do_not_use`` directory
names.

* **Parent -- Python Koans** (this repository): the interactive Python
  tutorial documented by this ``README.rst`` and the ``runner/`` framework
  docstrings.
* **Submodule 01 -- .gitignore templates**
  (``Submodule_01_Do_not_use_15Jun``): GitHub's collection of ``.gitignore``
  file templates, declared in this repo's ``.gitmodules``
  (Source: .gitmodules:1-3). See
  `Submodule 01 - .gitignore templates <Submodule_01_Do_not_use_15Jun/README.md>`_.
* **Submodule 02 -- Node.js/Express app** (nested inside Submodule 01 at
  ``Submodule_01_Do_not_use_15Jun/Submodule_02_Do_not_use_15Jun``): the
  Heroku "nodejs-getting-started" application, declared in Submodule 01's
  own ``.gitmodules`` (Source: Submodule_01_Do_not_use_15Jun/.gitmodules:1-3).
  Its README is reachable from the Submodule 01 README linked above.

.. code-block:: mermaid

    graph TD
        P["Parent repo: Python Koans<br/>README.rst + runner/ docstrings"]
        S1["Submodule_01_Do_not_use_15Jun<br/>.gitignore templates collection<br/>README.md"]
        S2["Submodule_02_Do_not_use_15Jun (nested)<br/>Node.js/Express app<br/>README.md + JSDoc in index.js, test.js"]
        P -->|".gitmodules"| S1
        S1 -->|".gitmodules (nested)"| S2
        P -.->|"README link"| S1
        S1 -.->|"README link"| S2

Getting the Most From the Koans
-------------------------------

Quoting the Ruby Koans instructions:

	"In test-driven development the mantra has always been, red, green,
	refactor. Write a failing test and run it (red), make the test pass
	(green), then refactor it (that is look at the code and see if you
	can make it any better). In this case you will need to run the koan
	and see it fail (red), make the test pass (green), then take a
	moment and reflect upon the test to see what it is teaching you
	and improve the code to better communicate its intent (refactor)."



Finding More Koan Projects
--------------------------

There are number of other great Koan projects out there for various languages
and frameworks. Most of them can be found in GitHub. Also there is a little
koans activity on Bitbucket.

* GitHub koan projects:
    https://github.com/search?q=koans&ref=cmdform

* Bitbucket koan projects:
    https://bitbucket.org/repo/all?name=koans

Translations
------------

Translations are always welcome! Feel free to add one to this README
if you happen to work on one:

https://github.com/mswell/python_koans_br

Acknowledgments
---------------

Thanks go to Jim Weirich and Joe O'Brien for the original Ruby Koans that the
Python Koans is based on! Also the Ruby Koans in turn borrows from Metakoans
so thanks also go to Ara Howard for that!

Also thanks to everyone who has contributed to Python Koans! I got a great
headstart by taking over a code base initiated by the combined Mikes of
FPIP. So here's a little plug for their very cool Python podcast:

* https://www.frompythonimportpodcast.com/

A big thanks also to Mike Pirnat @pirnat and Kevin Chase @kjc have pitched in
as co-maintainers at various times
