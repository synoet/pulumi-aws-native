# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'EnvironmentLoggingLevel',
    'EnvironmentWebserverAccessMode',
]


class EnvironmentLoggingLevel(str, Enum):
    CRITICAL = "CRITICAL"
    ERROR = "ERROR"
    WARNING = "WARNING"
    INFO = "INFO"
    DEBUG = "DEBUG"


class EnvironmentWebserverAccessMode(str, Enum):
    """
    Choice for mode of webserver access including over public internet or via private VPC endpoint.
    """
    PRIVATE_ONLY = "PRIVATE_ONLY"
    PUBLIC_ONLY = "PUBLIC_ONLY"
