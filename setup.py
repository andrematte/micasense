#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

# Parse the version from the main __init__.py
with open('micasense/__init__.py') as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            continue

setup(name='micasense',
      version=version,
      description=u"Micasense Image Processing, altered by GitHub user andrematte to use with RedEdge-P sensor data",
      author=u"MicaSense, Inc. - adapted by andrematte",
      url='https://github.com/andrematte/rededgep-processing',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'requests',
          'numpy',
          'opencv-python',
          'pysolar',
          'matplotlib',
          'scikit-image',
          'packaging',
          'pyexiftool<=0.4.13',
          'pytz',
          'pyzbar',
          'tqdm'
      ])
