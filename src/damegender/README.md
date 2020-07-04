# Name

damegender is a gender detection tool from the name coded by David Arroyo MEnéndez (DAME)

# Why?

- If you want determine gender gap in free software projects or mailing lists.
- If you don't know the gender about a name
- If you want research with statistics about why a name is related with males or females.
- If you want use a free gender detection tool from a name from a command with
  open data.
- If you want use the main solutions in gender detection (genderize,
  genderapi, namsor, nameapi and gender guesser) from a command.

DAMe Gender is for you!

# Tell me about DAMe Gender on Video

-   [Python Barcelona (Spanish)](https://www.youtube.com/embed/dvN0lMgQ9Pc)
-   [Damegender in Software Freedom Day (Spanish)](https://tv.urjc.es/iframe/5d895319d68b148f7a8c0da6)
-   [Damegender in URJC (English)](https://tv.urjc.es/video/5d895319d68b148f7a8c0da6)

# Install

## Installing Software

### Possible Debian/Ubuntu dependencies

    $ sudo apt-get install python3-nose-exclude python3-dev dict dict-freedict-eng-spa dict-freedict-spa-eng dictd

### From sources

    $ git clone https://github.com/davidam/damegender
    $ cd damegender
    $ pip3 install -r requirements.txt

### With python package

    $ python3 -m venv /tmp/d
    $ cd /tmp/d
    $ source bin/activate
    $ pip install --upgrade pip
    $ pip3 install damegender
    $ cd lib/python3.5/site-packages/damegender
    $ python3 main.py David

To install apis extra dependencies:

    $ pip3 install damegender[apis]

To install mailing lists and repositories extra dependencies:

    $ pip3 install damegender[mails_and_repositories]

To install all possible dependencies

    $ pip3 install damegender[all]

## Obtaining an api key

Currently you can need an api key from:
-   <https://store.genderize.io/documentation>
-   <https://gender-api.com>
-   <https://www.nameapi.org/>
-   <https://v2.namsor.com/NamSorAPIv2/sign-in.html>

You can execute:

    $ python3 apikeyadd.py

To configure your api key

## Configuring nltk

    $ python3
    >>> import nltk
    >>> nltk.download('names')

# Speeches, Seminars, Expressions of Support

-   [MadSeSe](http://gregoriorobles.github.io/MadSESE/201906.html)
-   [Python Barcelona](https://www.meetup.com/es-ES/python-185/events/261405719/)
-   [Taller de Periodismo de Datos (Medialab Prado, Madrid). NLTK & Damegender](https://www.medialab-prado.es/noticias/taller-de-periodismo-de-datos-2019-sesiones-formativas)
-   [Software Freedom Day (URJC, Móstoles). Damegender](https://tv.urjc.es/video/5d895319d68b148f7a8c0da6)

# Beautiful Snakes

![img](https://raw.githubusercontent.com/davidam/damegender/master/src/damegender/files/images/violet-snake3.png)

# Dame Music

[Listen music &#x2026;](https://www.youtube.com/playlist?list=PLeobXV-Yyn-LvQydcnr46ZkGh1V6tDGEk)

# License

Copyright (C) 2019 David Arroyo Menéndez
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in [GNU Free Documentation License](https://www.gnu.org/copyleft/fdl.html).

[![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/GFDL_Logo.svg/200px-GFDL_Logo.svg.png)](https://www.gnu.org/copyleft/fdl.html)