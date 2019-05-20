#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

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
import os

filepath = 'files/names/nam_dict.txt'
mylist = []
with open(filepath) as fp:
    for cnt, line in enumerate(fp):
        # From 3 to 25
        if (cnt > 292):
            name = ""
            for i in range(3,25):
                name = name + str(line[i])
            mylist += [name]
print(mylist)
# cmd1 = 'echo '+ str(mylist) +' > mylist.txt'
# print(os.system(cmd1))
file = open("files/names/nam_dict_list.txt", "w")
file.writelines(mylist)
file.close()
