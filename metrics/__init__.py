r"""Root package info."""
import logging as __logging
import os

_logger = __logging.getLogger("cookiecutter_metrics")
_logger.addHandler(__logging.StreamHandler())
_logger.setLevel(__logging.INFO)

_PACKAGE_ROOT = os.path.dirname(__file__)
_PROJECT_ROOT = os.path.dirname(_PACKAGE_ROOT)

from metrics import functional  # noqa: E402
from metrics.nlp import MANUALScore  # noqa: E402

__all__ = ["functional", "MANUALScore"]
