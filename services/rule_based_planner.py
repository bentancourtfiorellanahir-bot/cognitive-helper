from __future__ import annotations


def build_rule_based_plan(task: str, language: str, mode: str) -> dict:
    normalized_task = (task or "").strip()
    lowered = normalized_task.lower()

    task_type = detect_task_type(lowered)

    if language == "es":
        return build_spanish_plan(normalized_task, task_type, mode)

    return build_english_plan(normalized_task, task_type, mode)


def detect_task_type(task: str) -> str:
    study_keywords = [
        "study", "exam", "homework", "assignment", "essay", "class", "notes",
        "estudi", "examen", "tarea", "apunte", "trabajo práctico", "tp", "parcial"
    ]
    cleaning_keywords = [
        "clean", "room", "organize", "laundry", "kitchen", "mess",
        "ordenar", "limpiar", "cuarto", "habitación", "lavar", "ropa", "desorden"
    ]
    admin_keywords = [
        "email", "paperwork", "forms", "documents", "bank", "bills", "call",
        "mail", "correo", "formularios", "documentos", "facturas", "banco", "llamar"
    ]
    work_keywords = [
        "project", "deadline", "meeting", "report", "presentation", "work",
        "proyecto", "entrega", "reunión", "informe", "presentación", "trabajo"
    ]

    if any(keyword in task for keyword in study_keywords):
        return "study"
    if any(keyword in task for keyword in cleaning_keywords):
        return "cleaning"
    if any(keyword in task for keyword in admin_keywords):
        return "admin"
    if any(keyword in task for keyword in work_keywords):
        return "work"

    return "general"


