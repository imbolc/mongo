#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import mongo

setup(
    name         = 'mongo',
    version      = mongo.__version__,
    packages     = ['mongo'],
    requires     = ['pymongo'],
    description  = 'Minimalistic pymongo object wrapper',
    long_description = open('README.md').read(),
    author       = 'Imbolc',
    author_email = 'imbolc@imbolc.name',
    url          = 'https://github.com/imbolc/pongo',
    download_url = 'https://github.com/imbolc/pongo/tarball/master',
    license      = 'MIT License',
    keywords     = ['mongodb', 'pymongo', 'orm'],
    classifiers  = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
    ],
)
