import importlib
import logging
from typing import Any

from click.testing import CliRunner

from pytest_bdd import parsers, when
from types import ModuleType

logger = logging.getLogger("app-framework")


@when(parsers.parse("I call the {callable_path} function"))
def call_callable(request: Any, callable_path: str):
    variable_path, variable_method_name = callable_path.rsplit(".", 1)
    object_enviroment = importlib.import_module(variable_path)
    callable_function = getattr(object_enviroment, variable_method_name)
    try:
        process = CliRunner().invoke(callable_function)
    except Exception as exception:
        logger.exception(f"Exception in when calling {callable_path}")
        request.raised_exception = exception
