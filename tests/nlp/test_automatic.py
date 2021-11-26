from enum import Enum, unique
from functools import partial
from typing import Any, Dict

import pytest

from metrics.functional.nlp.automatic import automatic_score
from metrics.nlp.automatic import AUTOMATICScore

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


def automatic_score_original():
    ...


@pytest.mark.parametrize(
    ["preds", "targets"],
    [
        pytest.param(BATCHES["preds"], BATCHES["targets"]),
    ],
)
class TestAUTOMATICScore(TextTester):
    @pytest.mark.parametrize("ddp", [False, True])
    @pytest.mark.parametrize("dist_sync_on_step", [False, True])
    def test_manual_score_class(self, ddp, dist_sync_on_step, targets, preds):
        metric_args: Dict[str, Any] = {}
        original_metric = partial(automatic_score_original)

        self.run_class_metric_test(
            ddp=ddp,
            preds=preds,
            targets=targets,
            metric_class=AUTOMATICScore,
            sk_metric=original_metric,
            dist_sync_on_step=dist_sync_on_step,
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )

        return

    def test_manul_score_functional(self, targets, preds):
        metric_args: Dict[str, Any] = {}
        original_metric = partial(automatic_score_original)

        self.run_functional_metric_test(
            preds,
            targets,
            metric_functional=automatic_score,
            sk_metric=original_metric,
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )

    def test_bleu_score_differentiability(self, preds, targets):
        metric_args: Dict[str, Any] = {}

        self.run_differentiability_test(
            preds=preds,
            targets=targets,
            metric_module=AUTOMATICScore,
            metric_functional=automatic_score,
            metric_args=metric_args,
            input_order=INPUT_ORDER.TARGETS_FIRST,
        )
