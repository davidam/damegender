#!/bin/sh

# Copyright (C) 2021 David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gmail.com>
# Maintainer: David Arroyo Menéndez <davidam@gmail.com>

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

# export all_codes = ['ad', 'ae', 'af', 'ag', 'al', 'ao', 'am', 'ar', 'at', 'au', 'az', 'ba', 'bb', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bn', 'bo', 'br', 'bs', 'bt', 'bw', 'by', 'bz', 'ca', 'cd', 'cf', 'cg', 'ch', 'ci', 'cl', 'cm', 'cn', 'co', 'cr', 'cu', 'cv', 'cy', 'cz', 'de', 'dj', 'dk', 'dm', 'do', 'dz', 'ec', 'ee', 'eg', 'er', 'es', 'et', 'fi', 'fj', 'fm', 'fr', 'ga', 'gb', 'ge', 'gh', 'gm', 'gn', 'gq', 'gr', 'gt', 'gw', 'gy', 'hn', 'hr', 'ht', 'hu', 'id', 'ie', 'il', 'in', 'iq', 'ir', 'is', 'it', 'jm', 'jo', 'jp', 'ke', 'kg', 'kh', 'ki', 'km', 'kn', 'kp', 'kw', 'kz', 'la', 'lb', 'lc', 'li', 'lk', 'lr', 'ls', 'lt', 'lu', 'lv', 'ly', 'ma', 'mc', 'md', 'me', 'mg', 'mh', 'mk', 'ml', 'mm', 'mn', 'mr', 'mt', 'mu', 'mv', 'mw', 'mx', 'my', 'mz', 'na', 'ne', 'ng', 'ni', 'nl', 'no', 'np', 'nr', 'nz', 'om', 'pa', 'pe', 'pg', 'ph', 'pk', 'pl', 'pt', 'pw', 'py', 'qa', 'ro', 'rs', 'ru', 'rw', 'sa', 'sb', 'sc', 'sd', 'se', 'sg', 'si', 'sk', 'sl', 'sm', 'sn', 'so', 'sr', 'ss', 'st', 'sv', 'sy', 'sz', 'td', 'tg', 'th', 'tj', 'tl', 'tm', 'tn', 'to', 'tr', 'tt', 'tv', 'tw', 'tz', 'ua', 'ug', 'us', 'uy', 'uz', 'va', 'vc', 've', 'vn', 'vu', 'ws', 'ye', 'za', 'zm', 'zw']

# echo "Building csv files with name, neutral frequencies and percentages for males and females by countries"
# for i in $(all_codes); do
#     python3 mergeinterfiles.py --file1=files/names/names_$i/$ifemales.csv --file2=files/names/names_$i/$imales.csv --output=files/names/names_$i/$iall.csv --malefemale
#     python3 mergeinterfiles.py --file1=files/names/names_$i/$ifemales.csv --file2=files/names/names_$i/$imales.csv --output=files/names/names_$i/$ionlygender.csv --malefemaleonlygender
#     echo "$i done"
# done

sed '/^\,.*$/d' files/names/names_at/atmales.csv > files/tmp/atmales.csv
cp files/tmp/atmales.csv files/names/names_at/
sed '/^\,.*$/d' files/names/names_at/atfemales.csv > files/tmp/atfemales.csv
cp files/tmp/atfemales.csv files/names/names_at/
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_at/atfemales.csv" --output=files/names/names_at/atall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_at/atfemales.csv" --output=files/names/names_at/atonlygender.csv --malefemale_onlygender
echo "Austria done"


sed '/^\,.*$/d' files/names/names_ar/armales.csv > files/tmp/armales.csv
cp files/tmp/armales.csv files/names/names_ar/
sed '/^\,.*$/d' files/names/names_ar/arfemales.csv > files/tmp/arfemales.csv
cp files/tmp/arfemales.csv files/names/names_ar/
python3 mergeinterfiles.py --file1="files/names/names_ar/armales.csv" --file2="files/names/names_ar/arfemales.csv" --output=files/names/names_ar/arall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ar/armales.csv" --file2="files/names/names_ar/arfemales.csv" --output=files/names/names_ar/aronlygender.csv --malefemale_onlygender
echo "Argentina done"


sed '/^\,.*$/d' files/names/names_au/aumales.csv > files/tmp/aumales.csv
cp files/tmp/aumales.csv files/names/names_au/
sed '/^\,.*$/d' files/names/names_au/aufemales.csv > files/tmp/aufemales.csv
cp files/tmp/aufemales.csv files/names/names_au/
sed '/\,\,/d' files/names/names_au/aumales.csv > files/tmp/aumales.csv
cp files/tmp/aumales.csv files/names/names_au/
python3 mergeinterfiles.py --file1="files/names/names_au/aumales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/names/names_au/auall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_au/aumales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/names/names_au/auonlygender.csv --malefemale_onlygender
echo "Australia done"

