import unittest
from src.main import find_phones


class TestFindPhones(unittest.TestCase):
    def test_find_phones(self):
        text = "+1 812 9874561"
        result = find_phones(text)
        expected = {"+1 (812) 987-4561"}
        self.assertEqual(expected, result)

        text = "+1 812 9874561"
        result = find_phones(text)
        expected = {"+1 (812) 987-4561"}
        self.assertEqual(expected, result)
