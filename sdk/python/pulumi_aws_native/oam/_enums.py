# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'LinkResourceType',
]


class LinkResourceType(str, Enum):
    AWS_CLOUD_WATCH_METRIC = "AWS::CloudWatch::Metric"
    AWS_LOGS_LOG_GROUP = "AWS::Logs::LogGroup"
    AWSX_RAY_TRACE = "AWS::XRay::Trace"
