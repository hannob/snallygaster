#!/usr/bin/env python3

import os

import setuptools

package_name = "snallygaster"

with open(
    os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md"),
    encoding="utf-8",
) as f:
    readme = f.read()

setuptools.setup(
    name=package_name,
    version="0.0.14",
    description="Tool to scan for secret files on HTTP servers",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Hanno Böck",
    author_email="hanno@hboeck.de",
    url="https://github.com/hannob/snallygaster",
    packages=[],
    scripts=["snallygaster"],
    python_requires=">=3.7",
    install_requires=["dnspython", "lxml", "urllib3"],
    license="0BSD",
    zip_safe=True,
    keywords=["security", "vulnerability", "http"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Zero-Clause BSD (0BSD)",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
)
