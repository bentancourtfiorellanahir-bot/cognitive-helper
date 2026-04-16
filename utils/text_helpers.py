import re


def normalize_whitespace(text: str) -> str:
    # # Useful before sending text to the model or saving to history.
    return re.sub(r"\s+", " ", text).strip()


def strip_problematic_quotes(text: str) -> str:
    # # Small cleanup helper in case pasted content has mixed smart quotes.
    replacements = {
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'"
    }

    for original, replacement in replacements.items():
        text = text.replace(original, replacement)

    return text


def prepare_user_task(text: str) -> str:
    cleaned = strip_problematic_quotes(text or "")
    cleaned = normalize_whitespace(cleaned)
    return cleaned


def shorten_text(text: str, max_length: int = 160) -> str:
    text = normalize_whitespace(text)
    if len(text) <= max_length:
        return text
    return text[: max_length - 3].rstrip() + "..."


def detect_basic_language(text: str) -> str:
    # # This is intentionally lightweight.
    # # It is not perfect, but good enough as a future helper.
    lowered = (text or "").lower()

    spanish_markers = [
        "tengo", "necesito", "quiero", "estudiar", "ordenar",
        "por qué", "porque", "bloqueada", "cansada", "hacer"
    ]

    english_markers = [
        "i need", "i want", "study", "clean", "blocked",
        "overwhelmed", "start", "task", "exam"
    ]

    spanish_score = sum(marker in lowered for marker in spanish_markers)
    english_score = sum(marker in lowered for marker in english_markers)

    if spanish_score > english_score:
        return "es"

    return "en"