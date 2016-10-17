#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name = 'hcby',
    version = '0.0.1',
    description = 'A plugin for Hachi to detect spam.',
    author = 'MomingCoder',
    author_email = 'a398445075@gmail.com',
    url = 'https://github.com/guokr/Hachi',
    license = 'MIT',
    keywords = ['filter', 'Hachi', 'plugin', 'bayes'],
    classifiers = ['Topic :: Text Processing'],
    packages = find_packages(),
    install_requires = ['jieba', 'numpy', 'scipy', 'scikit-learn'],
    platform = ['Windows', 'Linux', 'Mac'],
)
