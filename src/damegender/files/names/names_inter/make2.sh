#!/usr/bin/sh

python3 mergeinterfiles.py --file1="atfemales.csv" --file2="aufemales.csv" --output=ataufemales.csv
python3 mergeinterfiles.py --file1="ataufemales.csv" --file2="befemales.csv" --output=ataubefemales.csv
python3 mergeinterfiles.py --file1="ataubefemales.csv" --file2="cafemales.csv" --output=ataubecafemales.csv
python3 mergeinterfiles.py --file1="ataubecafemales.csv" --file2="defemales.csv" --output=ataubecadefemales.csv
python3 mergeinterfiles.py --file1="ataubecadefemales.csv" --file2="dkfemales.csv" --output=ataubecadedkfemales.csv 

