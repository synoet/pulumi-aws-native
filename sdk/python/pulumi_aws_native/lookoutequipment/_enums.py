# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'InferenceSchedulerDataUploadFrequency',
]


class InferenceSchedulerDataUploadFrequency(str, Enum):
    """
    How often data is uploaded to the source S3 bucket for the input data.
    """
    PT5M = "PT5M"
    PT10M = "PT10M"
    PT15M = "PT15M"
    PT30M = "PT30M"
    PT1H = "PT1H"
