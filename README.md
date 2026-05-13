# Practical Software Testing with Python

Learner repo: <https://github.com/paulzuradzki/software-testing-workshop-pycon-us-2026>

Slides: <https://paulzuradzki.com/talks/pycon-us-2026-tutorial-software-testing/> (also bundled in this repo as `slides.pdf`)

## 👋 Start here

Before the workshop, set up your environment:

```bash
git clone https://github.com/paulzuradzki/software-testing-workshop-pycon-us-2026.git
cd software-testing-workshop-pycon-us-2026
uv sync
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pytest solutions/
```

You should see a green summary line like:

```
============================== N passed in 0.05s ==============================
```

What matters is `passed` with no failures or errors.

For full setup, including a GitHub Codespaces fallback and editor setup videos, see **[docs/prep.md](docs/prep.md)**.

> **If `pytest` isn't found**, your venv probably isn't active in this
> terminal. Re-activate, or prefix any command with `uv run` to bypass
> activation: `uv run pytest --version`. The starter files in this
> workshop assume an activated venv.

## Description

Level up your testing and software design skills in this introduction to software testing techniques and principles. We will use pytest with brief comparisons to unittest. The workshop is aimed at newcomers to testing. Experienced programmers will also benefit from extra practice, side quests, and peer discussion.

**Learning Goals.** You will learn how to write, organize, and run tests with pytest. You will understand the differences between unit, integration, and end-to-end tests and when to use each. You will have practiced fixtures, parameterized tests, and test isolation. You will also have been introduced to test-driven development and to designing code for testability with dependency injection and seams.

**Why learn software testing?** Testing tends to be under-appreciated until you land in an untested codebase where every change breaks something else. Investing in this skill helps you code with confidence and pushes you toward more flexible designs.

**Beyond vibe coding.** Testing matters even more when you're working with AI-assisted or agentic coding. Good automated tests let you verify that AI-generated code works and let agents self-correct.

**What the workshop looks like.** The workshop is built around exercises with short explanations between them. You will write tests from the first exercise and keep writing them throughout. Optional side quests give an extra challenge and leave room for peer discussion. The material moves through three parts: fundamentals of writing and running tests, practical tooling like fixtures and parameterized tests, and testing as a design discipline.

**Prerequisites.** You should be comfortable writing Python functions and able to run Python scripts.

We use object-oriented programming throughout. You will see classes with `__init__` and methods you call as `obj.method()`. Part 3 introduces abstract base classes (`abc.ABC`) for dependency injection. If `class`, `self`, and `__init__` are unfamiliar, Real Python's intro to OOP starts from those primitives: <https://realpython.com/python3-object-oriented-programming/>. You will not need to write your own classes from scratch.

---

## Schedule

| Time (PT) | Block | Min |
| --- | --- | --: |
| 1:30–2:25 | Part 1. Fundamentals: motivation, first tests, structuring code and tests | 55 |
| 2:25–2:30 | Stretch break | 5 |
| 2:30–3:00 | Part 2a. Unit vs integration vs E2E. Start parameterization | 30 |
| 3:00–3:30 | Coffee break | 30 |
| 3:30–4:05 | Part 2b. Finish parameterization. Fixtures (`tmp_path`, SQLite) | 35 |
| 4:05–4:45 | Part 3. Snapshot testing, black-box vs glass-box, DI and seams, TDD overview | 40 |
| 4:45–4:50 | Attendee survey | 5 |
| 4:50–5:00 | Wrap-up. CI/CD demo, agentic testing demo, signposts, Q&A | 10 |

## Outline

<details>
<summary>Click to expand the session outline</summary>

### Part 1. Fundamentals (55 min)
- Welcome and personal project brainstorm
- Why testing matters
- Exercise 1.1: warm-up. Test a Fahrenheit-to-Celsius converter
- Exercise 1.2: unittest and pytest side-by-side
- Anatomy of a test (Arrange-Act-Assert)
- Exercise 1.3: restructure a test into AAA format
- Demo 1.4: targeting tests (file, class, function, pattern, mark, verbosity)
- Exercise 1.5: `src/` and `tests/` package structure

### Part 2. Testing techniques and tools (65 min, split across the coffee break)
- Unit vs integration vs end-to-end. The test pyramid
- Exercise 2.1: unit test for a `ToDoTracker` method
- Exercise 2.2: integration test exercising multiple methods
- Exercise 2.3: parameterized table test with `pytest.mark.parametrize`
- Exercise 2.4: file fixture using `yield` and `tmp_path`
- Demos: `setUp`/`tearDown` vs pytest fixture. SQLite in-memory database fixture

### Part 3. Real-world testing and design (40 min)
- Exercise 3.1: parameterized snapshot test for an untested function
- Black-box vs glass-box testing
- Exercise 3.2: inject a dependency. Identify the seam in a notification scenario
- TDD, red-green-refactor, and TDD-lite overview

### Wrap-up (10 min)
- GitHub Actions example for running tests on every push
- Agentic testing demo
- Signposts to topics we did not cover (mocking, coverage, Hypothesis, plugins, debugging tests, design principles)
- Personal project revisit

</details>

## Directory Structure

```
modules/        # exercises, organized by part
solutions/      # completed solutions, mirroring modules/ layout
```

Inside each `modules/<exercise>/`:
- `*_DEMO.py` / `*_DEMO.md`. Demo code the instructor walks through.
- `*_START.py`. Starter code for hands-on exercises. Your edits go here.

Solutions live in `solutions/<exercise>/`.

Run terminal commands from the module subdirectory unless a section
says otherwise. Use `cd` to navigate there first.

To verify all solutions pass: `pytest solutions/`

## Instructor Notes on AI Usage

> **TL;DR:** Disable auto-completions. Use chat critically. Avoid agentic coding until you've tried by hand.

Personal opinions; your mileage may vary.

<details>
<summary>Detailed guidance (click to expand)</summary>

### Auto-Completions

(Copilot in VS Code, Cursor completions and Tab, etc.)

**Disable completions for this workshop.** Your editor should have an option to disable them per-project or "snooze" them. The goal is muscle memory.

### Chat

(VS Code Copilot Chat, Cursor Chat, ChatGPT, Claude, etc.)

Chat is fine for quick Q&A and pair programming. Use the instructor and your peers too. The social element of an in-person workshop is part of the value.

A few cautions:

- **Hallucinations are harder to spot** when you're new to a topic. Cross-reference with docs and mentors.
- **AI can lead you down rabbit holes.** For example, if you ask about mocking, chat might show you pytest's `monkeypatch`, or `unittest.mock`'s inline mocks, context managers, or decorators, without explaining when to use which. A structured lesson avoids this.
- **Type code by hand.** Reading AI-generated code is not the same as writing it. Treat it like doing exercises vs. highlighting a textbook.

If you use chat and notice something interesting or unclear, raise it with the class.

### Agentic Coding

(Coding agents that edit files and run commands on your behalf)

Avoid agents for this workshop's content until you've tried by hand. If you get stuck, an agent can help debug, but verify its output with instructors or TAs.

I've included AGENTS.md/CLAUDE.md files for folks who want to use agents after the workshop. Tools like Claude Code have a "Learning" output style (`/output-style`) that creates TODO comments for you to fill in rather than writing the code for you.

</details>
