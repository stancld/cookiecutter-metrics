from enum import Enum, unique
from functools import partial
from typing import Any, Dict

import pytest

from metrics.functional.nlp.{{cookiecutter.metric_shortened}} import {{cookiecutter.metric_functional}}
from metrics.nlp.{{cookiecutter.metric_shortened}} import {{cookiecutter.metric_module}}

TextTester = None  # dummy initialization


# initialization from torchmetrics
@unique
class INPUT_ORDER(Enum):
    PREDS_FIRST = 1
    TARGETS_FIRST = 2


# Test examples
BATCHES = {
    "targets": [["target sentence"]],
    "preds": ["hypothesis sentence"],
}


def {{cookiecutter.metric_functional}}_original():
    ...


@pytest.mark.parametrize(
    ["preds", "targets"],
    [
        pytest.param(BATCHES["preds"], BATCHES["targets"]),
    ],
)
class Test{{cookiecutter.metric_module}}(TextTester):
    @pytest.mark.parametrize("ddp", [False, True])
    @pytest.mark.parametrize("dist_sync_on_step", [False, True])
    def test_manual_score_class(self, ddp, dist_sync_on_step, targets, preds):
        metric_args: Dict[str, Any] = {}
        original_metric = partial({{cookiecutter.metric_functional}}_original)

        self.run_class_metric_test(
            ddp=ddp,
            preds=preds,
            targets=targets,
            metric_class={{cookiecutter.metric_module}},
            sk_metric=original_metric,
            dist_sync_on_step=dist_sync_on_step,
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )

        return

    def test_manul_score_functional(self, targets, preds):
        metric_args: Dict[str, Any] = {}
        original_metric = partial({{cookiecutter.metric_functional}}_original)

        self.run_functional_metric_test(
            preds,
            targets,
            metric_functional={{cookiecutter.metric_functional}},
            sk_metric=original_metric,
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )

    def test_bleu_score_differentiability(self, preds, targets):
        metric_args: Dict[str, Any] = {}

        self.run_differentiability_test(
            preds=preds,
            targets=targets,
            metric_module={{cookiecutter.metric_module}},
            metric_functional={{cookiecutter.metric_functional}},
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )
