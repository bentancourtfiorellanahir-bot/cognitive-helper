from textwrap import dedent


def build_planner_prompt(task: str, language: str, mode: str) -> str:
    # # Tone instructions help the app feel more niche and intentional.
    tone_map = {
        "gentle": {
            "en": "Use a calm, supportive tone.",
            "es": "Usa un tono tranquilo y de apoyo."
        },
        "direct": {
            "en": "Use a direct, concise, action-first tone.",
            "es": "Usa un tono directo, conciso y orientado a la acción."
        },
        "study": {
            "en": "Prioritize structure, clarity, and study-friendly sequencing.",
            "es": "Prioriza estructura, claridad y una secuencia útil para estudiar."
        },
        "low_energy": {
            "en": "Assume the user has low energy. Make steps especially small and low-friction.",
            "es": "Asume que la persona tiene baja energía. Haz los pasos especialmente pequeños y fáciles de iniciar."
        }
    }

    selected_tone = tone_map.get(mode, tone_map["gentle"]).get(language, tone_map["gentle"]["en"])

    if language == "es":
        return dedent(f"""
        Eres un asistente de accesibilidad cognitiva.
        Tu trabajo es reducir la sobrecarga mental y convertir tareas complejas en pasos pequeños, concretos y fáciles de empezar.

        Reglas:
        - Responde solo con JSON válido.
        - Usa español claro y simple.
        - No des consejos abstractos.
        - Prioriza acciones que puedan empezar en menos de 5 minutos.
        - Si la tarea es grande, divídela en partes manejables.
        - Evita párrafos largos.
        - {selected_tone}

        Devuelve exactamente esta estructura:
        {{
          "summary": "string",
          "first_step": "string",
          "steps": [
            {{
              "title": "string",
              "instruction": "string",
              "minutes": 0
            }}
          ],
          "focus_tip": "string",
          "break_after_minutes": 5
        }}

        Tarea del usuario:
        {task}
        """).strip()

    return dedent(f"""
    You are an accessibility-focused cognitive support assistant.
    Your job is to reduce cognitive overload and turn complex tasks into small, concrete, easy-to-start steps.

    Rules:
    - Return valid JSON only.
    - Use clear, simple English.
    - Avoid abstract advice.
    - Prefer actions that can start in under 5 minutes.
    - If the task is large, split it into manageable parts.
    - Avoid long paragraphs.
    - {selected_tone}

    Return exactly this structure:
    {{
      "summary": "string",
      "first_step": "string",
      "steps": [
        {{
          "title": "string",
          "instruction": "string",
          "minutes": 0
        }}
      ],
      "focus_tip": "string",
      "break_after_minutes": 5
    }}

    User task:
    {task}
    """).strip()