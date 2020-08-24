#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

rm files/apikeys/*
echo "[DEFAULT]
genderapi = no
genderize = no
nameapi = no
namsor = no
customsearch = no

[FILES]
genderapi = files/apikeys/genderapipass.txt
genderize = files/apikeys/genderizepass.txt
genderguesser = files/apikeys/genderguesserpass.txt
namsor = files/apikeys/namsorpass.txt
nameapi = files/apikeys/nameapipass.txt" > config.cfg
