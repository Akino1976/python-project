import logging
import os
from logging.config import dictConfig

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
APP_PATH = os.path.dirname(os.path.realpath(PROJECT_ROOT))
APP_NAME = os.getenv("APP_NAME", "python-project")
APP_COMPONENT = os.getenv("APP_COMPONENT")

logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "[%(asctime)s] - [%(levelname)-3s] - [%(name)-8s] - [%(message)s]",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        },
        "colored": {
            "()": "colorlog.ColoredFormatter",
            "format": "[%(blue)s%(asctime)s %(name)-1s %(reset)s] - [%(log_color)s%(levelname)-3s%(reset)s] -"
                      "[%(cyan)s%(message)s%(reset)s]",
            "datefmt": "%Y-%m-%d %H:%M:%S",
            "log_colors": {
                "DEBUG": "white",
                "INFO": "bold_green",
                "WARNING": "bold_yellow",
                "ERROR": "bold_red",
                "CRITICAL": "red,bg_white"
            }
        }
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "filters": None,
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "standard"
        },
        "info_file_handler": {
            "level": "INFO",
            "filters": None,
            "class": "logging.StreamHandler",
            "formatter": "standard"
        },
        "error_file_handler": {
            "level": "ERROR",
            "filters": None,
            "class": "logging.StreamHandler",
            "formatter": "standard"
        }
    },
    "loggers": {
        "root": {
            "handlers": ["console", "info_file_handler", "error_file_handler"],
            "propagate": True,
            "level": "INFO"
        }
    }
}
dictConfig(logging_config)

ENVIRONMENT = os.getenv("ENVIRONMENT", "test")
VERSION = os.getenv("VERSION")
DEFAULT_TIMEZONE = os.getenv("DEFAULT_TIMEZONE", "Europe/Stockholm")
