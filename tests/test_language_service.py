import unittest

from services.language_service import LanguageService


class TestLanguageService(unittest.TestCase):
    def setUp(self):
        self.language_service = LanguageService()

    def test_get_language_returns_supported_language(self):
        self.assertEqual(self.language_service.get_language("es"), "es")
        self.assertEqual(self.language_service.get_language("en"), "en")

    def test_get_language_falls_back_to_default(self):
        self.assertEqual(self.language_service.get_language("fr"), "en")

    def test_load_translations_english(self):
        translations = self.language_service.load_translations("en")
        self.assertIn("app_title", translations)
        self.assertEqual(translations["app_title"], "Cognitive Helper")

    def test_load_translations_spanish(self):
        translations = self.language_service.load_translations("es")
        self.assertIn("submit_button", translations)


if __name__ == "__main__":
    unittest.main()