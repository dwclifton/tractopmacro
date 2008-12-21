#!/usr/bin/env python

import os.path
from setuptools import setup

setup(
    name = 'TracTopMacro',
    packages = ['top'],
    version = '0.11.0',

    author = 'Douglas Clifton',
    author_email = 'dwclifton@gmail.com',
    description = 'Top of page Macro',
    long_description = open(os.path.join(os.path.dirname(__file__), 'README')).read(),
    keywords = '0.11 dwclifton macro wiki',
    url = 'http://trac-hacks.org/wiki/TopMacro',
    license = 'BSD',

    entry_points = { 'trac.plugins': [ 'top.macro = top.macro' ],
    classifiers = ['Framework :: Trac'],
    install_requires = ['Trac']
)
