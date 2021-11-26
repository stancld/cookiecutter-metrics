from typing import List, Union

from metrics.functional.nlp.utils import prepare_inputs


def _automatic_score_update(reference_corpus: List[List[str]], hypothesis_corpus: List[str]):
    """
    Appropriate docstring.
    """
    return


def _automatic_score_compute():
    """
    Appropriate docstring.
    """
    return


def automatic_score(reference_corpus: Union[List[str], List[List[str]]], hypothesis_corpus: Union[str, List[str]]):
    """
    Appropriate docstring.
    """
    reference_corpus, hypothesis_corpus = prepare_inputs(reference_corpus, hypothesis_corpus)

    return
