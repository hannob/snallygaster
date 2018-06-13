#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import setuptools

package_name = 'snallygaster'

with open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8') as f:
    readme = f.read()

setuptools.setup(
    name=package_name,
    version="0.0.2",
    description="Tool to scan for secret files on HTTP servers",
    long_description=readme,
    author="Hanno Böck",
    author_email='hanno@hboeck.de',
    url='https://github.com/hannob/snallygaster',
    packages=[],
    scripts=['snallygaster'],
    python_requires='>=3',
    install_requires=[
        'urllib3',
        'beautifulsoup4',
        'dnspython'
    ],
    license="CC0",
    zip_safe=True,
    keywords=('security', 'vulnerability', 'http'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
