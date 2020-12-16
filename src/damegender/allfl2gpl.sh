#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.



for i in $(ls test/test_dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls app/dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.sh); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/bash_gpl_header.txt; done
