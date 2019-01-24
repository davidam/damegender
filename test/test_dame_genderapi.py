# import unittest
# from app.dame_genderapi import DameGenderApi

# class TddInPythonExample(unittest.TestCase):

    # Deactivated tests only with api key
    # def test_dame_genderapi_guess_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     g = dga.guess("Sara", binary=False)
    #     self.assertEqual(g, "female")
    #     g = dga.guess("Sara", binary=True)
    #     self.assertEqual(g, 0)

    # def test_dame_genderapi_guess_list_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     self.assertEqual(['male', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'male'], dga.guess_list(path="files/partial.csv", binary=False))
    #     self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], dga.guess_list(path="files/partial.csv",binary=True))

    # def test_dame_genderapi_confusion_matrix_dame_method_returns_correct_result(self):
    #     g = DameGenderApi()
    #     cm = g.confusion_matrix_dame(path="files/min.csv")
    #     am = [[5, 0, 0], [0, 2, 0]]
    #     self.assertEqual(cm,am)   


    
