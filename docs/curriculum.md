# Curriculum & Manifest Reference

How the Python Koans curriculum is defined, ordered, counted, and discovered — a reference for `koans.txt` and the sentinel exercise model.

## Overview

The Python Koans curriculum is **data-driven**. Rather than hard-coding which
lessons to run, the project keeps an ordered, plain-text *manifest* —
[`koans.txt`](../koans.txt) — that lists every lesson `TestCase` to load. At
runtime the `path_to_enlightenment` discovery module reads that manifest and
assembles the listed `TestCase`s into a single ordered `unittest.TestSuite`,
and the `Sensei` reporter walks the suite to print your progress. `Source:
runner/path_to_enlightenment.py:L56-L62`, `Source: runner/sensei.py:L22`.

This document is the authoritative reference for that manifest: its format and
ordering rules, the full list of entries, the difference between the three
counts you will encounter (**39** manifest entries, **304** koans, and **37**
lessons), and the meaning of the four *sentinel* placeholders you fill in as you
learn.

- For the end-to-end control flow (CLI → `Mountain` → discovery → `unittest` →
  `Sensei`), see [architecture/overview.md](architecture/overview.md).
- For the programmatic discovery API (`koans()`, `koans_suite()`, and friends),
  see [api-reference/runner-engine.md](api-reference/runner-engine.md).
- For how to read the progress line on your first run, see
  [getting-started/first-steps.md](getting-started/first-steps.md).

## Manifest format (`koans.txt`)

The manifest is a UTF-8 plain-text file with **one fully-qualified `TestCase`
name per line**, for example `koans.about_asserts.AboutAsserts`. Each name uses
Python's dotted import path — `koans.<module>.<ClassName>` — so the loader can
import the lesson module from the `koans/` package and load the named
`TestCase` from it.

Two kinds of lines are ignored when the manifest is parsed:

- **Comment lines** — any line whose first non-whitespace character is `#` is
  skipped. Line 1 of the manifest is exactly such a comment: `# Lines starting
  with # are ignored.` `Source: koans.txt:L1`.
- **Blank lines** — empty lines (or lines containing only whitespace) are
  skipped.

This filtering is performed by the `filter_koan_names` generator, which strips
leading/trailing whitespace from each line, drops lines beginning with `#`, and
yields only the remaining non-blank names. `Source:
runner/path_to_enlightenment.py:L17-L28`.

### Order matters

The manifest is **ordered**, and that order is preserved end-to-end. When the
discovery layer builds the suite it explicitly disables the test loader's
alphabetical sorting by setting `loader.sortTestMethodsUsing = None`, then adds
each named `TestCase` to the suite in the exact sequence it appears in the
manifest. As a result, the koans run in manifest order — from
`koans.about_asserts.AboutAsserts` down to `koans.about_regex.AboutRegex` —
rather than alphabetically. `Source: runner/path_to_enlightenment.py:L42-L53`.

### Default manifest filename

The manifest path defaults to the module-level constant `KOANS_FILENAME =
'koans.txt'`, which the `koans()` discovery entry point uses unless a different
filename is supplied. `Source: runner/path_to_enlightenment.py:L14`,
`Source: runner/path_to_enlightenment.py:L56-L62`.

## The 39 ordered entries

The table below reproduces every `TestCase` entry in the manifest, in load
order. The manifest contains **39 entries** on lines 2–40; line 1 is the
comment described above. The "Manifest line" column is the literal line number
in [`koans.txt`](../koans.txt), and the "Lesson file" column is the
`koans/` module the dotted name resolves to. `Source: koans.txt:L1-L40`.

