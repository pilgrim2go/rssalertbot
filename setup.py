#!/usr/bin/env python

import os
import re
from setuptools import setup, find_packages

VERSION = "0.1.0a1"
# this is overwritten by the makefile.
try:
    with open(os.path.join(os.path.dirname(__file__), 'CHANGELOG.rst'), 'r') as f:
        for line in f.readlines():
            m = re.match('(\d+\.\d+\.\d+\S*)', line)
            if m:
                VERSION = m.group(1)
                break
except:
    import warnings
    warnings.warn("version not found, defaulting to {}".format(VERSION))

install_requires = [
    'aiohttp',
    'dateparser',
    'feedparser==5.2.1',
    'mailer',
    'pendulum',
    'html2text',
    'python-box>=3.1.1,<=3.999.999',
    'PyYAML==3.12',
    'zc.lockfile'
]
tests_require = install_requires + [
    "mock",
    'pynamodb',
    "pytest",
    'slackclient',
]

setup(
    name            = 'rssalertbot',
    version         = VERSION,
    description     = 'RSS fetch and alert bot',
    author          = 'Michael Stella',
    author_email    = 'michael@jwplayer.com',
    url             = 'https://github.com/JWPlayer/rssalertbot',
    packages        = find_packages(exclude=['tests']),
    entry_points    = {
        'console_scripts': [
            'rssalertbot=rssalertbot.cli:main',
        ]
    },
    python_requires  = ">=3.6",
    install_requires = install_requires,
    tests_require    = tests_require,
    extras_require   = {
        'dynamo': [
            'pynamodb',
        ],
        'slack': [
            'slackclient',
        ],
    },
    classifiers     = [
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
