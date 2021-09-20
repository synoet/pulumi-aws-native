# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'RepositoryAssociationType',
]


class RepositoryAssociationType(str, Enum):
    """
    The type of repository to be associated.
    """
    CODE_COMMIT = "CodeCommit"
    BITBUCKET = "Bitbucket"
    GIT_HUB_ENTERPRISE_SERVER = "GitHubEnterpriseServer"
    S3_BUCKET = "S3Bucket"
