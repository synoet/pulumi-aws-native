# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['UserArgs', 'User']

@pulumi.input_type
class UserArgs:
    def __init__(__self__, *,
                 instance_arn: pulumi.Input[str],
                 phone_config: pulumi.Input['UserPhoneConfigArgs'],
                 routing_profile_arn: pulumi.Input[str],
                 security_profile_arns: pulumi.Input[Sequence[pulumi.Input[str]]],
                 username: pulumi.Input[str],
                 directory_user_id: Optional[pulumi.Input[str]] = None,
                 hierarchy_group_arn: Optional[pulumi.Input[str]] = None,
                 identity_info: Optional[pulumi.Input['UserIdentityInfoArgs']] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]] = None,
                 user_proficiencies: Optional[pulumi.Input[Sequence[pulumi.Input['UserProficiencyArgs']]]] = None):
        """
        The set of arguments for constructing a User resource.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input['UserPhoneConfigArgs'] phone_config: The phone settings for the user.
        :param pulumi.Input[str] routing_profile_arn: The identifier of the routing profile for the user.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_profile_arns: One or more security profile arns for the user
        :param pulumi.Input[str] username: The user name for the account.
        :param pulumi.Input[str] directory_user_id: The identifier of the user account in the directory used for identity management.
        :param pulumi.Input[str] hierarchy_group_arn: The identifier of the hierarchy group for the user.
        :param pulumi.Input['UserIdentityInfoArgs'] identity_info: The information about the identity of the user.
        :param pulumi.Input[str] password: The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.
        :param pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]] tags: One or more tags.
        :param pulumi.Input[Sequence[pulumi.Input['UserProficiencyArgs']]] user_proficiencies: One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.
        """
        pulumi.set(__self__, "instance_arn", instance_arn)
        pulumi.set(__self__, "phone_config", phone_config)
        pulumi.set(__self__, "routing_profile_arn", routing_profile_arn)
        pulumi.set(__self__, "security_profile_arns", security_profile_arns)
        pulumi.set(__self__, "username", username)
        if directory_user_id is not None:
            pulumi.set(__self__, "directory_user_id", directory_user_id)
        if hierarchy_group_arn is not None:
            pulumi.set(__self__, "hierarchy_group_arn", hierarchy_group_arn)
        if identity_info is not None:
            pulumi.set(__self__, "identity_info", identity_info)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_proficiencies is not None:
            pulumi.set(__self__, "user_proficiencies", user_proficiencies)

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Input[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @instance_arn.setter
    def instance_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_arn", value)

    @property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> pulumi.Input['UserPhoneConfigArgs']:
        """
        The phone settings for the user.
        """
        return pulumi.get(self, "phone_config")

    @phone_config.setter
    def phone_config(self, value: pulumi.Input['UserPhoneConfigArgs']):
        pulumi.set(self, "phone_config", value)

    @property
    @pulumi.getter(name="routingProfileArn")
    def routing_profile_arn(self) -> pulumi.Input[str]:
        """
        The identifier of the routing profile for the user.
        """
        return pulumi.get(self, "routing_profile_arn")

    @routing_profile_arn.setter
    def routing_profile_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "routing_profile_arn", value)

    @property
    @pulumi.getter(name="securityProfileArns")
    def security_profile_arns(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        One or more security profile arns for the user
        """
        return pulumi.get(self, "security_profile_arns")

    @security_profile_arns.setter
    def security_profile_arns(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "security_profile_arns", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        """
        The user name for the account.
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="directoryUserId")
    def directory_user_id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the user account in the directory used for identity management.
        """
        return pulumi.get(self, "directory_user_id")

    @directory_user_id.setter
    def directory_user_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "directory_user_id", value)

    @property
    @pulumi.getter(name="hierarchyGroupArn")
    def hierarchy_group_arn(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the hierarchy group for the user.
        """
        return pulumi.get(self, "hierarchy_group_arn")

    @hierarchy_group_arn.setter
    def hierarchy_group_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hierarchy_group_arn", value)

    @property
    @pulumi.getter(name="identityInfo")
    def identity_info(self) -> Optional[pulumi.Input['UserIdentityInfoArgs']]:
        """
        The information about the identity of the user.
        """
        return pulumi.get(self, "identity_info")

    @identity_info.setter
    def identity_info(self, value: Optional[pulumi.Input['UserIdentityInfoArgs']]):
        pulumi.set(self, "identity_info", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="userProficiencies")
    def user_proficiencies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UserProficiencyArgs']]]]:
        """
        One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.
        """
        return pulumi.get(self, "user_proficiencies")

    @user_proficiencies.setter
    def user_proficiencies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UserProficiencyArgs']]]]):
        pulumi.set(self, "user_proficiencies", value)


