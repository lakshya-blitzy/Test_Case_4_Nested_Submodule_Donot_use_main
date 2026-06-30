# First steps

Run Python Koans for the first time, learn to read the progress report, and understand the fill-in-the-blank sentinel model — without any spoilers.

> This guide assumes you have already set up a Python 3 interpreter and a copy of the source tree as described in [installation.md](installation.md).

## Your first run

To start the curriculum, run **all** the koans from the repository root:

```bash
python3 contemplate_koans.py
```

On Unix and macOS the provided launcher does exactly the same thing — it invokes `python3 -B contemplate_koans.py` for you. `Source: ../../run.sh:L3`

```bash
./run.sh
```

Your very first run will show **failing koans** — that is entirely expected. A failing koan is the starting point of the exercise: each failure points you at the next thing to learn.

## Reading the output

As the runner works through the curriculum, three kinds of output scroll past. In the order you encounter them:

1. **Per-lesson banner.** For each new lesson class, the runner prints a blank line followed by a `Thinking <ClassName>` banner. The first banner you see is `Thinking AboutAsserts`, because `AboutAsserts` is the first lesson in the curriculum. `Source: ../../runner/sensei.py:L33-L35`
2. **Pass message (green).** When a koan passes, the runner prints, in bright green, a line of the form `  <test_method_name> has expanded your awareness.` (note the two leading spaces). `Source: ../../runner/sensei.py:L42-L45`
3. **Progress summary line.** At the end, `report_progress()` prints a single summary line of the form `You have completed X (P %) koans and Y (out of Z) lessons.` `Source: ../../runner/sensei.py:L169-L175`

Between the first banner and the summary you will see the runner attempt each koan; on a fresh checkout the very first one fails, which is why the run stops there and reports zero progress.

On a brand-new checkout, the relevant lines of the output look like this (terminal colors removed):

```text
Thinking AboutAsserts
...
You have completed 0 (0 %) koans and 0 (out of 37) lessons.
You are now 304 koans and 37 lessons away from reaching enlightenment.
```

The runner also prints a companion "remaining" line produced by `report_remaining()`, of the form `You are now <N> koans and <M> lessons away from reaching enlightenment.` On a fresh run it reads exactly `You are now 304 koans and 37 lessons away from reaching enlightenment.` `Source: ../../runner/sensei.py:L177-L184`

What the numbers mean:

- **X** (koans completed) and **Y** (lessons completed) start at `0` and **rise** as you solve koans and finish lessons. **P** is simply `X` as a percentage of the koan total.
- **Z** is the **fixed** total number of lessons — **37** — so the summary always reads `(out of 37)`.
- The full curriculum is **304 koans across 37 lessons**; on a fresh run you are `304 koans and 37 lessons away from reaching enlightenment`.

For how those counts are computed — and why the manifest's entry count is not the same as the lesson count — see the [curriculum reference](../curriculum.md). This guide only shows you how to *read* the line; the curriculum reference explains the math.

## Understanding sentinels

Most koans are written as a small, **failing** assertion in which a **sentinel** placeholder stands in for the value (or code) you must supply. The koan fails as shipped; your job is to replace the sentinel with the correct answer so the assertion passes. You discover that answer by **running the koan and reading the failure** — the failure tells you what was expected.

The README illustrates the idea with an unsolved assertion: `self.assertEqual(__, 1+2)`, where the `__` is the blank you must fill in. `Source: ../../README.rst:L33-L43`

There are four sentinels, all defined in `runner/koan.py`. Here is what each one **means** (not its answer):

- `__` — a value you must fill in. `Source: ../../runner/koan.py:L12`
- `___` — an exception type (a custom `Exception` subclass), used where a koan expects an error to be raised. `Source: ../../runner/koan.py:L14-L15`
- `____` — a true/false placeholder. `Source: ../../runner/koan.py:L17`
- `_____` — a number. `Source: ../../runner/koan.py:L19`

All four sentinels are exported via `__all__`, alongside the `Koan` base class. `Source: ../../runner/koan.py:L10`

**This guide deliberately does not reveal any correct answers.** You are meant to discover each value yourself by running the koans and reading their failures — that discovery *is* the exercise, and spoiling it would defeat the curriculum.

For the full sentinel semantics and the lesson/koan counting rules, see the [curriculum reference](../curriculum.md).

## The TDD loop

Filling in koans is a hands-on way to practice the **Test-Driven Development** rhythm of **red → green → refactor**, as the README's "Getting the Most From the Koans" section describes: run the koan and watch it **fail (red)**, make the test **pass (green)**, then pause to **reflect** on what the test is teaching you and **refactor** the code to better communicate its intent. `Source: ../../README.rst:L192-L203`

Repeat the loop koan by koan, lesson by lesson, and the progress line climbs toward enlightenment.

## Next

- **[CLI usage guide](../guides/cli-usage.md)** — once you are working through a lesson, you will often want to run a **single koan** (a whole `TestCase`) or even a **single test** so you can focus on one failing koan at a time. The run-single forms are introduced in `Contributor Notes.txt`; full command-line detail lives in the CLI usage guide. `Source: ../../Contributor Notes.txt:L8-L12`
- **[Installation](installation.md)** — back to prerequisites and how to get the source tree.
- **[Documentation home](../index.md)** — the full documentation index.

## Source citations

- [run.sh:L3]
- [runner/sensei.py:L33-L45]
- [runner/sensei.py:L169-L184]
- [runner/koan.py:L10-L19]
- [README.rst:L33-L51]
- [README.rst:L192-L203]
- [Contributor Notes.txt:L1-L13]
