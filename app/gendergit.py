#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author: David Arroyo Menéndez.
# Copyright (C) 2018  David Arroyo Menéndez

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

#from perceval.backends.core.mbox import MBox
from perceval.backends.core.git import Git
import re

class GenderGit(object):

    def numCommits(self, url, directory):
        repo = Git(uri=url, gitpath=directory)
        count = 0
        for commit in repo.fetch():
            count += 1
        return count

    def removeMail(self, s):
        result = ""
        if re.search(r'<.*@.*>', s):
            result = re.sub(r'<.*@.*>', '', s)
        return result

g = GenderGit()
print(g.numCommits("https://github.com/grimoirelab/perceval.git", "/tmp/clonedir"))
print(g.removeMail("Santiago Dueñas <sduenas@bitergia.com>"))
