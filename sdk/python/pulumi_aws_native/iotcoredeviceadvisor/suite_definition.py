# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from .. import _inputs as _root_inputs
from .. import outputs as _root_outputs

__all__ = ['SuiteDefinitionArgs', 'SuiteDefinition']

@pulumi.input_type
class SuiteDefinitionArgs:
    def __init__(__self__, *,
                 suite_definition_configuration: pulumi.Input[Union[Any, str]],
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a SuiteDefinition resource.
        :param pulumi.Input[Union[Any, str]] suite_definition_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        """
        pulumi.set(__self__, "suite_definition_configuration", suite_definition_configuration)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="suiteDefinitionConfiguration")
    def suite_definition_configuration(self) -> pulumi.Input[Union[Any, str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        """
        return pulumi.get(self, "suite_definition_configuration")

    @suite_definition_configuration.setter
    def suite_definition_configuration(self, value: pulumi.Input[Union[Any, str]]):
        pulumi.set(self, "suite_definition_configuration", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class SuiteDefinition(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 suite_definition_configuration: Optional[pulumi.Input[Union[Any, str]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[Any, str]] suite_definition_configuration: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SuiteDefinitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html

        :param str resource_name: The name of the resource.
        :param SuiteDefinitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SuiteDefinitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 suite_definition_configuration: Optional[pulumi.Input[Union[Any, str]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SuiteDefinitionArgs.__new__(SuiteDefinitionArgs)

            if suite_definition_configuration is None and not opts.urn:
                raise TypeError("Missing required property 'suite_definition_configuration'")
            __props__.__dict__["suite_definition_configuration"] = suite_definition_configuration
            __props__.__dict__["tags"] = tags
            __props__.__dict__["suite_definition_arn"] = None
            __props__.__dict__["suite_definition_id"] = None
            __props__.__dict__["suite_definition_version"] = None
        super(SuiteDefinition, __self__).__init__(
            'aws-native:iotcoredeviceadvisor:SuiteDefinition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SuiteDefinition':
        """
        Get an existing SuiteDefinition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SuiteDefinitionArgs.__new__(SuiteDefinitionArgs)

        __props__.__dict__["suite_definition_arn"] = None
        __props__.__dict__["suite_definition_configuration"] = None
        __props__.__dict__["suite_definition_id"] = None
        __props__.__dict__["suite_definition_version"] = None
        __props__.__dict__["tags"] = None
        return SuiteDefinition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="suiteDefinitionArn")
    def suite_definition_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "suite_definition_arn")

    @property
    @pulumi.getter(name="suiteDefinitionConfiguration")
    def suite_definition_configuration(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-suitedefinitionconfiguration
        """
        return pulumi.get(self, "suite_definition_configuration")

    @property
    @pulumi.getter(name="suiteDefinitionId")
    def suite_definition_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "suite_definition_id")

    @property
    @pulumi.getter(name="suiteDefinitionVersion")
    def suite_definition_version(self) -> pulumi.Output[str]:
        return pulumi.get(self, "suite_definition_version")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iotcoredeviceadvisor-suitedefinition.html#cfn-iotcoredeviceadvisor-suitedefinition-tags
        """
        return pulumi.get(self, "tags")

