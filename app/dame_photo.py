#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests, threading

class DamePhoto(threading.Thread):

    def __init__(self, s):
        self.url = s
        threading.Thread.__init__(self)

    def run(self):
        response = requests.get(self.url)
