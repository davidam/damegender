#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.


import unittest
import datetime
from datetime import timedelta
from app.dame_perceval import DamePerceval


class TddInPythonExample(unittest.TestCase):

    def test_numcommits_method_returns_correct_result(self):
        gg = DamePerceval()
        n = gg.numCommits("https://github.com/davidam/davidam.git",
                          "/tmp/clonedir")
        self.assertTrue(50 < n)

    def test_removeMail_method_returns_correct_result(self):
        gg = DamePerceval()
        nomail = gg.removeMail("Santiago Dueñas <sduenas@bitergia.com>")
        self.assertEqual(nomail, "Santiago Dueñas")

    def test_firstName_method_returns_correct_result(self):
        gg = DamePerceval()
        first = gg.firstName("Santiago Dueñas")
        self.assertEqual(first, "Santiago")

    def test_secondName_method_returns_correct_result(self):
        gg = DamePerceval()
        second = gg.secondName("Santiago Dueñas")
        self.assertEqual(second, "Dueñas")

    def test_list_committers_method_returns_correct_result(self):
        gg = DamePerceval()
        self.assertEqual(
            len(gg.list_committers(
                "https://github.com/davidam/davidam.git",
                "/tmp/clonedir")), 3)

    def test_list_mailers_method_returns_correct_result(self):
        gg = DamePerceval()
        n = gg.numMails(
            "http://mail-archives.apache.org/mod_mbox/httpd-announce/")
        self.assertTrue(n >= 0)

    def test_list_mailers_method_returns_correct_result(self):
        gg = DamePerceval()
        url = 'http://mail-archives.apache.org/mod_mbox/httpd-announce/'
        x = len(gg.list_mailers(url))
        self.assertTrue(x >= 0)

    def test_dicc_authors_and_mails_method_returns_correct_result(self):
        dp = DamePerceval()
        dicc = dp.dicc_authors_and_mails(
            "http://mail-archives.apache.org/mod_mbox/httpd-announce/")
        self.assertTrue(len(dicc) > 1)

    def test_dicc_authors_and_commits_method_returns_correct_result(self):
        dp = DamePerceval()
        dicc = dp.dicc_authors_and_commits(
            "https://github.com/davidam/davidam.git",
            "/tmp/clonedir")
        num = dicc['David Arroyo Menéndez <davidam@es.gnu.org>']
        self.assertTrue(len(dicc) > 1)

    def test_github_json_user_method_returns_correct_result(self):
        dp = DamePerceval()
        j = dp.get_github_json_user("davidam")
        self.assertEqual(j["id"], 1023217)
        self.assertEqual(j["blog"], "http://www.davidam.com")
        self.assertEqual(j["html_url"], "https://github.com/davidam")

    # def test_list_launchpad_method_returns_correct_result(self):
    #     dp = DamePerceval()
    #     d = datetime.datetime.now() - timedelta(hours=12)
    #     l1 = dp.list_launchpad("ubuntu", d)
    #     self.assertTrue(len(l1) > 1)
