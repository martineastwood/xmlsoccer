#!/usr/bin/env python

from distutils.core import setup

execfile('xmlsoccer/version.py')

setup(
    name = 'xmlsoccer',
    version = '0.1',
    description = 'Parse xmlsoccer feed',
    long_description = open('README.rst').read() + '\n\n' + open('HISTORY.rst').read(),
    author = 'Martin Eastwood',
    author_email = 'admin@stattaca.com',
    url = 'http://pena.lt/y',
    packages = ['xmlsoccer'])