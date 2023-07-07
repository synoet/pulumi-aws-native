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

__all__ = ['DocumentClassifierArgs', 'DocumentClassifier']

@pulumi.input_type
class DocumentClassifierArgs:
    def __init__(__self__, *,
                 data_access_role_arn: pulumi.Input[str],
                 input_data_config: pulumi.Input['DocumentClassifierInputDataConfigArgs'],
                 language_code: pulumi.Input['DocumentClassifierLanguageCode'],
                 document_classifier_name: Optional[pulumi.Input[str]] = None,
                 mode: Optional[pulumi.Input['DocumentClassifierMode']] = None,
                 model_kms_key_id: Optional[pulumi.Input[str]] = None,
                 model_policy: Optional[pulumi.Input[str]] = None,
                 output_data_config: Optional[pulumi.Input['DocumentClassifierOutputDataConfigArgs']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DocumentClassifierTagArgs']]]] = None,
                 version_name: Optional[pulumi.Input[str]] = None,
                 volume_kms_key_id: Optional[pulumi.Input[str]] = None,
                 vpc_config: Optional[pulumi.Input['DocumentClassifierVpcConfigArgs']] = None):
        """
        The set of arguments for constructing a DocumentClassifier resource.
        """
        pulumi.set(__self__, "data_access_role_arn", data_access_role_arn)
        pulumi.set(__self__, "input_data_config", input_data_config)
        pulumi.set(__self__, "language_code", language_code)
        if document_classifier_name is not None:
            pulumi.set(__self__, "document_classifier_name", document_classifier_name)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if model_kms_key_id is not None:
            pulumi.set(__self__, "model_kms_key_id", model_kms_key_id)
        if model_policy is not None:
            pulumi.set(__self__, "model_policy", model_policy)
        if output_data_config is not None:
            pulumi.set(__self__, "output_data_config", output_data_config)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if version_name is not None:
            pulumi.set(__self__, "version_name", version_name)
        if volume_kms_key_id is not None:
            pulumi.set(__self__, "volume_kms_key_id", volume_kms_key_id)
        if vpc_config is not None:
            pulumi.set(__self__, "vpc_config", vpc_config)

    @property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Input[str]:
        return pulumi.get(self, "data_access_role_arn")

    @data_access_role_arn.setter
    def data_access_role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "data_access_role_arn", value)

    @property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Input['DocumentClassifierInputDataConfigArgs']:
        return pulumi.get(self, "input_data_config")

    @input_data_config.setter
    def input_data_config(self, value: pulumi.Input['DocumentClassifierInputDataConfigArgs']):
        pulumi.set(self, "input_data_config", value)

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input['DocumentClassifierLanguageCode']:
        return pulumi.get(self, "language_code")

    @language_code.setter
    def language_code(self, value: pulumi.Input['DocumentClassifierLanguageCode']):
        pulumi.set(self, "language_code", value)

    @property
    @pulumi.getter(name="documentClassifierName")
    def document_classifier_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "document_classifier_name")

    @document_classifier_name.setter
    def document_classifier_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "document_classifier_name", value)

    @property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input['DocumentClassifierMode']]:
        return pulumi.get(self, "mode")

    @mode.setter
    def mode(self, value: Optional[pulumi.Input['DocumentClassifierMode']]):
        pulumi.set(self, "mode", value)

    @property
    @pulumi.getter(name="modelKmsKeyId")
    def model_kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_kms_key_id")

    @model_kms_key_id.setter
    def model_kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_kms_key_id", value)

    @property
    @pulumi.getter(name="modelPolicy")
    def model_policy(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "model_policy")

    @model_policy.setter
    def model_policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "model_policy", value)

    @property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> Optional[pulumi.Input['DocumentClassifierOutputDataConfigArgs']]:
        return pulumi.get(self, "output_data_config")

    @output_data_config.setter
    def output_data_config(self, value: Optional[pulumi.Input['DocumentClassifierOutputDataConfigArgs']]):
        pulumi.set(self, "output_data_config", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DocumentClassifierTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DocumentClassifierTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="versionName")
    def version_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "version_name")

    @version_name.setter
    def version_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "version_name", value)

    @property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "volume_kms_key_id")

    @volume_kms_key_id.setter
    def volume_kms_key_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "volume_kms_key_id", value)

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> Optional[pulumi.Input['DocumentClassifierVpcConfigArgs']]:
        return pulumi.get(self, "vpc_config")

    @vpc_config.setter
    def vpc_config(self, value: Optional[pulumi.Input['DocumentClassifierVpcConfigArgs']]):
        pulumi.set(self, "vpc_config", value)


