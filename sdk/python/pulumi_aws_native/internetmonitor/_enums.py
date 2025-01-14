# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'MonitorConfigState',
    'MonitorLocalHealthEventsConfigStatus',
    'MonitorProcessingStatusCode',
    'MonitorS3ConfigLogDeliveryStatus',
]


class MonitorConfigState(str, Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    ERROR = "ERROR"


class MonitorLocalHealthEventsConfigStatus(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class MonitorProcessingStatusCode(str, Enum):
    OK = "OK"
    INACTIVE = "INACTIVE"
    COLLECTING_DATA = "COLLECTING_DATA"
    INSUFFICIENT_DATA = "INSUFFICIENT_DATA"
    FAULT_SERVICE = "FAULT_SERVICE"
    FAULT_ACCESS_CLOUDWATCH = "FAULT_ACCESS_CLOUDWATCH"


class MonitorS3ConfigLogDeliveryStatus(str, Enum):
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"
