import unittest
from app.genderguesser import Genderguesser

class TddInPythonExample(unittest.TestCase):

    def test_genderguesser_list_method_returns_correct_result(self):
        gg = Genderguesser()
        self.assertEqual([('Pierre', 'male'), ('Raul', 'male'), ('Adriano', 'male'), ('Ralf', 'male'), ('Teppei', 'male'), ('Guillermo', 'male'), ('Catherine', 'female'), ('Sabina', 'female'), ('Ralf', 'male'), ('Karl', 'male'), ('Sushil', 'mostly_male'), ('Clemens', 'male'), ('Gregory', 'male'), ('Lester', 'male'), ('Claude', 'mostly_male'), ('Martin', 'male'), ('Vlad', 'male'), ('Pasquale', 'male'), ('Lourdes', 'female'), ('Bruno', 'male'), ('Thomas', 'male')], gg.list())
