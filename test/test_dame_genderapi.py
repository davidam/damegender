import unittest
from app.dame_genderapi import DameGenderApi

class TddInPythonExample(unittest.TestCase):

    def test_genderapi_guess_method_returns_correct_result(self):
        dga = DameGenderApi()
        g = dga.guess("Sara")
        self.assertEqual(g, "female")
