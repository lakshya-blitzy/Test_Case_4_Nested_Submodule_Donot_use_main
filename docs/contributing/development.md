# Contributing & Development

How to set up, extend, and verify Python Koans — the contributor workflow for adding koans, running the runner self-tests, continuous testing, and following the project's docstring conventions.

## Overview

Python Koans is a pure-Python, standard-library-only interactive tutorial — a port of Ruby Koans — in which a learner "walks the path to enlightenment" by editing failing `unittest` exercises until they pass. Contributors generally work in one of two areas: the *koans* themselves (the fill-in-the-blank `about_*` lessons under `koans/`) and the *runner* engine under `runner/` that discovers, runs, and reports on them. Everything runs with a Python 3 interpreter alone — there is **no package to install**, and the repository ships no `requirements.txt`, `setup.py`, or `pyproject.toml`. `Source: ../../contemplate_koans.py:L14-L34`.

At a glance, a full run reports **304 koans across 37 lessons**, while the curriculum manifest (`koans.txt`) lists **39** ordered `TestCase` entries; the reasons these three numbers differ are covered in the [curriculum reference](../curriculum.md). `Source: ../../runner/sensei.py:L251-L269`, `Source: ../../runner/sensei.py:L258-L259`, `Source: ../../koans.txt:L1-L40`.

New here? Start at the [documentation home](../index.md) for orientation, and read the [architecture overview](../architecture/overview.md) to see how the engine fits together before diving in.

## Project layout

The project is organized into three packages — `runner/`, `koans/`, and `libs/` — plus a handful of top-level entrypoints, the curriculum manifest, and launcher scripts.

```text
.
├── contemplate_koans.py          # CLI entry point: version gate -> Mountain().walk_the_path(sys.argv)
├── _runner_tests.py              # Runner self-test aggregator (the command CI runs)
├── scent.py                      # Sniffer continuous-test configuration
├── koans.txt                     # Curriculum manifest: 39 ordered TestCase entries
├── run.sh  /  run.bat            # Unix / Windows launcher scripts
├── runner/                       # The engine package (orchestration, discovery, reporting)
│   ├── mountain.py               #   Mountain orchestrator
│   ├── path_to_enlightenment.py  #   manifest-driven discovery
│   ├── sensei.py                 #   progress / failure reporter
│   ├── koan.py                   #   Koan base TestCase + sentinels
│   ├── helper.py                 #   small helpers (e.g. cls_name)
│   ├── mockable_test_result.py   #   mockable TestResult seam
│   ├── writeln_decorator.py      #   stream / output decorator
│   └── runner_tests/             #   the runner's OWN unit tests
├── koans/                        # The curriculum: about_*.py lessons + helpers + a_package_folder/
└── libs/                         # Vendored third-party code (colorama, mock) — not modified
```

`Source: ../../contemplate_koans.py:L14-L34`, `Source: ../../koans.txt:L1-L40`, `Source: ../../scent.py:L4-L12`.

