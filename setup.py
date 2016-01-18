#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='fashion',
    version=1.0,
    author='Leighton Lee',
    author_email='leightonlclee@gmail.com',
    url='',
    packages=find_packages(exclude=['*.tests']),
    setup_requires=[
    ],
    install_requires=[
        'flask>=0.10dev',
        'nose>=1.0',
        "mock>=1.0,<2.0",
        "requests>=2.9.1",
    ],
    tests_require=[
    ],
    test_suite='sfltest.tests',
    entry_points={
        'console_scripts': [
            'development = fashion.development:main',
            'createdb = fashion.createdb:main',
        ]
    }
)
