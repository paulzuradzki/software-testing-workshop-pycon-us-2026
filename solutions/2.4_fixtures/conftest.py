import sys
from pathlib import Path

# Earlier solution conftests (2.1, 2.2) inserted their own modules/<id>/todo.py
# onto sys.path and cached `todo` in sys.modules. The 2.1/2.2 todo.py has no
# FileToDoTracker, so we drop the cached module before our import runs.
sys.modules.pop("todo", None)
sys.path.insert(0, str(Path(__file__).resolve().parent))