sed '/^\,.*$/d' files/names/names_be/bemales.csv > files/tmp/bemales.csv
cp files/tmp/bemales.csv files/names/names_be/
sed '/^\,.*$/d' files/names/names_be/befemales.csv > files/tmp/befemales.csv
cp files/tmp/befemales.csv files/names/names_be/
python3 mergeinterfiles.py --file1="files/names/names_be/bemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/names/names_be/beall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_be/bemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/names/names_be/beonlygender.csv --malefemale_onlygender
echo "Belgium done"

sed '/^\,.*$/d' files/names/names_ca/camales.csv > files/tmp/camales.csv
cp files/tmp/camales.csv files/names/names_ca/
sed '/^\,.*$/d' files/names/names_ca/cafemales.csv > files/tmp/cafemales.csv
cp files/tmp/cafemales.csv files/names/names_ca/
python3 mergeinterfiles.py --file1="files/names/names_ca/camales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/names/names_ca/caall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ca/camales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/names/names_ca/caonlygender.csv --malefemale_onlygender
echo "Canada done"

sed '/^\,.*$/d' files/names/names_de/demales.csv > files/tmp/demales.csv
cp files/tmp/demales.csv files/names/names_de/
sed '/^\,.*$/d' files/names/names_de/defemales.csv > files/tmp/defemales.csv
cp files/tmp/defemales.csv files/names/names_de/
python3 mergeinterfiles.py --file1="files/names/names_de/demales.csv" --file2="files/names/names_de/defemales.csv" --output=files/names/names_de/deall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_de/demales.csv" --file2="files/names/names_de/defemales.csv" --output=files/names/names_de/deonlygender.csv --malefemale_onlygender
echo "Germany done"

sed '/^\,.*$/d' files/names/names_dk/dkmales.csv > files/tmp/dkmales.csv
cp files/tmp/dkmales.csv files/names/names_dk/
sed '/^\,.*$/d' files/names/names_dk/dkfemales.csv > files/tmp/dkfemales.csv
cp files/tmp/dkfemales.csv files/names/names_dk/
python3 mergeinterfiles.py --file1="files/names/names_dk/dkmales.csv" --file2="files/names/names_dk/dkfemales.csv" --output=files/names/names_dk/dkall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_dk/dkmales.csv" --file2="files/names/names_dk/dkfemales.csv" --output=files/names/names_dk/dkonlygender.csv --malefemale_onlygender
echo "Denkmark done"

sed '/^\,.*$/d' files/names/names_es/esmales.csv > files/tmp/esmales.csv
cp files/tmp/esmales.csv files/names/names_es/
sed '/^\,.*$/d' files/names/names_es/esfemales.csv > files/tmp/esfemales.csv
cp files/tmp/esfemales.csv files/names/names_es/
python3 mergeinterfiles.py --file1="files/names/names_es/esmales.csv" --file2="files/names/names_es/esfemales.csv" --output=files/names/names_es/esall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_es/esmales.csv" --file2="files/names/names_es/esfemales.csv" --output=files/names/names_es/esonlygender.csv --malefemale_onlygender
echo "Spanish done"

sed '/^\,.*$/d' files/names/names_fi/fimales.csv > files/tmp/fimales.csv
cp files/tmp/fimales.csv files/names/names_fi/
sed '/^\,.*$/d' files/names/names_fi/fifemales.csv > files/tmp/fifemales.csv
cp files/tmp/fifemales.csv files/names/names_fi/
python3 mergeinterfiles.py --file1="files/names/names_fi/fimales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/names/names_fi/fiall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_fi/fimales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/names/names_fi/fionlygender.csv --malefemale_onlygender
echo "Finland done"

sed '/^\,.*$/d' files/names/names_fr/frmales.csv > files/tmp/frmales.csv
cp files/tmp/frmales.csv files/names/names_fr/
sed '/^\,.*$/d' files/names/names_fr/frfemales.csv > files/tmp/frfemales.csv
cp files/tmp/frfemales.csv files/names/names_fr/
python3 mergeinterfiles.py --file1="files/names/names_fr/frmales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/names/names_fr/frall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_fr/frmales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/names/names_fr/fronlygender.csv --malefemale_onlygender
echo "France done"

sed '/^\,.*$/d' files/names/names_gb/gbmales.csv > files/tmp/gbmales.csv
cp files/tmp/gbmales.csv files/names/names_gb/
sed '/^\,.*$/d' files/names/names_gb/gbfemales.csv > files/tmp/gbfemales.csv
cp files/tmp/gbfemales.csv files/names/names_gb/
python3 mergeinterfiles.py --file1="files/names/names_gb/gbmales.csv" --file2="files/names/names_gb/gbfemales.csv" --output=files/names/names_gb/gball.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_gb/gbmales.csv" --file2="files/names/names_gb/gbfemales.csv" --output=files/names/names_gb/gbonlygender.csv --malefemale_onlygender
echo "Great Britain done"

