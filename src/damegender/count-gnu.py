#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Copyright (C) 2020  David Arroyo Menéndez (davidam@gmail.com)
# This file is part of Damegender.

# Damegender is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Damegender is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender.  If not, see <https://www.gnu.org/licenses/>.



import csv
import unicodedata
import unidecode
from pprint import pprint
import re
from app.dame_gender import Gender
from app.dame_utils import DameUtils
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--show', choices=['males', 'females', 'unknowns', 'all'])
args = parser.parse_args()

du = DameUtils()
g = Gender()

gnulist = ['Adam Bilbrough ', 'Adam Fedor ', 'Adam Spiers', 'Adrienne G. Thompson', 'Akim Demaille', 'Al Davis', 'Alejandro Sanchez Acosta ', 'Aleksandar Samardzic', 'Ales Cepek', 'Alessandro Rubini', 'Alexander Naumov', 'Alexandre Oliva', 'Alexandre Viau', 'Alex Muntada', 'Alex Sassmannshausen', 'Alfred M. Szmidt ', 'Allin Cottrell', 'Amin Bandali', 'Anand Babu', 'Andreas Enge', 'Andreas Grünbacher', 'Andrew Hughes', 'Andrew Makhorin', 'Anto Cvitić', 'Antonio Diaz Diaz', 'Anuradha Ratnaweera', 'Arnold Robbins', 'Arthur Schwarz', 'Assaf Gordon', 'Aubrey Jaffer', 'Aymeric Moizard', 'Baishampayan Ghose', 'Barry Warsaw', 'Ben Elliston', 'Ben Pfaff', 'Bernhard "Bero" Rosenkränzer', 'Bob Glickstein', 'Bradley M. Kuhn (aka bkuhn)', 'Brett Smith', 'Brian J. Fox', 'Brian Gough', 'Brigham Keys, Esq.', 'Bruno Félix Rezende Ribeiro', 'Carlo Wood', 'Chad C. Walstrom', 'Charles Henry Schoonover', 'Chet Ramey', 'Chris Allegretta', 'Chris Simon', 'Christian Grothoff', 'Christopher Dimech', 'Christopher Gutteridge', 'Claude Simon', 'Claudio Fontana', 'Craig Schock', 'Dale Mellor', 'Daniel Bump', 'Daniel Valentine', 'Darshit Shah', 'Dave Crossland', 'David C. Niemi', 'David Edelsohn', 'David MacKenzie', 'David R. Hill', 'David Pirotte', 'David Sugar', 'David Thompson', 'Debarshi Ray', 'Dennis Clarke', 'Denver Gingerich', 'David E. Evans', 'DJ Delorie', 'Emmanuel Medernach', 'Eric Blake ', 'Eric P. Hutchins', 'Eric S. Raymond', 'Eric A. Schulman ', 'Evgeny Grin', 'Filippo Rusconi', 'Francesco Portorti', 'Franco Iacomella', 'Frank de Lange', 'Franklin R. Jones', 'Georg C. F. Greve', 'Gerald Pfeifer', 'Germán Arias', 'Giuseppe Scrivano', 'Gordon Matzigkeit', 'Graham Percival', 'Gregory Casamento', 'Guillaume Morin', 'Han-Wen Nienhuys', 'Henning Köster', 'Henrik Abelsson', 'Henrik Sandklef', 'Hilaire L. S. Fernandes', 'Hugo Gayosso', 'Ian Dunn', 'Ian Lance Taylor', 'Ian Murdock', 'Igor Támara Patiño', 'IIDA Yosiaki', 'J. Abelardo Gutierrez', 'James Craig Burley', 'James Youngman', 'Jan Nieuwenhuizen', 'Jason Kitcat', 'Jason M. Felice', 'Jeff Binder', 'Jeremiah Benham', 'Jim Lowe', 'Jim Meyering', 'Joel E. Denny', 'Joel N. Weber II', 'Johan Vromas', 'John Catherino', 'John Collins', 'John Sullivan', 'John W. Eaton', 'Jonas Öberg', 'Joris van der Hoeven', 'Jose Antonio Ortega Ruiz', 'Jose E. Marchesi', 'Jose M. Moya', 'Juan A. Añel', 'Juan Bidini', 'Jürgen Sauermann', 'Justin Baugh', 'Karl Berry', 'Karl Heuer', 'Kathryn Ann Hargreaves', 'Kresten Krab Thorup', 'Klaus Treichel ', 'Krishna Padmasola', 'Lars Brinkhoff', 'Lars Magne Ingebrigtsen', 'Laurence Finston', 'Leonard Manzara', 'Les Kopari', 'Lezz Giles', 'Lisa M. Opus Goldstein', 'Loic Dachary', 'Lorenzo Bettini', 'L. Peter Deutsch', 'Luca Saiu', 'Luis Falcon', 'Marcos Serrou do Amaral', 'Marc Tardif', 'Marek Aaron Sapota', 'Mark Adler', 'Mark H. Weaver', 'Markus Steinborn', 'Martin Schanzenbach', 'Masayuki Hatta', 'Mats Lidell', 'Matt Lee', 'Matt Tytel', 'Maurizio Boriani', 'Maxim Cournoyer', 'Melissa Weisshaus', 'Michael Haardt', 'Micah Cowan', 'Michael Opdenacker', 'Mikael Djurfeldt', 'Mike Gerwitz', 'Mike Vanier', 'Miquel Puigpelat', 'Mohammed Isam', 'Mu Lei', 'Musawir Ali', 'Nagarjuna G', 'Nathan Nichols', 'Nazim Djafar', 'Nikos Mavroyanopoulos', 'Noah Friedman', 'Nils Gey', 'Ole Tange', 'Ovidiu Predescu', 'Paolo Bonzini', 'Paul Eggert', 'Paul D. Smith', 'Paul Goins', 'Pádraig Brady', 'Peter Gerwinski', 'Peter Miller', 'Peter Wainwright', 'Petra Millarova', 'Phillip Rulon', 'Phil Maker', 'Phil Nelson', 'Prof. Masayuki Ida', 'Raif S. Naffah', 'Rajesh Vaidheeswarran', 'Ralf S. Engelschall', 'Raman', 'Reinhard Müller', 'Remco Bras', 'Reuben Thomas', 'Ricardo Wurmus', 'Richard Shann', 'Richard Stallman', 'Robert J. Chassell', 'Rob Savoye', 'Roel Janssen', 'Roland McGrath', 'Roland Stigge', 'Sadrul Habib Chowdhury', 'Sam Steingold', 'Sandra Loosemore', 'Sebastian Wieseler', 'Sergey Poznyakoff', 'Shigio Yamguchi', 'Simon Josefsson', 'Stein Krogdahl', 'Stephen F. Booth', 'Stephen H. Dawson', 'Steve Kemp', 'Steven M. Rubin', 'Steve Oualline', 'Steve White', 'Susan Bassein', 'Sverre Hvammen Johansen', 'Sylvain Beucler', 'Terje Mjøs', 'Thomas Bushnell, BSG', 'Tim Retout', 'Tom Cato Amundsen', 'Werner Koch', 'W. G. Krebs', 'William M. Perry', 'Wojciech Polak', 'Yann Dirson', 'Yngve Svendsen', 'Yoni Rabkin', 'Zak Greant']

