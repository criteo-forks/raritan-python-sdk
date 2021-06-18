#!/usr/bin/env python3

from setuptools import setup, find_packages

version = "3.6.1"

setup(
    name='raritan-rpc',
    version=version,
    description='Fork of the Raritan PX3 python SDK',
    packages=find_packages(),
    python_requires='>=3',
)
