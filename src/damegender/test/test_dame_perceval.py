#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
from app.dame_perceval import DamePerceval

class TddInPythonExample(unittest.TestCase):

    def test_dame_perceval_numcommits_method_returns_correct_result(self):
        gg = DamePerceval()
        n = gg.numCommits("https://github.com/davidam/davidam.git",
                          "/tmp/clonedir")
        self.assertTrue(50 < n)

    def test_dame_perceval_removeMail_method_returns_correct_result(self):
        gg = DamePerceval()
        nomail = gg.removeMail("Santiago Dueñas <sduenas@bitergia.com>")
        self.assertEquals(nomail, "Santiago Dueñas")

    def test_dame_perceval_firstName_method_returns_correct_result(self):
        gg = DamePerceval()
        first = gg.firstName("Santiago Dueñas")
        self.assertEquals(first, "Santiago")

    def test_dame_perceval_secondName_method_returns_correct_result(self):
        gg = DamePerceval()
        second = gg.secondName("Santiago Dueñas")
        self.assertEquals(second, "Dueñas")

    def test_dame_perceval_list_committers_method_returns_correct_result(self):
        gg = DamePerceval()
        self.assertEqual(
            len(gg.list_committers(
                "https://github.com/davidam/davidam.git",
                "/tmp/clonedir")), 4)

    def test_dame_perceval_list_mailers_method_returns_correct_result(self):
        gg = DamePerceval()
        n = gg.numMails(
            "http://mail-archives.apache.org/mod_mbox/httpd-announce/")
        self.assertTrue(n >= 0)

    def test_dame_perceval_list_mailers_method_returns_correct_result(self):
        gg = DamePerceval()
        self.assertTrue(
            len(
                gg.list_mailers(
                    'http://mail-archives.apache.org/mod_mbox/httpd-announce/')
            ) >= 0)

    def test_dame_perceval_list_committers_method_returns_correct_result(self):
        dp = DamePerceval()
        l0 = dp.list_committers(
            "https://github.com/davidam/davidam.git",
            "/tmp/clonedir", mail=True)
        self.assertEqual(['David Arroyo Menéndez <davidam@es.gnu.org>', 'David Arroyo Menendez <davidam@gmail.com>', 'David Arroyo Menéndez <d.arroyome@alumnos.urjc.es>', 'David Arroyo <davidam@gmail.com>'], l0)                

    def test_dame_perceval_github_json_user_method_returns_correct_result(self):
        dp = DamePerceval()
        j = dp.get_github_json_user("davidam")
        self.assertEqual(j["id"], 1023217)
        self.assertEqual(j["blog"], "http://www.davidam.com")
        self.assertEqual(j["html_url"], "https://github.com/davidam")
        self.assertEqual(j["avatar_url"], "https://avatars2.githubusercontent.com/u/1023217?v=4")
        
        
