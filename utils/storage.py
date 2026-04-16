import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

USER_PREFERENCES_FILE = DATA_DIR / "user_preferences.json"
TASK_HISTORY_FILE = DATA_DIR / "task_history.json"
EXAMPLES_FILE = DATA_DIR / "examples.json"


def read_json_file(path: Path, default):
    if not path.exists():
        return default

    with path.open("r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return default


def write_json_file(path: Path, content) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(content, file, ensure_ascii=False, indent=2)


def load_user_preferences() -> dict:
    return read_json_file(USER_PREFERENCES_FILE, default={})


def save_user_preferences(preferences: dict) -> None:
    write_json_file(USER_PREFERENCES_FILE, preferences)


def load_task_history() -> list:
    return read_json_file(TASK_HISTORY_FILE, default=[])


def save_task_history(history: list) -> None:
    write_json_file(TASK_HISTORY_FILE, history)


def append_history_entry(
    task: str,
    language: str,
    mode: str,
    plan: dict,
    used_fallback: bool
) -> dict:
    history = load_task_history()

    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "task": task,
        "language": language,
        "mode": mode,
        "used_fallback": used_fallback,
        "plan": plan
    }

    history.append(entry)
    save_task_history(history)

    return entry


def load_examples() -> list:
    return read_json_file(EXAMPLES_FILE, default=[])