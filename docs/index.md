# Python Koans Documentation

Developer- and user-facing documentation for Python Koans — an interactive, test-driven tutorial for learning Python by making failing tests pass.

Python Koans is an interactive tutorial for learning the Python programming language by making tests pass — a port of Edgecase's "Ruby Koans." `Source: README.rst:L25-L31`. Most koans are *fixed* by filling in the missing part of an assertion (you replace a **sentinel** placeholder with the value or expression that makes the test pass), while a few require you to implement a small piece of code yourself, such as classifying a triangle as equilateral, isosceles, or scalene. `Source: README.rst:L33-L48`. Working through the koans is also a gentle on-ramp to Test-Driven Development (TDD): run the suite, see it fail (red), make it pass (green), then reflect on what the koan is teaching you. `Source: README.rst:L50-L51`. The tool runs on the **Python standard library alone** — you only need a Python 3 interpreter, then you can clone the repository and run it straight from the source tree with no package to install. `Source: README.rst:L62-L65, README.rst:L98-L108`.

This page is the documentation home and canonical table of contents for the `docs/` tree. Every guide below is plain Markdown that renders natively on GitHub; the project's high-level overview and status badges live in the canonical [README](../README.rst).

## Documentation map

The table below links to every document in the `docs/` tree using repository-relative paths, so the links resolve both on GitHub and in any future generated site.

| Document | Path | What it covers |
|---|---|---|
| Installation | [`getting-started/installation.md`](getting-started/installation.md) | Prerequisites, supported Python versions, zero-install clone-and-run, Unix vs. Windows |
| First steps | [`getting-started/first-steps.md`](getting-started/first-steps.md) | Your first run, reading the progress summary, understanding sentinels (no spoilers) |
| CLI usage | [`guides/cli-usage.md`](guides/cli-usage.md) | Run-all, run-single, the `-B` flag, `run.sh`/`run.bat` launchers, Sniffer continuous mode |
| Deployment & operations | [`guides/deployment.md`](guides/deployment.md) | Local run, Travis CI, Gitpod, Sniffer, Python version policy, Python 3.12 compatibility |
| Runner engine API reference | [`api-reference/runner-engine.md`](api-reference/runner-engine.md) | Public API of the `runner/` engine (Mountain, Sensei, discovery, Koan, helpers) |
| Architecture overview | [`architecture/overview.md`](architecture/overview.md) | Three-package layering, manifest-driven discovery, the `unittest` substrate, diagrams |
| Curriculum & manifest reference | [`curriculum.md`](curriculum.md) | `koans.txt` ordering, 304 koans / 37 lessons, sentinel semantics, lesson-exclusion logic |
| Contributing & development | [`contributing/development.md`](contributing/development.md) | Add-a-koan workflow, manifest registration, runner self-tests, docstring conventions |

The curriculum is defined by the [`koans.txt`](../koans.txt) manifest, which lists **39** ordered `TestCase` entries (line 1 is a `#` comment; the entries occupy lines 2–40). `Source: koans.txt:L1-L40`. A full run of those lessons reports **304 koans** across **37 lessons** — runtime-verified figures derived by the runner's own count logic. `Source: runner/sensei.py:L429-L437` (``total_koans``), `Source: runner/sensei.py:L413-L427` (``total_lessons``), and `Source: runner/sensei.py:L439-L456` (``filter_all_lessons``). See the [Curriculum & manifest reference](curriculum.md) for how the counts are derived.

## Where to start

New to Python Koans? Read the documentation in this order:

- **[Installation](getting-started/installation.md)** — install a Python 3 interpreter and get the source.
- **[First steps](getting-started/first-steps.md)** — run the koans for the first time and learn to read the progress summary.
- **[CLI usage](guides/cli-usage.md)** — the full command-line contract: run everything, a single lesson, or a single test.
- **[Deployment & operations](guides/deployment.md)** — run the koans locally, in CI, in the cloud, or under continuous testing.

Once you are comfortable running the koans, dig into the engine internals:

- **[Runner engine API reference](api-reference/runner-engine.md)** — the public API of the `runner/` package (Mountain, Sensei, path_to_enlightenment, Koan, WritelnDecorator).
- **[Architecture overview](architecture/overview.md)** — how the pieces fit together, with diagrams.
- **[Curriculum & manifest reference](curriculum.md)** — how `koans.txt` defines the lesson order and the koan/lesson counts.
- **[Contributing & development](contributing/development.md)** — add your own koan, register it in the manifest, and run the runner self-tests.

For the high-level project overview, screenshots, and status badges, see the canonical project [README](../README.rst).

## Conventions

- **Format.** These guides are written in Markdown with embedded Mermaid diagrams, both of which render natively on GitHub — no documentation generator or build tooling is required.
- **Source citations.** Every technical claim cites its origin inline as `` `Source: <path>:L<nn>` `` so any statement can be traced back to the code or configuration it describes.
- **Runtime-verified figures.** Quantitative figures — **304 koans**, **37 lessons**, and **39** manifest entries — are taken from actual runtime output and the `koans.txt` manifest rather than copied from secondary sources.
- **No spoilers.** The documentation never fills in or reveals the answer to a koan; the sentinel placeholders (`__`, `___`, `____`, `_____`) remain exercises for you to solve.
- **Terminology.** Consistent vocabulary throughout — *koan*, *lesson*, *sentinel*, *Mountain*, *Sensei*, *path_to_enlightenment*, *WritelnDecorator* — aligned with the canonical [README](../README.rst).

## Source citations

This page draws on the following files:

- `[README.rst:L1-L290]` — project synopsis, the fill-in-the-blank model, the TDD framing, and the install/getting-started notes.
- `[koans.txt:L1-L40]` — the curriculum manifest (line 1 is a `#` comment; 39 ordered `TestCase` entries on lines 2–40).
