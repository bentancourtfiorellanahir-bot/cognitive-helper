def build_fallback_plan(task: str, language: str) -> dict:
    # # This keeps the app useful even if the model fails.
    if language == "es":
        return {
            "summary": "La tarea parece grande. Empecemos por una versión más simple.",
            "first_step": "Abrí lo que necesites y elegí una sola parte para empezar.",
            "steps": [
                {
                    "title": "Elegir una sola parte",
                    "instruction": "No intentes hacer todo. Elegí solo una parte pequeña de la tarea.",
                    "minutes": 3,
                },
                {
                    "title": "Preparar materiales",
                    "instruction": "Abrí apuntes, documentos o herramientas necesarias.",
                    "minutes": 5,
                },
                {
                    "title": "Primer bloque corto",
                    "instruction": "Trabajá solo 15 minutos en una parte concreta.",
                    "minutes": 15,
                },
                {
                    "title": "Pausa breve",
                    "instruction": "Descansá, tomá agua y volvé cuando termine la pausa.",
                    "minutes": 5,
                }
            ],
            "focus_tip": "Hacé solo el paso actual.",
            "break_after_minutes": 15,
        }

    return {
        "summary": "This task looks big. Let’s start with a simpler version.",
        "first_step": "Open what you need and choose only one part to begin with.",
        "steps": [
            {
                "title": "Choose one small part",
                "instruction": "Do not try to do everything at once. Pick one small part of the task.",
                "minutes": 3,
            },
            {
                "title": "Prepare materials",
                "instruction": "Open the notes, documents, or tools you need.",
                "minutes": 5,
            },
            {
                "title": "First short work block",
                "instruction": "Work for only 15 minutes on one concrete part.",
                "minutes": 15,
            },
            {
                "title": "Take a short break",
                "instruction": "Pause, drink water, and come back after the break.",
                "minutes": 5,
            }
        ],
        "focus_tip": "Do only the current step.",
        "break_after_minutes": 15,
    }