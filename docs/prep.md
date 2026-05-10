# Pre-workshop prep

Goal: have this repo's tests passing on your laptop before the
workshop.

Set up before you arrive at the venue. Venue Wi-Fi can be unreliable.
A fresh look the day prior is fine. Anything I change after that
will be minor tweaks.

If you hit setup issues at the venue, I or a TA will help during
exercise blocks.

## Installation options

Use Path A. Use B or C only if A fails.

| Path | When to use | Time |
| --- | --- | --: |
| A. Local install | Default. | ~10 min |
| B. GitHub Codespaces | Local Python broken or restricted. | ~5 min |
| C. Offline bundle | A and B both unavailable. | varies |

## Path A. Local install

### Prerequisites

- Python 3.12 or newer (`python3 --version`)
- Git (`git --version`)
- A terminal you're comfortable with

If `python3` is 3.11 or older, install a current Python first:

- Mac: `brew install python@3.12` or download from python.org.
- Windows: download the python.org installer. Tick "Add Python to PATH".
- Linux: use your distribution's package manager.

### 1. Install uv

`uv` is the package manager this repo uses.

Mac and Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows (PowerShell):
```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verify:
```
uv --version
```

### 2. Clone the repo

```
git clone https://github.com/paulzuradzki/software-testing-workshop-pycon-us-2026.git
cd software-testing-workshop-pycon-us-2026
```

### 3. Install dependencies

```
uv sync
```

Creates `.venv/` and installs pytest. ~30 seconds the first time.
If no errors print, it worked.

### 4. Activate the virtual environment

Mac and Linux (bash, zsh):
```
source .venv/bin/activate
```

fish:
```
source .venv/bin/activate.fish
```

Windows (PowerShell):
```
.venv\Scripts\Activate.ps1
```

Windows (cmd):
```
.venv\Scripts\activate.bat
```

Re-activate when you open a new terminal. Your prompt shows `(.venv)`
once activated. If you forget, prefix commands with `uv run`:
`uv run pytest --version`.

**VS Code users:** point the editor at this venv so completion and
"Run" use the right Python. Open the command palette
(`Cmd/Ctrl + Shift + P`), pick **Python: Select Interpreter**, and
choose the one in `./.venv/bin/python`.

### 5. Verify

```
pytest --version
pytest solutions/
```

Expected output:

```
$ pytest --version
pytest 9.0.2

$ pytest solutions/
============================= test session starts ==============================
platform darwin -- Python 3.12.x, pytest-9.0.2, pluggy-1.6.0
rootdir: /path/to/software-testing-workshop-pycon-us-2026
configfile: pyproject.toml
collected N items

solutions/1.1_warm_up_temp_script/test_convert_f_to_c_warmup.py .
solutions/1.3_structuring_a_test/test_aaa.py .
solutions/2.1_unit_test_todotracker/test_todo_unit.py ..
solutions/2.2_integration_test_todotracker/test_todo_integration.py .
solutions/2.3_parameterized_tests/test_convert_f_to_c_parametrized.py ..
...

============================== N passed in 0.03s ==============================
```

The exact test count grows as more solutions land. The check that
matters is the green `passed` line with no failures or errors.

## Path B. GitHub Codespaces

Use this if Path A fails or your laptop can't run a local Python
environment. You'll need a free GitHub account.

1. Open one of the following:
   - Direct link: https://github.com/codespaces/new?repo=paulzuradzki/software-testing-workshop-pycon-us-2026&ref=main
   - Or on the GitHub repo page: click Code, then Codespaces, then
     Create codespace on main.
2. Wait about 2 minutes for the environment to build. The
   devcontainer installs uv and runs `uv sync` on first launch.
3. In the integrated terminal:
   ```
   source .venv/bin/activate
   pytest solutions/
   ```
4. If you see `passed` with no failures, you're ready.

Codespaces pause when your browser tab closes. Reopening the tab
resumes the same environment. You can also open a codespace in your
local VS Code via the GitHub Codespaces extension.

## Path C. Offline bundle

If A and B both fail, contact me before the workshop. I'll share a
pre-downloaded tarball plus the wheels needed to install pytest
without internet.

No USB drives. Many work laptops refuse them.

Final fallback: the workshop code is small enough that I can rewrite
the examples live with stdlib `unittest`.

## Editor

Use any editor or IDE that opens `.py` files. I'll invoke pytest and
`python -m unittest` from the command line, so IDE testing features
aren't required. VS Code with the Python extension and PyCharm
Community are common choices.

For AI completion guidance during the workshop, see [README.md](../README.md#instructor-notes-on-ai-usage).

### New to VS Code? Optional setup videos

Corey Schaefer's walkthroughs:

- Mac (youtube.com): https://www.youtube.com/watch?v=06I63_p-2A4
- Windows (youtube.com): https://www.youtube.com/watch?v=-nh9rCzPJ20

Recommended sections, skip if familiar:

1. Installation
2. Switching interpreters
3. The Python extension
4. Using virtual environments
5. Unit testing. Awareness only; the workshop uses the CLI.

## Final readiness checklist

- [ ] `python3 --version` shows 3.12 or newer
- [ ] `git --version` works
- [ ] You've cloned the repo
- [ ] `uv sync` completed without errors
- [ ] You can re-activate the venv in a new terminal
- [ ] `pytest --version` works in your activated venv
- [ ] `pytest solutions/` reports `passed` with no failures

If any fail, arrive 15 minutes early for help.

## Day-of troubleshooting

### `pytest: command not found`

Venv isn't activated. Re-activate, or prefix with `uv run`.

### `ModuleNotFoundError: No module named 'todo'`

Most exercises expect you to `cd` into the module folder first
(e.g. `cd modules/2.1_unit_test_todotracker`). Each module's
`README.md` says where.

### Codespace won't start

Check https://www.githubstatus.com. If the service is up but your
codespace is stuck, delete it and create a new one. State lives in
the repo.

### `git pull` says "divergent branches" or "non-fast-forward"

The remote `main` has been rewritten since you cloned. Re-sync by
stashing any local edits, hard-resetting to the remote, and popping
the stash back:

```
git stash
git fetch origin
git reset --hard origin/main
git stash pop
```

`git reset --hard` discards uncommitted changes, so the `stash` steps
matter if you've started typing into a `_START.py` file. If nothing
local is worth keeping, deleting the folder and re-cloning works too.

### Anything else

Raise your hand.
