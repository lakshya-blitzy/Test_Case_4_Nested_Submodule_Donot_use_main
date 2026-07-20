# Deployment & Run Guide

[← Back to README](../README.rst) · [Architecture](./architecture.md) · [API Reference](./api-reference.md)

This guide consolidates the **run**, **continuous-integration**, **cloud-workspace**, and **continuous-re-run** knowledge for the parent Python Koans project into a single reference. Historically this knowledge was scattered across `run.sh`, `run.bat`, `.travis.yml`, `.gitpod.yml`, `.gitpod.Dockerfile`, and `scent.py`; every entry point below is documented here with a citation back to its source.

Python Koans is an interactive, test-driven tutorial: you "walk the path" by making failing tests pass. There is nothing to compile or package — you simply run the launcher and start filling in koans.

## Prerequisites

- **Python 3 is required.** The launcher refuses to proceed under Python 2, printing guidance to re-run with `python3` instead of starting the runner. Source: contemplate_koans.py:L34
- On **Python 3 older than 3.7**, the launcher prints a warning that the koans were designed for Python 3.7 or greater but continues on a best-effort basis. Source: contemplate_koans.py:L43
- **No external pip packages are required to run the koans.** The launcher's only import is the project's own runner package (`from runner.mountain import Mountain`), Source: contemplate_koans.py:L57 — and the third-party libraries it relies on are vendored under `libs/` with no `requirements.txt` at the repository root. Source: libs/
- pip is only needed for the *optional* Sniffer auto-rerun tooling (see [Continuous Re-run (Sniffer)](#continuous-re-run-sniffer)) and the Gitpod test tooling (see [Cloud Workspace (Gitpod)](#cloud-workspace-gitpod)).

> **Tip:** confirm your interpreter with `python3 --version` before you begin.

## Running Locally

Two convenience launchers are provided — a POSIX shell script and a Windows batch file — and both ultimately invoke the same `contemplate_koans.py` entry point.

### POSIX (macOS / Linux)

The `run.sh` helper is a small shell script whose shebang is `#!/bin/sh`. Source: run.sh:L1

Run it directly, or invoke the launcher yourself:

```bash
# Option A — use the provided helper script
sh run.sh

# Option B — call the launcher directly (exactly what run.sh does)
python3 -B contemplate_koans.py
```

`run.sh` runs `python3 -B contemplate_koans.py`; the `-B` flag suppresses writing `.pyc` bytecode files. Source: run.sh:L3

The README documents the same launcher with the plain forms `python contemplate_koans.py` and `python3 contemplate_koans.py`. Source: README.rst:L103-L113

### Windows

On Windows, use the `run.bat` batch file. It defines the command it will run as `SET RUN_KOANS=python.exe -B contemplate_koans.py`. Source: run.bat:L5

It then sets a Python install folder to search and hunts for a runnable `python.exe` — first in the current directory, then under `%PYTHON_PATH%`, then under `%PYTHON%` — before invoking the launcher and offering a "Test again? y or n" loop. Source: run.bat:L8, L39-L42

```bat
REM Excerpt from run.bat — update this path to match your Python install
SET PYTHON_PATH=C:\Python311
```

**Update `SET PYTHON_PATH=C:\Python311` to match your local Python installation directory** if it differs; the value shipped in `run.bat` is `C:\Python311`. Source: run.bat:L8

> **Note — run a single lesson:** pass a koan/lesson name on the command line and the launcher forwards it to the runner, e.g. `python3 contemplate_koans.py about_asserts`. This works because `contemplate_koans.py` forwards the full process `argv` to `Mountain().walk_the_path(sys.argv)`. Source: contemplate_koans.py:L61 — see [`Mountain.walk_the_path`](./api-reference.md#mountain-runnermountainpy) in the API Reference for how that argument selects a single koan.

## Continuous Integration (Travis CI)

Continuous integration runs on Travis CI, configured by `.travis.yml`. The build language is Python. Source: .travis.yml:L1

Travis provisions **Python 3.9** for the build. Source: .travis.yml:L3-L4

The CI `script` step runs the runner-engine regression suite with `python _runner_tests.py`. Source: .travis.yml:L6-L7

```yaml
language: python

python:
    - 3.9

script:
    - python _runner_tests.py
```

That command executes `_runner_tests.py`, whose `suite()` aggregates the five runner-engine test cases, Source: _runner_tests.py:L36, L49-L55 — and whose `__main__` block exits non-zero when any test fails or errors, so CI can gate on the result. Source: _runner_tests.py:L58-L61

For what those runner components actually do, see the [API Reference](./api-reference.md) and the [Architecture](./architecture.md) guide.

## Cloud Workspace (Gitpod)

The project offers a one-click, browser-based development workspace via Gitpod; the README advertises this with a "ready-to-code" Gitpod badge and one-click installation links. Source: README.rst:L8-L21

The `.gitpod.yml` workspace configuration builds its container image from the repository's `.gitpod.Dockerfile`. Source: .gitpod.yml:L1-L2

On workspace start it auto-runs the koans launcher with `python contemplate_koans.py`. Source: .gitpod.yml:L4-L5

The Docker image is based on `gitpod/workspace-full:latest`, runs as the `gitpod` user, and installs the test tooling `pytest==4.4.2 pytest-testdox mock`. Source: .gitpod.Dockerfile:L7, L9, L11

```dockerfile
FROM gitpod/workspace-full:latest

USER gitpod

RUN pip3 install pytest==4.4.2 pytest-testdox mock
```

> GitHub prebuilds are enabled for the `master` branch so the workspace is ready quickly. Source: .gitpod.yml:L7-L14

## Continuous Re-run (Sniffer)

Sniffer is an **optional** tool that watches your files and reruns the koans automatically whenever you save a change — a hands-free red/green feedback loop.

Set it up by installing `sniffer` and the OS-specific file-system watcher for your platform:

```bash
# 1. Install Sniffer itself
python3 -m pip install sniffer

# 2. Install the watcher for your OS (pick one)
python3 -m pip install pyinotify     # Linux
python3 -m pip install pywin32       # Windows
python3 -m pip install MacFSEvents   # macOS
```

Install Sniffer with `python3 -m pip install sniffer`. Source: README.rst:L155

Then install the platform watcher — `pyinotify` on Linux, `pywin32` on Windows, or `MacFSEvents` on macOS — so changes trigger Sniffer immediately instead of by polling. Source: README.rst:L161-L181

Once set up, start it by running `sniffer` from the repository root. Source: README.rst:L187

Sniffer's behavior is controlled by `scent.py`. Source: README.rst:L190

Inside `scent.py`, the watched locations are `watch_paths = ['.', 'koans/']` — the repository root and the `koans/` directory. Source: scent.py:L24

When a watched, non-hidden `.py` file changes, Sniffer reruns the koans by shelling out to `python3 -B contemplate_koans.py` — the same command used to launch them manually. Source: scent.py:L45-L46, L63

## Entry-Point Summary

| Method | Command | Source |
|--------|---------|--------|
| Local — POSIX | `python3 -B contemplate_koans.py` (via `sh run.sh`) | run.sh:L3 |
| Local — Windows | `run.bat` (set `PYTHON_PATH=C:\Python311`) | run.bat:L5-L8 |
| Continuous Integration | `python _runner_tests.py` (Travis, Python 3.9) | .travis.yml:L7 |
| Cloud Workspace | `python contemplate_koans.py` (Gitpod auto-start) | .gitpod.yml:L5 |
| Continuous Re-run | `sniffer` → reruns `python3 -B contemplate_koans.py` | scent.py:L63 |

Four of the five surfaces drive the koans launcher `contemplate_koans.py` directly; Travis CI instead runs the runner-engine regression suite `_runner_tests.py`.

```mermaid
flowchart LR
    A["Local POSIX: sh run.sh"] --> K["contemplate_koans.py (koans launcher)"]
    B["Local Windows: run.bat"] --> K
    D["Gitpod: python contemplate_koans.py"] --> K
    E["Sniffer: sniffer via scent.py"] --> K
    C["Travis CI"] --> T["_runner_tests.py (regression suite)"]
```

*Run surfaces (Local POSIX/Windows, Gitpod, Sniffer) converge on the launcher `contemplate_koans.py`, while Travis CI runs the regression suite `_runner_tests.py`. Sources: run.sh:L3, run.bat:L5, .gitpod.yml:L5, scent.py:L63, .travis.yml:L7.*

## Related Documentation

- [Architecture](./architecture.md) — how the launcher, `Mountain`, curriculum loader, and `Sensei` fit together at runtime.
- [API Reference](./api-reference.md) — the `runner/` engine API (`Mountain`, `Sensei`, the curriculum loaders, and support types).
- [← Back to README](../README.rst) — project overview, installation, and getting started.
