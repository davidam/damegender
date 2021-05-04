#!/usr/bin/sh

echo "Building interfemales.csv"
python3 mergeinterfiles.py --file1="../names_at/atfemales.csv" --file2="../names_au/baby-names-1944-2013/aufemales.csv" --output=ataufemales.csv
python3 mergeinterfiles.py --file1="ataufemales.csv" --file2="../names_be/befemales.csv" --output=ataubefemales.csv
python3 mergeinterfiles.py --file1="ataubefemales.csv" --file2="../names_ca/cafemales.csv" --output=ataubecafemales.csv
python3 mergeinterfiles.py --file1="ataubecafemales.csv" --file2="../names_de/defemales.csv" --output=ataubecadefemales.csv
python3 mergeinterfiles.py --file1="ataubecadefemales.csv" --file2="../names_dk/females.csv" --output=ataubecadedkfemales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkfemales.csv" --file2="../names_es/esfemeninos.csv" --output=ataubecadedkesfemales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkesfemales.csv" --file2="../names_fi/fifemales.csv" --output=ataubecadedkesfifemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfifemales.csv" --file2="../names_ie/iefemales.csv" --output=ataubecadedkesfiiefemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiiefemales.csv" --file2="../names_is/isfemales.csv" --output=ataubecadedkesfiieisfemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieisfemales.csv" --file2="../names_mx/mujeres.csv" --output=ataubecadedkesfiieismxfemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxfemales.csv" --file2="../names_nz/nzfemales.csv" --output=ataubecadedkesfiieismxnzfemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzfemales.csv" --file2="../names_pt/ptfemales.csv" --output=ataubecadedkesfiieismxnzptfemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptfemales.csv" --file2="../names_si/sifemales.csv" --output=ataubecadedkesfiieismxnzptsifemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsifemales.csv" --file2="../names_us/usfemales.csv" --output=ataubecadedkesfiieismxnzptsiusfemales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsiusfemales.csv" --file2="../names_uy/uyfemeninos.csv" --output=ataubecadedkesfiieismxnzptsiusuyfemales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsiusuyfemales.csv" --file2="../names_fr/frfemales.csv" --output=ataubecadedkesfiieismxnzptsiusuyfrfemales.csv



echo "Building intermales.csv"
python3 mergeinterfiles.py --file1="../names_at/atmales.csv" --file2="../names_au/baby-names-1944-2013/aumales.csv" --output=ataumales.csv
python3 mergeinterfiles.py --file1="ataumales.csv" --file2="../names_be/bemales.csv" --output=ataubemales.csv
python3 mergeinterfiles.py --file1="ataubemales.csv" --file2="../names_ca/camales.csv" --output=ataubecamales.csv
python3 mergeinterfiles.py --file1="ataubecamales.csv" --file2="../names_de/demales.csv" --output=ataubecademales.csv
python3 mergeinterfiles.py --file1="ataubecademales.csv" --file2="../names_dk/males.csv" --output=ataubecadedkmales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkmales.csv" --file2="../names_es/esmasculinos.csv" --output=ataubecadedkesmales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkesmales.csv" --file2="../names_fi/fimales.csv" --output=ataubecadedkesfimales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfimales.csv" --file2="../names_ie/iemales.csv" --output=ataubecadedkesfiiemales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiiemales.csv" --file2="../names_is/ismales.csv" --output=ataubecadedkesfiieismales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismales.csv" --file2="../names_mx/hombres.csv" --output=ataubecadedkesfiieismxmales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxmales.csv" --file2="../names_nz/nzmales.csv" --output=ataubecadedkesfiieismxnzmales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzmales.csv" --file2="../names_pt/ptmales.csv" --output=ataubecadedkesfiieismxnzptmales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptmales.csv" --file2="../names_si/simales.csv" --output=ataubecadedkesfiieismxnzptsimales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsimales.csv" --file2="../names_us/usmales.csv" --output=ataubecadedkesfiieismxnzptsiusmales.csv 
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsiusmales.csv" --file2="../names_uy/uymasculinos.csv" --output=ataubecadedkesfiieismxnzptsiusuymales.csv
python3 mergeinterfiles.py --file1="ataubecadedkesfiieismxnzptsiusuymales.csv" --file2="../names_fr/frmales.csv" --output=ataubecadedkesfiieismxnzptsiusuyfrmales.csv

mv ataubecadedkesfiieismxnzptsiusuyfrmales.csv intermales.csv
mv ataubecadedkesfiieismxnzptsiusuyfrfemales.csv interfemales.csv

echo "Cleaning temporal files" 
rm atau*
