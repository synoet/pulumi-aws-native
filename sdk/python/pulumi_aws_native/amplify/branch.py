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

__all__ = ['BranchArgs', 'Branch']

@pulumi.input_type
class BranchArgs:
    def __init__(__self__, *,
                 app_id: pulumi.Input[str],
                 basic_auth_config: Optional[pulumi.Input['BranchBasicAuthConfigArgs']] = None,
                 branch_name: Optional[pulumi.Input[str]] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_auto_build: Optional[pulumi.Input[bool]] = None,
                 enable_performance_mode: Optional[pulumi.Input[bool]] = None,
                 enable_pull_request_preview: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['BranchEnvironmentVariableArgs']]]] = None,
                 pull_request_environment_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input['BranchStage']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['BranchTagArgs']]]] = None):
        """
        The set of arguments for constructing a Branch resource.
        """
        pulumi.set(__self__, "app_id", app_id)
        if basic_auth_config is not None:
            pulumi.set(__self__, "basic_auth_config", basic_auth_config)
        if branch_name is not None:
            pulumi.set(__self__, "branch_name", branch_name)
        if build_spec is not None:
            pulumi.set(__self__, "build_spec", build_spec)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if enable_auto_build is not None:
            pulumi.set(__self__, "enable_auto_build", enable_auto_build)
        if enable_performance_mode is not None:
            pulumi.set(__self__, "enable_performance_mode", enable_performance_mode)
        if enable_pull_request_preview is not None:
            pulumi.set(__self__, "enable_pull_request_preview", enable_pull_request_preview)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if pull_request_environment_name is not None:
            pulumi.set(__self__, "pull_request_environment_name", pull_request_environment_name)
        if stage is not None:
            pulumi.set(__self__, "stage", stage)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "app_id")

    @app_id.setter
    def app_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "app_id", value)

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> Optional[pulumi.Input['BranchBasicAuthConfigArgs']]:
        return pulumi.get(self, "basic_auth_config")

    @basic_auth_config.setter
    def basic_auth_config(self, value: Optional[pulumi.Input['BranchBasicAuthConfigArgs']]):
        pulumi.set(self, "basic_auth_config", value)

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "branch_name")

    @branch_name.setter
    def branch_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "branch_name", value)

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "build_spec")

    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_spec", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_auto_build")

    @enable_auto_build.setter
    def enable_auto_build(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto_build", value)

    @property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_performance_mode")

    @enable_performance_mode.setter
    def enable_performance_mode(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_performance_mode", value)

    @property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_pull_request_preview")

    @enable_pull_request_preview.setter
    def enable_pull_request_preview(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_pull_request_preview", value)

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchEnvironmentVariableArgs']]]]:
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchEnvironmentVariableArgs']]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pull_request_environment_name")

    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pull_request_environment_name", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input['BranchStage']]:
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input['BranchStage']]):
        pulumi.set(self, "stage", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['BranchTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['BranchTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Branch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 basic_auth_config: Optional[pulumi.Input[pulumi.InputType['BranchBasicAuthConfigArgs']]] = None,
                 branch_name: Optional[pulumi.Input[str]] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_auto_build: Optional[pulumi.Input[bool]] = None,
                 enable_performance_mode: Optional[pulumi.Input[bool]] = None,
                 enable_pull_request_preview: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchEnvironmentVariableArgs']]]]] = None,
                 pull_request_environment_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input['BranchStage']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::Amplify::Branch resource creates a new branch within an app.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BranchArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::Amplify::Branch resource creates a new branch within an app.

        :param str resource_name: The name of the resource.
        :param BranchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BranchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 app_id: Optional[pulumi.Input[str]] = None,
                 basic_auth_config: Optional[pulumi.Input[pulumi.InputType['BranchBasicAuthConfigArgs']]] = None,
                 branch_name: Optional[pulumi.Input[str]] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 enable_auto_build: Optional[pulumi.Input[bool]] = None,
                 enable_performance_mode: Optional[pulumi.Input[bool]] = None,
                 enable_pull_request_preview: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchEnvironmentVariableArgs']]]]] = None,
                 pull_request_environment_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input['BranchStage']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['BranchTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BranchArgs.__new__(BranchArgs)

            if app_id is None and not opts.urn:
                raise TypeError("Missing required property 'app_id'")
            __props__.__dict__["app_id"] = app_id
            __props__.__dict__["basic_auth_config"] = basic_auth_config
            __props__.__dict__["branch_name"] = branch_name
            __props__.__dict__["build_spec"] = build_spec
            __props__.__dict__["description"] = description
            __props__.__dict__["enable_auto_build"] = enable_auto_build
            __props__.__dict__["enable_performance_mode"] = enable_performance_mode
            __props__.__dict__["enable_pull_request_preview"] = enable_pull_request_preview
            __props__.__dict__["environment_variables"] = environment_variables
            __props__.__dict__["pull_request_environment_name"] = pull_request_environment_name
            __props__.__dict__["stage"] = stage
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(Branch, __self__).__init__(
            'aws-native:amplify:Branch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Branch':
        """
        Get an existing Branch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BranchArgs.__new__(BranchArgs)

        __props__.__dict__["app_id"] = None
        __props__.__dict__["arn"] = None
        __props__.__dict__["basic_auth_config"] = None
        __props__.__dict__["branch_name"] = None
        __props__.__dict__["build_spec"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["enable_auto_build"] = None
        __props__.__dict__["enable_performance_mode"] = None
        __props__.__dict__["enable_pull_request_preview"] = None
        __props__.__dict__["environment_variables"] = None
        __props__.__dict__["pull_request_environment_name"] = None
        __props__.__dict__["stage"] = None
        __props__.__dict__["tags"] = None
        return Branch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> pulumi.Output[Optional['outputs.BranchBasicAuthConfig']]:
        return pulumi.get(self, "basic_auth_config")

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "branch_name")

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "build_spec")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="enableAutoBuild")
    def enable_auto_build(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_auto_build")

    @property
    @pulumi.getter(name="enablePerformanceMode")
    def enable_performance_mode(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_performance_mode")

    @property
    @pulumi.getter(name="enablePullRequestPreview")
    def enable_pull_request_preview(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "enable_pull_request_preview")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> pulumi.Output[Optional[Sequence['outputs.BranchEnvironmentVariable']]]:
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "pull_request_environment_name")

    @property
    @pulumi.getter
    def stage(self) -> pulumi.Output[Optional['BranchStage']]:
        return pulumi.get(self, "stage")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.BranchTag']]]:
        return pulumi.get(self, "tags")

