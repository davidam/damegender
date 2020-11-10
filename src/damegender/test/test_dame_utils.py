#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.


import unittest
import os
from app.dame_utils import DameUtils
from app.dame_gender import Gender
from os.path import expanduser

class TddInPythonExample(unittest.TestCase):

    def test_string2array(self):
        du = DameUtils()
        array = "muchos    espacios en blanco"
        arr = du.string2array(array)
        self.assertEqual(["muchos", "espacios", "en", "blanco"], arr)

    def test_is_not_blank(self):
        du = DameUtils()
        self.assertEqual(du.is_not_blank("  "), False)
        self.assertEqual(du.is_not_blank("ok"), True)

    def test_various_words_p(self):
        du = DameUtils()
        self.assertEqual(du.various_words_p("david arroyo"), True)
        self.assertEqual(du.various_words_p("Abdul+Ahad"), True)
        self.assertEqual(du.various_words_p(" david arroyo "), True)

    def test_path2file(self):
        du = DameUtils()
        self.assertEqual(du.path2file("files/images/lalla.csv"),
                         "files_images_lalla.csv")

    def test_represents_int(self):
        du = DameUtils()
        self.assertEqual(du.represents_int("23"), True)
        self.assertEqual(du.represents_int("ok"), False)

    def test_split(self):
        u = DameUtils()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        sp = u.split(x, 5)
        self.assertEqual(sp, [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13]])
        y = list(range(1, 100))
        ysp = u.split(y, 10)
        self.assertEqual(ysp[0:2],
                         [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                          [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]])

    def test_drop_dots(self):
        u = DameUtils()
        self.assertEqual(1212, int(u.drop_dots(12.12)))

    def test_drop_accents(self):
        u = DameUtils()
        self.assertEqual("Ines", u.drop_accents("Inés"))

    def test_drop_white_space(self):
        u = DameUtils()
        self.assertEqual("In",
                         u.drop_white_space("In "))
        self.assertEqual("Ines",
                         u.drop_accents(u.drop_white_space("Inés ")))
        self.assertEqual("JuanCarlosI",
                         u.drop_accents(u.drop_white_space("Juan Carlos I ")))

    def test_drop_white_space_around(self):
        u = DameUtils()
        self.assertEqual("In",
                         u.drop_white_space_around(" In"))
        self.assertEqual("Juan Carlos I",
                         u.drop_white_space_around(" Juan Carlos I"))
        self.assertEqual("Juan Carlos I",
                         u.drop_white_space_around(" Juan Carlos I  "))
        self.assertEqual("Juan Carlos I",
                         u.drop_white_space_around(" Juan Carlos I "))
        self.assertEqual("Jose Maria",
                         u.drop_white_space_around(
                             u.drop_accents(" José María ")))
        self.assertEqual("Ines",
                         u.drop_white_space_around(
                             u.drop_accents("Inés ")))
        self.assertEqual("Ana", u.drop_white_space_around(" Ana"))
        self.assertEqual("David Arroyo Menéndez ", u.drop_white_space_around("David Arroyo Menéndez "))

        
    def test_drop_white_space_around(self):
        u = DameUtils()
        self.assertEqual(
            "Maria+Jose",
            u.white_space_inside_by(
                u.drop_accents(" María José "),
                "+"))

    def test_drop_quotes(self):
        u = DameUtils()
        self.assertEqual('Hola Mexico', u.drop_quotes('Hola "Mexico'))
        self.assertEqual("Hola Mexico", u.drop_quotes("Hola' 'Mexico"))

    def test_dame_utils_delete_duplicated_identities(self):
        g = Gender()
        du = DameUtils()
        self.assertEqual(du.delete_duplicated_identities(["David Arroyo Menéndez <davidam@gnu.org>", "David Arroyo Menéndez <davidam@gmail.com>"]), ['David Arroyo Menéndez <davidam@gnu.org>'])
        self.assertEqual(du.delete_duplicated_identities(["David Arroyo Menéndez <davidam@gnu.org>", "David Arroyo Menendez <davidam@gnu.org>"]), ['David Arroyo Menéndez <davidam@gnu.org>'])

    def test_dame_utils_delete_duplicated(self):
        g = Gender()
        du = DameUtils()
        self.assertEqual(sorted(du.delete_duplicated([1, 5, 2, 2, 1, 3, 5, 5, 5 , 5])), [1, 2, 3, 5])        
        
    def test_dame_utils_clean_list(self):
        du = DameUtils()
        self.assertEqual(
            du.clean_list(
                ['',
                 'H. Peter Anvin',
                 'hiranotaka@zng.info',
                 'Ram Yalamanchili',
                 'Ferenc Wagner']),
            ['H. Peter Anvin',
             'Ram Yalamanchili',
             'Ferenc Wagner'])
        l1 = ['', '', 'de', '', '', 'ar', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'ca', 'cl', '', '', '']
        self.assertEqual(du.clean_list(l1), ['de', 'ar', 'ca', 'cl'])

    def test_dame_utils_files_one_level(self):
        du = DameUtils()
        cwd = os.getcwd()
        self.assertTrue(len(du.files_one_level(cwd + '/files/')) > 10)

    def test_dame_utils_files_one_level_drop_pwd(self):
        du = DameUtils()
        cwd = os.getcwd()
        self.assertEqual(
            sorted(du.files_one_level_drop_pwd(cwd+"/files/datamodels/*sav")),
            ['files/datamodels/adaboost_model.sav',
             'files/datamodels/bernoulliNB_model.sav',
             'files/datamodels/forest_model.sav',
             'files/datamodels/gaussianNB_model.sav',
             'files/datamodels/mlp_model.sav',
             'files/datamodels/multinomialNB_model.sav',
             'files/datamodels/nltk_model.sav',
             'files/datamodels/sgd_model.sav',
             'files/datamodels/svc_model.sav',
             'files/datamodels/tree_model.sav'])

    def test_dame_utils_list2lower(self):
        du = DameUtils()
        x = ["Aaa", "bBb", "ccC"]
        self.assertEqual(du.list2lower(x), ["aaa", "bbb", "ccc"])

    def test_dame_utils_csvcolumn2list(self):
        du = DameUtils()
        l = du.csvcolumn2list('files/names/partial.csv', 0, header=True)
        self.assertEqual(len(l), 21)
        self.assertEqual(['"pierre"', '"raul"', '"adriano"', '"ralf"', '"teppei"', '"guillermo"', '"catherine"', '"sabina"', '"ralf"', '"karl"', '"sushil"', '"clemens"', '"gregory"', '"lester"', '"claude"', '"martin"', '"vlad"', '"pasquale"', '"lourdes"', '"bruno"', '"thomas"'], l)

    def test_dame_utils_csv2list(self):
        du = DameUtils()
        l = du.csv2list('files/names/min.csv')
        self.assertEqual(['"first_name"', '"middle_name"', '"last_name"', '"full_name"', '"gender"', '"origin"'], l[0])
        self.assertEqual(['"pierre"', '"paul"', '"grivel"', '"pierre paul grivel"', '"m"', '"zbmath"'], l[1])
        self.assertEqual(['"raul"', '""', '"serapioni"', '"raul serapioni"', '"m"', '"zbmath"'], l[2])

    def test_dame_utils_num_columns_in_csv(self):
        du = DameUtils()
        n = du.num_columns_in_csv('files/names/partial.csv')
        self.assertEqual(n, 6)

    def test_dame_utils_round_and_not_zero_division(self):
        du = DameUtils()
        self.assertEqual(du.round_and_not_zero_division(4, 2), 2)
        self.assertEqual(du.round_and_not_zero_division(3, 2), 1.5)
        self.assertEqual(du.round_and_not_zero_division(8, 7), 1.143)


    def test_dame_utils_identity2name_email(self):
        du = DameUtils()
        s = "David Arroyo Menéndez <davidam@gnu.org>"
        identity = du.identity2name_email(s)
        self.assertEqual(identity[0], "David Arroyo Menendez")
        self.assertEqual(identity[1], "davidam@gnu.org")

        s2 = "David Arroyo Menéndez <david.am@gnu.org>"
        identity2 = du.identity2name_email(s2)
        self.assertEqual(identity2[0], "David Arroyo Menendez")
        self.assertEqual(identity2[1], "david.am@gnu.org")
        
        s3 = "David Arroyo Menéndez <david@alumnos.urjc.es>"
        identity3 = du.identity2name_email(s3)
        self.assertEqual(identity3[0], "David Arroyo Menendez")
        self.assertEqual(identity3[1], "david@alumnos.urjc.es")

        s4 = "David Arroyo Menéndez <d.arroyome@alumnos.urjc.es>"
        identity4 = du.identity2name_email(s4)
        self.assertEqual(identity4[0], "David Arroyo Menendez")
        self.assertEqual(identity4[1], "d.arroyome@alumnos.urjc.es")

        s5 = "Jim Jagielski <jim@jaguNET.com>"
        identity5 = du.identity2name_email(s5)
        self.assertEqual(identity5[0], "Jim Jagielski")
        self.assertEqual(identity5[1], "jim@jaguNET.com")

        s6 = '"Jim Jagielski" <jim@jaguNET.com>'
        identity6 = du.identity2name_email(s6)
        self.assertEqual(identity6[0], 'Jim Jagielski')
        self.assertEqual(identity6[1], 'jim@jaguNET.com')
        
        
    def test_dame_utils_same_identity(self):
        du = DameUtils()
        s = du.same_identity("David Arroyo Menendez <davidam@gnu.org>", "David Arroyo Menendez <davidam@gnu.org>")
        self.assertTrue(s)
        s2 = du.same_identity("David Arroyo Menendez <davidam@gnu.org>", "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s2)
        s3 = du.same_identity("David Arroyo Menendez <davidam@gmail.com>", "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s2)
        s4 = du.same_identity("David <davidam@gnu.org>", "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s4)

    def test_dame_utils_initial_letters(self):
        du = DameUtils()
        s = du.initial_letters("D ")
        self.assertTrue(s)
        s = du.initial_letters("D. ")
        self.assertTrue(s)        
        s = du.initial_letters("David")
        self.assertFalse(s)
        s = du.initial_letters("J.L.")        
        self.assertTrue(s)
        s = du.initial_letters("JL")        
        self.assertTrue(s)

        
    # def test_dame_utils_delete_duplicated_identities(self):
    #     du = DameUtils()
    #     l = ['David Arroyo Menéndez <davidam@es.gnu.org>', 'David Arroyo Menendez <davidam@gmail.com>', 'David Arroyo Menéndez <d.arroyome@alumnos.urjc.es>', 'David Arroyo <davidam@gmail.com>']
    #     s = du.delete_duplicated_identities(l)
    #     self.assertEqual(s, 'David Arroyo Menéndez <davidam@es.gnu.org>')xs
