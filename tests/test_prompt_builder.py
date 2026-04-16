import unittest

from services.prompt_builder import build_planner_prompt


class TestPromptBuilder(unittest.TestCase):
    def test_build_prompt_in_english(self):
        prompt = build_planner_prompt(
            task="I need to study for an exam.",
            language="en",
            mode="study"
        )

        self.assertIn("Return valid JSON only", prompt)
        self.assertIn("I need to study for an exam.", prompt)

    def test_build_prompt_in_spanish(self):
        prompt = build_planner_prompt(
            task="Tengo que estudiar para un examen.",
            language="es",
            mode="gentle"
        )

        self.assertIn("Responde solo con JSON válido", prompt)
        self.assertIn("Tengo que estudiar para un examen.", prompt)

    def test_low_energy_mode_changes_tone(self):
        prompt = build_planner_prompt(
            task="I need to clean my room.",
            language="en",
            mode="low_energy"
        )

        self.assertIn("low energy", prompt.lower())


if __name__ == "__main__":
    unittest.main()