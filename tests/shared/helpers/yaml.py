import datetime
import functools
import io
import json
import logging
import os
import re
from typing import Any, Optional, Type

import inspect
import uuid
import yaml


logger = logging.getLogger(__name__)


def __load_node(loader, node):
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    if isinstance(node, yaml.MappingNode):
        return loader.construct_mapping(node)


def create_loader(request: Any) -> Type:
    return type("RequestLoader", (yaml.Loader, ), {"_pytest_request": request})


def get_fixture(loader):
    return loader._pytest_request.getfixturevalue("fixture_helper")


def load_with_tags(request: Any, yaml_string: str) -> Any:
    loader = create_loader(request)

    return yaml.load(io.StringIO(yaml_string), Loader=loader)


def yaml_tag(tag):
    def register_tag(f):
        yaml.Loader.add_multi_constructor(tag, f)

        return f

    return register_tag


def get_yaml(schema_path: str) -> dict[str, str]:
    if not os.path.isfile(schema_path):
        raise Exception(f"Yaml was not found {schema_path}")

    with open(schema_path) as file:
        payload_dict = yaml.load(
            file.read(),
            Loader=yaml.Loader
        )
    return payload_dict


@yaml_tag("!Ref")
def references_tag(loader, tag_suffix, node):
    name = loader.construct_scalar(node)
    return loader._pytest_request.getfixturevalue(name)