| Order | Manifest line | Fully-qualified `TestCase` | Lesson file |
|------:|--------------:|----------------------------|-------------|
| 1 | 2 | `koans.about_asserts.AboutAsserts` | `koans/about_asserts.py` |
| 2 | 3 | `koans.about_strings.AboutStrings` | `koans/about_strings.py` |
| 3 | 4 | `koans.about_none.AboutNone` | `koans/about_none.py` |
| 4 | 5 | `koans.about_lists.AboutLists` | `koans/about_lists.py` |
| 5 | 6 | `koans.about_list_assignments.AboutListAssignments` | `koans/about_list_assignments.py` |
| 6 | 7 | `koans.about_dictionaries.AboutDictionaries` | `koans/about_dictionaries.py` |
| 7 | 8 | `koans.about_string_manipulation.AboutStringManipulation` | `koans/about_string_manipulation.py` |
| 8 | 9 | `koans.about_tuples.AboutTuples` | `koans/about_tuples.py` |
| 9 | 10 | `koans.about_methods.AboutMethods` | `koans/about_methods.py` |
| 10 | 11 | `koans.about_control_statements.AboutControlStatements` | `koans/about_control_statements.py` |
| 11 | 12 | `koans.about_true_and_false.AboutTrueAndFalse` | `koans/about_true_and_false.py` |
| 12 | 13 | `koans.about_sets.AboutSets` | `koans/about_sets.py` |
| 13 | 14 | `koans.about_triangle_project.AboutTriangleProject` | `koans/about_triangle_project.py` |
| 14 | 15 | `koans.about_exceptions.AboutExceptions` | `koans/about_exceptions.py` |
| 15 | 16 | `koans.about_triangle_project2.AboutTriangleProject2` | `koans/about_triangle_project2.py` |
| 16 | 17 | `koans.about_iteration.AboutIteration` | `koans/about_iteration.py` |
| 17 | 18 | `koans.about_comprehension.AboutComprehension` | `koans/about_comprehension.py` |
| 18 | 19 | `koans.about_generators.AboutGenerators` | `koans/about_generators.py` |
| 19 | 20 | `koans.about_lambdas.AboutLambdas` | `koans/about_lambdas.py` |
| 20 | 21 | `koans.about_scoring_project.AboutScoringProject` | `koans/about_scoring_project.py` |
| 21 | 22 | `koans.about_classes.AboutClasses` | `koans/about_classes.py` |
| 22 | 23 | `koans.about_with_statements.AboutWithStatements` | `koans/about_with_statements.py` |
| 23 | 24 | `koans.about_monkey_patching.AboutMonkeyPatching` | `koans/about_monkey_patching.py` |
| 24 | 25 | `koans.about_dice_project.AboutDiceProject` | `koans/about_dice_project.py` |
| 25 | 26 | `koans.about_method_bindings.AboutMethodBindings` | `koans/about_method_bindings.py` |
| 26 | 27 | `koans.about_decorating_with_functions.AboutDecoratingWithFunctions` | `koans/about_decorating_with_functions.py` |
| 27 | 28 | `koans.about_decorating_with_classes.AboutDecoratingWithClasses` | `koans/about_decorating_with_classes.py` |
| 28 | 29 | `koans.about_inheritance.AboutInheritance` | `koans/about_inheritance.py` |
| 29 | 30 | `koans.about_multiple_inheritance.AboutMultipleInheritance` | `koans/about_multiple_inheritance.py` |
| 30 | 31 | `koans.about_scope.AboutScope` | `koans/about_scope.py` |
| 31 | 32 | `koans.about_modules.AboutModules` | `koans/about_modules.py` |
| 32 | 33 | `koans.about_packages.AboutPackages` | `koans/about_packages.py` |
| 33 | 34 | `koans.about_class_attributes.AboutClassAttributes` | `koans/about_class_attributes.py` |
| 34 | 35 | `koans.about_attribute_access.AboutAttributeAccess` | `koans/about_attribute_access.py` |
| 35 | 36 | `koans.about_deleting_objects.AboutDeletingObjects` | `koans/about_deleting_objects.py` |
| 36 | 37 | `koans.about_proxy_object_project.AboutProxyObjectProject` | `koans/about_proxy_object_project.py` |
| 37 | 38 | `koans.about_proxy_object_project.TelevisionTest` | `koans/about_proxy_object_project.py` |
| 38 | 39 | `koans.about_extra_credit.AboutExtraCredit` | `koans/about_extra_credit.py` |
| 39 | 40 | `koans.about_regex.AboutRegex` | `koans/about_regex.py` |

