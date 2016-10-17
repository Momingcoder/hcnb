#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name = 'hbml',
    version = '0.0.1',
    description = 'A plugin for Hachi to detect meaningless sentences.',
    author = 'MomingCoder',
    author_email = 'a398445075@gmail.com',
    url = 'https://github.com/guokr/Hachi',
    license = 'MIT',
    keywords = ['filter', 'Hachi', 'plugin', 'meaningless'],
    classifiers = ['Topic :: Text Processing'],
    packages = find_packages(),
    install_requires = [],
    platform = ['Windows', 'Linux', 'Mac'],
)
