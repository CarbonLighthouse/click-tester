from setuptools import setup, find_packages

setup(
    name='click-tester',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'click>=6,<7'
    ],
    author="CarbonLighthouse",
    description=("A unittest.TestCase subclass which provides"
                 "convenience methods for testing click commands."),
    long_description="See: http://github.com/CarbonLighthouse/click-tester",
    keywords="click testing unittest TestCase pocoo",
    license='MIT',
    url="http://github.com/CarbonLighthouse/click-tester"
)
