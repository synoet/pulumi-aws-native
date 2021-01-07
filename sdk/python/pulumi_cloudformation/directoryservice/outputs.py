# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs

__all__ = [
    'MicrosoftADAttributes',
    'MicrosoftADProperties',
    'MicrosoftADVpcSettings',
    'SimpleADAttributes',
    'SimpleADProperties',
    'SimpleADVpcSettings',
]

@pulumi.output_type
class MicrosoftADAttributes(dict):
    def __init__(__self__, *,
                 alias: str,
                 dns_ip_addresses: Sequence[str]):
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "dns_ip_addresses", dns_ip_addresses)

    @property
    @pulumi.getter(name="Alias")
    def alias(self) -> str:
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="DnsIpAddresses")
    def dns_ip_addresses(self) -> Sequence[str]:
        return pulumi.get(self, "dns_ip_addresses")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MicrosoftADProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
    """
    def __init__(__self__, *,
                 name: str,
                 password: str,
                 vpc_settings: 'outputs.MicrosoftADVpcSettings',
                 create_alias: Optional[bool] = None,
                 edition: Optional[str] = None,
                 enable_sso: Optional[bool] = None,
                 short_name: Optional[str] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html
        :param str name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        :param str password: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        :param 'MicrosoftADVpcSettingsArgs' vpc_settings: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        :param bool create_alias: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        :param str edition: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        :param bool enable_sso: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        :param str short_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "vpc_settings", vpc_settings)
        if create_alias is not None:
            pulumi.set(__self__, "create_alias", create_alias)
        if edition is not None:
            pulumi.set(__self__, "edition", edition)
        if enable_sso is not None:
            pulumi.set(__self__, "enable_sso", enable_sso)
        if short_name is not None:
            pulumi.set(__self__, "short_name", short_name)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="Password")
    def password(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="VpcSettings")
    def vpc_settings(self) -> 'outputs.MicrosoftADVpcSettings':
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-vpcsettings
        """
        return pulumi.get(self, "vpc_settings")

    @property
    @pulumi.getter(name="CreateAlias")
    def create_alias(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-createalias
        """
        return pulumi.get(self, "create_alias")

    @property
    @pulumi.getter(name="Edition")
    def edition(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-edition
        """
        return pulumi.get(self, "edition")

    @property
    @pulumi.getter(name="EnableSso")
    def enable_sso(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-enablesso
        """
        return pulumi.get(self, "enable_sso")

    @property
    @pulumi.getter(name="ShortName")
    def short_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-microsoftad.html#cfn-directoryservice-microsoftad-shortname
        """
        return pulumi.get(self, "short_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class MicrosoftADVpcSettings(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
    """
    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html
        :param Sequence[str] subnet_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
        :param str vpc_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
        """
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="SubnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-subnetids
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="VpcId")
    def vpc_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-microsoftad-vpcsettings.html#cfn-directoryservice-microsoftad-vpcsettings-vpcid
        """
        return pulumi.get(self, "vpc_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SimpleADAttributes(dict):
    def __init__(__self__, *,
                 alias: str,
                 dns_ip_addresses: Sequence[str]):
        pulumi.set(__self__, "alias", alias)
        pulumi.set(__self__, "dns_ip_addresses", dns_ip_addresses)

    @property
    @pulumi.getter(name="Alias")
    def alias(self) -> str:
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="DnsIpAddresses")
    def dns_ip_addresses(self) -> Sequence[str]:
        return pulumi.get(self, "dns_ip_addresses")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SimpleADProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
    """
    def __init__(__self__, *,
                 name: str,
                 password: str,
                 size: str,
                 vpc_settings: 'outputs.SimpleADVpcSettings',
                 create_alias: Optional[bool] = None,
                 description: Optional[str] = None,
                 enable_sso: Optional[bool] = None,
                 short_name: Optional[str] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html
        :param str name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        :param str password: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        :param str size: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        :param 'SimpleADVpcSettingsArgs' vpc_settings: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        :param bool create_alias: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        :param str description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        :param bool enable_sso: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        :param str short_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "size", size)
        pulumi.set(__self__, "vpc_settings", vpc_settings)
        if create_alias is not None:
            pulumi.set(__self__, "create_alias", create_alias)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_sso is not None:
            pulumi.set(__self__, "enable_sso", enable_sso)
        if short_name is not None:
            pulumi.set(__self__, "short_name", short_name)

    @property
    @pulumi.getter(name="Name")
    def name(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="Password")
    def password(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="Size")
    def size(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-size
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="VpcSettings")
    def vpc_settings(self) -> 'outputs.SimpleADVpcSettings':
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-vpcsettings
        """
        return pulumi.get(self, "vpc_settings")

    @property
    @pulumi.getter(name="CreateAlias")
    def create_alias(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-createalias
        """
        return pulumi.get(self, "create_alias")

    @property
    @pulumi.getter(name="Description")
    def description(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="EnableSso")
    def enable_sso(self) -> Optional[bool]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-enablesso
        """
        return pulumi.get(self, "enable_sso")

    @property
    @pulumi.getter(name="ShortName")
    def short_name(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-directoryservice-simplead.html#cfn-directoryservice-simplead-shortname
        """
        return pulumi.get(self, "short_name")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class SimpleADVpcSettings(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
    """
    def __init__(__self__, *,
                 subnet_ids: Sequence[str],
                 vpc_id: str):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html
        :param Sequence[str] subnet_ids: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
        :param str vpc_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
        """
        pulumi.set(__self__, "subnet_ids", subnet_ids)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="SubnetIds")
    def subnet_ids(self) -> Sequence[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-subnetids
        """
        return pulumi.get(self, "subnet_ids")

    @property
    @pulumi.getter(name="VpcId")
    def vpc_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-directoryservice-simplead-vpcsettings.html#cfn-directoryservice-simplead-vpcsettings-vpcid
        """
        return pulumi.get(self, "vpc_id")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

