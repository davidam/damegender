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

echo "Building csv files with name, neutral frequencies and percentages for males and females by countries"
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_at/atfemales.csv" --output=files/names/names_at/atall.csv --malefemale
echo "Argentina done"
python3 mergeinterfiles.py --file1="files/names/names_ar/armales.csv" --file2="files/names/names_ar/arfemales.csv" --output=files/names/names_ar/arall.csv --malefemale
echo "Austria done"
python3 mergeinterfiles.py --file1="files/names/names_au/aumales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/names/names_au/auall.csv --malefemale
echo "Australia done"
python3 mergeinterfiles.py --file1="files/names/names_be/bemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/names/names_be/beall.csv --malefemale
echo "Belgium done"
python3 mergeinterfiles.py --file1="files/names/names_ca/camales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/names/names_ca/caall.csv --malefemale
echo "Canada done"
python3 mergeinterfiles.py --file1="files/names/names_de/demales.csv" --file2="files/names/names_de/defemales.csv" --output=files/names/names_de/deall.csv --malefemale
echo "Germany done"
python3 mergeinterfiles.py --file1="files/names/names_dk/males.csv" --file2="files/names/names_dk/females.csv" --output=files/names/names_dk/dkall.csv --malefemale
echo "Denkmark done"
python3 mergeinterfiles.py --file1="files/names/names_es/esmasculinos.csv" --file2="files/names/names_es/esfemeninos.csv" --output=files/names/names_es/esall.csv --malefemale
echo "Spanish done"
python3 mergeinterfiles.py --file1="files/names/names_fi/fimales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/names/names_fi/fiall.csv --malefemale
echo "Finland done"
python3 mergeinterfiles.py --file1="files/names/names_fr/frmales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/names/names_fr/frall.csv --malefemale
echo "France done"
python3 mergeinterfiles.py --file1="files/names/names_gb/gbmales.csv" --file2="files/names/names_gb/gbfemales.csv" --output=files/names/names_gb/gball.csv --malefemale
echo "Great Britain done"
python3 mergeinterfiles.py --file1="files/names/names_ie/iemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/names/names_ie/ieall.csv --malefemale
echo "Ireland done"
python3 mergeinterfiles.py --file1="files/names/names_inter/intermales.csv" --file2="files/names/names_inter/interfemales.csv" --output=files/names/names_inter/interall.csv --malefemale
echo "International done"
python3 mergeinterfiles.py --file1="files/names/names_is/ismales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/names/names_is/isall.csv --malefemale
echo "Iceland done"
python3 mergeinterfiles.py --file1="files/names/names_it/itmales.csv" --file2="files/names/names_it/itfemales.csv" --output=files/names/names_it/itall.csv --malefemale
echo "Italy done"
python3 mergeinterfiles.py --file1="files/names/names_mx/hombres.csv" --file2="files/names/names_mx/mujeres.csv" --output=files/names/names_mx/mxall.csv --malefemale
echo "Mexico done"
python3 mergeinterfiles.py --file1="files/names/names_no/nomales.csv" --file2="files/names/names_no/nofemales.csv" --output=files/names/names_no/noall.csv --malefemale
echo "Norway done"
python3 mergeinterfiles.py --file1="files/names/names_nz/nzmales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/names/names_nz/nzall.csv --malefemale
echo "New Zealand done"
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/names/names_pt/ptall.csv --malefemale
echo "Portugal done"
python3 mergeinterfiles.py --file1="files/names/names_ru/rumales.csv" --file2="files/names/names_ru/rufemales.csv" --output=files/names/names_ru/ruall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ru/rumales.en.csv" --file2="files/names/names_ru/rufemales.en.csv" --output=files/names/names_ru/ruall.en.csv --malefemale
echo "Russia done"
python3 mergeinterfiles.py --file1="files/names/names_se/semales.csv" --file2="files/names/names_se/sefemales.csv" --output=files/names/names_se/seall.csv --malefemale
echo "Sweden done"
# python3 mergeinterfiles.py --file1="files/names/names_tr/trmales.csv" --file2="files/names/names_tr/trfemales.csv" --output=files/names/names_tr/trall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_uy/uymasculinos.csv" --file2="files/names/names_uy/uyfemeninos.csv" --output=files/names/names_uy/uyall.csv --malefemale
echo "Uruguay done"
