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
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

from app.dame_sexmachine import DameSexmachine
import sys
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("file", help="csv file")
parser.add_argument('--version', action='version', version='0.1')
args = parser.parse_args()
if (len(sys.argv) > 1):
    s = DameSexmachine()
    if (args.file == 'files/partial.csv'):
        s.gender_list()
    elif (args.file == 'files/all.csv'):
        s.gender_list(all=True)
    else:
        print("Perhaps this file has not the right format")
    print("The number of males in %s is %s" % (str(args.file), str(s.males)))
    print("The number of females in %s is %s" % (str(args.file), str(s.females)))
    print("The number of gender not recognised in %s is %s" % (str(args.file), str(s.unknown)))

