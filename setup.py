#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import sys
from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name="pipsec",
    version="0.0.1dev2",
    description="Security-hardened pip installer",
    long_description=readme,
    author="Benjamin Bach",
    author_email='benjamin@overtag.dk',
    url='https://github.com/benjaoming/pipsec',
    packages=[],
    license="MIT",
    zip_safe=False,
    keywords=('typosquatting',),
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)
