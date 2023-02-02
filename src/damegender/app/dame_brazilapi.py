#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

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


import requests
import json
import os
from app.dame_gender import Gender

class DameBrazilApi(Gender):

    def get(self, name):
        # it allows to download a name from Brazil API
        v = {}
        string = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/' + name
        string = string + "?sexo=F"
        r = requests.get(string)
        j = json.loads(r.text)
        count = 0
        for i in j[0]['res']:
            count = count + i['frequencia']
        v['female'] = count
        string2 = 'https://servicodados.ibge.gov.br/api/v2/censos/nomes/' + name
        string2 = string2 + "?sexo=M"
        r2 = requests.get(string2)
        j2 = json.loads(r2.text)
        count = 0
        for i in j2[0]['res']:
            pprint(i)
            count = count + i['frequencia']
        v['male'] = count
        return v

