#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with DameGender; see the file GPL.txt.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,


import unittest
import os
import collections
collections.Callable = collections.abc.Callable

from app.dame_utils import DameUtils
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

    def test_single_hyphen_p(self):
        u = DameUtils()
        self.assertTrue(u.single_hyphen_p("Magia-Antoñeta"))

    def test_replace_single_hyphen(self):
        u = DameUtils()
        self.assertEqual(u.replace_single_hyphen("Magia-Antogneta"),
                         "Magia Antogneta")

    def test_drop_white_space(self):
        u = DameUtils()
        self.assertEqual("In",
                         u.drop_white_space("In "))
        self.assertEqual("Ines",
                         u.drop_accents(u.drop_white_space("Inés ")))
        self.assertEqual("JuanCarlosI",
                         u.drop_accents(u.drop_white_space("Juan Carlos I ")))

    # def test_drop_internal_symbols(self):
    #     u = DameUtils()
    #     self.assertEqual("In",
    #                      u.drop_internal_symbols("I+n", ['+', ',']))
    #     self.assertEqual("Inés",
    #                      u.drop_internal_symbols("Inés", ['+']))
    #     self.assertEqual("JuanCarlosI",
    #                      u.drop_internal_symbols("Juan Carlos I ", [' ']))

        
    def test_drop_white_space_around(self):
        u = DameUtils()
        self.assertEqual("", u.drop_white_space_around(" "))
        self.assertEqual("", u.drop_white_space_around(""))
        self.assertEqual(" 阿", u.drop_white_space_around("阿"))
        self.assertEqual(" 阿 ", u.drop_white_space_around("阿"))
        self.assertEqual("阿 ", u.drop_white_space_around("阿"))
        self.assertEqual("In", u.drop_white_space_around(" In"))
        self.assertEqual("Juan Carlos I",
                         u.drop_white_space_around(" Juan Carlos I"))
        self.assertEqual("Juan-Carlos ",
                         u.drop_white_space_around("Juan-Carlos"))
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
        self.assertEqual("NILDA", u.drop_white_space_around(" NILDA"))
        self.assertEqual("NILDA", u.drop_white_space_around("NILDA "))
        self.assertEqual("David Arroyo Menéndez ",
                         u.drop_white_space_around("David Arroyo Menéndez "))

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

    # def test_drop_symbols(self):
    #     u = DameUtils()
    #     self.assertEqual('Hola Mexico', u.drop_symbols('Hola "Mexico', ['"']))
    #     self.assertEqual("Hola Mexico", u.drop_symbols("Hola@ #Mexico", ['@', '#']))

    def test_drop_external_quotes(self):
        u = DameUtils()
        self.assertEqual('Hola "Mexico', u.drop_external_quotes('"Hola "Mexico'))
        self.assertEqual("Hola' 'Mexico", u.drop_external_quotes("'Hola' 'Mexico'"))

    def test_initialize_dictionary_drop_external_symbols(self):
        du = DameUtils()
        self.assertEqual('', du.drop_external_symbols('"', ['"']))
        self.assertEqual('Hola "Mexico', du.drop_external_symbols('"Hola "Mexico', ['"']))
        self.assertEqual('Hola', du.drop_external_symbols('-Hola+', ['-', '+']))
        self.assertEqual('Hola Mexico', du.drop_external_symbols('-Hola Mexico+', ['-', '+']))

    def test_initialize_dictionary_drop_all_external_symbols(self):
        du = DameUtils()
        self.assertEqual('', du.drop_all_external_symbols('', ['"']))
        self.assertEqual('Hola "Mexico', du.drop_all_external_symbols('"""""Hola "Mexico', ['"']))

    def test_delete_duplicated_identities(self):
        g = Gender()
        du = DameUtils()
        id1 = "David Arroyo Menéndez <davidam@gnu.org>"
        id2 = "David Arroyo Menéndez <davidam@gmail.com>"
        l1 = du.delete_duplicated_identities([id1, id2])
        self.assertEqual(l1, ['David Arroyo Menéndez <davidam@gnu.org>'])
        self.assertEqual(du.delete_duplicated_identities([id1, id1]), [id1])

    def test_delete_duplicated(self):
        du = DameUtils()
        l1 = sorted(du.delete_duplicated([1, 5, 2, 2, 1, 3, 5, 5, 5, 5]))
        self.assertEqual(l1, [1, 2, 3, 5])

    def test_clean_list(self):
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
        l1 = ['', '', 'de', '', '', 'ar', '', '',  '', 'ca', 'cl', '', '']
        self.assertEqual(du.clean_list(l1), ['de', 'ar', 'ca', 'cl'])

    def test_files_one_level(self):
        du = DameUtils()
        cwd = os.getcwd()
        self.assertTrue(len(du.files_one_level(cwd + '/files/')) > 10)

    def test_files_one_level_drop_pwd(self):
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

    def test_list2lower(self):
        du = DameUtils()
        x = ["Aaa", "bBb", "ccC"]
        self.assertEqual(du.list2lower(x), ["aaa", "bbb", "ccc"])

    def test_csvcolumn2list(self):
        du = DameUtils()
        l1 = du.csvcolumn2list('files/names/partial.csv', position=0, header=True)
        self.assertEqual(len(l1), 21)
        self.assertEqual(['"pierre"', '"raul"', '"adriano"', '"ralf"',
                          '"teppei"', '"guillermo"', '"catherine"',
                          '"sabina"', '"ralf"', '"karl"', '"sushil"',
                          '"clemens"', '"gregory"', '"lester"', '"claude"',
                          '"martin"', '"vlad"', '"pasquale"', '"lourdes"',
                          '"bruno"', '"thomas"'], l1)
        l2 = du.csvcolumn2list('files/names/min.commas.csv', position=0,
                               header=True, delimiter=";")
        self.assertEqual(len(l2), 6)
        self.assertEqual(['"pierre"', '"raul"', '"adriano"',
                          '"ralf"', '"guillermo"', '"sabina"'], l2)
        l3 = du.csvcolumn2list('files/names/min.commas.csv', position=5,
                               header=True, delimiter=";")
        self.assertEqual(len(l3), 6)
        self.assertTrue('"zbmath"' in l3)

    def test_csv2list(self):
        du = DameUtils()
        l1 = du.csv2list('files/names/min.csv')
        self.assertEqual(['"pierre"', '"paul"', '"grivel"',
                          '"pierre paul grivel"', '"m"', '"zbmath"'], l1[0])
        self.assertEqual(['"raul"', '""', '"serapioni"',
                          '"raul serapioni"', '"m"', '"zbmath"'], l1[1])
        l2 = du.csv2list('files/names/min.commas.csv', delimiter=";")
        self.assertEqual(['"pierre"', '"paul"', '"grivel"',
                          '"pierre paul grivel"', '"m"', '"zbmath"'], l2[0])
        self.assertEqual(['"raul"', '""', '"serapioni"',
                          '"raul serapioni"', '"m"', '"zbmath"'], l2[1])

    def test_num_columns_in_csv(self):
        du = DameUtils()
        n = du.num_columns_in_csv('files/names/partial.csv')
        self.assertEqual(n, 6)

    def test_round_and_not_zero_division(self):
        du = DameUtils()
        self.assertEqual(du.round_and_not_zero_division(4, 2), 2)
        self.assertEqual(du.round_and_not_zero_division(3, 2), 1.5)
        self.assertEqual(du.round_and_not_zero_division(8, 7), 1.14)

    def test_identity2name_email(self):
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

    def test_same_identity(self):
        du = DameUtils()
        s = du.same_identity("David Arroyo Menendez <davidam@gnu.org>",
                             "David Arroyo Menendez <davidam@gnu.org>")
        self.assertTrue(s)
        s2 = du.same_identity("David Arroyo Menendez <davidam@gnu.org>",
                              "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s2)
        s3 = du.same_identity("David Arroyo Menendez <davidam@gmail.com>",
                              "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s2)
        s4 = du.same_identity("David <davidam@gnu.org>",
                              "David Arroyo Menéndez <davidam@gnu.org>")
        self.assertTrue(s4)

    def test_initial_letters(self):
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
        s = du.initial_letters("A.Jose")
        self.assertTrue(s)
        s = du.initial_letters("A. Jose")
        self.assertTrue(s)
        s = du.initial_letters("Antonio Jose")
        self.assertFalse(s)

    def test_diccnames2csvfile(self):
        du = DameUtils()
        dicc = {}
        dicc['Ana'] = 3
        dicc['Cristina'] = 4
        dicc['Maria'] = 7
        du.diccnames2csvfile(dicc, 'files/tests/dicc.csv')
        l0 = du.csvcolumn2list('files/tests/dicc.csv', position=0, header=False)
        l1 = du.csvcolumn2list('files/tests/dicc.csv', position=1, header=False)
        self.assertEqual(l0, ['Ana', 'Cristina', 'Maria'])
        self.assertEqual(l1, ['3', '4', '7'])

    def test_number_or_zero(self):
        du = DameUtils()
        noz = du.number_or_zero("-")
        self.assertEqual(noz, 0)
        noz = du.number_or_zero(27)
        self.assertTrue(noz > 0)
        self.assertEqual(noz, 27)

    def test_int2gender(self):
        du = DameUtils()
        self.assertEqual(du.int2gender(1), "male")
        self.assertEqual(du.int2gender(0), "female")
        self.assertEqual(du.int2gender(2), "unknown")

    def test_dicc_dataset(self):
        du = DameUtils()
        dicc = du.dicc_dataset("male")
        self.assertEqual(dicc["at"], "files/names/names_at/atmales.csv")
        dicc = du.dicc_dataset("female")
        self.assertEqual(dicc["at"], "files/names/names_at/atfemales.csv")

    def test_delete_duplicated_identities(self):
        du = DameUtils()
        l1 = ['David Arroyo Menéndez <davidam@es.gnu.org>',
              'David Arroyo Menendez <davidam@gmail.com>',
              'David Arroyo Menéndez <d.arroyome@alumnos.urjc.es>',
              'David Arroyo <davidam@gmail.com>']
        l2 = du.delete_duplicated_identities(l1)
        self.assertTrue('David Arroyo Menéndez <davidam@es.gnu.org>' in l2)
        id1 = 'David Arroyo Menéndez <davidam@es.gnu.org>'
        id2 = 'David Arroyo <davidam@gmail.com>'
        self.assertEqual(l2, [id1, id2])

    def test_init_dicc_names_from_file(self):
        du = DameUtils()
        file1 = "files/names/names_inter/dkfemales10.csv"
        dicc = du.init_dicc_names_from_file(file1, 0)
        l = sorted(dicc.keys())
        self.assertEqual(l, ["Clara", "Dilara", "Elena",
                             "Julia", "Luisa", "Martin",
                             "Roberta", "Rosa", "Sara",
                             "Tabita", "Una"])
        file2 = "files/tests/vsa10.csv"
        dicc2 = du.init_dicc_names_from_file(file2, 5)
        l2 = sorted(dicc2.keys())
        self.assertEqual(l2[0:5], ['Abbie', 'Abby', 'Abigail', 'Ada', 'Ailbhe'])
        # file2 = "files/names/names_uy/orig/nombre_nacim_x_anio_sexo.csv"
        # dicc2 = du.initialize_dictionary_names_from_file(file2, 2)
        # l2 = sorted(dicc2.keys())
        # self.assertEqual(l2[0:3], ["Clara", "Dilara", "Elena", "Julia"])

    # def test_reduce_csv_columns_to_name_and_freq(self):
    #### THIS METHOD HAS BEEN REPLACED BY dump_name_and_quantity_in_dicc and simple_dicc_to_file
    #     du = DameUtils()
    #     file1 = "files/tests/testorig1.csv"
    #     file2 = "files/tests/testres1.csv"
    #     file3 = "files/tmp/testout1.csv"      
    #     res = du.reduce_csv_columns_to_name_and_freq(file1, respath=file3, name=1, freq=2)
    #     file2f = open(file2, 'r')
    #     file3f = open(file3, 'r')
    #     file2_lines = file2f.readlines()
    #     file3_lines = file3f.readlines()
    #     file2f.close()
    #     file3f.close()
    #     self.assertEqual(file2_lines, file3_lines)

    def test_init_dicc_names_and_years(self):
        du = DameUtils()
        file1 = "files/tests/vsa10.csv"
        dicc = du.init_dicc_names_and_years(file1, 5, 1998, 2019)
        l = sorted(dicc.keys())
        self.assertEqual(l[0:5], ['Abbie', 'Abby', 'Abigail', 'Ada', 'Ailbhe'])
        self.assertEqual(dicc["Ada"][2019]["females"], 0)

    def test_find_max_and_min_in_column(self):
        du = DameUtils()
        file1 = "files/tests/testatde.csv"
        dicc1 = du.find_max_and_min_in_column(file1, 1)
        self.assertEqual(100, dicc1["min"])
        self.assertEqual(80445, dicc1["max"])

    def test_dump_name_and_quantity_in_dicc(self):
        du = DameUtils()
        file1 = "files/tests/bemin.csv"
        posname = 3
        posquant = 4
        dicc0 = {}
        dicc0 = du.dump_name_and_quantity_in_dicc(file1, posname, posquant, dicc=dicc0, delimiter=",")
        self.assertEqual(dicc0["MARIA"], 370)
        self.assertEqual(dicc0["INGRID"], 62)        
        filewien = "files/tests/testwien.csv"
        diccmales = {} 
        diccmales = du.dump_name_and_quantity_in_dicc(filewien, 7, 8, dicc=diccmales, delimiter=";",
                                                      filter_pos=5, filter_char='1')
        self.assertEqual(diccmales["DAVID"], 169)

    def test_is_json(self):
        du = DameUtils()
        file1 = "files/pca.json"
        self.assertTrue(du.is_json(file1))
        file2 = "files/gnu-maintainers.csv"
        self.assertFalse(du.is_json(file2))

    def test_is_csv(self):
        du = DameUtils()
        file1 = "files/gnu-maintainers.csv"
        self.assertTrue(du.is_csv(file1))
        file2 = "files/pca.json"
        self.assertFalse(du.is_csv(file2))
        file3 = "files/names/min.commas.csv"
        self.assertTrue(du.is_csv(file3))
        self.assertTrue(du.is_csv(file3, delimiter=";"))        
        file4 = "files/names/min.csv"
        self.assertTrue(du.is_csv(file4))
        
# def test_file_year2dicc_females(self):
#     du = DameUtils()
#     file1 = "files/names/names_de/orig/Vornamen_2020_Koeln.csv"
#     file2 = "files/names/names_de/orig/Vornamen_Koeln_2014.csv"
#     dicc = du.file_year2dicc_females(file1, name_position=1, quantity_position=0, gender_position=2, filter_females="w")
#     print(dicc["Marie"])
#     self.assertEqual(dicc["Marie"], 207)

# def test_fill_dictionary_names_and_years_from_file(self):
#     du = DameUtils()
#     file1 = "files/names/names_ie/orig/vsa10.csv"
#     dicc = du.fill_dictionary_names_and_years_from_file(file1, 5, 2)
#     l = sorted(dicc.keys())
#     self.assertEqual(l[0:5], ['Abbie', 'Abby', 'Abigail', 'Ada', 'Ailbhe'])
#     print(dicc["Ada"])
#     self.assertTrue(dicc["Ada"]["2019"]["females"] > 0)
