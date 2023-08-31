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
from ._inputs import *

__all__ = ['AlertArgs', 'Alert']

@pulumi.input_type
class AlertArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['AlertActionArgs'],
                 alert_sensitivity_threshold: pulumi.Input[int],
                 anomaly_detector_arn: pulumi.Input[str],
                 alert_description: Optional[pulumi.Input[str]] = None,
                 alert_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Alert resource.
        :param pulumi.Input['AlertActionArgs'] action: The action to be taken by the alert when an anomaly is detected.
        :param pulumi.Input[int] alert_sensitivity_threshold: A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        :param pulumi.Input[str] anomaly_detector_arn: The Amazon resource name (ARN) of the Anomaly Detector to alert.
        :param pulumi.Input[str] alert_description: A description for the alert.
        :param pulumi.Input[str] alert_name: The name of the alert. If not provided, a name is generated automatically.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "alert_sensitivity_threshold", alert_sensitivity_threshold)
        pulumi.set(__self__, "anomaly_detector_arn", anomaly_detector_arn)
        if alert_description is not None:
            pulumi.set(__self__, "alert_description", alert_description)
        if alert_name is not None:
            pulumi.set(__self__, "alert_name", alert_name)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['AlertActionArgs']:
        """
        The action to be taken by the alert when an anomaly is detected.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['AlertActionArgs']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="alertSensitivityThreshold")
    def alert_sensitivity_threshold(self) -> pulumi.Input[int]:
        """
        A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        """
        return pulumi.get(self, "alert_sensitivity_threshold")

    @alert_sensitivity_threshold.setter
    def alert_sensitivity_threshold(self, value: pulumi.Input[int]):
        pulumi.set(self, "alert_sensitivity_threshold", value)

    @property
    @pulumi.getter(name="anomalyDetectorArn")
    def anomaly_detector_arn(self) -> pulumi.Input[str]:
        """
        The Amazon resource name (ARN) of the Anomaly Detector to alert.
        """
        return pulumi.get(self, "anomaly_detector_arn")

    @anomaly_detector_arn.setter
    def anomaly_detector_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "anomaly_detector_arn", value)

    @property
    @pulumi.getter(name="alertDescription")
    def alert_description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the alert.
        """
        return pulumi.get(self, "alert_description")

    @alert_description.setter
    def alert_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_description", value)

    @property
    @pulumi.getter(name="alertName")
    def alert_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the alert. If not provided, a name is generated automatically.
        """
        return pulumi.get(self, "alert_name")

    @alert_name.setter
    def alert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "alert_name", value)


class Alert(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['AlertActionArgs']]] = None,
                 alert_description: Optional[pulumi.Input[str]] = None,
                 alert_name: Optional[pulumi.Input[str]] = None,
                 alert_sensitivity_threshold: Optional[pulumi.Input[int]] = None,
                 anomaly_detector_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::LookoutMetrics::Alert

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AlertActionArgs']] action: The action to be taken by the alert when an anomaly is detected.
        :param pulumi.Input[str] alert_description: A description for the alert.
        :param pulumi.Input[str] alert_name: The name of the alert. If not provided, a name is generated automatically.
        :param pulumi.Input[int] alert_sensitivity_threshold: A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        :param pulumi.Input[str] anomaly_detector_arn: The Amazon resource name (ARN) of the Anomaly Detector to alert.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AlertArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::LookoutMetrics::Alert

        :param str resource_name: The name of the resource.
        :param AlertArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AlertArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['AlertActionArgs']]] = None,
                 alert_description: Optional[pulumi.Input[str]] = None,
                 alert_name: Optional[pulumi.Input[str]] = None,
                 alert_sensitivity_threshold: Optional[pulumi.Input[int]] = None,
                 anomaly_detector_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AlertArgs.__new__(AlertArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            __props__.__dict__["alert_description"] = alert_description
            __props__.__dict__["alert_name"] = alert_name
            if alert_sensitivity_threshold is None and not opts.urn:
                raise TypeError("Missing required property 'alert_sensitivity_threshold'")
            __props__.__dict__["alert_sensitivity_threshold"] = alert_sensitivity_threshold
            if anomaly_detector_arn is None and not opts.urn:
                raise TypeError("Missing required property 'anomaly_detector_arn'")
            __props__.__dict__["anomaly_detector_arn"] = anomaly_detector_arn
            __props__.__dict__["arn"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["action", "alert_description", "alert_name", "alert_sensitivity_threshold", "anomaly_detector_arn"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Alert, __self__).__init__(
            'aws-native:lookoutmetrics:Alert',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Alert':
        """
        Get an existing Alert resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AlertArgs.__new__(AlertArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["alert_description"] = None
        __props__.__dict__["alert_name"] = None
        __props__.__dict__["alert_sensitivity_threshold"] = None
        __props__.__dict__["anomaly_detector_arn"] = None
        __props__.__dict__["arn"] = None
        return Alert(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['outputs.AlertAction']:
        """
        The action to be taken by the alert when an anomaly is detected.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="alertDescription")
    def alert_description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the alert.
        """
        return pulumi.get(self, "alert_description")

    @property
    @pulumi.getter(name="alertName")
    def alert_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the alert. If not provided, a name is generated automatically.
        """
        return pulumi.get(self, "alert_name")

    @property
    @pulumi.getter(name="alertSensitivityThreshold")
    def alert_sensitivity_threshold(self) -> pulumi.Output[int]:
        """
        A number between 0 and 100 (inclusive) that tunes the sensitivity of the alert.
        """
        return pulumi.get(self, "alert_sensitivity_threshold")

    @property
    @pulumi.getter(name="anomalyDetectorArn")
    def anomaly_detector_arn(self) -> pulumi.Output[str]:
        """
        The Amazon resource name (ARN) of the Anomaly Detector to alert.
        """
        return pulumi.get(self, "anomaly_detector_arn")

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        ARN assigned to the alert.
        """
        return pulumi.get(self, "arn")

