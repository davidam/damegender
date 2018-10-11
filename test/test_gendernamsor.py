#!/usr/bin/python
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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
from app.gendernamsor import Gendernamsor

class TddInPythonExample(unittest.TestCase):

    def test_gender_namsor_list_method_returns_correct_result(self):
        gn = Gendernamsor()
        self.assertEqual([('pierre', 'male'), ('raul', 'male'), ('adriano', 'male'), ('ralf', 'male'), ('teppei', 'male'), ('guillermo', 'male'), ('catherine', 'female'), ('sabina', 'female'), ('ralf', 'male'), ('karl', 'male'), ('sushil', 'male'), ('clemens', 'male'), ('gregory', 'male'), ('lester', 'male'), ('claude', 'male'), ('martin', 'male'), ('vlad', 'male'), ('pasquale', 'male'), ('lourdes', 'female'), ('bruno', 'male'), ('thomas', 'male')], gn.list())
