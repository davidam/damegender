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

# Tell me about DAMe Gender papers 

-   [Damegender:Writing and Comparing Gender Detection Tools (CEUR)](http://ceur-ws.org/Vol-2754/paper3.pdf)
-   [Damegender: Towards an International and Free Dataset about Name, Gender and Frequency](https://easychair.org/publications/preprint/q911)

# Websites

-   [Damegender](https://damegender.davidam.com)
-   [Damegender pypi](https://pypi.org/project/damegender/)

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
    $ pip3 install damegender[all]
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

## 2021

-   Jornadas Online "Género y Ciencia de Datos en Deporte y Salud"
    (UOC, 2021) <https://www.youtube.com/watch?v=hBDOf5qlcek&t=8903s>

-   VI Congreso Internacional de Jóvenes Investigadores con Perspectiva
    de Género (Mesa 17 Tecnología y Género) (UC3M, 2021)
    <https://eventos.uc3m.es/65927/programme/vi-congreso-internacional-de-jovenes-investigadorxs-con-perspectiva-de-genero.html>

-   Tecnologías I+D+I para la Igualdad (Mesas de Comunicaciones) (UC3M, 2021)
    <https://eventos.uc3m.es/63471/programme/tecnologias-idi-para-la-igualdad-soluciones-perspectivas-y-retos.html>


## 2020

-   Seminar Series on Advanced Techniques & Tools for Software
    Evolution. (Eindhoven University of Technology, 2020) <http://sattose.org/2020>

-   EsLibre (URJC, 2020) (<https://propuestas.eslib.re/2020/charlas/damegender>)


## 2019

-   Fifth Madrilenian Seminar on Software Research (URJC, 2019)
    (<https://gregoriorobles.github.io/MadSESE/201906.html>)

-   Procesamiento de Lenguaje Natural con Python NLTK, Damegender como
    caso de uso. (Medialab Madrid, 2019)
    (<https://www.medialab-matadero.es/actividades/procesamiento-de-lenguaje-natural-con-python-nltk>)

-   Software Freedom Day (URJC, 2019)
    (<https://tv.urjc.es/video/5d895319d68b148f7a8c0da6>)

-   Open South Code (Málaga, 2019)
    (<https://www.opensouthcode.org/conferences/opensouthcode2019/program/proposals/183>)

-   Group Retreat 2019 Workshop (URJC, 2019)

-   PyBCN - Damegender: gender detection with NLTK and Scikit
    (Barcelona, 2019) (<https://www.youtube.com/watch?v=dvN0lMgQ9Pc>)

# Beautiful Snakes

![img](https://raw.githubusercontent.com/davidam/damegender/master/src/damegender/files/images/violet-snake3.png)

# Dame Music

[Listen music](https://www.youtube.com/playlist?list=PLeobXV-Yyn-IgIRxmEyJxaFstJ02ebtRH)

# License

Copyright (C) 2019 David Arroyo Menéndez
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in [GNU Free Documentation License](https://www.gnu.org/copyleft/fdl.html).

[![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/GFDL_Logo.svg/200px-GFDL_Logo.svg.png)](https://www.gnu.org/copyleft/fdl.html)