| Path | Role | Notes |
|------|------|-------|
| `runner/` | The **engine** package: orchestration (`Mountain`), manifest-driven discovery (`path_to_enlightenment`), reporting (`Sensei`), the `Koan` base, and output helpers. Its own unit tests live in `runner/runner_tests/`. | The primary target for engine contributions. See the [runner-engine API reference](../api-reference/runner-engine.md) and the [architecture overview](../architecture/overview.md). |
| `koans/` | The **curriculum**: 40-plus `about_*.py` lesson modules plus helper modules (`triangle.py`, `local_module.py`, `jims.py`, `joes.py`, …) and the `a_package_folder/` package. These are the fill-in-the-blank exercises. | Referenced descriptively only — never solve or otherwise spoil a lesson (see [Adding a koan](#adding-a-koan)). |
| `libs/` | **Vendored** third-party code — `libs/colorama/` (terminal colors) and `libs/mock.py`. | Out of scope for this documentation effort; not modified. |
| `contemplate_koans.py` | The **CLI entry point**: it runs a version gate, then bootstraps the engine via `Mountain().walk_the_path(sys.argv)`. | `Source: ../../contemplate_koans.py:L14-L34`. |
| `_runner_tests.py` | The **runner self-test aggregator** that assembles the engine's own `unittest` suite. | `Source: ../../_runner_tests.py:L7-L26`. |
| `koans.txt` | The ordered **curriculum manifest**: 39 fully-qualified `TestCase` entries on lines 2–40 (line 1 is a `#` comment). | `Source: ../../koans.txt:L1-L40`. |
| `run.sh` / `run.bat` | **Launchers** for Unix (`python3 -B contemplate_koans.py`) and Windows. | Launcher details live in the [CLI usage guide](../guides/cli-usage.md). |
| `scent.py` | **Sniffer** continuous-test configuration. | `Source: ../../scent.py:L4-L12`. |

> A top-level `Submodule_01_Do_not_use_15Jun/` directory also exists in the tree. As its name indicates, it is **not part of this project** — ignore it entirely; it is neither documented nor modified here.

## Adding a koan

A koan is a `unittest` test case whose assertions contain *sentinels* — deliberately wrong placeholder values that the learner replaces to make the test pass. Adding one is a three-step, order-aware process.

**1. Create a lesson module.** Add `koans/about_<topic>.py`. Each lesson imports the koan toolkit and defines one or more `TestCase` subclasses of `Koan` — the project base class, which is itself `class Koan(unittest.TestCase)`. By convention a lesson begins with `from runner.koan import *` and declares `class About<Topic>(Koan):`. `Source: ../../runner/koan.py:L22-L23`.

**2. Write `test_*` methods using sentinels.** Name test methods `test_*` and place a sentinel wherever the learner must supply the answer. Show only the *unsolved* form — never a solved value:

```python
from runner.koan import *

class AboutNewTopic(Koan):
    def test_a_concept(self):
        # The learner replaces the __ sentinel with the correct value.
        self.assertEqual(__, 1 + 1)
```

The four sentinels are exported from `runner/koan.py` via `__all__`, alongside `Koan`. Their **intent** (never their answers) is described below. `Source: ../../runner/koan.py:L12-L19`.

| Sentinel | Purpose |
|----------|---------|
| `__` | A value to fill in (its placeholder string is `"-=> FILL ME IN! <=-"`). |
| `___` | A custom `Exception` subclass, for koans that expect an error to be raised. |
| `____` | A true/false placeholder (its placeholder string is `"-=> TRUE OR FALSE? <=-"`). |
| `_____` | A numeric placeholder (its sentinel value is `0`). |

For the full sentinel model and curriculum semantics, see the [curriculum reference](../curriculum.md#sentinels).

**3. Register the koan in the manifest.** Add the lesson's fully-qualified `TestCase` name to `koans.txt` at the curriculum position you want — for example, a line reading `koans.about_new_topic.AboutNewTopic`. **Order matters**: the discovery loader preserves manifest order (it sets `loader.sortTestMethodsUsing = None`), so where you place the line is exactly where the lesson appears in the run. `Source: ../../koans.txt:L1-L40`, `Source: ../../runner/path_to_enlightenment.py:L42-L62`.

A single lesson module may register **more than one** `TestCase`. For instance, `about_proxy_object_project.py` contributes two manifest entries — `koans.about_proxy_object_project.AboutProxyObjectProject` and `koans.about_proxy_object_project.TelevisionTest`. `Source: ../../koans.txt:L37-L38`.

> **Never author sentinel answers.** Examples in documentation, and any lesson meant to remain an exercise, must show only the fill-in form; do not commit "solved" koans. The four sentinels exist precisely so an un-edited koan fails loudly. `Source: ../../runner/koan.py:L12-L19`. See the [curriculum reference](../curriculum.md#adding-to-the-curriculum) for the complete manifest and sentinel reference.

## Testing a koan while authoring

While writing or modifying a lesson, run just that lesson instead of the whole curriculum. Pass the lesson name to the CLI entry point. `Source: ../../Contributor Notes.txt:L1-L13`.

Run a whole test case:

```bash
python3 contemplate_koans.py about_strings
```

Run a single test (use the abbreviated, generic form):

```bash
python3 contemplate_koans.py about_strings.AboutStrings.test_...
```

For the complete command-line contract — running all koans, running a subset, the `-B` flag, and the platform launchers — see the [CLI usage guide](../guides/cli-usage.md).

## Running the runner self-tests

The *runner* engine has its **own** unit tests, separate from the koan exercises. They are aggregated by `_runner_tests.py` and run with:

```bash
python3 _runner_tests.py
```

The aggregator's `suite()` loads five `TestCase` classes imported from `runner/runner_tests/`: `TestMountain`, `TestSensei`, `TestHelper`, `TestFilterKoanNames`, and `TestKoansSuite`. `Source: ../../_runner_tests.py:L7-L26`.

**This is the command CI runs.** Travis declares `language: python`, pins **Python 3.9**, and its `script:` step is `python _runner_tests.py`. `Source: ../../.travis.yml:L3-L4`, `Source: ../../.travis.yml:L7`.

### Known caveat: Python 3.12 `assertEquals`

On **Python 3.12** (and newer), `python3 _runner_tests.py` **fails**. Python 3.12 removed the long-deprecated `assertEquals` alias from `unittest`, and the runner self-tests still call `self.assertEquals(...)` (in `runner/runner_tests/test_helper.py`). The observed failure is:

```text
AttributeError: 'TestHelper' object has no attribute 'assertEquals'
```

and the run ends with `FAILED (errors=2)`. This is **documented, not fixed**, under this documentation effort — it is a code-level compatibility matter, not a documentation one. Run the self-tests on a **supported interpreter (≤ 3.11)**, matching the Python 3.9 that CI uses. `Source: ../../.travis.yml:L3-L7`. For the full version policy and the complete caveat write-up, see the deployment guide's [Python version policy](../guides/deployment.md#python-version-policy) and its [Python 3.12 caveat](../guides/deployment.md#known-caveat-python-312-assertequals).

## Continuous testing with Sniffer

For a fast edit-and-rerun loop, the project ships a Sniffer configuration in `scent.py`. It re-runs the koans automatically whenever a `.py` file changes: it watches `['.', 'koans/']` and, on each change, runs `python3 -B contemplate_koans.py`. `Source: ../../scent.py:L4-L12`.

Sniffer is an **optional developer aid**, not a runtime dependency of the koans. Its installation and per-platform setup belong to the [deployment guide](../guides/deployment.md) — see the Sniffer section there rather than duplicating setup steps here.

## Docstring conventions

In-source documentation follows the in-repo exemplar, `runner/path_to_enlightenment.py`: concise, triple-quoted (`'''…'''`), reStructuredText-flavored docstrings that wrap code terms in double backticks (for example, `` ``TestSuite`` `` and `` ``filename`` ``). `Source: ../../runner/path_to_enlightenment.py:L4-L60`.

A module-level docstring in that style looks like:

```python
'''
Functions to load the test cases ("koans") that make up the
Path to Enlightenment.
'''
```

`Source: ../../runner/path_to_enlightenment.py:L4-L7`.

This matches the documentation-only docstrings being added across the engine in the same effort — module, class, and method docstrings plus inline comments, with **no behavioral change** to signatures or control flow. When you document the discovery loader, note that it deliberately preserves manifest order with `loader.sortTestMethodsUsing = None`, which is why `koans.txt` ordering is authoritative. `Source: ../../runner/path_to_enlightenment.py:L42-L53`.

For the rendered engine API built from these docstrings, see the [runner-engine API reference](../api-reference/runner-engine.md).

## Source citations

- [koans.txt:L1-L40](../../koans.txt) — the curriculum manifest: line 1 is a `#` comment; the 39 ordered `TestCase` entries are on lines 2–40 (including the two entries contributed by `about_proxy_object_project`).
- [runner/path_to_enlightenment.py:L4-L62](../../runner/path_to_enlightenment.py) — the docstring-style exemplar, the order-preserving loader (`sortTestMethodsUsing = None`), and the `koans()` discovery entry point.
- [runner/koan.py:L10-L23](../../runner/koan.py) — the four sentinels, their `__all__` export, and the `Koan(unittest.TestCase)` base class.
- [_runner_tests.py:L7-L26](../../_runner_tests.py) — the runner self-test aggregator and its five `TestCase` classes (`TestMountain`, `TestSensei`, `TestHelper`, `TestFilterKoanNames`, `TestKoansSuite`).
- [.travis.yml:L3-L7](../../.travis.yml) — CI pins Python 3.9 and runs `python _runner_tests.py`.
- [scent.py:L4-L12](../../scent.py) — the Sniffer configuration (`watch_paths`, the `.py` file filter, and the `python3 -B contemplate_koans.py` action).
- [Contributor Notes.txt:L1-L13](../../Contributor%20Notes.txt) — the run-a-whole-case and run-a-single-test commands used while authoring.
- [contemplate_koans.py:L14-L34](../../contemplate_koans.py) — the CLI entry point, version gate, and `Mountain().walk_the_path(sys.argv)` bootstrap.
- [runner/sensei.py:L251-L269](../../runner/sensei.py) — `total_koans()` / `total_lessons()` / `filter_all_lessons()`, the logic behind the **304 koans** and **37 lessons** figures (`total_koans` = `self.tests.countTestCases()`, `Source: ../../runner/sensei.py:L258-L259`).
