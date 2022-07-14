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

__all__ = [
    'GetStudioComponentResult',
    'AwaitableGetStudioComponentResult',
    'get_studio_component',
    'get_studio_component_output',
]

@pulumi.output_type
class GetStudioComponentResult:
    def __init__(__self__, configuration=None, description=None, ec2_security_group_ids=None, initialization_scripts=None, name=None, script_parameters=None, studio_component_id=None, type=None):
        if configuration and not isinstance(configuration, dict):
            raise TypeError("Expected argument 'configuration' to be a dict")
        pulumi.set(__self__, "configuration", configuration)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if ec2_security_group_ids and not isinstance(ec2_security_group_ids, list):
            raise TypeError("Expected argument 'ec2_security_group_ids' to be a list")
        pulumi.set(__self__, "ec2_security_group_ids", ec2_security_group_ids)
        if initialization_scripts and not isinstance(initialization_scripts, list):
            raise TypeError("Expected argument 'initialization_scripts' to be a list")
        pulumi.set(__self__, "initialization_scripts", initialization_scripts)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if script_parameters and not isinstance(script_parameters, list):
            raise TypeError("Expected argument 'script_parameters' to be a list")
        pulumi.set(__self__, "script_parameters", script_parameters)
        if studio_component_id and not isinstance(studio_component_id, str):
            raise TypeError("Expected argument 'studio_component_id' to be a str")
        pulumi.set(__self__, "studio_component_id", studio_component_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def configuration(self) -> Optional['outputs.StudioComponentConfiguration']:
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        <p>The description.</p>
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ec2SecurityGroupIds")
    def ec2_security_group_ids(self) -> Optional[Sequence[str]]:
        """
        <p>The EC2 security groups that control access to the studio component.</p>
        """
        return pulumi.get(self, "ec2_security_group_ids")

    @property
    @pulumi.getter(name="initializationScripts")
    def initialization_scripts(self) -> Optional[Sequence['outputs.StudioComponentInitializationScript']]:
        """
        <p>Initialization scripts for studio components.</p>
        """
        return pulumi.get(self, "initialization_scripts")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        <p>The name for the studio component.</p>
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scriptParameters")
    def script_parameters(self) -> Optional[Sequence['outputs.StudioComponentScriptParameterKeyValue']]:
        """
        <p>Parameters for the studio component scripts.</p>
        """
        return pulumi.get(self, "script_parameters")

    @property
    @pulumi.getter(name="studioComponentId")
    def studio_component_id(self) -> Optional[str]:
        return pulumi.get(self, "studio_component_id")

    @property
    @pulumi.getter
    def type(self) -> Optional['StudioComponentType']:
        return pulumi.get(self, "type")


class AwaitableGetStudioComponentResult(GetStudioComponentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetStudioComponentResult(
            configuration=self.configuration,
            description=self.description,
            ec2_security_group_ids=self.ec2_security_group_ids,
            initialization_scripts=self.initialization_scripts,
            name=self.name,
            script_parameters=self.script_parameters,
            studio_component_id=self.studio_component_id,
            type=self.type)


def get_studio_component(studio_component_id: Optional[str] = None,
                         studio_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetStudioComponentResult:
    """
    Represents a studio component which connects a non-Nimble Studio resource in your account to your studio


    :param str studio_id: <p>The studioId. </p>
    """
    __args__ = dict()
    __args__['studioComponentId'] = studio_component_id
    __args__['studioId'] = studio_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:nimblestudio:getStudioComponent', __args__, opts=opts, typ=GetStudioComponentResult).value

    return AwaitableGetStudioComponentResult(
        configuration=__ret__.configuration,
        description=__ret__.description,
        ec2_security_group_ids=__ret__.ec2_security_group_ids,
        initialization_scripts=__ret__.initialization_scripts,
        name=__ret__.name,
        script_parameters=__ret__.script_parameters,
        studio_component_id=__ret__.studio_component_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_studio_component)
def get_studio_component_output(studio_component_id: Optional[pulumi.Input[str]] = None,
                                studio_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetStudioComponentResult]:
    """
    Represents a studio component which connects a non-Nimble Studio resource in your account to your studio


    :param str studio_id: <p>The studioId. </p>
    """
    ...
