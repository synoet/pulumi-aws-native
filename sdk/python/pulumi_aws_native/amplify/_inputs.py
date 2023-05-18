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
    'AppAutoBranchCreationConfigArgs',
    'AppBasicAuthConfigArgs',
    'AppCustomRuleArgs',
    'AppEnvironmentVariableArgs',
    'AppTagArgs',
    'BranchBasicAuthConfigArgs',
    'BranchEnvironmentVariableArgs',
    'BranchTagArgs',
    'DomainSubDomainSettingArgs',
]

@pulumi.input_type
class AppAutoBranchCreationConfigArgs:
    def __init__(__self__, *,
                 auto_branch_creation_patterns: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 basic_auth_config: Optional[pulumi.Input['AppBasicAuthConfigArgs']] = None,
                 build_spec: Optional[pulumi.Input[str]] = None,
                 enable_auto_branch_creation: Optional[pulumi.Input[bool]] = None,
                 enable_auto_build: Optional[pulumi.Input[bool]] = None,
                 enable_performance_mode: Optional[pulumi.Input[bool]] = None,
                 enable_pull_request_preview: Optional[pulumi.Input[bool]] = None,
                 environment_variables: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]] = None,
                 framework: Optional[pulumi.Input[str]] = None,
                 pull_request_environment_name: Optional[pulumi.Input[str]] = None,
                 stage: Optional[pulumi.Input['AppAutoBranchCreationConfigStage']] = None):
        if auto_branch_creation_patterns is not None:
            pulumi.set(__self__, "auto_branch_creation_patterns", auto_branch_creation_patterns)
        if basic_auth_config is not None:
            pulumi.set(__self__, "basic_auth_config", basic_auth_config)
        if build_spec is not None:
            pulumi.set(__self__, "build_spec", build_spec)
        if enable_auto_branch_creation is not None:
            pulumi.set(__self__, "enable_auto_branch_creation", enable_auto_branch_creation)
        if enable_auto_build is not None:
            pulumi.set(__self__, "enable_auto_build", enable_auto_build)
        if enable_performance_mode is not None:
            pulumi.set(__self__, "enable_performance_mode", enable_performance_mode)
        if enable_pull_request_preview is not None:
            pulumi.set(__self__, "enable_pull_request_preview", enable_pull_request_preview)
        if environment_variables is not None:
            pulumi.set(__self__, "environment_variables", environment_variables)
        if framework is not None:
            pulumi.set(__self__, "framework", framework)
        if pull_request_environment_name is not None:
            pulumi.set(__self__, "pull_request_environment_name", pull_request_environment_name)
        if stage is not None:
            pulumi.set(__self__, "stage", stage)

    @property
    @pulumi.getter(name="autoBranchCreationPatterns")
    def auto_branch_creation_patterns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "auto_branch_creation_patterns")

    @auto_branch_creation_patterns.setter
    def auto_branch_creation_patterns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "auto_branch_creation_patterns", value)

    @property
    @pulumi.getter(name="basicAuthConfig")
    def basic_auth_config(self) -> Optional[pulumi.Input['AppBasicAuthConfigArgs']]:
        return pulumi.get(self, "basic_auth_config")

    @basic_auth_config.setter
    def basic_auth_config(self, value: Optional[pulumi.Input['AppBasicAuthConfigArgs']]):
        pulumi.set(self, "basic_auth_config", value)

    @property
    @pulumi.getter(name="buildSpec")
    def build_spec(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "build_spec")

    @build_spec.setter
    def build_spec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "build_spec", value)

    @property
    @pulumi.getter(name="enableAutoBranchCreation")
    def enable_auto_branch_creation(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_auto_branch_creation")

    @enable_auto_branch_creation.setter
    def enable_auto_branch_creation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_auto_branch_creation", value)

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
    def environment_variables(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]:
        return pulumi.get(self, "environment_variables")

    @environment_variables.setter
    def environment_variables(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AppEnvironmentVariableArgs']]]]):
        pulumi.set(self, "environment_variables", value)

    @property
    @pulumi.getter
    def framework(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "framework")

    @framework.setter
    def framework(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "framework", value)

    @property
    @pulumi.getter(name="pullRequestEnvironmentName")
    def pull_request_environment_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "pull_request_environment_name")

    @pull_request_environment_name.setter
    def pull_request_environment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pull_request_environment_name", value)

    @property
    @pulumi.getter
    def stage(self) -> Optional[pulumi.Input['AppAutoBranchCreationConfigStage']]:
        return pulumi.get(self, "stage")

    @stage.setter
    def stage(self, value: Optional[pulumi.Input['AppAutoBranchCreationConfigStage']]):
        pulumi.set(self, "stage", value)


@pulumi.input_type
class AppBasicAuthConfigArgs:
    def __init__(__self__, *,
                 enable_basic_auth: Optional[pulumi.Input[bool]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        if enable_basic_auth is not None:
            pulumi.set(__self__, "enable_basic_auth", enable_basic_auth)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_basic_auth")

    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_basic_auth", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


@pulumi.input_type
class AppCustomRuleArgs:
    def __init__(__self__, *,
                 source: pulumi.Input[str],
                 target: pulumi.Input[str],
                 condition: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "source", source)
        pulumi.set(__self__, "target", target)
        if condition is not None:
            pulumi.set(__self__, "condition", condition)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def target(self) -> pulumi.Input[str]:
        return pulumi.get(self, "target")

    @target.setter
    def target(self, value: pulumi.Input[str]):
        pulumi.set(self, "target", value)

    @property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "condition")

    @condition.setter
    def condition(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "condition", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class AppEnvironmentVariableArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class AppTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class BranchBasicAuthConfigArgs:
    def __init__(__self__, *,
                 password: pulumi.Input[str],
                 username: pulumi.Input[str],
                 enable_basic_auth: Optional[pulumi.Input[bool]] = None):
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)
        if enable_basic_auth is not None:
            pulumi.set(__self__, "enable_basic_auth", enable_basic_auth)

    @property
    @pulumi.getter
    def password(self) -> pulumi.Input[str]:
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: pulumi.Input[str]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def username(self) -> pulumi.Input[str]:
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: pulumi.Input[str]):
        pulumi.set(self, "username", value)

    @property
    @pulumi.getter(name="enableBasicAuth")
    def enable_basic_auth(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "enable_basic_auth")

    @enable_basic_auth.setter
    def enable_basic_auth(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_basic_auth", value)


@pulumi.input_type
class BranchEnvironmentVariableArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class BranchTagArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 value: pulumi.Input[str]):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class DomainSubDomainSettingArgs:
    def __init__(__self__, *,
                 branch_name: pulumi.Input[str],
                 prefix: pulumi.Input[str]):
        pulumi.set(__self__, "branch_name", branch_name)
        pulumi.set(__self__, "prefix", prefix)

    @property
    @pulumi.getter(name="branchName")
    def branch_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "branch_name")

    @branch_name.setter
    def branch_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "branch_name", value)

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Input[str]:
        return pulumi.get(self, "prefix")

    @prefix.setter
    def prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "prefix", value)


