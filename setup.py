#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from glob import glob
from setuptools import setup

import DistUtilsExtra.command.build_extra
import DistUtilsExtra.command.build_i18n
import DistUtilsExtra.command.clean_i18n

# to update i18n .mo files (and merge .pot file into .po files) run on Linux:
#   tx pull -a --minimum-perc=5
#   python3 setup.py build_i18n -m
#   tx push -s

# silence pyflakes, __VERSION__ is properly assigned below...
__VERSION__ = '0.0.0.0'
with open('magnus') as f:
    for line in f:
        if (line.startswith('__VERSION__')):
            exec(line.strip())
            break

PROGRAM_VERSION = __VERSION__

def datafilelist(installbase, sourcebase):
    datafileList = []
    for root, subFolders, files in os.walk(sourcebase):
        fileList = []
        for f in files:
            fileList.append(os.path.join(root, f))
        datafileList.append((root.replace(sourcebase, installbase), fileList))
    return datafileList

data_files = [
    ('{prefix}/share/man/man1'.format(prefix=sys.prefix), glob('data/*.1')),
    ('{prefix}/share/applications'.format(prefix=sys.prefix), ['data/magnus.desktop',]),
    ('/etc/xdg/autostart'.format(prefix=sys.prefix), ['data/magnus-autostart.desktop',]),
]
#data_files.extend(datafilelist('{prefix}/share/locale'.format(prefix=sys.prefix), 'build/mo'))

cmdclass ={
            "build" : DistUtilsExtra.command.build_extra.build_extra,
            "build_i18n" :  DistUtilsExtra.command.build_i18n.build_i18n,
            "clean": DistUtilsExtra.command.clean_i18n.clean_i18n,
}

setup(
    name = "Magnus",
    version = PROGRAM_VERSION,
    description = "A very simple screen magnifier for Ubuntu",
    license = 'MIT',
    author = 'Stuart Langridge',
    url = 'https://github.com/stuartlangridge/magnus',
    package_dir = {'': '.'},
    data_files = data_files,
    install_requires = [ 'setuptools', ],
    scripts = ['magnus'],
    cmdclass = cmdclass,
)
