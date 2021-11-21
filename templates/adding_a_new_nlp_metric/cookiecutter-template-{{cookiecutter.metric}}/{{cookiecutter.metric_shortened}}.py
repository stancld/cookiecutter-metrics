from typing import List, Union

from metrics.functional.nlp.utils import prepare_inputs


def _{{cookiecutter.metric_functional}}_update(reference_corpus: List[List[str]], hypothesis_corpus: List[str]):
    """
    Appropriate docstring.
    """
    return


def _{{cookiecutter.metric_functional}}_compute():
    """
    Appropriate docstring.
    """
    return


def {{cookiecutter.metric_functional}}(reference_corpus: Union[List[str], List[List[str]]], hypothesis_corpus: Union[str, List[str]]):
    """
    Appropriate docstring.
    """
    reference_corpus, hypothesis_corpus = prepare_inputs(reference_corpus, hypothesis_corpus)

    return
