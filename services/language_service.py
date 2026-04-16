import json
from pathlib import Path

from config import Config


class LanguageService:
    def __init__(self) -> None:
        self.locales_dir = Path(__file__).resolve().parent.parent / "locales"

    def get_language(self, requested_language: str | None) -> str:
        if requested_language in Config.SUPPORTED_LANGUAGES:
            return requested_language
        return Config.DEFAULT_LANGUAGE

    def load_translations(self, language: str) -> dict:
        safe_language = self.get_language(language)
        file_path = self.locales_dir / f"{safe_language}.json"

        with file_path.open("r", encoding="utf-8") as file:
            return json.load(file)