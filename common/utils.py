import json
import logging
import os
import uuid
from collections.abc import Generator, Iterable
from datetime import datetime, timedelta
from glob import glob
from typing import Any, Optional, Union


logger = logging.getLogger(__name__)


def offset_datetime_strftime(base_date: Optional[datetime] = None,
                             format: Optional[str] = "%Y-%m-%dT%H:%M:%S",
                             **kwargs,) -> str:
    if base_date is None:
        base_date = datetime.now()
    offset_date = base_date - timedelta(**kwargs)
    offset_date = datetime.combine(offset_date, datetime.min.time())

    if format:
        return offset_date.strftime(format)

    return offset_date
