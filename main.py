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

from app.dame_sexmachine import DameSexmachine
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("name", help="display the gender")
parser.add_argument('--ml')
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()
if (len(sys.argv) > 1):
    if (args.ml):
        s = DameSexmachine()
        if (args.ml == "sgd"):
            m = s.sgd_load()
        elif (args.ml == "svc"):
            m = s.svc_load()
        fi = list(s.features_int(args.name).values())
        fi = [fi]
        predicted = m.predict(fi)
        sex = ""
        if predicted:
            sex = "male"
        else:
            sex = "female"
        print("%s gender is %s" % (str(args.name), sex))
    else:
        s = DameSexmachine()
        print("%s's gender is %s" % (str(args.name), s.guess(args.name)))
