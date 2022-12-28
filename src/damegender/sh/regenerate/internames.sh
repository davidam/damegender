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

mkdir -p files/tmp

echo "Building interfemales.csv"
python3 mergeinterfiles.py --file1="files/names/names_at/atfemales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/tmp/ataufemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataufemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/tmp/ataubefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubefemales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/tmp/ataubecafemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecafemales.csv" --file2="files/names/names_de/defemales.csv" --output=files/tmp/ataubecadefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadefemales.csv" --file2="files/names/names_dk/dkfemales.csv" --output=files/tmp/ataubecadedkfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkfemales.csv" --file2="files/names/names_es/esfemales.csv" --output=files/tmp/ataubecadedkesfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfemales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/tmp/ataubecadedkesfifemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfifemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/tmp/ataubecadedkesfiiefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiiefemales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/tmp/ataubecadedkesfiieisfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieisfemales.csv" --file2="files/names/names_mx/mxfemales.csv" --output=files/tmp/ataubecadedkesfiieismxfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxfemales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzfemales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptfemales.csv" --file2="files/names/names_si/sifemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsifemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsifemales.csv" --file2="files/names/names_us/usfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusfemales.csv" --file2="files/names/names_uy/uyfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfemales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrfemales.csv" --file2="files/names/names_ch/chfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchfemales.csv" --file2="files/names/names_se/sefemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsefemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsefemales.csv" --file2="files/names/names_no/nofemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenofemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenofemales.csv" --file2="files/names/names_ar/arfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoarfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoarfemales.csv" --file2="files/names/names_gb/gbfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbfemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbfemales.csv" --file2="files/names/names_ru/rufemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbrufemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbrufemales.csv" --file2="files/names/names_it/itfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbruitfemales.csv

# #python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenofemales.csv" --file2="files/names/names_tr/trfemales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenotrfemales.csv



# echo "Building intermales.csv"
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_au/aumales.csv" --output=files/tmp/ataumales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataumales.csv" --file2="files/names/names_be/bemales.csv" --output=files/tmp/ataubemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubemales.csv" --file2="files/names/names_ca/camales.csv" --output=files/tmp/ataubecamales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecamales.csv" --file2="files/names/names_de/demales.csv" --output=files/tmp/ataubecademales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecademales.csv" --file2="files/names/names_dk/dkmales.csv" --output=files/tmp/ataubecadedkmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkmales.csv" --file2="files/names/names_es/esmasculinos.csv" --output=files/tmp/ataubecadedkesmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesmales.csv" --file2="files/names/names_fi/fimales.csv" --output=files/tmp/ataubecadedkesfimales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfimales.csv" --file2="files/names/names_ie/iemales.csv" --output=files/tmp/ataubecadedkesfiiemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiiemales.csv" --file2="files/names/names_is/ismales.csv" --output=files/tmp/ataubecadedkesfiieismales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismales.csv" --file2="files/names/names_mx/mxmales.csv" --output=files/tmp/ataubecadedkesfiieismxmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxmales.csv" --file2="files/names/names_nz/nzmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzmales.csv" --file2="files/names/names_pt/ptmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptmales.csv" --file2="files/names/names_si/simales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsimales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsimales.csv" --file2="files/names/names_us/usmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusmales.csv" --file2="files/names/names_uy/uymales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuymales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuymales.csv" --file2="files/names/names_fr/frmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrmales.csv" --file2="files/names/names_ch/chmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchmales.csv" --file2="files/names/names_se/semales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsemales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsemales.csv" --file2="files/names/names_no/nomales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenomales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenomales.csv" --file2="files/names/names_ar/armales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoarmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoarmales.csv" --file2="files/names/names_gb/gbmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbmales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbmales.csv" --file2="files/names/names_ru/rumales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbrumales.csv
python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbrumales.csv" --file2="files/names/names_it/itmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbruitmales.csv

# # #python3 mergeinterfiles.py --file1="files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenomales.csv" --file2="files/names/names_tr/trmales.csv" --output=files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenotrmales.csv


mv files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbruitmales.csv files/names/names_inter/intermales.csv
mv files/tmp/ataubecadedkesfiieismxnzptsiusuyfrchsenoargbruitfemales.csv files/names/names_inter/interfemales.csv

python3 mergeinterfiles.py --file1="files/names/names_inter/intermales.csv" --file2="files/names/names_inter/interfemales.csv" --output="files/names/names_inter/interall.csv" --malefemale

echo "Cleaning temporal files"
rm files/tmp/*
