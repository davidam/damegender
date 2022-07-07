#!/bin/bash

#  Copyright (C) 2022 David Arroyo Menéndez

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
#  along with Damegender; see the file GPL.txt.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

# GIRLS ENGLAND AND WALES

echo "GIRLS ENGLAND AND WALES"

mkdir -p orig

cd orig

mkdir -p englandandwales
cd englandandwales

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2020/2020girlsnames.xlsx -O 2020girlsnames.xlsx

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2019/2019girlsnames.xlsx -O 2019girlsnames.xlsx

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2018/2018girlsnames.xls -O 2018girlsnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2017/2017girlsnames.xls -O 2017girlsnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2016/2016girlsnames.xls -O 2016girlsnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2015/2015girlsnamesfinal.xls -O 2015girlsnamesfinal.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2014/2014girlsbyareagorrsmonthwebtables_tcm77-413741.xls -O 2014girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2013/2013girlsbyareagorrsmonthwebtables_tcm77-374588.xls -O 2013girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2012/2012girlsbyareagorrsmonthwebtables_tcm77-323080.xls -O 2012girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2011/2011girlsbabynamesfinal_tcm77-276135.xls -O 2011girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2010/2010girls_tcm77-253930.xls -O 2010girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2009/2009girls_tcm77-253940.xls -O 2009girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2008/2008girls_tcm77-253964.xls -O 2008girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2007/2007girls_tcm77-253971.xls -O 2007girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2006/2006girls_tcm77-253976.xls -O 2006girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2005/2005girls_tcm77-253980.xls -O 2005girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2004/2004girls_tcm77-253984.xls -O 2004girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2003/2003girls_tcm77-253988.xls -O 2003girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2002/2002girls_tcm77-253992.xls -O 2002girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2001/2001girls_tcm77-253998.xls -O 2001girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f2000/2000girls_tcm77-254006.xls -O 2000girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f1999/1999girls_tcm77-254010.xls -O 1999girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f1998/1998girls_tcm77-254016.xls -O 1998girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f1997/1997girls_tcm77-254020.xls -O 1997girls.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsgirls%2f1996/1996girls_tcm77-254024.xls -O 1996girls.xls

# BOYS ENGLAND AND WALES

echo "BOYS ENGLAND AND WALES"

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2020/2020boysnames.xlsx -O 2020boysnames.xlsx

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2019/2019boysnames.xlsx -O 2019boysnames.xlsx

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2018/2018boysnames.xls -O 2018boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2017/2017boysnames.xls -O 2017boynames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2016/2016boysnames.xls -O 2016boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2015/2015boysnamesfinal.xls -O 2015boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2014/2014boysbyareagorrsmonthwebtables_tcm77-413738.xls -O 2014boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2013/2013boysbyareagorrsmonthwebtables_tcm77-374580.xls -O 2013boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2012/2012boysbyareagorrsmonthwebtables_tcm77-323077.xls -O 2012boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2011/2011boysbabynamesfinal_tcm77-276133.xls -O 2011boysnames.xls 

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2010/2010boys_tcm77-253928.xls -O 2010boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2009/2009boys_tcm77-253932.xls -O 2009boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2008/2008boys_tcm77-253966.xls -O 2008boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2007/2007boys_tcm77-253973.xls -O 2007boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2006/2006boys_tcm77-253978.xls -O 2006boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2005/2005boys_tcm77-253982.xls -O 2005boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2004/2004boys_tcm77-253986.xls -O 2004boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2003/2003boys_tcm77-253990.xls -O 2003boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2002/2002boys_tcm77-253994.xls -O 2002boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2001/2001boys_tcm77-254000.xls -O 2001boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f2000/2000boys_tcm77-254008.xls -O 2000boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f1999/1999boys_tcm77-254014.xls -O 1999boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f1998/1998boys_tcm77-254018.xls -O 1998boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f1997/1997boys_tcm77-254022.xls -O 1997boysnames.xls

wget -c https://www.ons.gov.uk/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%2flivebirths%2fdatasets%2fbabynamesenglandandwalesbabynamesstatisticsboys%2f1996/1996boys_tcm77-254026.xls -O 1996boysnames.xls

for i in $(ls *.xls*); do
    ssconvert -S $i $i.csv
done


# SCOTLAND

cd ..
mkdir -p scotland
cp ../scotland.py scotland
cd scotland

wget -c https://www.nrscotland.gov.uk/files//statistics/babies-names/20/babies-first-names-20-full-list.zip

wget -c https://www.nrscotland.gov.uk/files//statistics/babies-names/20/babies-first-names-all-names-all-years.csv

cp babies-first-names-all-names-all-years.csv scotland.orig.csv

python3 scotland.py

rm scotland.py

# NORTH IRELAND

cd ..
mkdir -p nisra
cp ../nisra.py nisra
cd nisra
wget -c https://www.nisra.gov.uk/sites/nisra.gov.uk/files/publications/Full_Name_List_9718.xlsx

ssconvert -S Full_Name_List_9718.xlsx Full_Name_List_9718.csv

cp Full_Name_List_9718.csv.4 nisra.females.csv
sed -i '1d' nisra.females.csv
sed -i '1d' nisra.females.csv
cp Full_Name_List_9718.csv.3 nisra.males.csv
sed -i '1d' nisra.males.csv
sed -i '1d' nisra.males.csv
python3 nisra.py
