import unittest

from services.response_parser import parse_ollama_json_response, validate_plan_schema


class TestResponseParser(unittest.TestCase):
    def test_parse_valid_json_response(self):
        raw = """
        {
          "summary": "Test summary",
          "first_step": "Start here",
          "steps": [
            {
              "title": "Step one",
              "instruction": "Do this first",
              "minutes": 5
            }
          ],
          "focus_tip": "Stay with one step",
          "break_after_minutes": 15
        }
        """

        parsed = parse_ollama_json_response(raw)
        self.assertEqual(parsed["summary"], "Test summary")

    def test_parse_json_wrapped_in_extra_text(self):
        raw = """
        here is your response:
        {
          "summary": "Wrapped summary",
          "first_step": "Open the notebook",
          "steps": [
            {
              "title": "Prepare",
              "instruction": "Get materials ready",
              "minutes": 4
            }
          ],
          "focus_tip": "One thing at a time",
          "break_after_minutes": 15
        }
        thank you
        """

        parsed = parse_ollama_json_response(raw)
        self.assertEqual(parsed["first_step"], "Open the notebook")

    def test_validate_plan_schema(self):
        data = {
            "summary": "Summary",
            "first_step": "Do this",
            "steps": [
                {
                    "title": "Step 1",
                    "instruction": "Instruction 1",
                    "minutes": 5
                }
            ],
            "focus_tip": "Tip",
            "break_after_minutes": 15
        }

        validated = validate_plan_schema(data)
        self.assertEqual(validated["steps"][0]["minutes"], 5)


if __name__ == "__main__":
    unittest.main()