class DocumentClassifier(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_access_role_arn: Optional[pulumi.Input[str]] = None,
                 document_classifier_name: Optional[pulumi.Input[str]] = None,
                 input_data_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierInputDataConfigArgs']]] = None,
                 language_code: Optional[pulumi.Input['DocumentClassifierLanguageCode']] = None,
                 mode: Optional[pulumi.Input['DocumentClassifierMode']] = None,
                 model_kms_key_id: Optional[pulumi.Input[str]] = None,
                 model_policy: Optional[pulumi.Input[str]] = None,
                 output_data_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierOutputDataConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DocumentClassifierTagArgs']]]]] = None,
                 version_name: Optional[pulumi.Input[str]] = None,
                 volume_kms_key_id: Optional[pulumi.Input[str]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierVpcConfigArgs']]] = None,
                 __props__=None):
        """
        Document Classifier enables training document classifier models.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DocumentClassifierArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Document Classifier enables training document classifier models.

        :param str resource_name: The name of the resource.
        :param DocumentClassifierArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DocumentClassifierArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 data_access_role_arn: Optional[pulumi.Input[str]] = None,
                 document_classifier_name: Optional[pulumi.Input[str]] = None,
                 input_data_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierInputDataConfigArgs']]] = None,
                 language_code: Optional[pulumi.Input['DocumentClassifierLanguageCode']] = None,
                 mode: Optional[pulumi.Input['DocumentClassifierMode']] = None,
                 model_kms_key_id: Optional[pulumi.Input[str]] = None,
                 model_policy: Optional[pulumi.Input[str]] = None,
                 output_data_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierOutputDataConfigArgs']]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DocumentClassifierTagArgs']]]]] = None,
                 version_name: Optional[pulumi.Input[str]] = None,
                 volume_kms_key_id: Optional[pulumi.Input[str]] = None,
                 vpc_config: Optional[pulumi.Input[pulumi.InputType['DocumentClassifierVpcConfigArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DocumentClassifierArgs.__new__(DocumentClassifierArgs)

            if data_access_role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'data_access_role_arn'")
            __props__.__dict__["data_access_role_arn"] = data_access_role_arn
            __props__.__dict__["document_classifier_name"] = document_classifier_name
            if input_data_config is None and not opts.urn:
                raise TypeError("Missing required property 'input_data_config'")
            __props__.__dict__["input_data_config"] = input_data_config
            if language_code is None and not opts.urn:
                raise TypeError("Missing required property 'language_code'")
            __props__.__dict__["language_code"] = language_code
            __props__.__dict__["mode"] = mode
            __props__.__dict__["model_kms_key_id"] = model_kms_key_id
            __props__.__dict__["model_policy"] = model_policy
            __props__.__dict__["output_data_config"] = output_data_config
            __props__.__dict__["tags"] = tags
            __props__.__dict__["version_name"] = version_name
            __props__.__dict__["volume_kms_key_id"] = volume_kms_key_id
            __props__.__dict__["vpc_config"] = vpc_config
            __props__.__dict__["arn"] = None
        super(DocumentClassifier, __self__).__init__(
            'aws-native:comprehend:DocumentClassifier',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DocumentClassifier':
        """
        Get an existing DocumentClassifier resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DocumentClassifierArgs.__new__(DocumentClassifierArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["data_access_role_arn"] = None
        __props__.__dict__["document_classifier_name"] = None
        __props__.__dict__["input_data_config"] = None
        __props__.__dict__["language_code"] = None
        __props__.__dict__["mode"] = None
        __props__.__dict__["model_kms_key_id"] = None
        __props__.__dict__["model_policy"] = None
        __props__.__dict__["output_data_config"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["version_name"] = None
        __props__.__dict__["volume_kms_key_id"] = None
        __props__.__dict__["vpc_config"] = None
        return DocumentClassifier(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="dataAccessRoleArn")
    def data_access_role_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "data_access_role_arn")

    @property
    @pulumi.getter(name="documentClassifierName")
    def document_classifier_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "document_classifier_name")

    @property
    @pulumi.getter(name="inputDataConfig")
    def input_data_config(self) -> pulumi.Output['outputs.DocumentClassifierInputDataConfig']:
        return pulumi.get(self, "input_data_config")

    @property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output['DocumentClassifierLanguageCode']:
        return pulumi.get(self, "language_code")

    @property
    @pulumi.getter
    def mode(self) -> pulumi.Output[Optional['DocumentClassifierMode']]:
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter(name="modelKmsKeyId")
    def model_kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_kms_key_id")

    @property
    @pulumi.getter(name="modelPolicy")
    def model_policy(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "model_policy")

    @property
    @pulumi.getter(name="outputDataConfig")
    def output_data_config(self) -> pulumi.Output[Optional['outputs.DocumentClassifierOutputDataConfig']]:
        return pulumi.get(self, "output_data_config")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DocumentClassifierTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="versionName")
    def version_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "version_name")

    @property
    @pulumi.getter(name="volumeKmsKeyId")
    def volume_kms_key_id(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "volume_kms_key_id")

    @property
    @pulumi.getter(name="vpcConfig")
    def vpc_config(self) -> pulumi.Output[Optional['outputs.DocumentClassifierVpcConfig']]:
        return pulumi.get(self, "vpc_config")

