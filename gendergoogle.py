#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
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
"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'davidam@gnu.org (David Arroyo Menéndez)'

import pprint
import argparse
from googleapiclient.discovery import build

parser = argparse.ArgumentParser()
parser.add_argument('name', help="Name to be detected")
#parser.add_argument('--gender', help="Male, female")
args = parser.parse_args()


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  filekey = open("apikey.txt", "r+")
  content = filekey.readline().rstrip()

  service = build("customsearch", "v1",
                  developerKey=content)

  res1 = service.cse().list(
      q=args.name+'+male',
#      cx='013315504628135767172:d6shbtxu-uo',
      cx='012930223948444503025:jc1-uqxxhcs',
    ).execute()
  print("Google results of %s as male: %s" % (args.name, res1['searchInformation']['totalResults']))
  res2 = service.cse().list(
      q=args.name+'+female',
#      cx='013315504628135767172:d6shbtxu-uo',
      cx='012930223948444503025:jc1-uqxxhcs',
    ).execute()
  print("Google results of %s as female: %s" % (args.name, res2['searchInformation']['totalResults']))

if __name__ == '__main__':
  main()
