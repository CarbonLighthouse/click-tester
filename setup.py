from setuptools import setup, find_packages

setup(
    name='click-tester',
    version='0.0.0+snapshot',
    description='Provides utilities for testing command line tools built with Click.',
    url='https://github.com/CarbonLighthouse/click-tester',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'click==6.6'
    ]
)
