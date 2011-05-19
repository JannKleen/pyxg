#!/usr/bin/env python

from distutils.core import setup
import bdist_mpkg

setup(name='PyXG',
    version='0.2.0',
    description='A Python interface to Xgrid',
    author='Brian Granger/Barry Wark/Jann Kleen',
    author_email='jann@pocketvillage.com',
    url='https://github.com/JannKleen/pyxg',
    packages = ['xg']
    )
