# Copyright 2020 The HuggingFace Team. All rights reserved.
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

import json
import os
import pathlib
import shutil
from argparse import ArgumentParser, Namespace

from cookiecutter.main import cookiecutter

from . import BaseMetricsCLICommand


def add_new_nlp_metric_command_factory(args: Namespace):
    return AddNewNLPMetriclCommand(args.path)


class AddNewNLPMetriclCommand(BaseMetricsCLICommand):
    @staticmethod
    def register_subcommand(parser: ArgumentParser):
        add_new_nlp_metric_parser = parser.add_parser("add-new-nlp-metric")
        add_new_nlp_metric_parser.add_argument(
            "--path", type=str, help="Path to cookiecutter. Should only be used for testing purposes."
        )
        add_new_nlp_metric_parser.set_defaults(func=add_new_nlp_metric_command_factory)

    def __init__(self, path=None, *args):
        self._path = path

    def run(self):
        # TODO: It would be necessary to dome some checks and error handling

        path_to_metric_root = (
            pathlib.Path(__file__).parent.parent.parent
            if self._path is None
            else pathlib.Path(self._path).parent
        )
        path_to_cookiecutter = path_to_metric_root / "templates" / "adding_a_new_nlp_metric"

        # Execute cookiecutter
        # TODO: Need to add testing
        cookiecutter(str(path_to_cookiecutter))

        directory = [directory for directory in os.listdir() if "cookiecutter-template-" in directory[:22]][0]
        metric_dir = os.path.join(path_to_metric_root, "metrics", "functional", "nlp")

        # Retrieve configuration
        with open(os.path.join(directory, "configuration.json"), "r") as configuration_file:
            configuration = json.load(configuration_file)
        os.remove(os.path.join(directory, "configuration.json"))

        metric_shortened = configuration["metric_shortened"]

        shutil.move(
            os.path.join(directory, f"{metric_shortened}.py"), os.path.join(metric_dir, f"{metric_shortened}.py")
        )

        # Clean root dir
        os.rmdir(directory)
