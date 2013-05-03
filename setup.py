#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup


setup(
    name='robotnik',
    version='0.1',
    description="Robotnik, python gemnasium",
    long_description="Robotnik, python gemnasium",
    keywords='gemnasium robotnik',
    author='Guilherme Souza',
    author_email='guivideojob@gmail.com',
    url='http://github.com/guilhermef/robotnik',
    license='Proprietary',
    classifiers=[],
    packages=['robotnik'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tornado>=3.0.1',
        'derpconf==0.4.7',
        'pycurl==7.19.0'
    ],

)
