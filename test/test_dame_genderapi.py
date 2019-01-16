import unittest
from app.dame_genderapi import DameGenderApi

class TddInPythonExample(unittest.TestCase):

    def test_dame_genderapi_guess_method_returns_correct_result(self):
        dga = DameGenderApi()
        g = dga.guess("Sara", binary=False)
        self.assertEqual(g, "female")
        g = dga.guess("Sara", binary=True)
        self.assertEqual(g, 0)

    def test_dame_genderapi_guess_list_method_returns_correct_result(self):
        dga = DameGenderApi()
        self.assertEqual(['male', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'male'], dga.guess_list(path="files/partial.csv", binary=False))
        self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], dga.guess_list(path="files/partial.csv",binary=True))
