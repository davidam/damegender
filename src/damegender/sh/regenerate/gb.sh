#!/bin/sh

# Copyright (C) 2021  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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

echo "Building england and wales females"

python3 mergeinterfiles.py --file1="files/names/names_gb/1996girls.csv" --file2="files/names/names_gb/1997girls.csv" --output=files/names/names_gb/1996+1997girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997girls.csv" --file2="files/names/names_gb/1998girls.csv" --output=files/names/names_gb/1996+1997+1998girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998girls.csv" --file2="files/names/names_gb/1999girls.csv" --output=files/names/names_gb/1996+1997+1998+1999girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999girls.csv" --file2="files/names/names_gb/2000girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000girls.csv" --file2="files/names/names_gb/2001girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001girls.csv" --file2="files/names/names_gb/2002girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002girls.csv" --file2="files/names/names_gb/2003girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003girls.csv" --file2="files/names/names_gb/2004girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004girls.csv" --file2="files/names/names_gb/2005girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005girls.csv" --file2="files/names/names_gb/2006girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006girls.csv" --file2="files/names/names_gb/2007girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007girls.csv" --file2="files/names/names_gb/2008girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008girls.csv" --file2="files/names/names_gb/2009girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009girls.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009girls.csv" --file2="files/names/names_gb/2010girls.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009+2010girls.csv

cd files/names/names_gb/
cp 1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009+2010girls.csv englandwales-girls.csv
cd ../../..

echo "Building england and wales boys"

python3 mergeinterfiles.py --file1="files/names/names_gb/1996boys.csv" --file2="files/names/names_gb/1997boys.csv" --output=files/names/names_gb/1996+1997boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997boys.csv" --file2="files/names/names_gb/1998boys.csv" --output=files/names/names_gb/1996+1997+1998boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998boys.csv" --file2="files/names/names_gb/1999boys.csv" --output=files/names/names_gb/1996+1997+1998+1999boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999boys.csv" --file2="files/names/names_gb/2000boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000boys.csv" --file2="files/names/names_gb/2001boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001boys.csv" --file2="files/names/names_gb/2002boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002boys.csv" --file2="files/names/names_gb/2003boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003boys.csv" --file2="files/names/names_gb/2004boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004boys.csv" --file2="files/names/names_gb/2005boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005boys.csv" --file2="files/names/names_gb/2006boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006boys.csv" --file2="files/names/names_gb/2007boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007boys.csv" --file2="files/names/names_gb/2008boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008boys.csv" --file2="files/names/names_gb/2009boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009boys.csv

python3 mergeinterfiles.py --file1="files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009boys.csv" --file2="files/names/names_gb/2010boys.csv" --output=files/names/names_gb/1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009+2010boys.csv

cd files/names/names_gb/
cp 1996+1997+1998+1999+2000+2001+2002+2003+2004+2005+2006+2007+2008+2009+2010boys.csv englandwales-boys.csv
cd ../../..

echo "Building gbfemales.csv from englandwales-girls.csv, northernireland.females.csv and scotland.females.csv"

python3 mergeinterfiles.py --file1="files/names/names_gb/englandwales-girls.csv" --file2="files/names/names_gb/scotland.females.csv" --output=files/names/names_gb/englandwales+scotland.females.csv
# python3 mergeinterfiles.py --file1="files/names/names_gb/englandwales+scotland.females.csv" --file2="files/names/names_gb/northernireland.females.csv" --output=files/names/names_gb/gbfemales.csv

# echo "Building gbmales.csv from englandwales-boys.csv, northernireland.males.csv and scotland.males.csv"

# python3 mergeinterfiles.py --file1="files/names/names_gb/englandwales-boys.csv" --file2="files/names/names_gb/scotland.males.csv" --output=files/names/names_gb/englandwales+scotland.males.csv
# python3 mergeinterfiles.py --file1="files/names/names_gb/englandwales+scotland.males.csv" --file2="files/names/names_gb/northernireland.males.csv" --output=files/names/names_gb/gbmales.csv


#python3 mergeinterfiles.py --file1="files/tmp/ukscotlandfemales.csv" --file2="files/names/names_gb/northerireland.females.csv" --output=files/tmp/ukscotlandnortherirelandfemales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandfemales.csv" --file2="files/names/names_gb/walesfemales.csv" --output=files/tmp/ukscotlandnortherirelandwalesfemales.csv
# cp files/tmp/ukscotlandnortherirelandwalesfemales.csv files/names/names_gb/gbfemales.csv

# echo "Building gbmales.csv"
# python3 mergeinterfiles.py --file1="files/names/names_gb/ukmales.csv" --file2="files/names/names_gb/scotland.males.csv" --output=files/tmp/ukscotlandmales.csv
# python3 mergeinterfiles.py --file1="files/tmp/ukscotlandmales.csv" --file2="files/names/names_gb/northerireland.males.csv" --output=files/tmp/ukscotlandnortherirelandmales.csv
# # python3 mergeinterfiles.py --file1="files/tmp/ukscotlandnortherirelandmales.csv" --file2="files/names/names_gb/walesmales.csv" --output=files/tmp/ukscotlandnortherirelandwalesmales.csv
# # cp files/tmp/ukscotlandnortherirelandwalesmales.csv files/names/names_gb/gbmales.csv


# echo "Cleaning temporal files"
# rm files/tmp/uk*

