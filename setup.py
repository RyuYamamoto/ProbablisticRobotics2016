#! /usr/bin/env python
from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages


setup(name='permamodel',
      version='0.1.0',
      author='Ryu Yamamoto',
      #author_email='james.stewart@colorado.edu',
      description='Permamodel',
      long_description=open('README.md').read(),
      packages=find_packages(),
      #install_requires=('numpy', 'nose', 'gdal', 'pyproj'),
      install_requires=('matplotlib', 'numpy', 'pygame',),
      package_data={'': ['examples/*.cfg', 'examples/*.dat']}
)
