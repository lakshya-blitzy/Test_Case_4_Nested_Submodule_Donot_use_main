# Installation

Get a Python 3 interpreter, clone the repository, and run Python Koans straight from the source tree — no package installation required.

## Prerequisites

The only thing you need to install is a **Python 3 interpreter**. Python Koans runs on the Python standard library alone, so there is **no `pip install` step** and **no dependency manifest** to process — the repository contains no `requirements.txt`, `setup.py`, or `pyproject.toml` (confirmed by repository inspection). Once you have Python 3 and a copy of the source tree, you are ready to go. `Source: ../../README.rst:L67-L68`

> Optional developer tools — the Sniffer continuous-test runner and `pytest` — are **separate** from running the koans and are not required to get started. They are covered in the [deployment guide](../guides/deployment.md).

## Supported Python versions

Python Koans is the **Python 3 edition**; the project's policy is to keep current with the latest production release of Python 3. `Source: ../../README.rst:L70-L71`

The command-line entry point, `contemplate_koans.py`, enforces this with an in-app version gate:

- It **prints an error if you run it under Python 2** (the `sys.version_info < (3, 0)` branch) and points you at `python3` instead. `Source: ../../contemplate_koans.py:L15-L19`
- It **prints a warning if your interpreter is older than Python 3.7** (the `sys.version_info < (3, 7)` branch) and then continues. `Source: ../../contemplate_koans.py:L21-L30`

Treat **Python 3.7+** as the supported baseline. Newer 3.x releases generally work fine for running the koans themselves. `Source: ../../README.rst:L73-L74`

> **Note:** A Python 3.12 compatibility caveat applies specifically to the runner self-tests (`python _runner_tests.py`), not to running the koans — see the [deployment guide](../guides/deployment.md) for the detail.

You can download Python from the official site: <https://www.python.org/downloads/>. `Source: ../../README.rst:L76-L78`

## Clone and run

Python Koans is "zero-install": clone the repository and run it directly from the source tree.

**1. Clone the repository** (`Source: ../../README.rst:L57-L61`):

```bash
git clone https://github.com/gregmalcolm/python_koans.git
cd python_koans
```

**2. Run the koans.**

On **Unix / macOS**, use the provided launcher, which runs `python3 -B contemplate_koans.py`:

```bash
./run.sh
```

`Source: ../../run.sh:L3`

Or invoke the interpreter directly:

```bash
python3 -B contemplate_koans.py
```

On **Windows**, use the `run.bat` launcher. It sets `SET PYTHON_PATH=C:\Python311` and runs `python.exe -B contemplate_koans.py`:

```bash
run.bat
```

`Source: ../../run.bat:L8`, `Source: ../../run.bat:L5`

Or invoke the interpreter directly:

```bash
python.exe -B contemplate_koans.py
```

**About the `-B` flag:** `-B` tells Python **not to write `.pyc` bytecode files**, which keeps the source tree clean as you edit the koans. Both launchers pass it. `Source: ../../run.sh:L3`, `Source: ../../run.bat:L5`

## Platform notes

- On **Unix / macOS**, the interpreter is invoked as `python3`. `Source: ../../README.rst:L80-L82`
- On **Windows**, the interpreter is `python.exe`, typically launched via `run.bat`. Make sure the folder containing Python is on your system `PATH`, or set the path inside `run.bat`. `Source: ../../README.rst:L80-L82`, `Source: ../../run.bat:L8`
- The Windows path to set in `run.bat` is `C:\Python311` — adjust it to match where Python is installed on your machine. `Source: ../../run.bat:L8`

## Next steps

- **[First steps](first-steps.md)** — run the koans and read your first progress report.
- **[CLI usage guide](../guides/cli-usage.md)** — the full command-line contract (run-all, run-single, launchers, Sniffer).
- **[Documentation home](../index.md)** — back to the documentation index.

## Source citations

- [README.rst:L57-L91]
- [contemplate_koans.py:L15-L30]
- [run.sh:L3]
- [run.bat:L5-L8]
