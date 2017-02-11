#!/usr/bin/env python
#
import os
from setuptools import setup
#from distutils.core import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# https://pypi.python.org/pypi?%3Aaction=list_classifiers
setup(name='SavingStar API',
      version='0.0.5',
      author='Robert Carr',
      author_email='rcarr@savingstar.com',
      description='Python Wrapper for the SavingStar Public API',
      license='MIT',
      keywords='savingstar api',
      url='https://www.python.org/sigs/distutils-sig/',
      packages=['savingstar'],
      long_description=read('README'),
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: API",
        "License :: MIT License",
        ],
     )
