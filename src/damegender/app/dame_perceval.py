#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: David Arroyo Menéndez.
# Copyright (C) 2018  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.

import requests
import json
import re
from perceval.backends.core.mbox import MBox
from perceval.backends.core.git import Git
from app.dame_utils import DameUtils
from app.dame_gender import Gender

class DamePerceval(object):

    def numCommits(self, url, directory):
        repo = Git(uri=url, gitpath=directory)
        count = 0
        for commit in repo.fetch():
            count += 1
        return count

    def numMails(self, url, directory="files/mbox"):
        repo = MBox(uri=url, dirpath=directory)
        count = 0
        for message in repo.fetch():
            count += 1
        return count

    def removeMail(self, s):
        result = ""
        if re.search(r' ?<.*@.*>', s):
            result = re.sub(r' ?<.*@.*>', '', s)
        return result

    def firstName(self, s):
        result = ""
        m = re.match("(\w+)", s)
        if m:
            first = m.group(1)
        else:
            first = ""
        return first

    def secondName(self, s):
        result = ""
        m = re.match("(\w+) (\w+)", s)
        if m:
            second = m.group(2)
        else:
            second = ""
        return second

    def list_committers(self, url, directory, *args, **kwargs):
        # make a list from a csv file
        mail = kwargs.get('mail', False)
        du = DameUtils()
        repo = Git(uri=url, gitpath=directory)
        list_committers = []
        for r in repo.fetch():
            if (mail == True):
                committer = r['data']['Author']
            else:
                committer = self.removeMail(r['data']['Author'])                
            list_committers.append(committer)
        list_committers = du.delete_duplicated(list_committers)            
        return list_committers
    
    def list_mailers(self, url, directory="files/mbox"):
        repo = MBox(uri=url, dirpath=directory)
        count = 0
        list_mailers = []
        for message in repo.fetch():
            list_mailers.append(message['data']['From'])
        return list_mailers

    def count_gender_in_list(self, l):
        g = Gender()
        males = 0
        females = 0
        for elem in l:
            if (int(g.name_frec(str(elem.upper()), 'us')['females']) > int(g.name_frec(str(elem.upper()), 'us')['males'] )):
                females = females + 1
            else:
                males = males + 1
        return [females, males]

    def get_github_json_user(self, nick):
        string = 'https://api.github.com/users/'
        string = string + nick
        r = requests.get(string)
        d = json.loads(r.text)
        return d
        
    
