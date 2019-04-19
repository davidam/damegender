#!/usr/bin/python3
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

import os
import re
from setuptools import setup


cwd = os.getcwd()

def files_one_level(directory):
    f = os.popen('find '+ directory )
    l = []
    for line in f:
        fields = line.strip().split()
        l.append(fields[0])
    return l

def files_one_level_drop_pwd(directory):
    f = os.popen('find '+ directory)
    l = []
    for line in f:
        fields = line.strip().split()
        if not(os.path.isdir(fields[0])) and ("__init__.py" not in fields[0]):
            l.append(drop_pwd(fields[0]))
    return l

def drop_pwd(s):
    cwd = os.getcwd()
    result = ""
    if re.search(cwd, s):
        result = re.sub(cwd+'/', '', s)
    return result



#files_one_level_drop_pwd
#print(du.files_one_level_drop_pwd("~/git/damegender/src/damegender/files"))
print(files_one_level_drop_pwd(cwd+"/src/damegender/files/names"))

setup(name='damegender',
      version='0.0.37',
      description='Gender Detection Tool by David Arroyo MEnéndez',
      long_description='Gender Detection Tool by David Arroyo MEnéndez',
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
          "Operating System :: OS Independent",
      ],
      keywords='gender repositories',
      url='http://github.com/davidam/damegender',
      author='David Arroyo Menéndez',
      author_email='davidam@gnu.org',
      license='GPLv3',
      packages=['damegender', 'damegender.app', 'damegender.files'],
      package_dir={'damegender': 'src/damegender', 'damegender.app': 'src/damegender/app', 'damegender.files': 'src/damegender/files'},
#      data_files=[('damegender', ['src/damegender/files/features_list.csv', 'src/damegender/files/features_list_cat.csv', 'src/damegender/files/features_list_no_cat.csv', 'src/damegender/files/names/all.csv', 'src/damegender/files/names/partial.csv', 'src/damegender/files/names/names_es/femeninos_original.csv', 'src/damegender/files/names/names_es/masculinos_original.csv', 'src/damegender/files/names/names_es/masculinos.txt', 'src/damegender/files/names/names_es/femeninos.txt'])],
      data_files=[('damegender', ['src/damegender/files/features_list.csv', 'src/damegender/files/features_list_cat.csv', 'src/damegender/files/features_list_no_cat.csv'] + files_one_level_drop_pwd(cwd+"/src/damegender/files/images") + files_one_level_drop_pwd(cwd+"/src/damegender/files/datamodels") + files_one_level_drop_pwd(cwd+"/src/damegender/files/mbox") + files_one_level_drop_pwd(cwd+"/src/damegender/files/names"))],
      scripts=files_one_level(cwd+"/src/damegender/bin"),
      install_requires=[
          'markdown',
          'nltk',
          'perceval',
          'requests',
          'gender_guesser',
          'genderize',
          'numpy',
          'scikit-learn',
          'pyhyphen',
          'unidecode',
          'pandas',
          'matplotlib',
          'google-api-python-client',
          'json2html',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['damegender=damegender'],
      },
      include_package_data=True,
      zip_safe=False)
