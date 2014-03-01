#!/usr/bin/env python2

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.environ['PYTHONDONTWRITEBYTECODE'] = '1'

packages = [
        'connman_dispatcher'
]


requires = [
    'pyee >= 0.0.9'
]

setup(
    name='connman-dispatcher',
    version='0.0.5',
    description='Call scripts on network changes',
    long_description=open('README.rst').read(),
    author='Alexandr Skurikhin',
    author_email='a.skurikhin@gmail.com',
    url='http://github.com/a-sk/connman-dispatcher',
    scripts=['bin/connman-dispatcher'],
    packages=packages,
    package_data={'': ['LICENSE']},
    install_requires=requires,
    license=open('LICENSE').read(),
)

del os.environ['PYTHONDONTWRITEBYTECODE']
