#!/usr/bin/env python
"""scrapli_stubs"""
import setuptools

__author__ = "Carl Montanari"

with open("README.md", "r", encoding="utf-8") as f:
    README = f.read()

setuptools.setup(
    name="scrapli_stubs",
    version="2020.10.10",
    author=__author__,
    author_email="carl.r.montanari@gmail.com",
    description="mypy stubs for scrapli SSH|Telnet screen scraping library",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/scrapli/scrapli_stubs",
    packages=setuptools.find_packages(),
    install_requires=[],
    extras_require={},
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
    ],
    python_requires=">=3.6",
)
