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

from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_namsor import DameNamsor
from app.dame_genderize import DameGenderize

dn = DameNamsor()
namsor_accuracy = dn.accuracy(path="files/partial.csv")
print("Namsor accuracy: %s" % namsor_accuracy)

dg = DameGenderize()

gl = dg.gender_list(path="files/partial.csv")
sl = dg.guess_list(path="files/partial.csv", binary=True)

genderize_accuracy = dg.accuracy(path="files/partial.csv")
print("Genderize accuracy: %s" % genderize_accuracy)


ds = DameSexmachine()
sexmachine_accuracy = ds.accuracy(path="files/partial.csv")
print("Sexmachine accuracy: %s" % sexmachine_accuracy)
