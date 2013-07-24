#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
from os.path import join, dirname

import texscrap

setup(name='texscrap',
      version = texscrap.__version__,
      author = texscrap.__author__ , 
      author_email = texscrap.__email__,
      url = 'http://github.com/johnjosephhorton/texscrap',
      packages = [''],
      package_data = {'':['*.md', 'templates/*.tex']},
      package_dir= {'':'.'}, 
      entry_points={
          'console_scripts':
              ['texscrap = texscrap:main',
               ]}, 
      classifiers=(
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Web Environment',
          'License :: OSI Approved :: GNU General Public License v3 or '
          'later (GPLv3+)',
          'Natural Language :: English',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
      ),
      install_requires=['Jinja2>=2.6'],
      )
