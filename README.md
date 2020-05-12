<div id="table-of-contents">
<h2>Table of Contents</h2>
<div id="text-table-of-contents">
<ul>
<li><a href="#sec-1">1. Logo</a></li>
<li><a href="#sec-2">2. Name</a></li>
<li><a href="#sec-3">3. Why?</a></li>
<li><a href="#sec-4">4. Tell me about DAMe Gender on Video</a></li>
<li><a href="#sec-5">5. Install</a>
<ul>
<li><a href="#sec-5-1">5.1. Installing Software</a>
<ul>
<li><a href="#sec-5-1-1">5.1.1. Possible Debian/Ubuntu dependencies</a></li>
<li><a href="#sec-5-1-2">5.1.2. From sources</a></li>
<li><a href="#sec-5-1-3">5.1.3. With python package</a></li>
</ul>
</li>
<li><a href="#sec-5-2">5.2. Obtaining an api key</a></li>
<li><a href="#sec-5-3">5.3. Configuring nltk</a></li>
</ul>
</li>
<li><a href="#sec-6">6. Speeches, Seminars, Expressions of Support</a></li>
<li><a href="#sec-7">7. Beautiful Snakes</a></li>
<li><a href="#sec-8">8. Dame Music</a></li>
<li><a href="#sec-9">9. License</a></li>
</ul>
</div>
</div>

# Logo<a id="sec-1" name="sec-1"></a>

![img](https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/CaravaggioDavidGoliathVienna.jpg/620px-CaravaggioDavidGoliathVienna.jpg)

# Name<a id="sec-2" name="sec-2"></a>

damegender is a gender detection tool from the name coded by David Arroyo MEnéndez (DAME)

# Why?<a id="sec-3" name="sec-3"></a>

-   If you want determine gender gap in free software projects or mailing lists.
-   If you don't know the gender about a name
-   If you want research with statistics about why a name is related with males or females.
-   If you want use a free gender detection tool from a name from a command with
    open data.
-   If you want use the main solutions in gender detection (genderize,
    genderapi, namsor, nameapi and gender guesser) from a command.

DAMe Gender is for you!

# Tell me about DAMe Gender on Video<a id="sec-4" name="sec-4"></a>

-   [Python Barcelona (Spanish)](https://www.youtube.com/embed/dvN0lMgQ9Pc)
-   [Damegender in Software Freedom Day (Spanish)](https://tv.urjc.es/iframe/5d895319d68b148f7a8c0da6)
-   [Damegender in URJC (English)](https://tv.urjc.es/video/5d895319d68b148f7a8c0da6)

# Install<a id="sec-5" name="sec-5"></a>

## Installing Software<a id="sec-5-1" name="sec-5-1"></a>

### Possible Debian/Ubuntu dependencies<a id="sec-5-1-1" name="sec-5-1-1"></a>

    $ sudo apt-get install python3-nose-exclude python3-dev dict dict-freedict-eng-spa dict-freedict-spa-eng dictd

### From sources<a id="sec-5-1-2" name="sec-5-1-2"></a>

    $ git clone https://github.com/davidam/damegender
    $ cd damegender
    $ pip3 install -r requirements.txt

### With python package<a id="sec-5-1-3" name="sec-5-1-3"></a>

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

## Obtaining an api key<a id="sec-5-2" name="sec-5-2"></a>

Currently you can need an api key from:
-   <https://store.genderize.io/documentation>
-   <https://gender-api.com>
-   <https://www.nameapi.org/>
-   <https://v2.namsor.com/NamSorAPIv2/sign-in.html>

You can execute:

    $ python3 apikeyadd.py

To configure your api key

## Configuring nltk<a id="sec-5-3" name="sec-5-3"></a>

    $ python3
    >>> import nltk
    >>> nltk.download('names')

# Speeches, Seminars, Expressions of Support<a id="sec-6" name="sec-6"></a>

-   [MadSeSe](http://gregoriorobles.github.io/MadSESE/201906.html)
-   [Python Barcelona](https://www.meetup.com/es-ES/python-185/events/261405719/)
-   [Taller de Periodismo de Datos (Medialab Prado, Madrid). NLTK & Damegender](https://www.medialab-prado.es/noticias/taller-de-periodismo-de-datos-2019-sesiones-formativas)
-   [Software Freedom Day (URJC, Móstoles). Damegender](https://tv.urjc.es/video/5d895319d68b148f7a8c0da6)

# Beautiful Snakes<a id="sec-7" name="sec-7"></a>

![img](https://raw.githubusercontent.com/davidam/damegender/master/src/damegender/files/images/violet-snake3.png)

# Dame Music<a id="sec-8" name="sec-8"></a>

[Listen music &#x2026;](https://www.youtube.com/playlist?list=PLeobXV-Yyn-LvQydcnr46ZkGh1V6tDGEk)

# License<a id="sec-9" name="sec-9"></a>

Copyright (C) 2019 David Arroyo Menéndez
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in [GNU Free Documentation License](https://www.gnu.org/copyleft/fdl.html).

[![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/GFDL_Logo.svg/200px-GFDL_Logo.svg.png)](https://www.gnu.org/copyleft/fdl.html)