A few details worth calling out:

- The manifest **begins** with `koans.about_asserts.AboutAsserts` (line 2) and
  **ends** with `koans.about_regex.AboutRegex` (line 40). `Source:
  koans.txt:L2`, `Source: koans.txt:L40`.
- **Two entries share one lesson file.** Orders 36 and 37 —
  `koans.about_proxy_object_project.AboutProxyObjectProject` and
  `koans.about_proxy_object_project.TelevisionTest` — both come from
  `koans/about_proxy_object_project.py`. `Source: koans.txt:L37-L38`. This is
  the reason the **39 manifest entries do not map one-to-one to lesson files**.
- `koans.about_extra_credit.AboutExtraCredit` (order 38, line 39) points at the
  optional extra-credit lesson, which — as the counting rules below explain — is
  treated specially. `Source: koans.txt:L39`.

## Counts: koans vs. lessons (and why they differ)

Three different numbers describe the curriculum, and it is easy to confuse
them. They are computed from different sources, so they are intentionally *not*
equal:

| Count | Value | What it measures | Source |
|-------|------:|------------------|--------|
| Manifest entries | **39** | Lines the suite is built from (the rows in the table above) | `koans.txt:L2-L40` |
| Koans | **304** | Total individual test methods across the assembled suite | `runner/sensei.py:L258-L259` |
| Lessons | **37** | Lesson files counted toward progress | `runner/sensei.py:L251-L269` |

### 39 manifest entries

The **39** value is simply the number of non-comment, non-blank lines in
[`koans.txt`](../koans.txt) — the entries enumerated in the table above.
`Source: koans.txt:L2-L40`.

### 304 koans

A *koan* is a single test method. The total, **304**, is what
`Sensei.total_koans()` returns: it asks the assembled suite how many test cases
it contains via `self.tests.countTestCases()`. Because the suite is built from
the manifest by [`path_to_enlightenment.koans()`](../runner/path_to_enlightenment.py),
this counts every individual test method inside every `TestCase` listed in the
manifest. `Source: runner/sensei.py:L258-L259`,
`Source: runner/sensei.py:L22`.

### 37 lessons

A *lesson* corresponds to an `about_*.py` file, but the count is **not** taken
from the manifest. `Sensei.total_lessons()` returns the length of
`filter_all_lessons()`, which discovers lesson files directly from the
filesystem with `glob.glob('.../koans/about*.py')` and then removes any path
containing `about_extra_credit`. There are **38** files matching
`koans/about*.py`; removing the single `about_extra_credit` entry leaves
**37**. `Source: runner/sensei.py:L251-L269`.

### Why the three numbers differ

- **39 entries vs. 37 lessons.** The manifest lists two `TestCase`s from the
  same file (`AboutProxyObjectProject` and `TelevisionTest`, orders 36 and 37
  above), and it includes `AboutExtraCredit`. The lesson count, by contrast,
  globs files on disk and drops `about_extra_credit`. The two figures therefore
  arise from different sources — manifest lines versus filtered file globbing —
  and are not expected to match. `Source: koans.txt:L37-L38`,
  `Source: runner/sensei.py:L261-L269`.
- **304 koans vs. 39 entries / 37 lessons.** Each `TestCase` (and therefore each
  lesson) contains many individual test methods, so the koan total is much
  larger than either the entry count or the lesson count. `Source:
  runner/sensei.py:L258-L259`.

### Lesson-exclusion logic

There are two independent places where lessons are filtered, and they are worth
distinguishing:

1. **Lesson discovery** — `filter_all_lessons()` globs `koans/about*.py` and
   removes paths containing `about_extra_credit`, so the optional extra-credit
   lesson never contributes to the **37**-lesson denominator. `Source:
   runner/sensei.py:L261-L269`.
