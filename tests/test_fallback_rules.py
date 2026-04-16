import unittest

from services.fallback_rules import build_fallback_plan


class TestFallbackRules(unittest.TestCase):
    def test_build_fallback_plan_english(self):
        plan = build_fallback_plan(task="I need to study", language="en")

        self.assertIn("summary", plan)
        self.assertEqual(plan["steps"][0]["title"], "Choose one small part")

    def test_build_fallback_plan_spanish(self):
        plan = build_fallback_plan(task="Tengo que estudiar", language="es")

        self.assertIn("summary", plan)
        self.assertEqual(plan["steps"][0]["title"], "Elegir una sola parte")

    def test_fallback_contains_steps(self):
        plan = build_fallback_plan(task="Something", language="en")

        self.assertTrue(len(plan["steps"]) > 0)


if __name__ == "__main__":
    unittest.main()