# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AnomalyDetectorCsvFormatDescriptorFileCompression',
    'AnomalyDetectorFrequency',
    'AnomalyDetectorJsonFormatDescriptorFileCompression',
    'AnomalyDetectorMetricAggregationFunction',
    'AnomalyDetectorMetricSetMetricSetFrequency',
]


class AnomalyDetectorCsvFormatDescriptorFileCompression(str, Enum):
    NONE = "NONE"
    GZIP = "GZIP"


class AnomalyDetectorFrequency(str, Enum):
    """
    Frequency of anomaly detection
    """
    PT5M = "PT5M"
    PT10M = "PT10M"
    PT1H = "PT1H"
    P1D = "P1D"


class AnomalyDetectorJsonFormatDescriptorFileCompression(str, Enum):
    NONE = "NONE"
    GZIP = "GZIP"


class AnomalyDetectorMetricAggregationFunction(str, Enum):
    """
    Operator used to aggregate metric values
    """
    AVG = "AVG"
    SUM = "SUM"


class AnomalyDetectorMetricSetMetricSetFrequency(str, Enum):
    """
    A frequency period to aggregate the data
    """
    PT5M = "PT5M"
    PT10M = "PT10M"
    PT1H = "PT1H"
    P1D = "P1D"