result=""
dm = []

males = 0
females = 0
unknows = 0

males_list = []
females_list = []
unknows_list = []

for k in gnulist:
    vector = k.split()
    firstname = vector[0]
    if (len(firstname) == 1):
        unknows = unknows + 1                
    else:
        sex = g.guess(firstname, binary=False, dataset='us')
        if (sex == "male"):
            males = males + 1
            males_list.append(k)
        elif (sex == "female"):
            females = females + 1
            females_list.append(k)            
        else:
            unknows = unknows + 1
            unknows_list.append(k)
            
# print("gnu males: %s" % males)
# print("gnu females: %s" % females)
# print("unknow gender about gnu people: %s" % unknowns)

print("The list has been retrieved from https://www.gnu.org/people/people.html")

print("The number of gnu males is %s" % str(len(males_list)))
if ((args.show=='males') or (args.show=='all')):
    print("The list of gnu males is:")
    print(males_list)
    
print("The number of gnu females is %s" % str(len(females_list)))
if ((args.show=='females') or (args.show=='all')):
    print("The list of gnu females is:")
    print(females_list)
    
print("The number of people with unknown gender in GNU is %s" % str(len(unknows_list)))    
if ((args.show=='unknowns') or (args.show=='all')):
    print("The list of GNU people with unknown gender is:")
    print(unknows_list)

import matplotlib.pyplot as plt

data = [len(males_list), len(females_list), len(unknows_list)]
gender = ["Males","Females","Unknows"]
plt.title("GNU people grouped by gender")
plt.pie(data, labels=gender, autopct="%0.1f %%")
plt.axis("equal")
plt.savefig('files/images/gnu_by_gender.png')
plt.show()
