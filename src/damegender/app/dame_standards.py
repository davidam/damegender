#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2023  David Arroyo Menéndez (davidam@gmail.com)
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

# This file is about Gender Standards: coding about males, females, ...
# there are other file about ethnicity standards: dame_ethnicity.py

class DameGenderStandards():

    def dicc_damegender(self):
        # Before the standards DameGender was using a coding system, too
        # Sex has to do with people's genitals, men's penis looks like
        # a one in numbers and the vagina, women's hole could be painted
        # with a zero in numbers
        dicc = {0: "female",
                1: "male",
                2: "unknown"}
        return dicc
    
    def dicc_isoiec5218(self):
        # https://www.iso.org/standard/81682.html
        dicc = {0: "not know",
                1: "male",
                2: "female",
                9: "not applicable"}
        return dicc

    def dicc_rfc6350(self):
        # https://datatracker.ietf.org/doc/html/rfc6350#section-6.2.7
        dicc = {"m": "male",
                "f": "female",
                "o": "other",
                "n": "not applicable",
                "u": "undefined"}
        return dicc
        
    def dicc_isoiec5218_to_rfc6350(self):
        dicc = {0: "u",
                1: "m",
                2: "f",
                9: "n"}

