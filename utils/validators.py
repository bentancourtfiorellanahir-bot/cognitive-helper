from config import Config


def validate_task_input(task: str) -> tuple[bool, str | None]:
    # # Centralized validation keeps route handlers cleaner.
    if task is None:
        return False, "Task is required."

    cleaned_task = task.strip()

    if not cleaned_task:
        return False, "Task cannot be empty."

    if len(cleaned_task) > Config.MAX_TASK_LENGTH:
        return False, f"Task cannot exceed {Config.MAX_TASK_LENGTH} characters."

    return True, None


def validate_language(language: str | None) -> bool:
    return language in Config.SUPPORTED_LANGUAGES


def validate_mode(mode: str | None) -> bool:
    return mode in Config.SUPPORTED_MODES


def validate_plan_structure(plan: dict) -> tuple[bool, str | None]:
    required_keys = {"summary", "first_step", "steps", "focus_tip", "break_after_minutes"}

    if not isinstance(plan, dict):
        return False, "Plan must be a dictionary."

    missing = required_keys - set(plan.keys())
    if missing:
        return False, f"Missing keys: {', '.join(sorted(missing))}"

    if not isinstance(plan["steps"], list):
        return False, "Steps must be a list."

    if len(plan["steps"]) == 0:
        return False, "Steps cannot be empty."

    return True, None