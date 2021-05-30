#!/usr/bin/bash
#  Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
#  This file is part of Damegender.

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.



for i in $(ls test/test_dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls app/dame_*.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.py); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/python_gpl_header.txt; done

# for i in $(ls *.sh); do ./home/davidam/git/damegender/src/damegender/fl2gplv3.sh $i files/bash_gpl_header.txt; done
