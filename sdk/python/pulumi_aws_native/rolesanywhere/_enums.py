# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'TrustAnchorType',
]


class TrustAnchorType(str, Enum):
    AWS_ACM_PCA = "AWS_ACM_PCA"
    CERTIFICATE_BUNDLE = "CERTIFICATE_BUNDLE"
    SELF_SIGNED_REPOSITORY = "SELF_SIGNED_REPOSITORY"
