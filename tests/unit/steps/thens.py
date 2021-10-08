from collections.abc import Callable, Generator
from typing import Any

from pytest_bdd import parsers, then
from types import ModuleType

import helpers.comparisons as comparisons
import helpers.yaml as yaml


@then(parsers.parse("the result should be {yaml_string}"))
@then(parsers.parse("the result should contain:\n{yaml_string}"))
def should_contain(request: Any, yaml_string: Any):
    options = yaml.load_with_tags(request, yaml_string)
    if options == "Generator":
        assert isinstance(request.return_value, Generator)
    else:
        assert comparisons.contains(request.return_value, options)


@then(parsers.parse("the function should raise {expected_exception_type}"))
def should_raise_exception(request: Any, expected_exception_type: str):
    assert type(request.raised_exception).__name__ == expected_exception_type
