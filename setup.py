#!/usr/bin/env python3

from setuptools import setup, find_packages

version = "4.0.20"

setup(
    name='raritan-rpc',
    version=version,
    description='Fork of the Raritan PX3 python SDK',
    packages=find_packages(),
    python_requires='>=3',
)
