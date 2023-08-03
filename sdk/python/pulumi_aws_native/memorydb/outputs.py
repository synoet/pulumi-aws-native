# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AclTag',
    'AuthenticationModeProperties',
    'ClusterEndpoint',
    'ClusterTag',
    'ParameterGroupTag',
    'SubnetGroupTag',
    'UserTag',
]

@pulumi.output_type
class AclTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: Optional[str] = None):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class AuthenticationModeProperties(dict):
    def __init__(__self__, *,
                 passwords: Optional[Sequence[str]] = None,
                 type: Optional['UserAuthenticationModePropertiesType'] = None):
        """
        :param Sequence[str] passwords: Passwords used for this user account. You can create up to two passwords for each user.
        :param 'UserAuthenticationModePropertiesType' type: Type of authentication strategy for this user.
        """
        if passwords is not None:
            pulumi.set(__self__, "passwords", passwords)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def passwords(self) -> Optional[Sequence[str]]:
        """
        Passwords used for this user account. You can create up to two passwords for each user.
        """
        return pulumi.get(self, "passwords")

    @property
    @pulumi.getter
    def type(self) -> Optional['UserAuthenticationModePropertiesType']:
        """
        Type of authentication strategy for this user.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ClusterEndpoint(dict):
    def __init__(__self__, *,
                 address: Optional[str] = None,
                 port: Optional[int] = None):
        """
        :param str address: The DNS address of the primary read-write node.
        :param int port: The port number that the engine is listening on. 
        """
        if address is not None:
            pulumi.set(__self__, "address", address)
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter
    def address(self) -> Optional[str]:
        """
        The DNS address of the primary read-write node.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        """
        The port number that the engine is listening on. 
        """
        return pulumi.get(self, "port")


@pulumi.output_type
class ClusterTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for the tag. May not be null.
        :param str value: The tag's value. May be null.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for the tag. May not be null.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The tag's value. May be null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class ParameterGroupTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for the tag. May not be null.
        :param str value: The tag's value. May be null.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for the tag. May not be null.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The tag's value. May be null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class SubnetGroupTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key for the tag. May not be null.
        :param str value: The tag's value. May be null.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key for the tag. May not be null.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The tag's value. May be null.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class UserTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: Optional[str] = None):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        :param str value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with 'aws:'. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
        """
        return pulumi.get(self, "value")


