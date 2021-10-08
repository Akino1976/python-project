import contextlib
import importlib
import logging
from typing import Any, Callable, Dict, List

import builtins
from pytest_bdd import parsers, when
from types import ModuleType

logger = logging.getLogger("app-framework")


@when(parsers.parse("I call the {callable_path} function"))
def call_callable(request: Any, callable_path: str, parameters: Dict[str, Any], module: ModuleType):
    module = importlib.import_module(module)
    callable = getattr(module, callable_path)

    try:
        request.return_value = callable(**parameters)

    except Exception as exception:
        logger.exception(f"Exception in when calling {callable_path}")
        request.raised_exception = exception
