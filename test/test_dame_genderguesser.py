import unittest
from app.dame_genderguesser import DameGenderGuesser

class TddInPythonExample(unittest.TestCase):

    def test_genderguesser_list_method_returns_correct_result(self):
        dgg = DameGenderGuesser()
        g1 = dgg.guess("Sara", binary=False)
        self.assertEqual(g1, "female")
        g2 = dgg.guess("Sara", binary=True)
        self.assertEqual(g2, 0)
        g3 = dgg.guess("Laura", binary=False)
        self.assertEqual(g3, "female")
        g4 = dgg.guess("Laura", binary=True)
        self.assertEqual(g4, 0)

    def test_dame_genderguesser_accuracy_method_returns_correct_result(self):
        dgg = DameGenderGuesser()
        self.assertTrue(dgg.accuracy(path="files/partial.csv") >= 0.5)