sed '/^\,.*$/d' files/names/names_ie/iemales.csv > files/tmp/iemales.csv
cp files/tmp/iemales.csv files/names/names_ie/
sed '/^\,.*$/d' files/names/names_ie/iefemales.csv > files/tmp/iefemales.csv
cp files/tmp/iefemales.csv files/names/names_ie/
python3 mergeinterfiles.py --file1="files/names/names_ie/iemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/names/names_ie/ieall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ie/iemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/names/names_ie/ieonlygender.csv --malefemale_onlygender
echo "Ireland done"

sed '/^\,.*$/d' files/names/names_inter/intermales.csv > files/tmp/intermales.csv
cp files/tmp/intermales.csv files/names/names_inter/
sed '/^\,.*$/d' files/names/names_inter/interfemales.csv > files/tmp/interfemales.csv
cp files/tmp/interfemales.csv files/names/names_inter/
python3 mergeinterfiles.py --file1="files/names/names_inter/intermales.csv" --file2="files/names/names_inter/interfemales.csv" --output=files/names/names_inter/interall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_inter/intermales.csv" --file2="files/names/names_inter/interfemales.csv" --output=files/names/names_inter/interonlygender.csv --malefemale_onlygender
echo "International done"

sed '/^\,.*$/d' files/names/names_is/ismales.csv > files/tmp/ismales.csv
cp files/tmp/ismales.csv files/names/names_is/
sed '/^\,.*$/d' files/names/names_is/isfemales.csv > files/tmp/isfemales.csv
cp files/tmp/isfemales.csv files/names/names_is/
python3 mergeinterfiles.py --file1="files/names/names_is/ismales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/names/names_is/isall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_is/ismales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/names/names_is/isonlygender.csv --malefemale_onlygender
echo "Iceland done"

sed '/^\,.*$/d' files/names/names_it/itmales.csv > files/tmp/itmales.csv
cp files/tmp/itmales.csv files/names/names_it/
sed '/^\,.*$/d' files/names/names_it/itfemales.csv > files/tmp/itfemales.csv
cp files/tmp/itfemales.csv files/names/names_it/
python3 mergeinterfiles.py --file1="files/names/names_it/itmales.csv" --file2="files/names/names_it/itfemales.csv" --output=files/names/names_it/itall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_it/itmales.csv" --file2="files/names/names_it/itfemales.csv" --output=files/names/names_it/itonlygender.csv --malefemale_onlygender
echo "Italy done"

sed '/^\,.*$/d' files/names/names_mx/mxmales.csv > files/tmp/mxmales.csv
cp files/tmp/mxmales.csv files/names/names_mx/
sed '/^\,.*$/d' files/names/names_mx/mxfemales.csv > files/tmp/mxfemales.csv
cp files/tmp/mxfemales.csv files/names/names_mx/
python3 mergeinterfiles.py --file1="files/names/names_mx/mxmales.csv" --file2="files/names/names_mx/mxfemales.csv" --output=files/names/names_mx/mxall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_mx/mxmales.csv" --file2="files/names/names_mx/mxfemales.csv" --output=files/names/names_mx/mxonlygender.csv --malefemale_onlygender
echo "Mexico done"

sed '/^\,.*$/d' files/names/names_no/nomales.csv > files/tmp/nomales.csv
cp files/tmp/nomales.csv files/names/names_no/
sed '/^\,.*$/d' files/names/names_no/nofemales.csv > files/tmp/nofemales.csv
cp files/tmp/nofemales.csv files/names/names_no/
python3 mergeinterfiles.py --file1="files/names/names_no/nomales.csv" --file2="files/names/names_no/nofemales.csv" --output=files/names/names_no/noall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_no/nomales.csv" --file2="files/names/names_no/nofemales.csv" --output=files/names/names_no/noonlygender.csv --malefemale_onlygender
echo "Norway done"

sed '/^\,.*$/d' files/names/names_nz/nzmales.csv > files/tmp/nzmales.csv
cp files/tmp/nzmales.csv files/names/names_nz/
sed '/^\,.*$/d' files/names/names_nz/nzfemales.csv > files/tmp/nzfemales.csv
cp files/tmp/nzfemales.csv files/names/names_nz/
python3 mergeinterfiles.py --file1="files/names/names_nz/nzmales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/names/names_nz/nzall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_nz/nzmales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/names/names_nz/nzonlygender.csv --malefemale_onlygender
echo "New Zealand done"

