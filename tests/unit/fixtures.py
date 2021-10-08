import datetime
import io
from typing import Any, Optional

import pytest


@pytest.fixture
def parameters() -> dict[str, Any]:
    return dict()


@pytest.fixture
def yester_day_date():
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    return yesterday.strftime("%Y-%m-%d")


@pytest.fixture
def current_year():
    return datetime.datetime.now().strftime("%Y")