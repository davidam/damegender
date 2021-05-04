#!/usr/bin/bash
#  Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
#  This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
#
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#  Boston, MA 02110-1301 USA,



for i in $(ls test/test_dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls app/dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.sh); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/bash_gpl_header.txt; done