sed '/^\,.*$/d' files/names/names_pt/ptmales.csv > files/tmp/ptmales.csv
cp files/tmp/ptmales.csv files/names/names_pt/
sed '/^\,.*$/d' files/names/names_pt/ptfemales.csv > files/tmp/ptfemales.csv
cp files/tmp/ptfemales.csv files/names/names_pt/
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/names/names_pt/ptall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/names/names_pt/ptonlygender.csv --malefemale_onlygender
echo "Portugal done"

sed '/^\,.*$/d' files/names/names_ru/rumales.csv > files/tmp/rumales.csv
cp files/tmp/rumales.csv files/names/names_ru/
sed '/^\,.*$/d' files/names/names_ru/rufemales.csv > files/tmp/rufemales.csv
cp files/tmp/rufemales.csv files/names/names_ru/
sed '/^\,.*$/d' files/names/names_ru/rufemales.en.csv > files/tmp/rufemales.en.csv
cp files/tmp/rufemales.en.csv files/names/names_ru/
sed '/^\,.*$/d' files/names/names_ru/rumales.en.csv > files/tmp/rumales.en.csv
cp files/tmp/rumales.en.csv files/names/names_ru/

python3 mergeinterfiles.py --file1="files/names/names_ru/rumales.csv" --file2="files/names/names_ru/rufemales.csv" --output=files/names/names_ru/ruall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ru/rumales.csv" --file2="files/names/names_ru/rufemales.csv" --output=files/names/names_ru/ruonlygender.csv --malefemale_onlygender
python3 mergeinterfiles.py --file1="files/names/names_ru/rumales.en.csv" --file2="files/names/names_ru/rufemales.en.csv" --output=files/names/names_ru/ruonlygender.en.csv --malefemale_onlygender
echo "Russia done"

sed '/^\,.*$/d' files/names/names_se/semales.csv > files/tmp/semales.csv
cp files/tmp/semales.csv files/names/names_se/
sed '/^\,.*$/d' files/names/names_se/sefemales.csv > files/tmp/sefemales.csv
cp files/tmp/sefemales.csv files/names/names_se/
python3 mergeinterfiles.py --file1="files/names/names_se/semales.csv" --file2="files/names/names_se/sefemales.csv" --output=files/names/names_se/seall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_se/semales.csv" --file2="files/names/names_se/sefemales.csv" --output=files/names/names_se/seonlygender.csv --malefemale_onlygender
echo "Sweden done"

sed '/^\,.*$/d' files/names/names_si/simales.csv > files/tmp/simales.csv
cp files/tmp/simales.csv files/names/names_si/
sed '/^\,.*$/d' files/names/names_si/sifemales.csv > files/tmp/sifemales.csv
cp files/tmp/sifemales.csv files/names/names_si/
python3 mergeinterfiles.py --file1="files/names/names_si/simales.csv" --file2="files/names/names_si/sifemales.csv" --output=files/names/names_si/siall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_si/simales.csv" --file2="files/names/names_si/sifemales.csv" --output=files/names/names_si/sionlygender.csv --malefemale_onlygender
echo "Slovenia done"

# # python3 mergeinterfiles.py --file1="files/names/names_tr/trmales.csv" --file2="files/names/names_tr/trfemales.csv" --output=files/names/names_tr/trall.csv --malefemale
# # python3 mergeinterfiles.py --file1="files/names/names_tr/trmales.csv" --file2="files/names/names_tr/trfemales.csv" --output=files/names/names_tr/trall.csv --malefemale_onlygender
# # echo "Turkish done"

sed '/^\,.*$/d' files/names/names_uy/uymales.csv > files/tmp/uymales.csv
cp files/tmp/uymales.csv files/names/names_uy/
sed '/^\,.*$/d' files/names/names_uy/uyfemales.csv > files/tmp/uyfemales.csv
cp files/tmp/uyfemales.csv files/names/names_uy/
python3 mergeinterfiles.py --file1="files/names/names_uy/uymales.csv" --file2="files/names/names_uy/uyfemales.csv" --output=files/names/names_uy/uyall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_uy/uymales.csv" --file2="files/names/names_uy/uyfemales.csv" --output=files/names/names_uy/uyonlygender.csv --malefemale_onlygender
echo "Uruguay done"

sed '/^\,.*$/d' files/names/names_us/usmales.csv > files/tmp/usmales.csv
cp files/tmp/usmales.csv files/names/names_us/
sed '/^\,.*$/d' files/names/names_us/usfemales.csv > files/tmp/usfemales.csv
cp files/tmp/usfemales.csv files/names/names_us/

python3 mergeinterfiles.py --file1="files/names/names_us/usmales.csv" --file2="files/names/names_us/usfemales.csv" --output=files/names/names_us/usall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_us/usmales.csv" --file2="files/names/names_us/usfemales.csv" --output=files/names/names_us/usonlygender.csv --malefemale_onlygender
echo "United States of America done"
