# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'RepositoryEncryptionType',
    'RepositoryImageTagMutability',
]


class RepositoryEncryptionType(str, Enum):
    """
    The encryption type to use.
    """
    AES256 = "AES256"
    KMS = "KMS"


class RepositoryImageTagMutability(str, Enum):
    """
    The image tag mutability setting for the repository.
    """
    MUTABLE = "MUTABLE"
    IMMUTABLE = "IMMUTABLE"
