#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import setuptools

package_name = 'snallygaster'

f = open(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'README.md'), encoding='utf-8')
readme = f.read()
f.close()

setuptools.setup(
    name=package_name,
    version="0.0.6",
    description="Tool to scan for secret files on HTTP servers",
    long_description=readme,
    long_description_content_type='text/markdown',
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
    keywords=['security', 'vulnerability', 'http'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
