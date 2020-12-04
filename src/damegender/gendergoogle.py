#!/usr/bin/bash
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.




"""Simple command-line example for Custom Search.

Command-line application that does a search.
"""

__author__ = 'davidam@gnu.org (David Arroyo Menéndez)'

import pprint
import argparse
from app.dame_customsearch import DameCustomsearch

# from googleapiclient.discovery import build

parser = argparse.ArgumentParser()
parser.add_argument('name', help="Name to be detected")
args = parser.parse_args()


def main():
  # Build a service object for interacting with the API. Visit
  # the Google APIs Console <http://code.google.com/apis/console>
  # to get an API key for your own application.
  g = DameCustomsearch()
  d = g.get(args.name, binary=True)
  print("Google results of %s as male: %s" % (args.name, d["rmale"]))
  print("Google results of %s as female: %s" % (args.name, d["rfemale"]))

if __name__ == '__main__':
  main()
