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

__all__ = ['ModelPackageGroupArgs', 'ModelPackageGroup']

@pulumi.input_type
class ModelPackageGroupArgs:
    def __init__(__self__, *,
                 model_package_group_name: pulumi.Input[str],
                 model_package_group_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_policy: Optional[pulumi.Input[Union[Any, str]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]] = None):
        """
        The set of arguments for constructing a ModelPackageGroup resource.
        :param pulumi.Input[str] model_package_group_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        :param pulumi.Input[str] model_package_group_description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        :param pulumi.Input[Union[Any, str]] model_package_group_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        :param pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        pulumi.set(__self__, "model_package_group_name", model_package_group_name)
        if model_package_group_description is not None:
            pulumi.set(__self__, "model_package_group_description", model_package_group_description)
        if model_package_group_policy is not None:
            pulumi.set(__self__, "model_package_group_policy", model_package_group_policy)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> pulumi.Input[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        """
        return pulumi.get(self, "model_package_group_name")

    @model_package_group_name.setter
    def model_package_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "model_package_group_name", value)

    @property
    @pulumi.getter(name="modelPackageGroupDescription")
    def model_package_group_description(self) -> Optional[pulumi.Input[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        """
        return pulumi.get(self, "model_package_group_description")

    @model_package_group_description.setter
    def model_package_group_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_package_group_description", value)

    @property
    @pulumi.getter(name="modelPackageGroupPolicy")
    def model_package_group_policy(self) -> Optional[pulumi.Input[Union[Any, str]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        """
        return pulumi.get(self, "model_package_group_policy")

    @model_package_group_policy.setter
    def model_package_group_policy(self, value: Optional[pulumi.Input[Union[Any, str]]]):
        pulumi.set(self, "model_package_group_policy", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['_root_inputs.TagArgs']]]]):
        pulumi.set(self, "tags", value)


class ModelPackageGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 model_package_group_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_name: Optional[pulumi.Input[str]] = None,
                 model_package_group_policy: Optional[pulumi.Input[Union[Any, str]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]]] = None,
                 __props__=None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] model_package_group_description: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        :param pulumi.Input[str] model_package_group_name: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        :param pulumi.Input[Union[Any, str]] model_package_group_policy: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['_root_inputs.TagArgs']]]] tags: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModelPackageGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html

        :param str resource_name: The name of the resource.
        :param ModelPackageGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModelPackageGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 model_package_group_description: Optional[pulumi.Input[str]] = None,
                 model_package_group_name: Optional[pulumi.Input[str]] = None,
                 model_package_group_policy: Optional[pulumi.Input[Union[Any, str]]] = None,
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
            __props__ = ModelPackageGroupArgs.__new__(ModelPackageGroupArgs)

            __props__.__dict__["model_package_group_description"] = model_package_group_description
            if model_package_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'model_package_group_name'")
            __props__.__dict__["model_package_group_name"] = model_package_group_name
            __props__.__dict__["model_package_group_policy"] = model_package_group_policy
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["model_package_group_arn"] = None
            __props__.__dict__["model_package_group_status"] = None
        super(ModelPackageGroup, __self__).__init__(
            'aws-native:sagemaker:ModelPackageGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModelPackageGroup':
        """
        Get an existing ModelPackageGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModelPackageGroupArgs.__new__(ModelPackageGroupArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["model_package_group_arn"] = None
        __props__.__dict__["model_package_group_description"] = None
        __props__.__dict__["model_package_group_name"] = None
        __props__.__dict__["model_package_group_policy"] = None
        __props__.__dict__["model_package_group_status"] = None
        __props__.__dict__["tags"] = None
        return ModelPackageGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="modelPackageGroupArn")
    def model_package_group_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "model_package_group_arn")

    @property
    @pulumi.getter(name="modelPackageGroupDescription")
    def model_package_group_description(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupdescription
        """
        return pulumi.get(self, "model_package_group_description")

    @property
    @pulumi.getter(name="modelPackageGroupName")
    def model_package_group_name(self) -> pulumi.Output[str]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegroupname
        """
        return pulumi.get(self, "model_package_group_name")

    @property
    @pulumi.getter(name="modelPackageGroupPolicy")
    def model_package_group_policy(self) -> pulumi.Output[Optional[str]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-modelpackagegrouppolicy
        """
        return pulumi.get(self, "model_package_group_policy")

    @property
    @pulumi.getter(name="modelPackageGroupStatus")
    def model_package_group_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "model_package_group_status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['_root_outputs.Tag']]]:
        """
        http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelpackagegroup.html#cfn-sagemaker-modelpackagegroup-tags
        """
        return pulumi.get(self, "tags")

