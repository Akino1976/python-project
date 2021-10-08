import logging
import os
from typing import Any
import common.utils as utils
import click

logger = logging.getLogger(__name__)


@click.group()
def cli():
    pass


@cli.command()
def event_handler():
    today = utils.offset_datetime_strftime(format='%Y%m')
    return today


if __name__ == "__main__":
    cli()
