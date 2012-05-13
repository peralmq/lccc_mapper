#!/usr/bin/env python
import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='lccc_mapper',
    version='0.0.1',
    packages=['lccc_mapper'],
    author = 'Per Almquist',
    author_email = 'per.almquist@gmail.com',
    description = ('Locale currency country code mapper'),
    license = 'BSD',
    keywords = 'country currency ISO 3166 4217',
    url = 'http://packages.python.org/lccc_mapper',
    long_description=read('README.md'),
)

