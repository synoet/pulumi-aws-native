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

__all__ = ['ImageVersionArgs', 'ImageVersion']

@pulumi.input_type
class ImageVersionArgs:
    def __init__(__self__, *,
                 base_image: pulumi.Input[str],
                 image_name: pulumi.Input[str],
                 alias: Optional[pulumi.Input[str]] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 horovod: Optional[pulumi.Input[bool]] = None,
                 job_type: Optional[pulumi.Input['ImageVersionJobType']] = None,
                 ml_framework: Optional[pulumi.Input[str]] = None,
                 processor: Optional[pulumi.Input['ImageVersionProcessor']] = None,
                 programming_lang: Optional[pulumi.Input[str]] = None,
                 release_notes: Optional[pulumi.Input[str]] = None,
                 vendor_guidance: Optional[pulumi.Input['ImageVersionVendorGuidance']] = None):
        """
        The set of arguments for constructing a ImageVersion resource.
        """
        pulumi.set(__self__, "base_image", base_image)
        pulumi.set(__self__, "image_name", image_name)
        if alias is not None:
            pulumi.set(__self__, "alias", alias)
        if aliases is not None:
            pulumi.set(__self__, "aliases", aliases)
        if horovod is not None:
            pulumi.set(__self__, "horovod", horovod)
        if job_type is not None:
            pulumi.set(__self__, "job_type", job_type)
        if ml_framework is not None:
            pulumi.set(__self__, "ml_framework", ml_framework)
        if processor is not None:
            pulumi.set(__self__, "processor", processor)
        if programming_lang is not None:
            pulumi.set(__self__, "programming_lang", programming_lang)
        if release_notes is not None:
            pulumi.set(__self__, "release_notes", release_notes)
        if vendor_guidance is not None:
            pulumi.set(__self__, "vendor_guidance", vendor_guidance)

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Input[str]:
        return pulumi.get(self, "base_image")

    @base_image.setter
    def base_image(self, value: pulumi.Input[str]):
        pulumi.set(self, "base_image", value)

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "image_name")

    @image_name.setter
    def image_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "image_name", value)

    @property
    @pulumi.getter
    def alias(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "alias")

    @alias.setter
    def alias(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alias", value)

    @property
    @pulumi.getter
    def aliases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "aliases")

    @aliases.setter
    def aliases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "aliases", value)

    @property
    @pulumi.getter
    def horovod(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "horovod")

    @horovod.setter
    def horovod(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "horovod", value)

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> Optional[pulumi.Input['ImageVersionJobType']]:
        return pulumi.get(self, "job_type")

    @job_type.setter
    def job_type(self, value: Optional[pulumi.Input['ImageVersionJobType']]):
        pulumi.set(self, "job_type", value)

    @property
    @pulumi.getter(name="mlFramework")
    def ml_framework(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "ml_framework")

    @ml_framework.setter
    def ml_framework(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ml_framework", value)

    @property
    @pulumi.getter
    def processor(self) -> Optional[pulumi.Input['ImageVersionProcessor']]:
        return pulumi.get(self, "processor")

    @processor.setter
    def processor(self, value: Optional[pulumi.Input['ImageVersionProcessor']]):
        pulumi.set(self, "processor", value)

    @property
    @pulumi.getter(name="programmingLang")
    def programming_lang(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "programming_lang")

    @programming_lang.setter
    def programming_lang(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "programming_lang", value)

    @property
    @pulumi.getter(name="releaseNotes")
    def release_notes(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "release_notes")

    @release_notes.setter
    def release_notes(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "release_notes", value)

    @property
    @pulumi.getter(name="vendorGuidance")
    def vendor_guidance(self) -> Optional[pulumi.Input['ImageVersionVendorGuidance']]:
        return pulumi.get(self, "vendor_guidance")

    @vendor_guidance.setter
    def vendor_guidance(self, value: Optional[pulumi.Input['ImageVersionVendorGuidance']]):
        pulumi.set(self, "vendor_guidance", value)


class ImageVersion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 base_image: Optional[pulumi.Input[str]] = None,
                 horovod: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 job_type: Optional[pulumi.Input['ImageVersionJobType']] = None,
                 ml_framework: Optional[pulumi.Input[str]] = None,
                 processor: Optional[pulumi.Input['ImageVersionProcessor']] = None,
                 programming_lang: Optional[pulumi.Input[str]] = None,
                 release_notes: Optional[pulumi.Input[str]] = None,
                 vendor_guidance: Optional[pulumi.Input['ImageVersionVendorGuidance']] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::ImageVersion

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ImageVersionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::ImageVersion

        :param str resource_name: The name of the resource.
        :param ImageVersionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ImageVersionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 alias: Optional[pulumi.Input[str]] = None,
                 aliases: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 base_image: Optional[pulumi.Input[str]] = None,
                 horovod: Optional[pulumi.Input[bool]] = None,
                 image_name: Optional[pulumi.Input[str]] = None,
                 job_type: Optional[pulumi.Input['ImageVersionJobType']] = None,
                 ml_framework: Optional[pulumi.Input[str]] = None,
                 processor: Optional[pulumi.Input['ImageVersionProcessor']] = None,
                 programming_lang: Optional[pulumi.Input[str]] = None,
                 release_notes: Optional[pulumi.Input[str]] = None,
                 vendor_guidance: Optional[pulumi.Input['ImageVersionVendorGuidance']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ImageVersionArgs.__new__(ImageVersionArgs)

            __props__.__dict__["alias"] = alias
            __props__.__dict__["aliases"] = aliases
            if base_image is None and not opts.urn:
                raise TypeError("Missing required property 'base_image'")
            __props__.__dict__["base_image"] = base_image
            __props__.__dict__["horovod"] = horovod
            if image_name is None and not opts.urn:
                raise TypeError("Missing required property 'image_name'")
            __props__.__dict__["image_name"] = image_name
            __props__.__dict__["job_type"] = job_type
            __props__.__dict__["ml_framework"] = ml_framework
            __props__.__dict__["processor"] = processor
            __props__.__dict__["programming_lang"] = programming_lang
            __props__.__dict__["release_notes"] = release_notes
            __props__.__dict__["vendor_guidance"] = vendor_guidance
            __props__.__dict__["container_image"] = None
            __props__.__dict__["image_arn"] = None
            __props__.__dict__["image_version_arn"] = None
            __props__.__dict__["version"] = None
        super(ImageVersion, __self__).__init__(
            'aws-native:sagemaker:ImageVersion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ImageVersion':
        """
        Get an existing ImageVersion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ImageVersionArgs.__new__(ImageVersionArgs)

        __props__.__dict__["alias"] = None
        __props__.__dict__["aliases"] = None
        __props__.__dict__["base_image"] = None
        __props__.__dict__["container_image"] = None
        __props__.__dict__["horovod"] = None
        __props__.__dict__["image_arn"] = None
        __props__.__dict__["image_name"] = None
        __props__.__dict__["image_version_arn"] = None
        __props__.__dict__["job_type"] = None
        __props__.__dict__["ml_framework"] = None
        __props__.__dict__["processor"] = None
        __props__.__dict__["programming_lang"] = None
        __props__.__dict__["release_notes"] = None
        __props__.__dict__["vendor_guidance"] = None
        __props__.__dict__["version"] = None
        return ImageVersion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def alias(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter
    def aliases(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "aliases")

    @property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> pulumi.Output[str]:
        return pulumi.get(self, "base_image")

    @property
    @pulumi.getter(name="containerImage")
    def container_image(self) -> pulumi.Output[str]:
        return pulumi.get(self, "container_image")

    @property
    @pulumi.getter
    def horovod(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "horovod")

    @property
    @pulumi.getter(name="imageArn")
    def image_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "image_arn")

    @property
    @pulumi.getter(name="imageName")
    def image_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "image_name")

    @property
    @pulumi.getter(name="imageVersionArn")
    def image_version_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "image_version_arn")

    @property
    @pulumi.getter(name="jobType")
    def job_type(self) -> pulumi.Output[Optional['ImageVersionJobType']]:
        return pulumi.get(self, "job_type")

    @property
    @pulumi.getter(name="mlFramework")
    def ml_framework(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "ml_framework")

    @property
    @pulumi.getter
    def processor(self) -> pulumi.Output[Optional['ImageVersionProcessor']]:
        return pulumi.get(self, "processor")

    @property
    @pulumi.getter(name="programmingLang")
    def programming_lang(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "programming_lang")

    @property
    @pulumi.getter(name="releaseNotes")
    def release_notes(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "release_notes")

    @property
    @pulumi.getter(name="vendorGuidance")
    def vendor_guidance(self) -> pulumi.Output[Optional['ImageVersionVendorGuidance']]:
        return pulumi.get(self, "vendor_guidance")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[int]:
        return pulumi.get(self, "version")

