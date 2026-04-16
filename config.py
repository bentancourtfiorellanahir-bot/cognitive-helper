import os


class Config:
    # # Base app configuration
    APP_NAME = "Cognitive Helper"
    DEBUG = True

    # # Ollama local API
    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:1.5b")
    OLLAMA_TIMEOUT = int(os.getenv("OLLAMA_TIMEOUT", "90"))

    # # UX / validation
    MAX_TASK_LENGTH = 1200
    DEFAULT_BREAK_MINUTES = 5
    DEFAULT_WORK_MINUTES = 15

    # # Supported languages
    SUPPORTED_LANGUAGES = ("en", "es")
    DEFAULT_LANGUAGE = "en"

    # # Accessibility / tone presets
    SUPPORTED_MODES = ("gentle", "direct", "study", "low_energy")
    DEFAULT_MODE = "gentle"