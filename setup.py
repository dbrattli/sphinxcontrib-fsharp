#!/usr/bin/env python3
# coding: utf8

# Copyright 2017 Vincent Jacques <vincent@vincent-jacques.net>

import setuptools


version = "0.3.0"

setuptools.setup(
    name="sphinxcontrib-fsharp",
    version=version,
    description="Sphinx extension to document F# libraries",
    long_description=open("README.rst").read(),
    author="Dag Brattli",
    author_email="dag@brattli.net",
    url="http://github.com/dbrattli/sphinx-fsharp",
    packages=setuptools.find_packages(),
    namespace_packages=["sphinxcontrib"],
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Documentation",
        "Topic :: Documentation :: Sphinx",
    ],
    use_2to3=True,
    # install_requires=[],
    # tests_require=[],
    # test_suite="",
    command_options={
        "build_sphinx": {
            "version": ("setup.py", version),
            "release": ("setup.py", version),
            "source_dir": ("setup.py", "doc"),
        },
    },
)
