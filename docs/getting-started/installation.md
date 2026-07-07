# Installation

Get a Python 3 interpreter, clone the repository, and run Python Koans straight from the source tree — no package installation required.

## Prerequisites

The only thing you need to install is a **Python 3 interpreter**. Python Koans runs on the Python standard library alone, so there is **no `pip install` step** and **no dependency manifest** to process — the repository contains no `requirements.txt`, `setup.py`, or `pyproject.toml` (confirmed by repository inspection). Once you have Python 3 and a copy of the source tree, you are ready to go. `Source: ../../README.rst:L62-L65, ../../README.rst:L101-L105`

> Optional developer tools — the Sniffer continuous-test runner and `pytest` — are **separate** from running the koans and are not required to get started. They are covered in the [deployment guide](../guides/deployment.md).

## Supported Python versions

Python Koans is the **Python 3 edition**; the project's policy is to keep current with the latest production release of Python 3. `Source: ../../README.rst:L104-L105`

The command-line entry point, `contemplate_koans.py`, enforces this with an in-app version gate:

- It **prints an error if you run it under Python 2** (the `sys.version_info < (3, 0)` branch) and points you at `python3` instead. `Source: ../../contemplate_koans.py:L38-L42`
- It **prints a warning if your interpreter is older than Python 3.7** (the `sys.version_info < (3, 7)` branch) and then continues. `Source: ../../contemplate_koans.py:L45-L54`

Treat **Python 3.7+** as the supported baseline. Releases through **3.11** and **Python 3.12+** all run the koans well; see the Note below. `Source: ../../README.rst:L110-L113`

> **Note:** Python Koans is compatible with **Python 3.12+**. Both the runner self-tests (`python _runner_tests.py`) and the koan exercises run cleanly, because the previously removed `assertEquals` alias has been replaced with the canonical `assertEqual` throughout the runner tests and koans. No interpreter downgrade is required — see the [deployment guide](../guides/deployment.md) for detail. `Source: ../../runner/runner_tests/test_helper.py:L15-L18`, `Source: ../../koans/about_regex.py:L85`

You can download Python from the official site: <https://www.python.org/downloads/>. `Source: ../../README.rst:L117-L119`

## Clone and run

Python Koans is "zero-install": clone the repository and run it directly from the source tree.

**1. Clone the repository** (`Source: ../../README.rst:L91-L95`):

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

- On **Unix / macOS**, the interpreter is invoked as `python3`. `Source: ../../README.rst:L121-L123`
- On **Windows**, the interpreter is `python.exe`, typically launched via `run.bat`. Make sure the folder containing Python is on your system `PATH`, or set the path inside `run.bat`. `Source: ../../README.rst:L121-L123`, `Source: ../../run.bat:L8`
- The Windows path to set in `run.bat` is `C:\Python311` — adjust it to match where Python is installed on your machine. `Source: ../../run.bat:L8`

## Next steps

- **[First steps](first-steps.md)** — run the koans and read your first progress report.
- **[CLI usage guide](../guides/cli-usage.md)** — the full command-line contract (run-all, run-single, launchers, Sniffer).
- **[Documentation home](../index.md)** — back to the documentation index.

## Source citations

- [README.rst:L88-L132]
- [contemplate_koans.py:L38-L54]
- [run.sh:L3]
- [run.bat:L5-L8]
