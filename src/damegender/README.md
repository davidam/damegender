
# Table of Contents

1.  [Logo](#org5dc9778)
2.  [Name](#orga02e621)
3.  [Why?](#orgb4337c6)
4.  [Tell me about DAMe Gender on Youtube](#org580eb02)
5.  [Install](#org49eac8d)
    1.  [Docker Image](#org6ad3f45)
    2.  [Installing Software](#orgb908e7d)
        1.  [Possible Debian/Ubuntu dependencies](#orga51cbd2)
        2.  [From sources](#orga956618)
        3.  [With python package](#orge6fba01)
    3.  [Obtaining an api key](#orga2af7da)
    4.  [Configuring nltk](#org970e67a)
6.  [Check test](#org862f5af)
    1.  [All unit tests](#org9bb857a)
        1.  [Using Docker image](#org60cf798)
    2.  [Single unit test](#orgc9bb15e)
        1.  [Using Docker image](#org62594c1)
    3.  [Tests from commands](#orga5513b6)
7.  [Execute program](#orge828861)
8.  [Benchmarking](#orgca16723)
    1.  [Market Study](#orgf55f944)
    2.  [Accuracy](#orgb6c60b6)
    3.  [Accuracy (Damegender ML)](#org0bff294)
    4.  [Confusion Matrix](#org07a2c75)
    5.  [Errors with files/names/all.csv has:](#org12fc7f0)
    6.  [Performance](#org56aaef7)
9.  [Statistics for damegender](#org79b212f)
    1.  [Measuring success and fails](#org8c8cf96)
    2.  [PCA](#orgfb83d99)
        1.  [Concepts](#orge1790bb)
        2.  [Choosing components](#orgb5231b5)
        3.  [Load Dataset](#orgc3decdd)
        4.  [Standarize the data](#orgfa130da)
        5.  [Pca Projection to N Dimensions](#org6caf71c)
        6.  [Analyze components to determine gender in names](#orgd2268fe)
10. [Speeches, Seminars, Expressions of Support](#org0b03af4)
11. [Beautiful Snakes](#org6c584e3)
12. [Dame Music](#org64c405a)
13. [License](#org23c90b4)


<a id="org5dc9778"></a>

# Logo

![img](src/damegender/files/images/CaravaggioDavidGoliathVienna.jpg)


<a id="orga02e621"></a>

# Name

damegender is a gender detection tool from the name coded by David Arroyo MEnéndez (DAME)


<a id="orgb4337c6"></a>

# Why?

-   If you want determine gender gap in free software projects or mailing lists.
-   If you don't know the gender about a name
-   If you want research with statistics about why a name is related with males or females.
-   If you want use a free gender detection tool from a name from a command with
    open data.
-   If you want use the main solutions in gender detection (genderize,
    genderapi, namsor, nameapi and gender guesser) from a command.

DAMe Gender is for you!


<a id="org580eb02"></a>

# Tell me about DAMe Gender on Youtube

[![img](src/damegender/files/images/damegender-front-youtube.png)](https://www.youtube.com/embed/dvN0lMgQ9Pc)


<a id="org49eac8d"></a>

# Install


<a id="org6ad3f45"></a>

## Docker Image

    # Build the container image
    $ docker build . -t damegender/damegender:latest
    
    # Run the container
    $ docker run -ti damegender/damegender:latest main.py David


<a id="orgb908e7d"></a>

## Installing Software


<a id="orga51cbd2"></a>

### Possible Debian/Ubuntu dependencies

    $ sudo apt-get install python3-nose-exclude python3-dev dict dict-freedict-eng-spa dict-freedict-spa-eng dictd


<a id="orga956618"></a>

### From sources

    $ git clone https://github.com/davidam/damegender
    $ cd damegender
    $ pip3 install -r requirements.txt


<a id="orge6fba01"></a>

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


<a id="orga2af7da"></a>

## Obtaining an api key

Currently you can need an api key from:

-   <https://store.genderize.io/documentation>
-   <https://gender-api.com>
-   <https://www.nameapi.org/>
-   <https://v2.namsor.com/NamSorAPIv2/sign-in.html>

You can execute:

    $ python3 apikeyadd.py

To configure your api key


<a id="org970e67a"></a>

## Configuring nltk

    $ python3
    >>> import nltk
    >>> nltk.download('names')


<a id="org862f5af"></a>

# Check test


<a id="org9bb857a"></a>

## All unit tests

    $ nosetest3 test


<a id="org60cf798"></a>

### Using Docker image

    $ docker run -ti --entrypoint nosetests damegender/damegender:latest test


<a id="orgc9bb15e"></a>

## Single unit test

    $ nosetests3 test/test_dame_sexmachine.py:TddInPythonExample.test_string2array_method_returns_correct_result


<a id="org62594c1"></a>

### Using Docker image

    $ docker run -ti --entrypoint nosetests damegender/damegender:latest test/test_dame_sexmachine.py:TddInPythonExample.test_string2array_method_returns_correct_result


<a id="orga5513b6"></a>

## Tests from commands

    $ cd src/damegender
    $ ./testsbycommands.sh         # It must run for you
    $ ./testsbycommandsextralocal.sh    # You will need all dependencies with: $ pip3 install damegender[all]
    $ ./testsbycommandsextranet.sh    # You will need api keys


<a id="orge828861"></a>

# Execute program

    # Detect gender from a name (INE is the dataset used by default)
    $ python3 main.py David
    David gender is male
     363559  males for David from INE.es
    0 females for David from INE.es
    
    # Detect gender from a name only using machine learning (experimental way)
    $ python3 main.py Mesa --ml=nltk
    Mesa gender is female
    0 males for Mesa from INE.es
    0 females for Mesa from INE.es
    
    # Detect gender from a name (all census and machine learning)
    $ python3 main.py David --verbose
    365196 males for David from INE.es
    0 females for David from INE.es
    1193 males for David from Uruguay census
    5 females for David from Uruguay census
    26645 males for David from United Kingdom census
    0 females for David from United Kingdom census
    3552580 males for David from United States of America census
    12826 females for David from United States of America census
    David gender predicted with nltk is male
    David gender predicted with sgd is male
    David gender predicted with svc is male
    David gender predicted with gaussianNB is male
    David gender predicted with multinomialNB is male
    David gender predicted with bernoulliNB is male
    David gender predicted with forest is male
    David gender predicted with tree is male
    David gender predicted with mlp is male
    
    # Find your name in different countries
    $ python3 nameincountries.py David
    grep -i " David " files/names/nam_dict.txt > files/grep.tmp
    males: ['Albania', 'Armenia', 'Austria', 'Azerbaijan', 'Belgium', 'Bosnia and Herzegovina', 'Czech Republic', 'Denmark', 'East Frisia', 'France', 'Georgia', 'Germany', 'Great Britain', 'Iceland', 'Ireland', 'Israel', 'Italy', 'Kazakhstan/Uzbekistan', 'Luxembourg', 'Malta', 'Norway', 'Portugal', 'Romania', 'Slovenia', 'Spain', 'Sweden', 'Swiss', 'The Netherlands', 'USA', 'Ukraine']
    females: []
    both: []
    
    # Count gender from a git repository
    $ python3 git2gender.py https://github.com/chaoss/grimoirelab-perceval.git --directory="/tmp/clonedir"
    The number of males sending commits is 15
    The number of females sending commits is 7
    
    # Count gender from a mailing list
    $ cd files/mbox
    $ wget -c http://mail-archives.apache.org/mod_mbox/httpd-announce/201706.mbox
    $ cd ..
    $ python3 mail2gender.py http://mail-archives.apache.org/mod_mbox/httpd-announce/
    
    # Use an api to detect the gender
    $ python3 api2gender.py Leticia --surname="Martin" --api=namsor
    female
    scale: 0.99
    
    # Google popularity for a name
    $ python3 gendergoogle.py Leticia
    Google results of Leticia as male: 42300
    Google results of Leticia as female: 63400
    
    # Give me informative features
    $ python3 infofeatures.py
    Females with last letter a: 0.4705246078961601
    Males with last letter a: 0.048672566371681415
    Females with last letter consonant: 0.2735841767750908
    Males with last letter consonant: 0.6355328972681801
    Females with last letter vocal: 0.7262612995441552
    Males with last letter vocal: 0.3640823393612928
    
    # Download results from an api and save in a file
    $ python3 downloadjson --csv=files/names/min.csv --api=genderize
    $ cat files/names/genderizefiles_names_min.csv.json
    
    # To measure success
    $ python3 accuracy.py --csv=files/names/min.csv
    ################### NLTK!!
    Gender list: [1, 1, 1, 1, 2, 1, 0, 0]
    Guess list:  [1, 1, 1, 1, 0, 1, 0, 0]
    Dame Gender accuracy: 0.875
    
    $ python3 accuracy.py --api="genderize" --csv=files/names/min.csv
    ################### Genderize!!
    Gender list: [1, 1, 1, 1, 2, 1, 0, 0]
    Guess list:  [1, 1, 1, 1, 2, 1, 0, 0]
    Genderize accuracy: 1
    
    $ python3 confusion.py --csv="files/names/partial.csv" --api=nameapi --jsondownloaded="files/names/nameapifiles_names_partial.csv.json"
    A confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i but predicted to be in group j.
    If the classifier is nice, the diagonal is high because there are true positives
    Nameapi confusion matrix:
    
    [[ 3, 0, 0]
     [ 0, 15, 1]]
    
    
    # To analyze errors guessing names from a csv
    $ python3 errors.py --csv="files/names/all.csv" --api="genderguesser"
    Gender Guesser with files/names/all.csv has:
    + The error code: 0.22564457518601835
    + The error code without na: 0.026539047204698716
    + The na coded: 0.20453365634192766
    + The error gender bias: 0.0026103980857080703
    
    # To deploy a graph about correlation between variables
    $ python3 corr.py
    $ python3 corr.py --csv="categorical"
    $ python3 corr.py --csv="nocategorical"
    # To create files from scripts. Example: the pickle models, or csv processed from original files.
    $ python3 postinstall.py
    # Experiments to determine features with weight (not finished)
    $ python3 pca-components.py --csv="files/features_list.csv" # To determine number of components
    $ python3 pca-features.py                                   # To understand the weight between variables for a target
    
    # Counting surnames
    $ python3 surname.py Gil --total=es
    There are 140004 people using Gil in Spain
    
    $ python3 surname.py Lenon --total=us
    There are 837 people using Lenon in United States of America
    
    # Measuring Ethnicity of surnames
    $ python3 ethnicity.py Smith
    In United States of America the percentages about the race of Smith surname is:
    White: 73.35
    Black: 22.22
    Hispanic: 1.56
    Asian Pacific Indian American: 0.40
    American Indian and Alaska Native: 0.85
    Various races: 1.63


<a id="orgca16723"></a>

# Benchmarking


<a id="orgf55f944"></a>

## Market Study

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<tbody>
<tr>
<td class="org-left">&#xa0;</td>
<td class="org-left">Gender API</td>
<td class="org-left">gender-guesser</td>
<td class="org-left">genderize.io</td>
<td class="org-left">NameAPI</td>
<td class="org-left">NamSor</td>
<td class="org-left">damegender</td>
</tr>


<tr>
<td class="org-left">Database size</td>
<td class="org-left">431322102</td>
<td class="org-left">45376</td>
<td class="org-left">114541298</td>
<td class="org-left">1428345</td>
<td class="org-left">4407502834</td>
<td class="org-left">57282</td>
</tr>


<tr>
<td class="org-left">Regular data updates</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes, developing</td>
</tr>


<tr>
<td class="org-left">Handles unstructured full name strings</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">Handles surnames</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">Handles non-Latin alphabets</td>
<td class="org-left">partially</td>
<td class="org-left">no</td>
<td class="org-left">partially</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">Implicit geo-localization</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
</tr>


<tr>
<td class="org-left">Exists locale</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">Assingment type</td>
<td class="org-left">probilistic</td>
<td class="org-left">binary</td>
<td class="org-left">probabilistic</td>
<td class="org-left">probabilistic</td>
<td class="org-left">probabilistic</td>
<td class="org-left">probabilistic</td>
</tr>


<tr>
<td class="org-left">Free parameters</td>
<td class="org-left">total<sub>names</sub>, probability</td>
<td class="org-left">gender</td>
<td class="org-left">probability, count</td>
<td class="org-left">confidence</td>
<td class="org-left">scale</td>
<td class="org-left">total<sub>names</sub>, count</td>
</tr>


<tr>
<td class="org-left">Prediction</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">Free license</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
</tr>


<tr>
<td class="org-left">API</td>
<td class="org-left">yes</td>
<td class="org-left">no</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">future</td>
</tr>


<tr>
<td class="org-left">free requests limited</td>
<td class="org-left">yes (200)</td>
<td class="org-left">unlimited</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">yes</td>
<td class="org-left">unlimited</td>
</tr>
</tbody>
</table>

(Checked: 2019/06/27)


<a id="orgb6c60b6"></a>

## Accuracy

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Name</td>
<td class="org-right">Accuracy</td>
<td class="org-right">Precision</td>
<td class="org-right">F1score</td>
<td class="org-right">Recall</td>
</tr>


<tr>
<td class="org-left">Genderapi</td>
<td class="org-right">0.9687686966482124</td>
<td class="org-right">0.9717050018254838</td>
<td class="org-right">0.9637877964874163</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Genderize</td>
<td class="org-right">0.926775</td>
<td class="org-right">0.9761303240374678</td>
<td class="org-right">0.9655113956503119</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Namsor</td>
<td class="org-right">0.8672551055728626</td>
<td class="org-right">0.9730097087378641</td>
<td class="org-right">0.9236866359447006</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Nameapi</td>
<td class="org-right">0.8301886792452831</td>
<td class="org-right">0.97420272191753</td>
<td class="org-right">0.9054181612233341</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Gender Guesser</td>
<td class="org-right">0.7743554248139817</td>
<td class="org-right">0.9848151408450704</td>
<td class="org-right">0.8715900233826968</td>
<td class="org-right">1.0</td>
</tr>
</tbody>
</table>

(Checked: 2019/10 until 2019/12)

These accuracies has been measured thinking in Lucía Santamaría and
Helena Mihaljevic dataset as base of truth.


<a id="org0bff294"></a>

## Accuracy (Damegender ML)

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<tbody>
<tr>
<td class="org-left">Name</td>
<td class="org-right">Accuracy</td>
<td class="org-right">Precision</td>
<td class="org-right">F1score</td>
<td class="org-right">Recall</td>
</tr>


<tr>
<td class="org-left">SVC</td>
<td class="org-right">0.879</td>
<td class="org-right">0.972</td>
<td class="org-right">0.972</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Random Forest</td>
<td class="org-right">0.862</td>
<td class="org-right">0.902</td>
<td class="org-right">0.902</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">NLTK (Bayes)</td>
<td class="org-right">0.862</td>
<td class="org-right">0.902</td>
<td class="org-right">0.902</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">MultinomialNB</td>
<td class="org-right">0.782</td>
<td class="org-right">0.791</td>
<td class="org-right">0.791</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">Tree</td>
<td class="org-right">0.764</td>
<td class="org-right">0.821</td>
<td class="org-right">0.796</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">SGD</td>
<td class="org-right">0.709</td>
<td class="org-right">0.943</td>
<td class="org-right">0.815</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">GaussianNB</td>
<td class="org-right">0.709</td>
<td class="org-right">0.968</td>
<td class="org-right">0.887</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">BernoulliNB</td>
<td class="org-right">0.699</td>
<td class="org-right">0.965</td>
<td class="org-right">0.816</td>
<td class="org-right">1.0</td>
</tr>


<tr>
<td class="org-left">MLP</td>
<td class="org-right">0.677</td>
<td class="org-right">0.819</td>
<td class="org-right">0.755</td>
<td class="org-right">1.0</td>
</tr>

<tbody>
<tr>
</tr>
</tbody>
</table>

In Damegender we are using the next datasets:

-   INE.es (Spain)
-   USA
-   United Kingdom
-   Uruguay

We hope better results with more languages.

Machine Learning Algorithms in DameGender
These results are experimental, we are improving the choosing of features.


<a id="org07a2c75"></a>

## Confusion Matrix

1.  GenderApi

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefined</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">3589</td>
    <td class="org-right">155</td>
    <td class="org-right">67</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">211</td>
    <td class="org-right">1734</td>
    <td class="org-right">23</td>
    </tr>
    </tbody>
    </table>

2.  Genderguesser

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefided</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">3326</td>
    <td class="org-right">139</td>
    <td class="org-right">346</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">78</td>
    <td class="org-right">1686</td>
    <td class="org-right">204</td>
    </tr>
    </tbody>
    </table>

3.  Genderize

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefined</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">3157</td>
    <td class="org-right">242</td>
    <td class="org-right">412</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">75</td>
    <td class="org-right">1742</td>
    <td class="org-right">151</td>
    </tr>
    </tbody>
    </table>

4.  Namsor

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefined</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">3325</td>
    <td class="org-right">139</td>
    <td class="org-right">346</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">78</td>
    <td class="org-right">1686</td>
    <td class="org-right">204</td>
    </tr>
    </tbody>
    </table>

5.  Nameapi

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefined</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">2627</td>
    <td class="org-right">674</td>
    <td class="org-right">507</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">667</td>
    <td class="org-right">1061</td>
    <td class="org-right">240</td>
    </tr>
    </tbody>
    </table>

6.  Dame Gender

    <table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">
    
    
    <colgroup>
    <col  class="org-left" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    
    <col  class="org-right" />
    </colgroup>
    <tbody>
    <tr>
    <td class="org-left">&#x2026;</td>
    <td class="org-right">male</td>
    <td class="org-right">female</td>
    <td class="org-right">undefined</td>
    </tr>
    
    
    <tr>
    <td class="org-left">male</td>
    <td class="org-right">3033</td>
    <td class="org-right">778</td>
    <td class="org-right">0</td>
    </tr>
    
    
    <tr>
    <td class="org-left">female</td>
    <td class="org-right">276</td>
    <td class="org-right">1692</td>
    <td class="org-right">0</td>
    </tr>
    </tbody>
    </table>
    
    In this version of Dame Gender, we are not considering decide names as
    undefined.


<a id="org12fc7f0"></a>

## Errors with files/names/all.csv has:

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<tbody>
<tr>
<td class="org-left">API</td>
<td class="org-right">error code</td>
<td class="org-right">error code without na</td>
<td class="org-right">na coded</td>
<td class="org-right">error gender bias</td>
</tr>


<tr>
<td class="org-left">Genderize</td>
<td class="org-right">0.0727</td>
<td class="org-right">0.053</td>
<td class="org-right">0.02</td>
<td class="org-right">-0.008</td>
</tr>


<tr>
<td class="org-left">Damegender</td>
<td class="org-right">0.2547594323295258</td>
<td class="org-right">0.2547594323295258</td>
<td class="org-right">0.0</td>
<td class="org-right">-0.04949809622706819</td>
</tr>


<tr>
<td class="org-left">GenderApi</td>
<td class="org-right">0.16666666666666666</td>
<td class="org-right">0.16666666666666666</td>
<td class="org-right">0.0</td>
<td class="org-right">-0.16666666666666666</td>
</tr>


<tr>
<td class="org-left">Gender Guesser</td>
<td class="org-right">0.2255105572862582</td>
<td class="org-right">0.026962383126766687</td>
<td class="org-right">0.20404984423676012</td>
<td class="org-right">0.0030441400304414</td>
</tr>


<tr>
<td class="org-left">Namsor</td>
<td class="org-right">0.16666666666666666</td>
<td class="org-right">0.16666666666666666</td>
<td class="org-right">0.0</td>
<td class="org-right">0.16666666666666666</td>
</tr>


<tr>
<td class="org-left">Nameapi</td>
<td class="org-right">0.361</td>
<td class="org-right">0.267</td>
<td class="org-right">0.129</td>
<td class="org-right">0.001</td>
</tr>
</tbody>
</table>


<a id="org56aaef7"></a>

## Performance

These performance metrics requires and csv json downloaded
\################### Damegender!!
Gender list: [1, 1, 1, 1, 1, 0]
Guess list:  [1, 1, 1, 1, 1, 0]
Damegender accuracy: 1.0

real	0m1.270s
user	0m0.876s
sys	0m0.416s
\################### Genderize!!
Gender list: [1, 1, 1, 1, 1, 0]
Guess list:  [1, 1, 1, 1, 1, 0]
Genderize accuracy: 1.0

real	0m0.811s
user	0m0.776s
sys	0m0.312s
\################### Genderapi!!
Gender list: [1, 1, 1, 1, 1, 0]
Guess list:  [1, 1, 1, 1, 1, 0]
Genderapi accuracy: 1.0

real	0m0.763s
user	0m0.744s
sys	0m0.232s
\################### Namsor!!
Gender list: [1, 1, 1, 1, 1, 0]
Guess list:  [1, 1, 1, 1, 1, 0]
Namsor accuracy: 1.0

real	0m0.811s
user	0m0.776s
sys	0m0.356s
\################### Nameapi!!
Gender list: [1, 1, 1, 1, 1, 0]
Guess list:  [1, 1, 1, 1, 1, 0]
Nameapi accuracy: 1.0

real	0m0.832s
user	0m0.816s
sys	0m0.336s
A confusion matrix C is such that Ci,j is equal to the number of observations known to be in group i but predicted to be in group j.
If the classifier is nice, the diagonal is high because there are true positives
Damegender confusion matrix:

[[ 5, 0, 0 ]
 [ 0, 1, 0 ]]

real	0m0.812s
user	0m0.784s
sys	0m0.300s
Damegender with files/names/partial.csv has:

-   The error code: 0.10526315789473684
-   The error code without na: 0.10526315789473684
-   The na coded: 0.0
-   The error gender bias: 0.0

real	0m9.099s
user	0m9.008s
sys	0m0.412s


<a id="org79b212f"></a>

# Statistics for damegender

Some theory could be useful to understand some commands


<a id="org8c8cf96"></a>

## Measuring success and fails

To guess the sex, we have an true idea (example: female) and we obtain
a result with a method (example: using an api, querying a dataset or
with a machine learning model). The guessed result could be male,
female or perhaps unknown. Remember some definitions about results
about this matter:

**True positive** is find a value guessed as true if the value in
the data source is positive.

**True negative** is find a value guessed as true if the the
value in the data source is negative.

**False positive** is find a value guessed as false if the the
value in the data source is positive.

**False negative** is find a value guessed as false if the the
value in the data source is negative.

So, we can find a vocabulary for measure true, false, success and
errors. We can make a summary in the gender name context about
mathematical concepts:

**Precision** is about true positives divided by true positives plus false
positives

    (femalefemale + malemale ) /
    (femalefemale + malemale + femalemale)

**Recall** is about true positives divided by true positives plus false
negatives.

    (femalefemale + malemale ) /
    (femalefemale + malemale + malefemale + femaleundefined + maleundefined)

**Accuray** is about true positives divided by all.

    (femalefemale + malemale ) /
    (femalefemale + malemale + malefemale + femalemale + femaleundefined + maleundefined)

The **F1 score** is the harmonic mean of precision and recall taking
both metrics into account in the following equation:

    2 * (
    (precision * recall) /
    (precision + recall))

In Damengender, we are using accuracy.py to apply these concepts. Take
a look to practice:

    $ python3 accuracy.py --api="damegender" --measure="f1score" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="damegender" --measure="recall" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="damegender" --measure="precision" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="damegender" --measure="accuracy" --csv="files/names/partialnoundefined.csv"
    
    $ python3 accuracy.py --api="genderguesser" --measure="f1score" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="genderguesser" --measure="recall" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="genderguesser" --measure="precision" --csv="files/names/partialnoundefined.csv"
    $ python3 accuracy.py --api="genderguesser" --measure="accuracy" --csv="files/names/partialnoundefined.csv"

**Error coded** is about the true is different than the guessed:

    (femalemale + malefemale + maleundefined + femaleundefined) /
    (malemale + femalemale + malefemale +
    femalefemale + maleundefined + femaleundefined)

**Error coded without na** is about the true is different than the
guessed, but without undefined results.

    (maleundefined + femaleundefined) /
    (malemale + femalemale + malefemale +
    femalefemale + maleundefined + femaleundefined)

**Error gender bias** is to understand if the error is bigger guessing
males than females or viceversa.

    (malefemale - femalemale) /
    (malemale + femalemale + malefemale + femalefemale)

**The weighted error** is about the true is different than the guessed,
but giving a weight to the guessed as undefined.

    (femalemale + malefemale +
    + w * (maleundefined + femaleundefined)) /
    (malemale + femalemale + malefemale + femalefemale +
    + w * (maleundefined + femaleundefined))

In Damengeder, we have coded errors.py to implement the different definitions in diffrent apis.

The **confusion matrix** creates a matrix about the true and the
guess. If you have this confusion matrix:

    [[ 2, 0, 0]
     [ 0, 5, 0]]

It means, I have 2 females true and I've guessed 2 females and I've 5
males true and I've guessed 5 males. I don't have errors in my
classifier.

    [[ 2  1  0]
    [ 2 14  0]

It means, I have 2 females true and I've guessed 2 females and I've 14
males true and I've guessed 14 males. 1 female was considered male, 2
males was considered female.

In Damegender, we have coded confusion.py to implement this concept
with the different apis.


<a id="orgfb83d99"></a>

## PCA


<a id="orge1790bb"></a>

### Concepts

The dispersion measures between 1 variable, for instance, variance,
standard deviation, &#x2026;

![img](src/damegender/files/images/variance.png)

If you have 2 variables, you can write a formula so similar to variance.

![img](src/damegender/files/images/covariance.png)

If you have 3 variables or more, you can write a covariance matrix.

![img](src/damegender/files/images/matrix-covariance.png)

In essence, an eigenvector v of a linear transformation T is a
non-zero vector that, when T is applied to it, does not change
direction. Applying T to the eigenvector only scales the eigenvector
by the scalar value λ, called an eigenvalue.

![img](src/damegender/files/images/eigenvector.png)

A feature vector is constructed taking the eigenvectors that you want
to keep from the list of eigenvectors.

The new dataset take the transpose of the vector and multiply it on
the left of the original data set, transposed.

    FinalData = RowFeatureVector x RowDataAdjust

We can choose PCA using the covariance method as opposed to the
correlation method.

The [covariance method](https://en.wikipedia.org/wiki/Principal_component_analysis#Computing_PCA_using_the_covariance_method) has the next steps:

1.  Organize the data set
2.  Calculate the empirical mean
3.  Calculate the deviations from the mean
4.  Find the covariance matrix
5.  Find the eigenvectors and eigenvalues of the covariance matrix
6.  Rearrange the eigenvectors and eigenvalues
7.  Compute the cumulative energy content for each eigenvector
8.  Select a subset of the eigenvectors as basis vectors
9.  Project the z-scores of the data onto the new basis

The [correlation method](https://www.itl.nist.gov/div898/handbook/pmc/section5/pmc552.htm) has the next steps:

1.  Compute the correlation matrix
2.  Solve for the correlation roots of R (product of eigenvalues)
3.  Compute the first column of the V matrix
4.  Compute the remaining columns of the V matrix
5.  Compute the L<sup>(1/2)</sup> matrix
6.  Compute the communality
7.  Diagonal elements report how much of the variability is explained
8.  Compute the coefficient matrix
9.  Compute the principal factors


<a id="orgb5231b5"></a>

### Choosing components

We can choose components with:

    import numpy as np
    from sklearn.decomposition import PCA
    from sklearn.preprocessing import MinMaxScaler
    import matplotlib.pyplot as plt
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv')
    args = parser.parse_args()
    
    #filepath = 'files/features_list.csv' #your path here
    data = np.genfromtxt(args.csv, delimiter=',', dtype='float64')
    
    scaler = MinMaxScaler(feature_range=[0, 1])
    data_rescaled = scaler.fit_transform(data[1:, 0:8])
    
    #Fitting the PCA algorithm with our Data
    pca = PCA().fit(data_rescaled)
    #Plotting the Cumulative Summation of the Explained Variance
    plt.figure()
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel('Number of Components')
    plt.ylabel('Variance (%)') #for each component
    plt.title('Dataset Explained Variance')
    plt.show()

![img](src/damegender/files/images/pca-number-components.png)

Taking a look to the image. We can choose 6 components.


<a id="orgc3decdd"></a>

### Load Dataset

We choose the file all.csv to generate features and a list to determine gender (male or female)

    from pprint import pprint
    import pandas as pd
    import matplotlib.pyplot as plt
    from app.dame_sexmachine import DameSexmachine
    from app.dame_gender import Gender
    
    ## LOAD DATASET
    g = Gender()
    g.features_list2csv(categorical="both", path="files/names/all.csv")
    features = "files/features_list.csv"
    
    print("STEP1: N COMPONENTS + 1 TARGET")
    
    x = pd.read_csv(features)
    print(x.columns)
    
    y = g.dataset2genderlist(dataset="files/names/all.csv")
    print(y)


<a id="orgfa130da"></a>

### Standarize the data

    print("STEP2: STANDARIZE THE DATA")
    from sklearn.preprocessing import StandardScaler
    # Standardizing the features
    x = StandardScaler().fit_transform(x)


<a id="org6caf71c"></a>

### Pca Projection to N Dimensions

Finally, we create the pca transform with 6 dimensions and we add the target component.

    from sklearn.decomposition import PCA
    pca = PCA(n_components=6)
    principalComponents = pca.fit_transform(x)
    print("STEP3: PCA PROJECTION")
    pprint(principalComponents)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['principal component 1', 'principal component 2', 'principal component 3', 'principal component 4', 'principal component 5', 'principal component 6'])
    
    target = pd.DataFrame(data = y, columns = ['target component'])
    
    print(principalDf.join(target))


<a id="orgd2268fe"></a>

### Analyze components to determine gender in names

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />

<col  class="org-right" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-right">first\\<sub>letter</sub></th>
<th scope="col" class="org-right">last\\<sub>letter</sub></th>
<th scope="col" class="org-right">last\\<sub>letter</sub>\\<sub>a</sub></th>
<th scope="col" class="org-right">first\\<sub>letter</sub>\\<sub>vocal</sub></th>
<th scope="col" class="org-right">last\\<sub>letter</sub>\\<sub>vocal</sub></th>
<th scope="col" class="org-right">last\\<sub>letter</sub>\\<sub>consonant</sub></th>
<th scope="col" class="org-right">target component</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-right">-0.2080025204</td>
<td class="org-right">-0.3208958517</td>
<td class="org-right">0.2352509625</td>
<td class="org-right">0.2113242731</td>
<td class="org-right">**0.6095269139**</td>
<td class="org-right">**-0.6095269139**</td>
<td class="org-right">-0.1035071139</td>
</tr>


<tr>
<td class="org-right">**-0.6037951881**</td>
<td class="org-right">**0.5174873789**</td>
<td class="org-right">-0.4252467151</td>
<td class="org-right">0.4278794455</td>
<td class="org-right">0.0388287435</td>
<td class="org-right">-0.0388287435</td>
<td class="org-right">-0.0265942125</td>
</tr>


<tr>
<td class="org-right">0.1049343046</td>
<td class="org-right">0.1158117877</td>
<td class="org-right">-0.2867605971</td>
<td class="org-right">-0.3473950734</td>
<td class="org-right">0.0901034539</td>
<td class="org-right">-0.0901034539</td>
<td class="org-right">-0.8697264971</td>
</tr>


<tr>
<td class="org-right">0.2026467275</td>
<td class="org-right">0.3142402839</td>
<td class="org-right">**0.630802294**</td>
<td class="org-right">**0.5325769702**</td>
<td class="org-right">-0.1291229841</td>
<td class="org-right">0.1291229841</td>
<td class="org-right">-0.3811720011</td>
</tr>
</tbody>
</table>

In this analysis, we can observe 4 components.

The first component is about if the last letter is vocal or
consonant. If the last letter is vocal we can find a male and if the
last letter is a consonant we can find a male.

The second component is about the first letter. The last letter is
determining females and the first letter is determining males.

The third component is not giving relevant information.

The fourth component is giving the last<sub>letter</sub><sub>a</sub> and the
first<sub>letter</sub><sub>vocal</sub> is for females.


<a id="org0b03af4"></a>

# Speeches, Seminars, Expressions of Support

-   [MadSeSe](http://gregoriorobles.github.io/MadSESE/201906.html)
-   [Python Barcelona](https://www.meetup.com/es-ES/python-185/events/261405719/)
-   [Taller de Periodismo de Datos (Medialab Prado, Madrid). NLTK & Damegender](https://www.medialab-prado.es/noticias/taller-de-periodismo-de-datos-2019-sesiones-formativas)
-   [Software Freedom Day (URJC, Móstoles). Damegender](https://tv.urjc.es/video/5d895319d68b148f7a8c0da6)


<a id="org6c584e3"></a>

# Beautiful Snakes

![img](src/damegender/files/images/violet-snake3.png)


<a id="org64c405a"></a>

# Dame Music

[Listen music &#x2026;](https://www.youtube.com/playlist?list=PLeobXV-Yyn-LvQydcnr46ZkGh1V6tDGEk)


<a id="org23c90b4"></a>

# License

Copyright (C) 2019 David Arroyo Menendez
    Permission is granted to copy, distribute and/or modify this document
    under the terms of the GNU Free Documentation License, Version 1.3
    or any later version published by the Free Software Foundation;
    with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts.
    A copy of the license is included in [GNU Free Documentation License](https://www.gnu.org/copyleft/fdl.html).

[![img](https://upload.wikimedia.org/wikipedia/commons/thumb/4/42/GFDL_Logo.svg/200px-GFDL_Logo.svg.png)](https://www.gnu.org/copyleft/fdl.html)

