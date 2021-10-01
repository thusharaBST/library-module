from setuptools import setup, find_packages

setup(
    name='lib-module',
    version='0.1.0',
    packages=find_packages(include=['inner_module', 'inner_module.*'])
)
