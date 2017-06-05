# vim: set et nosi ai ts=2 sts=2 sw=2:
# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals

from setuptools import setup


setup(
    name='flake8-grok',
    install_requires=[
        'flake8-import-order',
    ],
    entry_points={
        'flake8_import_order.styles': [
            'grok = flake8_grok:GrokImportOrderStyle',
        ],
    },
)