class User(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_user_id: Optional[pulumi.Input[str]] = None,
                 hierarchy_group_arn: Optional[pulumi.Input[str]] = None,
                 identity_info: Optional[pulumi.Input[pulumi.InputType['UserIdentityInfoArgs']]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 phone_config: Optional[pulumi.Input[pulumi.InputType['UserPhoneConfigArgs']]] = None,
                 routing_profile_arn: Optional[pulumi.Input[str]] = None,
                 security_profile_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserTagArgs']]]]] = None,
                 user_proficiencies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserProficiencyArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Connect::User

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] directory_user_id: The identifier of the user account in the directory used for identity management.
        :param pulumi.Input[str] hierarchy_group_arn: The identifier of the hierarchy group for the user.
        :param pulumi.Input[pulumi.InputType['UserIdentityInfoArgs']] identity_info: The information about the identity of the user.
        :param pulumi.Input[str] instance_arn: The identifier of the Amazon Connect instance.
        :param pulumi.Input[str] password: The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.
        :param pulumi.Input[pulumi.InputType['UserPhoneConfigArgs']] phone_config: The phone settings for the user.
        :param pulumi.Input[str] routing_profile_arn: The identifier of the routing profile for the user.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_profile_arns: One or more security profile arns for the user
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserTagArgs']]]] tags: One or more tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserProficiencyArgs']]]] user_proficiencies: One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.
        :param pulumi.Input[str] username: The user name for the account.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Connect::User

        :param str resource_name: The name of the resource.
        :param UserArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 directory_user_id: Optional[pulumi.Input[str]] = None,
                 hierarchy_group_arn: Optional[pulumi.Input[str]] = None,
                 identity_info: Optional[pulumi.Input[pulumi.InputType['UserIdentityInfoArgs']]] = None,
                 instance_arn: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 phone_config: Optional[pulumi.Input[pulumi.InputType['UserPhoneConfigArgs']]] = None,
                 routing_profile_arn: Optional[pulumi.Input[str]] = None,
                 security_profile_arns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserTagArgs']]]]] = None,
                 user_proficiencies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UserProficiencyArgs']]]]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserArgs.__new__(UserArgs)

            __props__.__dict__["directory_user_id"] = directory_user_id
            __props__.__dict__["hierarchy_group_arn"] = hierarchy_group_arn
            __props__.__dict__["identity_info"] = identity_info
            if instance_arn is None and not opts.urn:
                raise TypeError("Missing required property 'instance_arn'")
            __props__.__dict__["instance_arn"] = instance_arn
            __props__.__dict__["password"] = password
            if phone_config is None and not opts.urn:
                raise TypeError("Missing required property 'phone_config'")
            __props__.__dict__["phone_config"] = phone_config
            if routing_profile_arn is None and not opts.urn:
                raise TypeError("Missing required property 'routing_profile_arn'")
            __props__.__dict__["routing_profile_arn"] = routing_profile_arn
            if security_profile_arns is None and not opts.urn:
                raise TypeError("Missing required property 'security_profile_arns'")
            __props__.__dict__["security_profile_arns"] = security_profile_arns
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_proficiencies"] = user_proficiencies
            if username is None and not opts.urn:
                raise TypeError("Missing required property 'username'")
            __props__.__dict__["username"] = username
            __props__.__dict__["user_arn"] = None
        super(User, __self__).__init__(
            'aws-native:connect:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserArgs.__new__(UserArgs)

        __props__.__dict__["directory_user_id"] = None
        __props__.__dict__["hierarchy_group_arn"] = None
        __props__.__dict__["identity_info"] = None
        __props__.__dict__["instance_arn"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["phone_config"] = None
        __props__.__dict__["routing_profile_arn"] = None
        __props__.__dict__["security_profile_arns"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["user_arn"] = None
        __props__.__dict__["user_proficiencies"] = None
        __props__.__dict__["username"] = None
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="directoryUserId")
    def directory_user_id(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the user account in the directory used for identity management.
        """
        return pulumi.get(self, "directory_user_id")

    @property
    @pulumi.getter(name="hierarchyGroupArn")
    def hierarchy_group_arn(self) -> pulumi.Output[Optional[str]]:
        """
        The identifier of the hierarchy group for the user.
        """
        return pulumi.get(self, "hierarchy_group_arn")

    @property
    @pulumi.getter(name="identityInfo")
    def identity_info(self) -> pulumi.Output[Optional['outputs.UserIdentityInfo']]:
        """
        The information about the identity of the user.
        """
        return pulumi.get(self, "identity_info")

    @property
    @pulumi.getter(name="instanceArn")
    def instance_arn(self) -> pulumi.Output[str]:
        """
        The identifier of the Amazon Connect instance.
        """
        return pulumi.get(self, "instance_arn")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="phoneConfig")
    def phone_config(self) -> pulumi.Output['outputs.UserPhoneConfig']:
        """
        The phone settings for the user.
        """
        return pulumi.get(self, "phone_config")

    @property
    @pulumi.getter(name="routingProfileArn")
    def routing_profile_arn(self) -> pulumi.Output[str]:
        """
        The identifier of the routing profile for the user.
        """
        return pulumi.get(self, "routing_profile_arn")

    @property
    @pulumi.getter(name="securityProfileArns")
    def security_profile_arns(self) -> pulumi.Output[Sequence[str]]:
        """
        One or more security profile arns for the user
        """
        return pulumi.get(self, "security_profile_arns")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.UserTag']]]:
        """
        One or more tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="userArn")
    def user_arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) for the user.
        """
        return pulumi.get(self, "user_arn")

    @property
    @pulumi.getter(name="userProficiencies")
    def user_proficiencies(self) -> pulumi.Output[Optional[Sequence['outputs.UserProficiency']]]:
        """
        One or more predefined attributes assigned to a user, with a level that indicates how skilled they are.
        """
        return pulumi.get(self, "user_proficiencies")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[str]:
        """
        The user name for the account.
        """
        return pulumi.get(self, "username")

