import unittest
from app.dame_genderguesser import DameGenderGuesser

class TddInPythonExample(unittest.TestCase):

    def test_genderguesser_list_method_returns_correct_result(self):
        dgg = DameGenderGuesser()
        self.assertEqual(dgg.guess("Sara", binary=False), "female")
        self.assertEqual(dgg.guess("Sara", binary=True), 0)
        self.assertEqual(dgg.guess("Laura", binary=False), "female")
        self.assertEqual(dgg.guess("Laura", binary=True), 0)

    def test_dame_genderguesser_accuracy_method_returns_correct_result(self):
        dgg = DameGenderGuesser()
        self.assertTrue(dgg.accuracy(path="files/partial.csv") >= 0.5)
