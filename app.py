from flask import Flask, jsonify, render_template, request

from config import Config
from services.language_service import LanguageService
from services.planner_service import PlannerService
from utils.text_helpers import prepare_user_task
from utils.validators import validate_task_input
from utils.storage import append_history_entry

app = Flask(__name__)
app.config.from_object(Config)

language_service = LanguageService()
planner_service = PlannerService()


@app.route("/", methods=["GET"])
def home():
    language = language_service.get_language(request.args.get("lang"))
    translations = language_service.load_translations(language)

    return render_template(
        "index.html",
        t=translations,
        current_language=language,
        supported_languages=Config.SUPPORTED_LANGUAGES,
        supported_modes=Config.SUPPORTED_MODES,
        default_mode=Config.DEFAULT_MODE,
    )


@app.route("/api/plan", methods=["POST"])
def generate_plan():
    data = request.get_json(silent=True) or {}

    task = data.get("task") or ""
    language = language_service.get_language(data.get("language"))

    mode = data.get("mode") or Config.DEFAULT_MODE
    if mode not in Config.SUPPORTED_MODES:
        mode = Config.DEFAULT_MODE

    task = prepare_user_task(task)

    is_valid, error_message = validate_task_input(task)
    if not is_valid:
        return jsonify({"error": error_message}), 400

    plan, used_fallback = planner_service.create_plan(
        task=task,
        language=language,
        mode=mode,
    )

    append_history_entry(
        task=task,
        language=language,
        mode=mode,
        plan=plan,
        used_fallback=used_fallback,
    )

    return jsonify(
        {
            "plan": plan,
            "used_fallback": used_fallback,
            "language": language,
        }
    )


if __name__ == "__main__":
    app.run(debug=Config.DEBUG)