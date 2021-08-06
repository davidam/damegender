#!/usr/bin/sh

#  Copyright (C) 2021 David Arroyo Menéndez

#  Author: David Arroyo Menéndez <davidam@gmail.com>
#  Maintainer: David Arroyo Menéndez <davidam@gmail.com>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

echo "Building csv files with name, neutral frequencies and percentages for males and females by countries"
python3 mergeinterfiles.py --file1="files/names/names_at/atmales.csv" --file2="files/names/names_at/atfemales.csv" --output=files/names/names_at/atall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_au/aumales.csv" --file2="files/names/names_au/aufemales.csv" --output=files/names/names_au/auall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_be/bemales.csv" --file2="files/names/names_be/befemales.csv" --output=files/names/names_be/beall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ca/camales.csv" --file2="files/names/names_ca/cafemales.csv" --output=files/names/names_ca/caall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_de/demales.csv" --file2="files/names/names_de/defemales.csv" --output=files/names/names_de/deall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_dk/males.csv" --file2="files/names/names_dk/females.csv" --output=files/names/names_dk/dkall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_es/esmasculinos.csv" --file2="files/names/names_es/esfemeninos.csv" --output=files/names/names_es/esall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_fi/fimales.csv" --file2="files/names/names_fi/fifemales.csv" --output=files/names/names_fi/fiall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_fr/frmales.csv" --file2="files/names/names_fr/frfemales.csv" --output=files/names/names_fr/frall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_ie/iemales.csv" --file2="files/names/names_ie/iefemales.csv" --output=files/names/names_ie/ieall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_inter/intermales.csv" --file2="files/names/names_inter/interfemales.csv" --output=files/names/names_inter/interall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_is/ismales.csv" --file2="files/names/names_is/isfemales.csv" --output=files/names/names_is/isall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_mx/hombres.csv" --file2="files/names/names_mx/mujeres.csv" --output=files/names/names_mx/mxall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_nz/nzmales.csv" --file2="files/names/names_nz/nzfemales.csv" --output=files/names/names_nz/nzall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_pt/ptmales.csv" --file2="files/names/names_pt/ptfemales.csv" --output=files/names/names_pt/ptall.csv --malefemale
python3 mergeinterfiles.py --file1="files/names/names_uy/uymasculinos.csv" --file2="files/names/names_uy/uyfemeninos.csv" --output=files/names/names_uy/uyall.csv --malefemale

