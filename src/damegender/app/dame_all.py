#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# You can share, copy and modify this software if you are a woman or you
# are David Arroyo Menéndez and you include this note.




from app.dame_gender import Gender
from app.dame_sexmachine import DameSexmachine
from app.dame_genderize import DameGenderize
from app.dame_genderapi import DameGenderApi
from app.dame_namsor import DameNamsor
from app.dame_genderguesser import DameGenderGuesser


class DameAll(Gender):
    def average(self, name, surname):
        r = 0
        count = 0
        avg = 0
        dgg = DameGenderGuesser()
        guess1 = int(dgg.guess(name, binary="True"))
        if (guess1 != 2):
            r = r + guess1
            count = count + 1
        if (self.config['DEFAULT']['genderapi'] == 'yes'):
            dga = DameGenderApi()
            guess2 = int(dga.guess(name, binary="True"))
            if (guess2 != 2):
                r = r + guess2
                count = count + 1
        if (self.config['DEFAULT']['genderize'] == 'yes'):
            dg = DameGenderize()
            guess3 = int(dg.guess(name, binary="True"))
            if (guess3 != 2):
                r = r + guess3
                count = count + 1
        if (self.config['DEFAULT']['namsor'] == 'yes'):
            dn = DameNamsor()
            guess4 = int(dn.guess(str(name), str(surname), binary="True"))
            if (guess4 != 2):
                r = r + guess4
                count = count + 1
        avg = r / count
        return avg
