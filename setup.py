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
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    packages=['robotnik'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'tornado>=3.0.1',
        'derpconf==0.4.7',
        'pycurl==7.19.0'
    ],

    entry_points={
        'console_scripts': [
            'robotnik=robotnik.server:main'
        ],
    },

)
