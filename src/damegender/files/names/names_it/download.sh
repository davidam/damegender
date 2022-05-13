#!/bin/sh

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

mkdir -p orig
cd orig
wget -c https://demo.istat.it/altridati/IscrittiNascita/2018/T2.9.xls -O 2018.xls
ssconvert -S 2018.xls 2018.csv
sed '1,5d' 2018.csv.0 > 2018.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2017/T2.9.xls -O 2017.xls
ssconvert -S 2017.xls 2017.csv
sed '1,5d' 2017.csv.0 > 2017.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2016/T2.9.xls -O 2016.xls
ssconvert -S 2016.xls 2016.csv
sed '1,5d' 2016.csv.0 > 2016.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2015/T2.9.xls -O 2015.xls
ssconvert -S 2015.xls 2015.csv
sed '1,5d' 2015.csv.0 > 2015.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2014/T2.9.xls -O 2014.xls
ssconvert -S 2014.xls 2014.csv
sed '1,5d' 2014.csv.0 > 2014.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2013/T2.9.xls -O 2013.xls
ssconvert -S 2013.xls 2013.csv
sed '1,5d' 2013.csv.0 > 2013.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2012/T2.9.xls -O 2012.xls
ssconvert -S 2012.xls 2012.csv
sed '1,5d' 2012.csv.0 > 2012.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2011/T2.9.xls -O 2011.xls
ssconvert -S 2011.xls 2011.csv
sed '1,5d' 2011.csv.0 > 2011.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2010/T2.9.xls -O 2010.xls
ssconvert -S 2010.xls 2010.csv
sed '1,5d' 2010.csv.0 > 2010.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2009/T2.9.xls -O 2009.xls
ssconvert -S 2009.xls 2009.csv
sed '1,5d' 2009.csv.0 > 2009.csv
wget -c https://demo.istat.it/altridati/IscrittiNascita/2008/T2.9.xls -O 2008.xls
ssconvert -S 2008.xls 2008.csv
sed '1,5d' 2008.csv.0 > 2008.csv
