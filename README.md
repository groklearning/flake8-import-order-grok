# flake8-import-order-grok

A [flake8-import-order](https://github.com/PyCQA/flake8-import-order) ordering definition, defining Grok Learning's preferred import order style.

The import order enforced by this style is:
1. `__future__`
2. builtins
3. Django
4. Non-django third-party, grouped by package
5. Application packages

All groups of imports require a line break between them, except between `__future__` and builtins.

All imports must be alphabetical horizontally and vertically.
Within an import unit, names must be constants first, followed by classes, followed by functions (i.e. `CAPITAL_CASE`, `CamelCase`, `underscore_case`).

The names of the application packages can be configured via the `application-import-names` setting in `flake8`.

For example, if `application-import-names` is set to `my_project`, this import ordering enforces the following ordering:

```python
# coding: utf-8
from __future__ import absolute_import, print_function, unicode_literals  # 1. `__future__`
import io  # 2. Builtins.
import logging
import os
import tarfile

from django.conf import settings  # 3. Django.
from django.utils.http import urlencode

from dns.exception import DNSException, Timeout  # 4. Non-Django third-party packages, each one separated by a blank line.
from dns.resolver import NXDOMAIN, NoAnswer, Resolver

import requests

import ujson

from my_project.core.enums import Enum  # 5. Application packages.
from my_project.utils.download import DOWNLOAD_TIMEOUT, InvalidURLException, download_content_url
```

## Usage

Install the `flake8-import-order-grok` package using `pip`, then tell `flake8` to use this import order style using the `--import-order-style=grok` command-line option, or by setting it in `setup.cfg`.
The names of your application package(s) can be set by the `application-import-names` setting:

```
[flake8]
import-order-style = grok
application-import-names = my_package1, my_package2
```
