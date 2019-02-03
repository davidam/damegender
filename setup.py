from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='damegender',
      version='0.1.2',
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
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: GPLv3 License",
          "Operating System :: OS Independent",
      ],
      zip_safe=False)
