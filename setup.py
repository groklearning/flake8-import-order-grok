# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals
import os

from setuptools import setup


def readme():
    path = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(path, 'README.md'), 'rU', encoding='utf-8') as f:
        return f.read()


setup(
    name="flake8-import-order-grok",
    version="0.3.1",
    author="Grok Learning",
    author_email="opensource@groklearning.com",
    description="Grok Learning's flake8-import-order plugin.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords="flake8-import-order grok",
    license="MIT",
    url="https://github.com/groklearning/flake8-import-order-grok",
    packages=["flake8_import_order_grok"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
    install_requires=["flake8-import-order>=0.18"],
    entry_points={
        "flake8_import_order.styles": [
            "grok = flake8_import_order_grok:GrokImportOrderStyle"
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Flake8",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
)
