from config import Config
from services.fallback_rules import build_fallback_plan
from services.rule_based_planner import build_rule_based_plan


class PlannerService:
    def __init__(self) -> None:
        pass

    def create_plan(self, task: str, language: str, mode: str) -> tuple[dict, bool]:
        task = (task or "").strip()
        language = (
            language
            if language in Config.SUPPORTED_LANGUAGES
            else Config.DEFAULT_LANGUAGE
        )
        mode = mode if mode in Config.SUPPORTED_MODES else Config.DEFAULT_MODE

        if not task:
            return build_fallback_plan(task="", language=language), True

        try:
            plan = build_rule_based_plan(
                task=task,
                language=language,
                mode=mode,
            )
            return plan, False
        except Exception as e:
            print(f"Planner error: {e}")
            return build_fallback_plan(task=task, language=language), True