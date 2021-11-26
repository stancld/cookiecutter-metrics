from typing import Any, Callable, List, Optional, Union

from torchmetrics import Metric

from metrics.functional.nlp.manual import _manual_score_compute, _manual_score_update
from metrics.functional.nlp.utils import prepare_inputs


class AUTOMATICScore(Metric):
    """Calculate `AUTOMATIC score`_ of TODO: Appropriate docstring.
    Args:
        compute_on_step:
            Forward only calls ``update()`` and returns None if this is set to False. default: True
        dist_sync_on_step:
            Synchronize metric state across processes at each ``forward()``
            before returning the value at the step.
        process_group:
            Specify the process group on which synchronization is called. default: None (which selects the entire world)
        dist_sync_fn:
            Callback that performs the allgather operation on the metric state. When `None`, DDP
            will be used to perform the allgather.
    Example:
        TODO: Appropriate example.

    References:
        TODO: Appropriate references.
    """

    is_differentiable = False
    higher_is_better = True

    def __init__(
        self,
        compute_on_step: bool = True,
        dist_sync_on_step: bool = False,
        process_group: Optional[Any] = None,
        dist_sync_fn: Optional[Callable] = None,
    ):
        super().__init__(
            compute_on_step=compute_on_step,
            dist_sync_on_step=dist_sync_on_step,
            process_group=process_group,
            dist_sync_fn=dist_sync_fn,
        )

        pass

    def update(
        self, reference_corpus: Union[List[str], List[List[str]]], hypothesis_corpus: Union[str, List[str]]
    ) -> None:
        """
        Appropraite docstings
        """
        reference_corpus, hypothesis_corpus = prepare_inputs(reference_corpus, hypothesis_corpus)
        _manual_score_update(reference_corpus, hypothesis_corpus)

    def compute(self):
        """
        Appropriate docstring.
        """
        _manual_score_compute()
        return
