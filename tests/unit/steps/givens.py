import logging
import os
from typing import Any

from pytest_bdd import given, parsers
from types import ModuleType

import helpers.yaml as yaml

logger = logging.getLogger("dump-framework")


@given(parsers.parse('the values:\n{yaml_string}'))
def create_values(request: Any, yaml_string: Any) -> None:
    yaml.load_with_tags(request, yaml_string)
    pass


@given(parsers.parse("the parameters:\n{yaml_string}"), target_fixture="parameters")
def create_parameters(request: Any, yaml_string: dict[str, Any]) -> dict[str, Any]:
    return yaml.load_with_tags(request, yaml_string)


@given(parsers.parse("the module {module:S}"))
def set_module(module: str):
    logger.info(f"Base module set to {module}")
    pass
