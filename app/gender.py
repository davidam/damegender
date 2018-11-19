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

from nltk.corpus import names

class Gender(object):
# That's the root class in the heritage, apis classes and sexmachine is inheriting from gender
    def guess(self, name, binary=False):
    # guess method to check names dictionary
        guess = ''
        if name in names.words('male.txt'):
            if binary:
                guess = 1
            else:
                guess = 'male'
        elif name in names.words('female.txt'):
            if binary:
                guess = 0
            else:
                guess = 'female'
        else:
            if binary:
                guess = 2
            else:
                guess = 'unknown'
        return guess
