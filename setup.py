#!/usr/bin/env python
# -*- coding: utf-8 -*-
# module: setup.py


from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

from setuptools import setup, find_packages

import PyFMask as package

setup(
    name=package.__name__,
    version=package.__version__,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'numexpr',
        'scikit-image',
        'pygdal',
    ],
    entry_points="""
        [console_scripts]
        fmask.py=PyFMask.fmask:main
    """,
)
