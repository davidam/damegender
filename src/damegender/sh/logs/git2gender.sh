#!/bin/sh

#  Copyright (C) 2023 David Arroyo Menendez

#  Author: David Arroyo Menendez <davidam@gmail.com>
#  Maintainer: David Arroyo Menendez <davidam@gmail.com>
#  This file is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3, or (at your option)
#  any later version.
# 
#  This file is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with DameGender; see the file LICENSE.  If not, write to
#  the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor, 
#  Boston, MA 02110-1301 USA,

cd ../..
python3 git2gender.py https://github.com/ruby/ruby --directory="tmp/cloneruby" --country="inter" --show=all --verbose > files/logs/git2gender_ruby-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/python/cpython --country='inter' --directory="tmp/clonecpython" --show=all --verbose > files/logs/git2genderpython-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/Perl/perl5 --country='inter' --directory="tmp/cloneperl" --show=all --verbose > files/logs/git2genderperl-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/tcltk/tcl --country='inter' --directory="tmp/clonetcl" --show=all --verbose > files/logs/git2gendertcl-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://git.savannah.gnu.org/git/bash.git --country='inter' --directory="tmp/clonebash" --show=all --verbose > files/logs/git2genderbash-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://gcc.gnu.org/git/gcc.git --country='inter' --directory="tmp/clonegcc" --show=all --verbose > files/logs/git2gendergcc-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/r-devel/r-svn --country="inter" --directory="tmp/cloner" --show=all --verbose > files/logs/git2gender-r-devel-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py git://git.sv.gnu.org/emacs.git --country="inter" --directory="/tmp/emacs" --show=all --verbose > files/logs/git2gender-emacs-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/tc39/ecma262 --country="inter" --directory="/tmp/ecma262" --show=all --verbose > files/logs/ecma262-$(date "+%Y-%m-%d-%H").txt
python3 git2gender.py https://github.com/php/php-src.git --directory="/tmp/clonephp" --country="inter" --show=all --verbose > files/logs/git2gender_php-$(date "+%Y-%m-%d-%H").txt
