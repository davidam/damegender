#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with GNU Emacs; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import configparser
config = configparser.ConfigParser()

genderapi_p = input("Do you have a genderapi key: (Y|N) ")
if (genderapi_p == "Y"):
   config['DEFAULT']['genderapi'] = 'yes'
   genderapi_key = str(input("Introduce your genderapi key: "))
   fo = open("files/genderapipass.txt", "w")
   fo.write(genderapi_key)
   fo.close()
else:
   config['DEFAULT']['genderapi'] = 'no'

genderize_p = input("Do you have a genderize key: (Y|N) ")
if (genderize_p == "Y"):
   config['DEFAULT']['genderize'] = 'yes'
   genderize_key = input("Introduce your genderize key: ")
   fo = open("files/genderizepass.txt", "w")
   fo.write(genderize_key)
   fo.close()
else:
   config['DEFAULT']['genderize'] = 'no'

nameapi_p = input("Do you have a nameapi key: (Y|N) ")
if (nameapi_p == "Y"):
   config['DEFAULT']['nameapi'] = 'yes'
   nameapi_key = input("Introduce your nameapi key: ")
   fo = open("files/nameapipass.txt", "w")
   fo.write(nameapi_key)
   fo.close()
else:
   config['DEFAULT']['nameapi'] = 'no'

with open('config.cfg', 'w') as configfile:
   config.write(configfile)


# import configparser

# config = configparser.RawConfigParser()
# config.read('example.ini')

# for key in config['bitbucket.org']:
#    print(key)

# print(config['bitbucket.org']['ForwardX11'])
