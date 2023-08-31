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

__all__ = ['DetectorArgs', 'Detector']

@pulumi.input_type
class DetectorArgs:
    def __init__(__self__, *,
                 detector_id: pulumi.Input[str],
                 event_type: pulumi.Input['DetectorEventTypeArgs'],
                 rules: pulumi.Input[Sequence[pulumi.Input['DetectorRuleArgs']]],
                 associated_models: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelArgs']]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_version_status: Optional[pulumi.Input['DetectorVersionStatus']] = None,
                 rule_execution_mode: Optional[pulumi.Input['DetectorRuleExecutionMode']] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagArgs']]]] = None):
        """
        The set of arguments for constructing a Detector resource.
        :param pulumi.Input[str] detector_id: The ID of the detector
        :param pulumi.Input['DetectorEventTypeArgs'] event_type: The event type to associate this detector with.
        :param pulumi.Input[Sequence[pulumi.Input['DetectorModelArgs']]] associated_models: The models to associate with this detector.
        :param pulumi.Input[str] description: The description of the detector.
        :param pulumi.Input['DetectorVersionStatus'] detector_version_status: The desired detector version status for the detector
        :param pulumi.Input[Sequence[pulumi.Input['DetectorTagArgs']]] tags: Tags associated with this detector.
        """
        pulumi.set(__self__, "detector_id", detector_id)
        pulumi.set(__self__, "event_type", event_type)
        pulumi.set(__self__, "rules", rules)
        if associated_models is not None:
            pulumi.set(__self__, "associated_models", associated_models)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if detector_version_status is not None:
            pulumi.set(__self__, "detector_version_status", detector_version_status)
        if rule_execution_mode is not None:
            pulumi.set(__self__, "rule_execution_mode", rule_execution_mode)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Input[str]:
        """
        The ID of the detector
        """
        return pulumi.get(self, "detector_id")

    @detector_id.setter
    def detector_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "detector_id", value)

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Input['DetectorEventTypeArgs']:
        """
        The event type to associate this detector with.
        """
        return pulumi.get(self, "event_type")

    @event_type.setter
    def event_type(self, value: pulumi.Input['DetectorEventTypeArgs']):
        pulumi.set(self, "event_type", value)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['DetectorRuleArgs']]]:
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['DetectorRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="associatedModels")
    def associated_models(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelArgs']]]]:
        """
        The models to associate with this detector.
        """
        return pulumi.get(self, "associated_models")

    @associated_models.setter
    def associated_models(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorModelArgs']]]]):
        pulumi.set(self, "associated_models", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the detector.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="detectorVersionStatus")
    def detector_version_status(self) -> Optional[pulumi.Input['DetectorVersionStatus']]:
        """
        The desired detector version status for the detector
        """
        return pulumi.get(self, "detector_version_status")

    @detector_version_status.setter
    def detector_version_status(self, value: Optional[pulumi.Input['DetectorVersionStatus']]):
        pulumi.set(self, "detector_version_status", value)

    @property
    @pulumi.getter(name="ruleExecutionMode")
    def rule_execution_mode(self) -> Optional[pulumi.Input['DetectorRuleExecutionMode']]:
        return pulumi.get(self, "rule_execution_mode")

    @rule_execution_mode.setter
    def rule_execution_mode(self, value: Optional[pulumi.Input['DetectorRuleExecutionMode']]):
        pulumi.set(self, "rule_execution_mode", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagArgs']]]]:
        """
        Tags associated with this detector.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DetectorTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Detector(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_models: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 detector_version_status: Optional[pulumi.Input['DetectorVersionStatus']] = None,
                 event_type: Optional[pulumi.Input[pulumi.InputType['DetectorEventTypeArgs']]] = None,
                 rule_execution_mode: Optional[pulumi.Input['DetectorRuleExecutionMode']] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorTagArgs']]]]] = None,
                 __props__=None):
        """
        A resource schema for a Detector in Amazon Fraud Detector.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelArgs']]]] associated_models: The models to associate with this detector.
        :param pulumi.Input[str] description: The description of the detector.
        :param pulumi.Input[str] detector_id: The ID of the detector
        :param pulumi.Input['DetectorVersionStatus'] detector_version_status: The desired detector version status for the detector
        :param pulumi.Input[pulumi.InputType['DetectorEventTypeArgs']] event_type: The event type to associate this detector with.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorTagArgs']]]] tags: Tags associated with this detector.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DetectorArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A resource schema for a Detector in Amazon Fraud Detector.

        :param str resource_name: The name of the resource.
        :param DetectorArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DetectorArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_models: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorModelArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 detector_id: Optional[pulumi.Input[str]] = None,
                 detector_version_status: Optional[pulumi.Input['DetectorVersionStatus']] = None,
                 event_type: Optional[pulumi.Input[pulumi.InputType['DetectorEventTypeArgs']]] = None,
                 rule_execution_mode: Optional[pulumi.Input['DetectorRuleExecutionMode']] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DetectorTagArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DetectorArgs.__new__(DetectorArgs)

            __props__.__dict__["associated_models"] = associated_models
            __props__.__dict__["description"] = description
            if detector_id is None and not opts.urn:
                raise TypeError("Missing required property 'detector_id'")
            __props__.__dict__["detector_id"] = detector_id
            __props__.__dict__["detector_version_status"] = detector_version_status
            if event_type is None and not opts.urn:
                raise TypeError("Missing required property 'event_type'")
            __props__.__dict__["event_type"] = event_type
            __props__.__dict__["rule_execution_mode"] = rule_execution_mode
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["created_time"] = None
            __props__.__dict__["detector_version_id"] = None
            __props__.__dict__["last_updated_time"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["detector_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Detector, __self__).__init__(
            'aws-native:frauddetector:Detector',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Detector':
        """
        Get an existing Detector resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DetectorArgs.__new__(DetectorArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["associated_models"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["detector_id"] = None
        __props__.__dict__["detector_version_id"] = None
        __props__.__dict__["detector_version_status"] = None
        __props__.__dict__["event_type"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["rule_execution_mode"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["tags"] = None
        return Detector(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The ARN of the detector.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associatedModels")
    def associated_models(self) -> pulumi.Output[Optional[Sequence['outputs.DetectorModel']]]:
        """
        The models to associate with this detector.
        """
        return pulumi.get(self, "associated_models")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[str]:
        """
        The time when the detector was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the detector.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="detectorId")
    def detector_id(self) -> pulumi.Output[str]:
        """
        The ID of the detector
        """
        return pulumi.get(self, "detector_id")

    @property
    @pulumi.getter(name="detectorVersionId")
    def detector_version_id(self) -> pulumi.Output[str]:
        """
        The active version ID of the detector
        """
        return pulumi.get(self, "detector_version_id")

    @property
    @pulumi.getter(name="detectorVersionStatus")
    def detector_version_status(self) -> pulumi.Output[Optional['DetectorVersionStatus']]:
        """
        The desired detector version status for the detector
        """
        return pulumi.get(self, "detector_version_status")

    @property
    @pulumi.getter(name="eventType")
    def event_type(self) -> pulumi.Output['outputs.DetectorEventType']:
        """
        The event type to associate this detector with.
        """
        return pulumi.get(self, "event_type")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        The time when the detector was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="ruleExecutionMode")
    def rule_execution_mode(self) -> pulumi.Output[Optional['DetectorRuleExecutionMode']]:
        return pulumi.get(self, "rule_execution_mode")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.DetectorRule']]:
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.DetectorTag']]]:
        """
        Tags associated with this detector.
        """
        return pulumi.get(self, "tags")

