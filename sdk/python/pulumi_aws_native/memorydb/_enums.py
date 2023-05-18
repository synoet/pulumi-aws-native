# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ClusterDataTieringStatus',
    'UserAuthenticationModePropertiesType',
]


class ClusterDataTieringStatus(str, Enum):
    TRUE = "true"
    FALSE = "false"


class UserAuthenticationModePropertiesType(str, Enum):
    """
    Type of authentication strategy for this user.
    """
    PASSWORD = "password"
    IAM = "iam"
