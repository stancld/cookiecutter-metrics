from typing import List, Union


def prepare_inputs(reference_corpus: Union[List[str], List[List[str]]], hypothesis_corpus: Union[str, List[str]]):
    if isinstance(hypothesis_corpus, str):
        hypothesis_corpus = [hypothesis_corpus]

    # Ensure reference corpus is properly of a type List[List[str]]
    if all(isinstance(ref, str) for ref in reference_corpus):
        if len(hypothesis_corpus) == 1:
            reference_corpus = [reference_corpus]  # typing: ignore
        else:
            reference_corpus = [[ref] for ref in reference_corpus]  # typing: ignore

    if len(reference_corpus) != len(hypothesis_corpus):
        raise ValueError(f"Corpus has different size {len(reference_corpus)} != {len(hypothesis_corpus)}")
