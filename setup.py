#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename, dirname, join, splitext

from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names), encoding=kwargs.get("encoding", "utf8")
    ) as fh:
        return fh.read()


setup(
    name="heroku_config_vars_formatter",
    version="1.0.0",
    description="A small utility to set Heroku config vars in a shell.",
    long_description="%s\n%s"
    % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.md")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.md")),
    ),
    author="Martin Winkel",
    author_email="martin@pythomation.de",
    url="https://github.com/SaturnFromTitan/heroku_config_vars_formatter",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/ionelmc/python-nameless/blob/master/CHANGELOG.md",
        "Issue Tracker": "https://github.com/SaturnFromTitan/heroku_config_vars_formatter/issues",
    },
    keywords=[
        "heroku",
    ],
    python_requires=">=3.9",
    install_requires=["pyperclip>=1.8.2"],
    entry_points={
        "console_scripts": [
            "nameless = nameless.cli:main",
        ]
    },
)
