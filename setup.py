#!/usr/bin/env python
# Copyright Daniel Stancl
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="cookiecutter-metric",
    version="0.0.1",
    url="https://github.com/stancld/cookiecutter-metrics",
    author="Daniel Stancl",
    author_email="daniel.stancl@gmail.com",
    description="This repo tests cookiecutter for automatic preparation of NLP metrics.",
    long_description='',
    packages=find_packages(),
    install_requires=install_requires,
    dependency_links=[],
    include_package_data=True,
    entry_points={"console_scripts": ["metrics-cli=metrics.commands.metrics_cli:main"]},
)
