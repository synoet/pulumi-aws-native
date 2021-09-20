# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'DatasetDatasetParameterType',
    'DatasetFilesLimitOrder',
    'DatasetFilesLimitOrderedBy',
    'DatasetFormat',
    'JobDatabaseOutputDatabaseOutputMode',
    'JobEncryptionMode',
    'JobLogSubscription',
    'JobOutputCompressionFormat',
    'JobOutputFormat',
    'JobSampleMode',
    'JobType',
    'ProjectSampleType',
]


class DatasetDatasetParameterType(str, Enum):
    """
    Parameter type
    """
    STRING = "String"
    NUMBER = "Number"
    DATETIME = "Datetime"


class DatasetFilesLimitOrder(str, Enum):
    """
    Order
    """
    ASCENDING = "ASCENDING"
    DESCENDING = "DESCENDING"


class DatasetFilesLimitOrderedBy(str, Enum):
    """
    Ordered by
    """
    LAST_MODIFIED_DATE = "LAST_MODIFIED_DATE"


class DatasetFormat(str, Enum):
    """
    Dataset format
    """
    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"
    EXCEL = "EXCEL"


class JobDatabaseOutputDatabaseOutputMode(str, Enum):
    """
    Database table name
    """
    NEW_TABLE = "NEW_TABLE"


class JobEncryptionMode(str, Enum):
    """
    Encryption mode
    """
    SSE_KMS = "SSE-KMS"
    SSE_S3 = "SSE-S3"


class JobLogSubscription(str, Enum):
    """
    Log subscription
    """
    ENABLE = "ENABLE"
    DISABLE = "DISABLE"


class JobOutputCompressionFormat(str, Enum):
    GZIP = "GZIP"
    LZ4 = "LZ4"
    SNAPPY = "SNAPPY"
    BZIP2 = "BZIP2"
    DEFLATE = "DEFLATE"
    LZO = "LZO"
    BROTLI = "BROTLI"
    ZSTD = "ZSTD"
    ZLIB = "ZLIB"


class JobOutputFormat(str, Enum):
    CSV = "CSV"
    JSON = "JSON"
    PARQUET = "PARQUET"
    GLUEPARQUET = "GLUEPARQUET"
    AVRO = "AVRO"
    ORC = "ORC"
    XML = "XML"
    TABLEAUHYPER = "TABLEAUHYPER"


class JobSampleMode(str, Enum):
    """
    Sample configuration mode for profile jobs.
    """
    FULL_DATASET = "FULL_DATASET"
    CUSTOM_ROWS = "CUSTOM_ROWS"


class JobType(str, Enum):
    """
    Job type
    """
    PROFILE = "PROFILE"
    RECIPE = "RECIPE"


class ProjectSampleType(str, Enum):
    """
    Sample type
    """
    FIRST_N = "FIRST_N"
    LAST_N = "LAST_N"
    RANDOM = "RANDOM"
