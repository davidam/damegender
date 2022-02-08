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

echo "These datasets are official statistics given by the government. The intention given in the footer speaks about Open Data but I can't see the Open Data License link, so the author is not redistributing these data. Please, if you can see the Open Data link write a damegender issue in github or similar"

wget -c https://data.tuik.gov.tr/Bulten/DownloadIstatistikselTablo?p=kAlb2Cr8Bweu46waDHZGrzZgXSxYr8PdhX7MtSl/tim87hYadA2q/KlQ4ftu6g4/
wget -c https://data.tuik.gov.tr/Bulten/DownloadIstatistikselTablo?p=GBtAEaFtTisp7HEjtf17DJVclMunEmxClFcme5oZ/d0NrHlSeR5e2aAouVPLv4Z1

echo "These datasets are not official statistics reached by webscraping to perhaps government sources Turkish Citizenship Database"

wget -c https://github.com/mkozturk/turkishnames/blob/master/turkishnames.zip
