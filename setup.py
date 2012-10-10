#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from setuptools import setup


VERSION = '0.1.0'


if sys.argv[-1] in ['test', 'publish']:
    import doctest

    if doctest.testfile('README.md', verbose=True).failed:
        sys.exit()

    if sys.argv[-1] == 'publish':
        os.system('python setup.py sdist upload')
        sys.exit()

setup(
    name         = 'mongo',
    version      = VERSION,
    description  = 'Minimalistic pymongo object wrapper',
    url          = 'https://github.com/imbolc/mongo',

    packages     = ['mongo'],
    install_requires = ['pymongo'],

    author       = 'Imbolc',
    author_email = 'imbolc@imbolc.name',
    license      = open('LICENSE').read(),
    long_description = open('README.md').read(),

    keywords     = ['mongodb', 'pymongo', 'orm'],
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
    ],
)
