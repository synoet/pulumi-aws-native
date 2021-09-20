# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DetectorModelArgs', 'DetectorModel']

@pulumi.input_type
class DetectorModelArgs:
    def __init__(__self__, *,
                 detector_model_definition: pulumi.Input['DetectorModelDetectorModelDefinitionArgs'],
                 role_arn: pulumi.Input[str],
                 detector_model_description: Optional[pulumi.Input[str]] = None,
                 detector_model_name: Optional[pulumi.Input[str]] = None,
                 evaluation_method: Optional[pulumi.Input['DetectorModelEvaluationMethod']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelTagArgs']]]] = None):
        """
        The set of arguments for constructing a DetectorModel resource.
        :param pulumi.Input[str] role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param pulumi.Input[str] detector_model_description: A brief description of the detector model.
        :param pulumi.Input[str] detector_model_name: The name of the detector model.
        :param pulumi.Input['DetectorModelEvaluationMethod'] evaluation_method: Information about the order in which events are evaluated and how actions are executed.
        :param pulumi.Input[str] key: The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
               
               This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        :param pulumi.Input[Sequence[pulumi.Input['DetectorModelTagArgs']]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        pulumi.set(__self__, "detector_model_definition", detector_model_definition)
        pulumi.set(__self__, "role_arn", role_arn)
        if detector_model_description is not None:
            pulumi.set(__self__, "detector_model_description", detector_model_description)
        if detector_model_name is not None:
            pulumi.set(__self__, "detector_model_name", detector_model_name)
        if evaluation_method is not None:
            pulumi.set(__self__, "evaluation_method", evaluation_method)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="detectorModelDefinition")
    def detector_model_definition(self) -> pulumi.Input['DetectorModelDetectorModelDefinitionArgs']:
        return pulumi.get(self, "detector_model_definition")

    @detector_model_definition.setter
    def detector_model_definition(self, value: pulumi.Input['DetectorModelDetectorModelDefinitionArgs']):
        pulumi.set(self, "detector_model_definition", value)

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[str]:
        """
        The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        """
        return pulumi.get(self, "role_arn")

    @role_arn.setter
    def role_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_arn", value)

    @property
    @pulumi.getter(name="detectorModelDescription")
    def detector_model_description(self) -> Optional[pulumi.Input[str]]:
        """
        A brief description of the detector model.
        """
        return pulumi.get(self, "detector_model_description")

    @detector_model_description.setter
    def detector_model_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detector_model_description", value)

    @property
    @pulumi.getter(name="detectorModelName")
    def detector_model_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the detector model.
        """
        return pulumi.get(self, "detector_model_name")

    @detector_model_name.setter
    def detector_model_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "detector_model_name", value)

    @property
    @pulumi.getter(name="evaluationMethod")
    def evaluation_method(self) -> Optional[pulumi.Input['DetectorModelEvaluationMethod']]:
        """
        Information about the order in which events are evaluated and how actions are executed.
        """
        return pulumi.get(self, "evaluation_method")

    @evaluation_method.setter
    def evaluation_method(self, value: Optional[pulumi.Input['DetectorModelEvaluationMethod']]):
        pulumi.set(self, "evaluation_method", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.

        This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelTagArgs']]]]):
        pulumi.set(self, "tags", value)


class DetectorModel(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_model_definition: Optional[pulumi.Input[pulumi.InputType['DetectorModelDetectorModelDefinitionArgs']]] = None,
                 detector_model_description: Optional[pulumi.Input[str]] = None,
                 detector_model_name: Optional[pulumi.Input[str]] = None,
                 evaluation_method: Optional[pulumi.Input['DetectorModelEvaluationMethod']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] detector_model_description: A brief description of the detector model.
        :param pulumi.Input[str] detector_model_name: The name of the detector model.
        :param pulumi.Input['DetectorModelEvaluationMethod'] evaluation_method: Information about the order in which events are evaluated and how actions are executed.
        :param pulumi.Input[str] key: The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.
               
               This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        :param pulumi.Input[str] role_arn: The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
               
               For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DetectorModelArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::IoTEvents::DetectorModel resource creates a detector model. You create a *detector model* (a model of your equipment or process) using *states*. For each state, you define conditional (Boolean) logic that evaluates the incoming inputs to detect significant events. When an event is detected, it can change the state or trigger custom-built or predefined actions using other AWS services. You can define additional events that trigger actions when entering or exiting a state and, optionally, when a condition is met. For more information, see [How to Use AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/how-to-use-iotevents.html) in the *AWS IoT Events Developer Guide*.

        :param str resource_name: The name of the resource.
        :param DetectorModelArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DetectorModelArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 detector_model_definition: Optional[pulumi.Input[pulumi.InputType['DetectorModelDetectorModelDefinitionArgs']]] = None,
                 detector_model_description: Optional[pulumi.Input[str]] = None,
                 detector_model_name: Optional[pulumi.Input[str]] = None,
                 evaluation_method: Optional[pulumi.Input['DetectorModelEvaluationMethod']] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 role_arn: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelTagArgs']]]]] = None,
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
            __props__ = DetectorModelArgs.__new__(DetectorModelArgs)

            if detector_model_definition is None and not opts.urn:
                raise TypeError("Missing required property 'detector_model_definition'")
            __props__.__dict__["detector_model_definition"] = detector_model_definition
            __props__.__dict__["detector_model_description"] = detector_model_description
            __props__.__dict__["detector_model_name"] = detector_model_name
            __props__.__dict__["evaluation_method"] = evaluation_method
            __props__.__dict__["key"] = key
            if role_arn is None and not opts.urn:
                raise TypeError("Missing required property 'role_arn'")
            __props__.__dict__["role_arn"] = role_arn
            __props__.__dict__["tags"] = tags
        super(DetectorModel, __self__).__init__(
            'aws-native:iotevents:DetectorModel',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DetectorModel':
        """
        Get an existing DetectorModel resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DetectorModelArgs.__new__(DetectorModelArgs)

        __props__.__dict__["detector_model_definition"] = None
        __props__.__dict__["detector_model_description"] = None
        __props__.__dict__["detector_model_name"] = None
        __props__.__dict__["evaluation_method"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["role_arn"] = None
        __props__.__dict__["tags"] = None
        return DetectorModel(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detectorModelDefinition")
    def detector_model_definition(self) -> pulumi.Output['outputs.DetectorModelDetectorModelDefinition']:
        return pulumi.get(self, "detector_model_definition")

    @property
    @pulumi.getter(name="detectorModelDescription")
    def detector_model_description(self) -> pulumi.Output[Optional[str]]:
        """
        A brief description of the detector model.
        """
        return pulumi.get(self, "detector_model_description")

    @property
    @pulumi.getter(name="detectorModelName")
    def detector_model_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the detector model.
        """
        return pulumi.get(self, "detector_model_name")

    @property
    @pulumi.getter(name="evaluationMethod")
    def evaluation_method(self) -> pulumi.Output[Optional['DetectorModelEvaluationMethod']]:
        """
        Information about the order in which events are evaluated and how actions are executed.
        """
        return pulumi.get(self, "evaluation_method")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        The value used to identify a detector instance. When a device or system sends input, a new detector instance with a unique key value is created. AWS IoT Events can continue to route input to its corresponding detector instance based on this identifying information.

        This parameter uses a JSON-path expression to select the attribute-value pair in the message payload that is used for identification. To route the message to the correct detector instance, the device must send a message payload that contains the same attribute-value.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Output[str]:
        """
        The ARN of the role that grants permission to AWS IoT Events to perform its operations.
        """
        return pulumi.get(self, "role_arn")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DetectorModelTag']]]:
        """
        An array of key-value pairs to apply to this resource.

        For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
        """
        return pulumi.get(self, "tags")

