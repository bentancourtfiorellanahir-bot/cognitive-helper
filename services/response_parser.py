import json


def parse_ollama_json_response(raw_text: str) -> dict:
    raw_text = raw_text.strip()

    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        pass

    start = raw_text.find("{")
    end = raw_text.rfind("}")

    if start == -1 or end == -1:
        raise ValueError("No JSON object found in model response.")

    json_candidate = raw_text[start:end + 1]
    return json.loads(json_candidate)


def validate_plan_schema(data: dict) -> dict:
    required_top_keys = ["summary", "first_step", "steps", "focus_tip", "break_after_minutes"]

    for key in required_top_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")

    if not isinstance(data["steps"], list) or not data["steps"]:
        raise ValueError("Steps must be a non-empty list.")

    cleaned_steps = []
    for step in data["steps"]:
        title = str(step.get("title", "")).strip()
        instruction = str(step.get("instruction", "")).strip()
        minutes = max(1, int(step.get("minutes", 5) or 5))

        if not title:
            raise ValueError("Each step must include a non-empty title.")

        if not instruction:
            raise ValueError("Each step must include a non-empty instruction.")

        cleaned_steps.append(
            {
                "title": title,
                "instruction": instruction,
                "minutes": minutes,
            }
        )

    return {
        "summary": str(data["summary"]).strip(),
        "first_step": str(data["first_step"]).strip(),
        "steps": cleaned_steps,
        "focus_tip": str(data["focus_tip"]).strip(),
        "break_after_minutes": max(1, int(data["break_after_minutes"] or 5)),
    }