def build_english_plan(task: str, task_type: str, mode: str) -> dict:
    tone = english_tone(mode)

    if task_type == "study":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["study_summary"]}',
            "first_step": tone["study_first_step"],
            "steps": [
                {
                    "title": tone["study_step_1_title"],
                    "instruction": tone["study_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["study_step_2_title"],
                    "instruction": tone["study_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["study_step_3_title"],
                    "instruction": tone["study_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["study_step_4_title"],
                    "instruction": tone["study_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "cleaning":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["cleaning_summary"]}',
            "first_step": tone["cleaning_first_step"],
            "steps": [
                {
                    "title": tone["cleaning_step_1_title"],
                    "instruction": tone["cleaning_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["cleaning_step_2_title"],
                    "instruction": tone["cleaning_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["cleaning_step_3_title"],
                    "instruction": tone["cleaning_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["cleaning_step_4_title"],
                    "instruction": tone["cleaning_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "admin":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["admin_summary"]}',
            "first_step": tone["admin_first_step"],
            "steps": [
                {
                    "title": tone["admin_step_1_title"],
                    "instruction": tone["admin_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["admin_step_2_title"],
                    "instruction": tone["admin_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["admin_step_3_title"],
                    "instruction": tone["admin_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["admin_step_4_title"],
                    "instruction": tone["admin_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "work":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["work_summary"]}',
            "first_step": tone["work_first_step"],
            "steps": [
                {
                    "title": tone["work_step_1_title"],
                    "instruction": tone["work_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["work_step_2_title"],
                    "instruction": tone["work_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["work_step_3_title"],
                    "instruction": tone["work_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["work_step_4_title"],
                    "instruction": tone["work_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    return {
        "summary": f'{tone["summary_prefix"]} {tone["general_summary"]}',
        "first_step": tone["general_first_step"],
        "steps": [
            {
                "title": tone["general_step_1_title"],
                "instruction": tone["general_step_1_instruction"],
                "minutes": tone["small_minutes"],
            },
            {
                "title": tone["general_step_2_title"],
                "instruction": tone["general_step_2_instruction"],
                "minutes": tone["medium_minutes"],
            },
            {
                "title": tone["general_step_3_title"],
                "instruction": tone["general_step_3_instruction"],
                "minutes": tone["focus_minutes"],
            },
            {
                "title": tone["general_step_4_title"],
                "instruction": tone["general_step_4_instruction"],
                "minutes": tone["closing_minutes"],
            }
        ],
        "focus_tip": tone["focus_tip"],
        "break_after_minutes": tone["focus_minutes"],
    }


def build_spanish_plan(task: str, task_type: str, mode: str) -> dict:
    tone = spanish_tone(mode)

    if task_type == "study":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["study_summary"]}',
            "first_step": tone["study_first_step"],
            "steps": [
                {
                    "title": tone["study_step_1_title"],
                    "instruction": tone["study_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["study_step_2_title"],
                    "instruction": tone["study_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["study_step_3_title"],
                    "instruction": tone["study_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["study_step_4_title"],
                    "instruction": tone["study_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "cleaning":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["cleaning_summary"]}',
            "first_step": tone["cleaning_first_step"],
            "steps": [
                {
                    "title": tone["cleaning_step_1_title"],
                    "instruction": tone["cleaning_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["cleaning_step_2_title"],
                    "instruction": tone["cleaning_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["cleaning_step_3_title"],
                    "instruction": tone["cleaning_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["cleaning_step_4_title"],
                    "instruction": tone["cleaning_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "admin":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["admin_summary"]}',
            "first_step": tone["admin_first_step"],
            "steps": [
                {
                    "title": tone["admin_step_1_title"],
                    "instruction": tone["admin_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["admin_step_2_title"],
                    "instruction": tone["admin_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["admin_step_3_title"],
                    "instruction": tone["admin_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["admin_step_4_title"],
                    "instruction": tone["admin_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    if task_type == "work":
        return {
            "summary": f'{tone["summary_prefix"]} {tone["work_summary"]}',
            "first_step": tone["work_first_step"],
            "steps": [
                {
                    "title": tone["work_step_1_title"],
                    "instruction": tone["work_step_1_instruction"],
                    "minutes": tone["small_minutes"],
                },
                {
                    "title": tone["work_step_2_title"],
                    "instruction": tone["work_step_2_instruction"],
                    "minutes": tone["medium_minutes"],
                },
                {
                    "title": tone["work_step_3_title"],
                    "instruction": tone["work_step_3_instruction"],
                    "minutes": tone["focus_minutes"],
                },
                {
                    "title": tone["work_step_4_title"],
                    "instruction": tone["work_step_4_instruction"],
                    "minutes": tone["closing_minutes"],
                }
            ],
            "focus_tip": tone["focus_tip"],
            "break_after_minutes": tone["focus_minutes"],
        }

    return {
        "summary": f'{tone["summary_prefix"]} {tone["general_summary"]}',
        "first_step": tone["general_first_step"],
        "steps": [
            {
                "title": tone["general_step_1_title"],
                "instruction": tone["general_step_1_instruction"],
                "minutes": tone["small_minutes"],
            },
            {
                "title": tone["general_step_2_title"],
                "instruction": tone["general_step_2_instruction"],
                "minutes": tone["medium_minutes"],
            },
            {
                "title": tone["general_step_3_title"],
                "instruction": tone["general_step_3_instruction"],
                "minutes": tone["focus_minutes"],
            },
            {
                "title": tone["general_step_4_title"],
                "instruction": tone["general_step_4_instruction"],
                "minutes": tone["closing_minutes"],
            }
        ],
        "focus_tip": tone["focus_tip"],
        "break_after_minutes": tone["focus_minutes"],
    }


def english_tone(mode: str) -> dict:
    mapping = {
        "gentle": {
            "summary_prefix": "You do not need to do everything at once.",
            "focus_tip": "Stay with only the current step.",
            "small_minutes": 3,
            "medium_minutes": 5,
            "focus_minutes": 15,
            "closing_minutes": 5,

            "study_summary": "This looks like a study task, so the goal is to make it feel lighter and easier to begin.",
            "study_first_step": "Open your notes and choose only one topic to look at first.",
            "study_step_1_title": "Choose one topic",
            "study_step_1_instruction": "Pick only one chapter, question set, or topic. Leave the rest aside for now.",
            "study_step_2_title": "Prepare materials",
            "study_step_2_instruction": "Open your notes, slides, book, or document and keep one blank page nearby.",
            "study_step_3_title": "Do one short study block",
            "study_step_3_instruction": "Study only that one topic for a short block. You are just getting started.",
            "study_step_4_title": "Mark what is still unclear",
            "study_step_4_instruction": "Write down the parts you still do not understand so the next step feels easier.",

            "cleaning_summary": "This looks like a cleaning task, so we will make it smaller and more manageable.",
            "cleaning_first_step": "Choose one small surface or one corner only.",
            "cleaning_step_1_title": "Choose one zone",
            "cleaning_step_1_instruction": "Pick one desk, chair, bed section, or one corner of the room.",
            "cleaning_step_2_title": "Remove visible clutter",
            "cleaning_step_2_instruction": "Take away the most obvious clutter or misplaced items first.",
            "cleaning_step_3_title": "Do one short reset",
            "cleaning_step_3_instruction": "Spend one short block putting things back where they belong in that area only.",
            "cleaning_step_4_title": "Pause before expanding",
            "cleaning_step_4_instruction": "Stop and check whether you want to continue or stay with this single finished area.",

            "admin_summary": "This looks like an admin task, so the goal is to reduce friction and start gently.",
            "admin_first_step": "Open the document, message, website, or app related to the task.",
            "admin_step_1_title": "Open what you need",
            "admin_step_1_instruction": "Bring up the email, form, website, document, or account connected to the task.",
            "admin_step_2_title": "Find the first action",
            "admin_step_2_instruction": "Identify the first visible action, like reading, replying, or filling one field.",
            "admin_step_3_title": "Complete one concrete action",
            "admin_step_3_instruction": "Do only that first concrete action. Do not worry about finishing everything yet.",
            "admin_step_4_title": "Write the next action",
            "admin_step_4_instruction": "Leave a short note with the next step so returning later feels easier.",

            "work_summary": "This looks like a work task, so we will reduce it to one manageable output.",
            "work_first_step": "Define the exact output you need first.",
            "work_step_1_title": "Define the output",
            "work_step_1_instruction": "Decide what the task needs at the end: a message, draft, file, report, or finished section.",
            "work_step_2_title": "Open the relevant tools",
            "work_step_2_instruction": "Open the document, app, messages, or files related to that output.",
            "work_step_3_title": "Do one focused block",
            "work_step_3_instruction": "Work only on the first part of the output. Keep the scope small.",
            "work_step_4_title": "Leave a checkpoint",
            "work_step_4_instruction": "Write one sentence about what is done and what comes next.",

            "general_summary": "This task feels large, so the goal is to make the first move smaller and clearer.",
            "general_first_step": "Open what you need and choose one part only.",
            "general_step_1_title": "Choose one part",
            "general_step_1_instruction": "Do not try to solve the whole task. Pick one part you can begin now.",
            "general_step_2_title": "Prepare the materials",
            "general_step_2_instruction": "Open the tools, notes, files, or space you need.",
            "general_step_3_title": "Do one short work block",
            "general_step_3_instruction": "Work only on that one part for a short block.",
            "general_step_4_title": "Pause and decide the next move",
            "general_step_4_instruction": "Stop briefly and choose whether to continue, rest, or define the next step.",
        },

        "direct": {
            "summary_prefix": "Keep this simple and practical.",
            "focus_tip": "Do the current step and ignore the rest.",
            "small_minutes": 2,
            "medium_minutes": 3,
            "focus_minutes": 12,
            "closing_minutes": 2,

            "study_summary": "This is a study task. Make it specific and move.",
            "study_first_step": "Open your notes and pick one topic.",
            "study_step_1_title": "Pick one topic",
            "study_step_1_instruction": "Choose one chapter, question set, or topic. Ignore everything else.",
            "study_step_2_title": "Open materials",
            "study_step_2_instruction": "Open the notes, book, slides, or file you need.",
            "study_step_3_title": "Study now",
            "study_step_3_instruction": "Study that one topic for one focused block.",
            "study_step_4_title": "Mark the gap",
            "study_step_4_instruction": "Write down what is still unclear.",

            "cleaning_summary": "This is a cleaning task. Shrink the area and start.",
            "cleaning_first_step": "Pick one zone only.",
            "cleaning_step_1_title": "Pick one zone",
            "cleaning_step_1_instruction": "Choose one desk, one corner, or one surface.",
            "cleaning_step_2_title": "Clear clutter",
            "cleaning_step_2_instruction": "Remove the most visible clutter first.",
            "cleaning_step_3_title": "Reset the area",
            "cleaning_step_3_instruction": "Put things back where they belong in that area only.",
            "cleaning_step_4_title": "Stop and check",
            "cleaning_step_4_instruction": "Decide whether to continue or stop there.",

            "admin_summary": "This is an admin task. Open it and do the first action.",
            "admin_first_step": "Open the task source now.",
            "admin_step_1_title": "Open it",
            "admin_step_1_instruction": "Open the email, form, website, or document.",
            "admin_step_2_title": "Find the first action",
            "admin_step_2_instruction": "Identify the first concrete thing to do.",
            "admin_step_3_title": "Do it",
            "admin_step_3_instruction": "Complete that one concrete action.",
            "admin_step_4_title": "Leave the next step",
            "admin_step_4_instruction": "Write one short note about what comes next.",

            "work_summary": "This is a work task. Define the output and start producing.",
            "work_first_step": "Define the exact deliverable.",
            "work_step_1_title": "Define the deliverable",
            "work_step_1_instruction": "Name the output: message, file, report, or section.",
            "work_step_2_title": "Open tools",
            "work_step_2_instruction": "Open only the tools related to that output.",
            "work_step_3_title": "Produce the first part",
            "work_step_3_instruction": "Work on the first part without multitasking.",
            "work_step_4_title": "Leave a checkpoint",
            "work_step_4_instruction": "Write what is done and what is next.",

            "general_summary": "This task is too big in your head. Cut it down and start.",
            "general_first_step": "Choose one part only.",
            "general_step_1_title": "Choose the part",
            "general_step_1_instruction": "Pick the smallest useful part you can begin now.",
            "general_step_2_title": "Open what you need",
            "general_step_2_instruction": "Bring up the tools or materials.",
            "general_step_3_title": "Work one block",
            "general_step_3_instruction": "Do one short focused block.",
            "general_step_4_title": "Define the next step",
            "general_step_4_instruction": "Write the next move clearly.",
        },

        "study": {
            "summary_prefix": "Use structure and clarity first.",
            "focus_tip": "Finish one study step before moving on.",
            "small_minutes": 3,
            "medium_minutes": 7,
            "focus_minutes": 20,
            "closing_minutes": 7,

            "study_summary": "This is a study task, so the priority is sequence, clarity, and retention.",
            "study_first_step": "Open your materials and define the exact topic you will cover first.",
            "study_step_1_title": "Define the study target",
            "study_step_1_instruction": "Choose one chapter, concept, or question set and name it clearly.",
            "study_step_2_title": "Gather study materials",
            "study_step_2_instruction": "Open your notes, book, slides, and one page for active recall or summary.",
            "study_step_3_title": "Do a focused study block",
            "study_step_3_instruction": "Study the topic in one uninterrupted block, aiming to understand the main points.",
            "study_step_4_title": "Summarize and mark gaps",
            "study_step_4_instruction": "Write a short summary and list what still needs review.",

            "cleaning_summary": "This is not a study task, but we will still keep it structured and sequenced.",
            "cleaning_first_step": "Define the area you will complete first.",
            "cleaning_step_1_title": "Define the area",
            "cleaning_step_1_instruction": "Choose one section to finish fully before moving on.",
            "cleaning_step_2_title": "Sort by type",
            "cleaning_step_2_instruction": "Group visible items into trash, keep, and relocate.",
            "cleaning_step_3_title": "Complete the reset",
            "cleaning_step_3_instruction": "Return items to their place and finish that one area.",
            "cleaning_step_4_title": "Review the result",
            "cleaning_step_4_instruction": "Check what improved and what area would come next.",

            "admin_summary": "This admin task will work better with sequence and visible structure.",
            "admin_first_step": "Open the relevant source and identify the required outcome.",
            "admin_step_1_title": "Define the outcome",
            "admin_step_1_instruction": "State what must be completed: reply sent, form submitted, or document checked.",
            "admin_step_2_title": "Gather needed information",
            "admin_step_2_instruction": "Open the related files, messages, websites, or references.",
            "admin_step_3_title": "Complete the main action",
            "admin_step_3_instruction": "Finish the most important administrative action first.",
            "admin_step_4_title": "Record pending items",
            "admin_step_4_instruction": "Write any pending detail that still needs follow-up.",

            "work_summary": "This work task will be easier with a clear sequence and defined output.",
            "work_first_step": "Identify the deliverable and define the first segment.",
            "work_step_1_title": "Identify the deliverable",
            "work_step_1_instruction": "State exactly what you need to produce.",
            "work_step_2_title": "Gather references and tools",
            "work_step_2_instruction": "Open the files, apps, or notes linked to that deliverable.",
            "work_step_3_title": "Complete one focused block",
            "work_step_3_instruction": "Work on the first meaningful part of the deliverable.",
            "work_step_4_title": "Review and note next steps",
            "work_step_4_instruction": "Write what is complete and what remains.",

            "general_summary": "This task needs structure, so we will define a sequence before acting.",
            "general_first_step": "Define the first concrete part of the task.",
            "general_step_1_title": "Define the first part",
            "general_step_1_instruction": "Choose the first part that would make the task clearer.",
            "general_step_2_title": "Prepare materials",
            "general_step_2_instruction": "Open or gather everything needed for that part.",
            "general_step_3_title": "Complete one structured block",
            "general_step_3_instruction": "Work in one focused block with a single goal.",
            "general_step_4_title": "Review progress",
            "general_step_4_instruction": "Write down what was done and what should come next.",
        },

        "low_energy": {
            "summary_prefix": "Use the smallest possible version of the task.",
            "focus_tip": "Keep the step tiny and easy to start.",
            "small_minutes": 2,
            "medium_minutes": 3,
            "focus_minutes": 8,
            "closing_minutes": 2,

            "study_summary": "This looks like a study task, so the goal is to make it feel very light.",
            "study_first_step": "Open your notes and look at one topic only.",
            "study_step_1_title": "Choose one tiny topic",
            "study_step_1_instruction": "Pick the smallest topic, question, or section you can handle right now.",
            "study_step_2_title": "Open materials gently",
            "study_step_2_instruction": "Open only the notes or file you need for that tiny topic.",
            "study_step_3_title": "Do a very short study block",
            "study_step_3_instruction": "Study for a very short block. Stopping early is okay.",
            "study_step_4_title": "Leave one note",
            "study_step_4_instruction": "Write one sentence about what to come back to later.",

            "cleaning_summary": "This looks like a cleaning task, so the goal is to keep it very small.",
            "cleaning_first_step": "Choose one tiny area only.",
            "cleaning_step_1_title": "Choose a tiny zone",
            "cleaning_step_1_instruction": "Pick one shelf, one chair, or one small surface.",
            "cleaning_step_2_title": "Remove a few visible items",
            "cleaning_step_2_instruction": "Take away only the most obvious clutter.",
            "cleaning_step_3_title": "Reset for a short moment",
            "cleaning_step_3_instruction": "Put a few things back where they belong.",
            "cleaning_step_4_title": "Stop without guilt",
            "cleaning_step_4_instruction": "Pause here. A small reset still counts.",

            "admin_summary": "This looks like an admin task, so reduce it to one very easy action.",
            "admin_first_step": "Open the task source only.",
            "admin_step_1_title": "Open it",
            "admin_step_1_instruction": "Open the email, form, site, or file.",
            "admin_step_2_title": "Read the first part",
            "admin_step_2_instruction": "Only read or look at the first visible section.",
            "admin_step_3_title": "Do one tiny action",
            "admin_step_3_instruction": "Reply to one line, fill one field, or check one document.",
            "admin_step_4_title": "Leave it ready",
            "admin_step_4_instruction": "Leave a note or keep the tab open for next time.",

            "work_summary": "This looks like a work task, so the goal is to reduce pressure and begin lightly.",
            "work_first_step": "Name the smallest possible output.",
            "work_step_1_title": "Name the smallest output",
            "work_step_1_instruction": "Choose the smallest useful piece you can produce.",
            "work_step_2_title": "Open only what matters",
            "work_step_2_instruction": "Open just the app or file you need right now.",
            "work_step_3_title": "Do one tiny block",
            "work_step_3_instruction": "Work for a short block on only that small piece.",
            "work_step_4_title": "Pause and save progress",
            "work_step_4_instruction": "Stop and leave things ready for next time.",

            "general_summary": "This task feels heavy, so make it as small and low-pressure as possible.",
            "general_first_step": "Choose the easiest part you can start now.",
            "general_step_1_title": "Choose the easiest part",
            "general_step_1_instruction": "Pick the lightest possible starting point.",
            "general_step_2_title": "Open what you need",
            "general_step_2_instruction": "Bring up only the minimum needed.",
            "general_step_3_title": "Do a tiny block",
            "general_step_3_instruction": "Work for a very short block only.",
            "general_step_4_title": "Pause kindly",
            "general_step_4_instruction": "Stop and count this as progress.",
        },
    }

    return mapping.get(mode, mapping["gentle"])


def spanish_tone(mode: str) -> dict:
    mapping = {
        "gentle": {
            "summary_prefix": "No hace falta hacer todo de una vez.",
            "focus_tip": "Quedate solo con el paso actual.",
            "small_minutes": 3,
            "medium_minutes": 5,
            "focus_minutes": 15,
            "closing_minutes": 5,

            "study_summary": "Parece una tarea de estudio, así que la idea es volverla más liviana y fácil de empezar.",
            "study_first_step": "Abrí tus apuntes y elegí un solo tema para mirar primero.",
            "study_step_1_title": "Elegir un tema",
            "study_step_1_instruction": "Elegí un solo capítulo, grupo de preguntas o tema. Dejando el resto aparte por ahora.",
            "study_step_2_title": "Preparar materiales",
            "study_step_2_instruction": "Abrí apuntes, diapositivas, libro o documento y dejá una hoja cerca.",
            "study_step_3_title": "Hacer un bloque corto de estudio",
            "study_step_3_instruction": "Estudiá solo ese tema durante un bloque corto. Solo estás empezando.",
            "study_step_4_title": "Marcar lo que no está claro",
            "study_step_4_instruction": "Anotá qué partes todavía no entendés para que el próximo paso sea más fácil.",

            "cleaning_summary": "Parece una tarea de orden o limpieza, así que la vamos a hacer más manejable.",
            "cleaning_first_step": "Elegí una superficie chica o un rincón solamente.",
            "cleaning_step_1_title": "Elegir una zona",
            "cleaning_step_1_instruction": "Elegí un escritorio, una silla, una parte de la cama o un rincón del cuarto.",
            "cleaning_step_2_title": "Sacar el desorden visible",
            "cleaning_step_2_instruction": "Retirá primero el desorden más evidente o los objetos fuera de lugar.",
            "cleaning_step_3_title": "Hacer un bloque corto de orden",
            "cleaning_step_3_instruction": "Ordená solo esa zona durante un bloque corto.",
            "cleaning_step_4_title": "Pausar antes de expandir",
            "cleaning_step_4_instruction": "Frená y revisá si querés seguir o quedarte con esa sola zona terminada.",

            "admin_summary": "Parece una tarea administrativa, así que la idea es bajar la fricción y empezar suave.",
            "admin_first_step": "Abrí el documento, mensaje, sitio o app relacionada con la tarea.",
            "admin_step_1_title": "Abrir lo necesario",
            "admin_step_1_instruction": "Abrí el mail, formulario, sitio, documento o cuenta vinculada a la tarea.",
            "admin_step_2_title": "Encontrar la primera acción",
            "admin_step_2_instruction": "Identificá la primera acción visible, como leer, responder o completar un campo.",
            "admin_step_3_title": "Hacer una acción concreta",
            "admin_step_3_instruction": "Hacé solo esa primera acción concreta. No hace falta terminar todo ya.",
            "admin_step_4_title": "Dejar anotado el siguiente paso",
            "admin_step_4_instruction": "Dejá una nota corta con el paso siguiente para volver más fácil después.",

            "work_summary": "Parece una tarea de trabajo, así que la vamos a reducir a un resultado manejable.",
            "work_first_step": "Definí primero el resultado exacto que necesitás.",
            "work_step_1_title": "Definir el resultado",
            "work_step_1_instruction": "Definí si al final necesitás un mensaje, borrador, archivo, informe o sección terminada.",
            "work_step_2_title": "Abrir herramientas",
            "work_step_2_instruction": "Abrí documentos, apps, mensajes o archivos relacionados con ese resultado.",
            "work_step_3_title": "Hacer un bloque de foco",
            "work_step_3_instruction": "Trabajá solo en la primera parte del resultado. Manteniendo el alcance chico.",
            "work_step_4_title": "Dejar un checkpoint",
            "work_step_4_instruction": "Escribí una frase sobre lo que ya está hecho y lo que sigue.",

            "general_summary": "La tarea se siente grande, así que la idea es volver el primer movimiento más chico y claro.",
            "general_first_step": "Abrí lo que necesites y elegí una sola parte.",
            "general_step_1_title": "Elegir una parte",
            "general_step_1_instruction": "No intentes resolver todo. Elegí una parte que puedas empezar ahora.",
            "general_step_2_title": "Preparar materiales",
            "general_step_2_instruction": "Abrí herramientas, apuntes, archivos o el espacio que necesites.",
            "general_step_3_title": "Hacer un bloque corto",
            "general_step_3_instruction": "Trabajá solo en esa parte durante un bloque corto.",
            "general_step_4_title": "Pausar y decidir",
            "general_step_4_instruction": "Frená un momento y decidí si seguís, descansás o definís el próximo paso.",
        },

        "direct": {
            "summary_prefix": "Mantené esto simple y práctico.",
            "focus_tip": "Hacé el paso actual e ignorá el resto.",
            "small_minutes": 2,
            "medium_minutes": 3,
            "focus_minutes": 12,
            "closing_minutes": 2,

            "study_summary": "Esto es estudio. Hacelo específico y arrancá.",
            "study_first_step": "Abrí apuntes y elegí un tema.",
            "study_step_1_title": "Elegí un tema",
            "study_step_1_instruction": "Elegí un capítulo, grupo de preguntas o tema. Ignorá lo demás.",
            "study_step_2_title": "Abrí materiales",
            "study_step_2_instruction": "Abrí apuntes, libro, diapositivas o archivo.",
            "study_step_3_title": "Estudiá ahora",
            "study_step_3_instruction": "Estudiá ese tema en un bloque de foco.",
            "study_step_4_title": "Marcá el hueco",
            "study_step_4_instruction": "Anotá lo que todavía no entendés.",

            "cleaning_summary": "Esto es orden o limpieza. Reducí la zona y empezá.",
            "cleaning_first_step": "Elegí una sola zona.",
            "cleaning_step_1_title": "Elegí una zona",
            "cleaning_step_1_instruction": "Elegí una superficie, un rincón o una parte del cuarto.",
            "cleaning_step_2_title": "Sacá el desorden",
            "cleaning_step_2_instruction": "Retirá primero lo más visible.",
            "cleaning_step_3_title": "Ordená la zona",
            "cleaning_step_3_instruction": "Poné las cosas en su lugar solo en esa zona.",
            "cleaning_step_4_title": "Frená y revisá",
            "cleaning_step_4_instruction": "Decidí si seguís o terminás ahí.",

            "admin_summary": "Esto es administrativo. Abrilo y hacé la primera acción.",
            "admin_first_step": "Abrí la fuente de la tarea ahora.",
            "admin_step_1_title": "Abrilo",
            "admin_step_1_instruction": "Abrí el mail, formulario, sitio o documento.",
            "admin_step_2_title": "Encontrá la primera acción",
            "admin_step_2_instruction": "Identificá la primera cosa concreta que hay que hacer.",
            "admin_step_3_title": "Hacela",
            "admin_step_3_instruction": "Completá esa acción concreta.",
            "admin_step_4_title": "Dejá el siguiente paso",
            "admin_step_4_instruction": "Escribí una nota corta sobre lo que sigue.",

            "work_summary": "Esto es trabajo. Definí el resultado y empezá a producir.",
            "work_first_step": "Definí el entregable exacto.",
            "work_step_1_title": "Definí el entregable",
            "work_step_1_instruction": "Nombrá el resultado: mensaje, archivo, informe o sección.",
            "work_step_2_title": "Abrí herramientas",
            "work_step_2_instruction": "Abrí solo lo relacionado con ese resultado.",
            "work_step_3_title": "Hacé la primera parte",
            "work_step_3_instruction": "Trabajá en la primera parte sin multitasking.",
            "work_step_4_title": "Dejá un checkpoint",
            "work_step_4_instruction": "Escribí qué quedó hecho y qué sigue.",

            "general_summary": "La tarea está demasiado grande en tu cabeza. Recortala y arrancá.",
            "general_first_step": "Elegí una sola parte.",
            "general_step_1_title": "Elegí la parte",
            "general_step_1_instruction": "Elegí la parte más chica y útil que puedas empezar ahora.",
            "general_step_2_title": "Abrí lo necesario",
            "general_step_2_instruction": "Abrí materiales o herramientas.",
            "general_step_3_title": "Hacé un bloque",
            "general_step_3_instruction": "Trabajá en un bloque corto de foco.",
            "general_step_4_title": "Definí el siguiente paso",
            "general_step_4_instruction": "Escribí con claridad qué sigue.",
        },

        "study": {
            "summary_prefix": "Primero usá estructura y claridad.",
            "focus_tip": "Terminá un paso de estudio antes de pasar al siguiente.",
            "small_minutes": 3,
            "medium_minutes": 7,
            "focus_minutes": 20,
            "closing_minutes": 7,

            "study_summary": "Esto es estudio, así que la prioridad es secuencia, claridad y retención.",
            "study_first_step": "Abrí tus materiales y definí exactamente qué tema vas a cubrir primero.",
            "study_step_1_title": "Definir el objetivo de estudio",
            "study_step_1_instruction": "Elegí un capítulo, concepto o grupo de preguntas y nombralo con claridad.",
            "study_step_2_title": "Reunir materiales",
            "study_step_2_instruction": "Abrí apuntes, libro, diapositivas y una hoja para resumen o recuerdo activo.",
            "study_step_3_title": "Hacer un bloque de estudio enfocado",
            "study_step_3_instruction": "Estudiá ese tema en un bloque sin interrupciones buscando entender las ideas principales.",
            "study_step_4_title": "Resumir y marcar huecos",
            "study_step_4_instruction": "Escribí un resumen breve y anotá qué falta repasar.",

            "cleaning_summary": "No es estudio, pero igual vamos a mantener estructura y secuencia clara.",
            "cleaning_first_step": "Definí el área que vas a completar primero.",
            "cleaning_step_1_title": "Definir el área",
            "cleaning_step_1_instruction": "Elegí una sección para terminar por completo antes de pasar a otra.",
            "cleaning_step_2_title": "Clasificar por tipo",
            "cleaning_step_2_instruction": "Agrupá lo visible en basura, guardar y reubicar.",
            "cleaning_step_3_title": "Completar el orden",
            "cleaning_step_3_instruction": "Dejá esa zona terminada devolviendo cada cosa a su lugar.",
            "cleaning_step_4_title": "Revisar el resultado",
            "cleaning_step_4_instruction": "Chequeá qué mejoró y qué área seguiría después.",

            "admin_summary": "Esta tarea administrativa va a funcionar mejor con secuencia y estructura visible.",
            "admin_first_step": "Abrí la fuente relevante e identificá el resultado requerido.",
            "admin_step_1_title": "Definir el resultado",
            "admin_step_1_instruction": "Nombrá qué tiene que quedar hecho: respuesta enviada, formulario completo o documento revisado.",
            "admin_step_2_title": "Reunir información",
            "admin_step_2_instruction": "Abrí archivos, mails, sitios o referencias relacionadas.",
            "admin_step_3_title": "Completar la acción principal",
            "admin_step_3_instruction": "Terminá primero la acción administrativa más importante.",
            "admin_step_4_title": "Registrar pendientes",
            "admin_step_4_instruction": "Anotá lo que todavía necesita seguimiento.",

            "work_summary": "Esta tarea de trabajo va a ser más fácil con una secuencia clara y un resultado definido.",
            "work_first_step": "Identificá el entregable y definí el primer segmento.",
            "work_step_1_title": "Identificar el entregable",
            "work_step_1_instruction": "Definí exactamente qué necesitás producir.",
            "work_step_2_title": "Reunir referencias y herramientas",
            "work_step_2_instruction": "Abrí archivos, apps o notas vinculadas a ese entregable.",
            "work_step_3_title": "Completar un bloque de foco",
            "work_step_3_instruction": "Trabajá en la primera parte significativa del entregable.",
            "work_step_4_title": "Revisar y anotar lo siguiente",
            "work_step_4_instruction": "Escribí qué está completo y qué falta.",

            "general_summary": "Esta tarea necesita estructura, así que primero vamos a definir una secuencia.",
            "general_first_step": "Definí la primera parte concreta de la tarea.",
            "general_step_1_title": "Definir la primera parte",
            "general_step_1_instruction": "Elegí la primera parte que haría la tarea más clara.",
            "general_step_2_title": "Preparar materiales",
            "general_step_2_instruction": "Reuní o abrí todo lo necesario para esa parte.",
            "general_step_3_title": "Completar un bloque estructurado",
            "general_step_3_instruction": "Trabajá en un solo bloque de foco con un objetivo definido.",
            "general_step_4_title": "Revisar el avance",
            "general_step_4_instruction": "Anotá qué quedó hecho y qué debería seguir.",
        },

        "low_energy": {
            "summary_prefix": "Usá la versión más pequeña posible de la tarea.",
            "focus_tip": "Mantené el paso chico y fácil de iniciar.",
            "small_minutes": 2,
            "medium_minutes": 3,
            "focus_minutes": 8,
            "closing_minutes": 2,

            "study_summary": "Parece una tarea de estudio, así que la idea es volverla muy liviana.",
            "study_first_step": "Abrí tus apuntes y mirá un solo tema.",
            "study_step_1_title": "Elegí un tema mínimo",
            "study_step_1_instruction": "Elegí el tema, pregunta o sección más chica que puedas sostener ahora.",
            "study_step_2_title": "Abrí materiales suavemente",
            "study_step_2_instruction": "Abrí solo el apunte o archivo que necesitás para ese tema mínimo.",
            "study_step_3_title": "Hacé un bloque muy corto",
            "study_step_3_instruction": "Estudiá durante un bloque muy corto. Frenar antes también está bien.",
            "study_step_4_title": "Dejá una nota",
            "study_step_4_instruction": "Escribí una sola frase sobre qué retomar después.",

            "cleaning_summary": "Parece una tarea de orden o limpieza, así que la idea es hacerla muy chica.",
            "cleaning_first_step": "Elegí una zona mínima.",
            "cleaning_step_1_title": "Elegí una zona mínima",
            "cleaning_step_1_instruction": "Elegí un estante, una silla o una superficie chica.",
            "cleaning_step_2_title": "Sacá algunos objetos visibles",
            "cleaning_step_2_instruction": "Retirá solo lo más evidente.",
            "cleaning_step_3_title": "Ordená un momento corto",
            "cleaning_step_3_instruction": "Poné unas pocas cosas en su lugar.",
            "cleaning_step_4_title": "Frená sin culpa",
            "cleaning_step_4_instruction": "Pausá acá. Un pequeño orden también cuenta.",

            "admin_summary": "Parece una tarea administrativa, así que la vamos a reducir a una sola acción fácil.",
            "admin_first_step": "Abrí solo la fuente de la tarea.",
            "admin_step_1_title": "Abrilo",
            "admin_step_1_instruction": "Abrí el mail, formulario, sitio o archivo.",
            "admin_step_2_title": "Leé la primera parte",
            "admin_step_2_instruction": "Mir á solo la primera sección visible.",
            "admin_step_3_title": "Hacé una acción mínima",
            "admin_step_3_instruction": "Respondé una línea, completá un campo o revisá un documento.",
            "admin_step_4_title": "Dejalo listo",
            "admin_step_4_instruction": "Dejá una nota o la pestaña abierta para después.",

            "work_summary": "Parece una tarea de trabajo, así que la idea es bajar la presión y arrancar liviano.",
            "work_first_step": "Nombrá el resultado más pequeño posible.",
            "work_step_1_title": "Nombrar el resultado mínimo",
            "work_step_1_instruction": "Elegí la pieza útil más chica que puedas producir.",
            "work_step_2_title": "Abrí solo lo importante",
            "work_step_2_instruction": "Abrí solo la app o archivo que necesitás ahora.",
            "work_step_3_title": "Hacé un bloque mínimo",
            "work_step_3_instruction": "Trabajá en esa pieza chica durante un bloque corto.",
            "work_step_4_title": "Pausá y guardá avance",
            "work_step_4_instruction": "Frená y dejá todo listo para retomar.",

            "general_summary": "La tarea se siente pesada, así que la vamos a volver lo más chica y liviana posible.",
            "general_first_step": "Elegí la parte más fácil que puedas empezar ahora.",
            "general_step_1_title": "Elegir la parte más fácil",
            "general_step_1_instruction": "Elegí el punto de entrada más liviano posible.",
            "general_step_2_title": "Abrir lo necesario",
            "general_step_2_instruction": "Abrí solo lo mínimo indispensable.",
            "general_step_3_title": "Hacer un bloque mínimo",
            "general_step_3_instruction": "Trabajá durante un bloque muy corto nada más.",
            "general_step_4_title": "Pausar con amabilidad",
            "general_step_4_instruction": "Frená y contalo como avance.",
        },
    }

    return mapping.get(mode, mapping["gentle"])