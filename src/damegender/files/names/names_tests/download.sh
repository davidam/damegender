#!/bin/sh
#  Copyright (C) 2022 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com> 
#  Maintainer: David Arroyo Menendez <davidam@gmail.com> 
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

# BNE
wget -c https://www.bne.es/media/datosgob/dominiopublico/Dominio-publico-1941-CP1252.csv

# Represaliats terrasa
wget -c https://datos.gob.es/es/catalogo/l01082798-represaliados-y-victimas-terrasenses-del-fascismo.csv -O represaliats.csv

# Funcionarios Uruguay
wget -c https://catalogodatos.gub.uy/dataset/ab3fa56a-2267-468a-bdd8-d353bc847a58/resource/2e28d48b-b667-45f1-ae79-a1573bc90ebc/download/funcionarios.csv

# Base de datos de Autores de Uruguay
wget -c https://autores.uy/sites/default/files/datos/autores.csv.zip
echo "y" | unzip autores.csv.zip
rm autores.csv.zip

# French database
wget -c https://www.data.gouv.fr/fr/datasets/r/a26910c1-4860-4fa6-b077-7f49d2b856d9 -O frtest.csv

# New York Database
wget -c https://data.cityofnewyork.us/api/views/25th-nujf/rows.csv -O popular_baby_names.csv

# Paris prenoms
wget -c "https://opendata.paris.fr/explore/dataset/liste_des_prenoms/download/?format=csv&timezone=America/Argentina/Buenos_Aires&lang=fr&use_labels_for_header=true&csv_separator=%3B" -O liste_des_prenoms.paris.csv

# Performance of gender detection tools: a comparative study of name-to-gender inference services
wget -c https://osf.io/wjv7q/

# FIFA
wget -c https://www.kaggle.com/datasets/thec03u5/fifa-18-demo-player-dataset
