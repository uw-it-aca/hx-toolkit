# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-it-aca/hx_toolkit>`_.
"""

# The VERSION file is created by travis-ci, based on the tag name
version_path = 'hx_toolkit/VERSION'
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

url = "https://github.com/uw-it-aca/hx_toolkit"
setup(
    name='UW_HX_Toolkit',
    version=VERSION,
    packages=['hx_toolkit'],
    author="UW-IT T&LS",
    author_email="aca-it@uw.edu",
    include_package_data=True,
    install_requires=[
        'Django>4.2,<6',
        'django-compressor',
        'pillow'
    ],
    license='Apache License, Version 2.0',
    description=('An application for managing and serving HXT content'),
    long_description=README,
    url=url,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
