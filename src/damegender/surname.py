#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

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

from app.dame_gender import Gender
import sys
import os
import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("surname", help="display the gender")
parser.add_argument('--total', required=True, default="ine", choices=['ine', 'es', 'us'])
parser.add_argument('--version', action='version', version='0.1')
parser.add_argument('--verbose', default=False, action="store_true")
args = parser.parse_args()

results = []

g = Gender()
v = g.guess_surname(args.surname, args.total)
if (v[0] == True):
        if ((args.total == 'es') or (args.total == 'ine')):
                print("There are %s people using %s in Spain" % (v[1], args.surname))
        elif (args.total == 'us'):
                print("There are %s people using %s in United States of America" % (v[1], args.surname))
else:
        if ((args.total == 'es') or (args.total == 'ine')):
                print("There are not people using %s in Spain" % args.surname)
        elif (args.total == 'us'):
                print("There are not people using %s in United States of America" % args.surname)
