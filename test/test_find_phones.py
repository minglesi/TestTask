import unittest
from src.main import find_phones


class TestFindPhones(unittest.TestCase):
    def test_find_phones(self):
        text = "+1 812 9874561"
        result = find_phones(text)
        expected = {"+1 (812) 987-4561"}
        self.assertEqual(expected, result)

        text = "+2 (812) 123-45-67"
        result = find_phones(text)
        expected = {"+2 (812) 123-4567"}
        self.assertEqual(expected, result)

        text = "+3 812 123-4567"
        result = find_phones(text)
        expected = {"+3 (812) 123-4567"}
        self.assertEqual(expected, result)

        text = "+47581234567"
        result = find_phones(text)
        expected = {"+4 (758) 123-4567"}
        self.assertEqual(expected, result)

        text = "+5812 1234567"
        result = find_phones(text)
        expected = {"+5 (812) 123-4567"}
        self.assertEqual(expected, result)

        text = "+6-812-123-45-67"
        result = find_phones(text)
        expected = {"+6 (812) 123-4567"}
        self.assertEqual(expected, result)

        text = "(712) 123-4567"
        result = find_phones(text)
        expected = {"+7 (712) 123-4567"}
        self.assertEqual(expected, result)

        text = "812 1234567"
        result = find_phones(text)
        expected = {"+7 (812) 123-4567"}
        self.assertEqual(expected, result)

        text = "915-1234567"
        result = find_phones(text)
        expected = {"+7 (915) 123-4567"}
        self.assertEqual(expected, result)

        text = "987-6543"
        result = find_phones(text)
        expected = {"+7 (812) 987-6543"}
        self.assertEqual(expected, result)

        text = "876-54-32"
        result = find_phones(text)
        expected = {"+7 (812) 876-5432"}
        self.assertEqual(expected, result)

        text = "7654321"
        result = find_phones(text)
        expected = {"+7 (812) 765-4321"}
        self.assertEqual(expected, result)