2. **Lesson pass tally** — separately, while walking the suite in `startTest`,
   the `lesson_pass_count` is **not** incremented when the current class is
   named `AboutAsserts` or `AboutExtraCredit`; those two are skipped from the
   "lessons completed" tally. `Source: runner/sensei.py:L36-L37`.

### The progress line

These counts come together in the progress line a learner sees, produced by
`report_progress()`:

```text
You have completed X (P %) koans and Y (out of Z) lessons.
```

Here `X` is the running koan pass count, `P` is `X * 100 // total_koans()`, `Y`
is the lesson pass count, and `Z` is `total_lessons()` (the **37** above).
`Source: runner/sensei.py:L169-L175`. For a walkthrough of how to read this
line on your first run, see
[getting-started/first-steps.md](getting-started/first-steps.md).

## Sentinels

Each koan is a small failing assertion with a **sentinel** standing in for the
value you must supply. A sentinel is a deliberately obvious placeholder: when a
test runs as shipped, the sentinel makes the assertion fail, and your task is to
replace it with the correct value so the test passes. There are four sentinels,
all defined in [`runner/koan.py`](../runner/koan.py) and exported (alongside the
`Koan` base class) via `__all__`. `Source: runner/koan.py:L10`.

| Sentinel | Meaning / intent | Shipped placeholder |
|----------|------------------|---------------------|
| `__` | A value you must fill in | the marker string `"-=> FILL ME IN! <=-"` |
| `___` | An exception **class** — used where a koan expects a specific error type; defined as a custom `Exception` subclass | a placeholder `Exception` subclass |
| `____` | A true/false answer | the marker string `"-=> TRUE OR FALSE? <=-"` |
| `_____` | A numeric value | the placeholder number `0` |

- `__` is a generic "fill me in" placeholder for an arbitrary value. `Source:
  runner/koan.py:L12`.
- `___` is a custom `Exception` subclass, used in koans that expect you to name
  the error type involved. `Source: runner/koan.py:L14-L15`.
- `____` marks a place where the answer is either true or false. `Source:
  runner/koan.py:L17`.
- `_____` marks a place where the answer is a number. `Source:
  runner/koan.py:L19`.

These placeholders are **intentional pedagogy**: the sentinel values shown above
are the *unsolved* markers as they ship in the source, not answers. This
reference deliberately **does not reveal any correct answer** — you discover
each value by reading the koan and running it until it passes. The marker
strings and the numeric `0` are quoted here only so you can recognize an
unsolved blank when you see one; for a hands-on walkthrough of replacing your
first blank, see [getting-started/first-steps.md](getting-started/first-steps.md).

## Adding to the curriculum

To add a new lesson, create an `about_*.py` module under `koans/` containing a
`TestCase`, then register its fully-qualified name (for example
`koans.about_my_topic.AboutMyTopic`) on its own line in
[`koans.txt`](../koans.txt) at the position where you want it to run — order in
the manifest is the order learners encounter it. The full contributor workflow,
including running the runner self-tests, is documented in
[contributing/development.md](contributing/development.md). `Source:
koans.txt:L1-L40`.

## Source citations

- [koans.txt:L1-L40](../koans.txt) — the manifest: line 1 comment and the 39
  ordered `TestCase` entries on lines 2–40.
- [runner/path_to_enlightenment.py:L14-L62](../runner/path_to_enlightenment.py)
  — `KOANS_FILENAME` constant, `filter_koan_names` parsing, order-preserving
  suite assembly (`sortTestMethodsUsing = None`), and the `koans()` entry point.
- [runner/sensei.py:L36-L37](../runner/sensei.py) — lesson pass tally skips
  `AboutAsserts` and `AboutExtraCredit`.
- [runner/sensei.py:L169-L175](../runner/sensei.py) — `report_progress()`
  progress-line format.
- [runner/sensei.py:L251-L269](../runner/sensei.py) — `total_lessons()`,
  `total_koans()`, and `filter_all_lessons()` (the 304-koan and 37-lesson
  counts and the `about_extra_credit` exclusion).
- [runner/koan.py:L10-L19](../runner/koan.py) — the four sentinels and the
  `__all__` export.
