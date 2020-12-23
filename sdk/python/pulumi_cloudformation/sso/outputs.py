# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from .. import outputs as _root_outputs

__all__ = [
    'AssignmentAttributes',
    'AssignmentProperties',
    'InstanceAccessControlAttributeConfigurationAttributes',
    'InstanceAccessControlAttributeConfigurationProperties',
    'PermissionSetAttributes',
    'PermissionSetProperties',
]

@pulumi.output_type
class AssignmentAttributes(dict):
    def __init__(__self__):
        pass

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class AssignmentProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
    """
    def __init__(__self__, *,
                 instance_arn: str,
                 permission_set_arn: str,
                 principal_id: str,
                 principal_type: str,
                 target_id: str,
                 target_type: str):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html
        :param str instance_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        :param str permission_set_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        :param str principal_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        :param str principal_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        :param str target_id: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        :param str target_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        pulumi.set(__self__, "permission_set_arn", permission_set_arn)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "principal_type", principal_type)
        pulumi.set(__self__, "target_id", target_id)
        pulumi.set(__self__, "target_type", target_type)

    @property
    @pulumi.getter(name="InstanceArn")
    def instance_arn(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-instancearn
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="PermissionSetArn")
    def permission_set_arn(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-permissionsetarn
        """
        return pulumi.get(self, "permission_set_arn")

    @property
    @pulumi.getter(name="PrincipalId")
    def principal_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principalid
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="PrincipalType")
    def principal_type(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-principaltype
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="TargetId")
    def target_id(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targetid
        """
        return pulumi.get(self, "target_id")

    @property
    @pulumi.getter(name="TargetType")
    def target_type(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-assignment.html#cfn-sso-assignment-targettype
        """
        return pulumi.get(self, "target_type")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceAccessControlAttributeConfigurationAttributes(dict):
    def __init__(__self__):
        pass

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class InstanceAccessControlAttributeConfigurationProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
    """
    def __init__(__self__, *,
                 instance_access_control_attribute_configuration: str,
                 instance_arn: str):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html
        :param Union[Any, str] instance_access_control_attribute_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration
        :param str instance_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        """
        pulumi.set(__self__, "instance_access_control_attribute_configuration", instance_access_control_attribute_configuration)
        pulumi.set(__self__, "instance_arn", instance_arn)

    @property
    @pulumi.getter(name="InstanceAccessControlAttributeConfiguration")
    def instance_access_control_attribute_configuration(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instanceaccesscontrolattributeconfiguration
        """
        return pulumi.get(self, "instance_access_control_attribute_configuration")

    @property
    @pulumi.getter(name="InstanceArn")
    def instance_arn(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-instanceaccesscontrolattributeconfiguration.html#cfn-sso-instanceaccesscontrolattributeconfiguration-instancearn
        """
        return pulumi.get(self, "instance_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PermissionSetAttributes(dict):
    def __init__(__self__, *,
                 permission_set_arn: str):
        pulumi.set(__self__, "permission_set_arn", permission_set_arn)

    @property
    @pulumi.getter(name="PermissionSetArn")
    def permission_set_arn(self) -> str:
        return pulumi.get(self, "permission_set_arn")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


@pulumi.output_type
class PermissionSetProperties(dict):
    """
    http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
    """
    def __init__(__self__, *,
                 instance_arn: str,
                 name: str,
                 description: Optional[str] = None,
                 inline_policy: Optional[str] = None,
                 managed_policies: Optional[Sequence[str]] = None,
                 relay_state_type: Optional[str] = None,
                 session_duration: Optional[str] = None,
                 tags: Optional[Sequence['_root_outputs.Tag']] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html
        :param str instance_arn: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        :param str name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        :param str description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        :param str inline_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        :param Sequence[str] managed_policies: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        :param str relay_state_type: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        :param str session_duration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        :param Sequence['_root_inputs.TagArgs'] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        pulumi.set(__self__, "name", name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if inline_policy is not None:
            pulumi.set(__self__, "inline_policy", inline_policy)
        if managed_policies is not None:
            pulumi.set(__self__, "managed_policies", managed_policies)
        if relay_state_type is not None:
            pulumi.set(__self__, "relay_state_type", relay_state_type)
        if session_duration is not None:
            pulumi.set(__self__, "session_duration", session_duration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="InstanceArn")
    def instance_arn(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-instancearn
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter(name="Name")
    def name(self) -> str:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="Description")
    def description(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="InlinePolicy")
    def inline_policy(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-inlinepolicy
        """
        return pulumi.get(self, "inline_policy")

    @property
    @pulumi.getter(name="ManagedPolicies")
    def managed_policies(self) -> Optional[Sequence[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-managedpolicies
        """
        return pulumi.get(self, "managed_policies")

    @property
    @pulumi.getter(name="RelayStateType")
    def relay_state_type(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-relaystatetype
        """
        return pulumi.get(self, "relay_state_type")

    @property
    @pulumi.getter(name="SessionDuration")
    def session_duration(self) -> Optional[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-sessionduration
        """
        return pulumi.get(self, "session_duration")

    @property
    @pulumi.getter(name="Tags")
    def tags(self) -> Optional[Sequence['_root_outputs.Tag']]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sso-permissionset.html#cfn-sso-permissionset-tags
        """
        return pulumi.get(self, "tags")

    def _translate_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop


