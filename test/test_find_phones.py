import unittest
from src.main import find_phones


class TestFindPhones(unittest.TestCase):
    def test_find_phones(self):
        text = "+1 812 9874561"
        result = find_phones(text)
        expected = {18129874561}
        self.assertEqual(expected, result)

        text = "+2 (812) 123-45-67"
        result = find_phones(text)
        expected = {28121234567}
        self.assertEqual(expected, result)

        text = "+3 812 123-4567"
        result = find_phones(text)
        expected = {38121234567}
        self.assertEqual(expected, result)

        text = "+47581234567"
        result = find_phones(text)
        expected = {47581234567}
        self.assertEqual(expected, result)

        text = "+5812 1234567"
        result = find_phones(text)
        expected = {58121234567}
        self.assertEqual(expected, result)

        text = "6-812-123-45-67"
        result = find_phones(text)
        expected = {68121234567}
        self.assertEqual(expected, result)

        text = "(712) 123-4567"
        result = find_phones(text)
        expected = {77121234567}
        self.assertEqual(expected, result)

        text = "812 1234567"
        result = find_phones(text)
        expected = {78121234567}
        self.assertEqual(expected, result)

        text = "915-1234567"
        result = find_phones(text)
        expected = {79151234567}
        self.assertEqual(expected, result)

        text = "987-6543"
        result = find_phones(text)
        expected = {78129876543}
        self.assertEqual(expected, result)

        text = "876-54-32"
        result = find_phones(text)
        expected = {78128765432}
        self.assertEqual(expected, result)

        text = "7654321"
        result = find_phones(text)
        expected = {78127654321}
        self.assertEqual(expected, result)

    def test_find_phones_not_found(self):
        expected = set()

        text = "+1 - - -323 -1111111"
        result = find_phones(text)
        self.assertEqual(expected, result)

        text = "+1 323 -22222228"
        result = find_phones(text)
        self.assertEqual(expected, result)

        text = "323 - -3333333"
        result = find_phones(text)
        self.assertEqual(expected, result)

        text = "323 444-44-445"
        result = find_phones(text)
        self.assertEqual(expected, result)

        text = "5555555-666-66-66"
        result = find_phones(text)
        self.assertEqual(expected, result)

        text = "999999999999999888888888888888877777777777777"
        result = find_phones(text)
        self.assertEqual(expected, result)
