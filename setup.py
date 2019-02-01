from setuptools import setup

setup(name='damegender',
      version='0.1',
      description='Gender Detection Tool by David Arroyo MEnéndez',
      url='http://github.com/davidam/damegender',
      author='David Arroyo Menéndez',
      author_email='davidam@gnu.org',
      license='GPLv3',
      packages=['damegender'],
      install_requires=[
          'nltk',
          'perceval',
          'requests',
          'gender_guesser',
          'genderize',
          'numpy',
          'scikit-learn',
          'pyhyphen',
          'unidecode',
          'pandas',
          'matplotlib',
      ],
      zip_safe=False)
