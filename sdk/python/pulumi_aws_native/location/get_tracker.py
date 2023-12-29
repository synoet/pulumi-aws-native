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
    'GetTrackerResult',
    'AwaitableGetTrackerResult',
    'get_tracker',
    'get_tracker_output',
]

@pulumi.output_type
class GetTrackerResult:
    def __init__(__self__, arn=None, create_time=None, description=None, event_bridge_enabled=None, kms_key_enable_geospatial_queries=None, position_filtering=None, pricing_plan=None, pricing_plan_data_source=None, tags=None, tracker_arn=None, update_time=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if event_bridge_enabled and not isinstance(event_bridge_enabled, bool):
            raise TypeError("Expected argument 'event_bridge_enabled' to be a bool")
        pulumi.set(__self__, "event_bridge_enabled", event_bridge_enabled)
        if kms_key_enable_geospatial_queries and not isinstance(kms_key_enable_geospatial_queries, bool):
            raise TypeError("Expected argument 'kms_key_enable_geospatial_queries' to be a bool")
        pulumi.set(__self__, "kms_key_enable_geospatial_queries", kms_key_enable_geospatial_queries)
        if position_filtering and not isinstance(position_filtering, str):
            raise TypeError("Expected argument 'position_filtering' to be a str")
        pulumi.set(__self__, "position_filtering", position_filtering)
        if pricing_plan and not isinstance(pricing_plan, str):
            raise TypeError("Expected argument 'pricing_plan' to be a str")
        pulumi.set(__self__, "pricing_plan", pricing_plan)
        if pricing_plan_data_source and not isinstance(pricing_plan_data_source, str):
            raise TypeError("Expected argument 'pricing_plan_data_source' to be a str")
        pulumi.set(__self__, "pricing_plan_data_source", pricing_plan_data_source)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if tracker_arn and not isinstance(tracker_arn, str):
            raise TypeError("Expected argument 'tracker_arn' to be a str")
        pulumi.set(__self__, "tracker_arn", tracker_arn)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[str]:
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="eventBridgeEnabled")
    def event_bridge_enabled(self) -> Optional[bool]:
        return pulumi.get(self, "event_bridge_enabled")

    @property
    @pulumi.getter(name="kmsKeyEnableGeospatialQueries")
    def kms_key_enable_geospatial_queries(self) -> Optional[bool]:
        return pulumi.get(self, "kms_key_enable_geospatial_queries")

    @property
    @pulumi.getter(name="positionFiltering")
    def position_filtering(self) -> Optional['TrackerPositionFiltering']:
        return pulumi.get(self, "position_filtering")

    @property
    @pulumi.getter(name="pricingPlan")
    def pricing_plan(self) -> Optional['TrackerPricingPlan']:
        return pulumi.get(self, "pricing_plan")

    @property
    @pulumi.getter(name="pricingPlanDataSource")
    def pricing_plan_data_source(self) -> Optional[str]:
        return pulumi.get(self, "pricing_plan_data_source")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TrackerTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="trackerArn")
    def tracker_arn(self) -> Optional[str]:
        return pulumi.get(self, "tracker_arn")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[str]:
        return pulumi.get(self, "update_time")


class AwaitableGetTrackerResult(GetTrackerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrackerResult(
            arn=self.arn,
            create_time=self.create_time,
            description=self.description,
            event_bridge_enabled=self.event_bridge_enabled,
            kms_key_enable_geospatial_queries=self.kms_key_enable_geospatial_queries,
            position_filtering=self.position_filtering,
            pricing_plan=self.pricing_plan,
            pricing_plan_data_source=self.pricing_plan_data_source,
            tags=self.tags,
            tracker_arn=self.tracker_arn,
            update_time=self.update_time)


def get_tracker(tracker_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrackerResult:
    """
    Definition of AWS::Location::Tracker Resource Type
    """
    __args__ = dict()
    __args__['trackerName'] = tracker_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:location:getTracker', __args__, opts=opts, typ=GetTrackerResult).value

    return AwaitableGetTrackerResult(
        arn=pulumi.get(__ret__, 'arn'),
        create_time=pulumi.get(__ret__, 'create_time'),
        description=pulumi.get(__ret__, 'description'),
        event_bridge_enabled=pulumi.get(__ret__, 'event_bridge_enabled'),
        kms_key_enable_geospatial_queries=pulumi.get(__ret__, 'kms_key_enable_geospatial_queries'),
        position_filtering=pulumi.get(__ret__, 'position_filtering'),
        pricing_plan=pulumi.get(__ret__, 'pricing_plan'),
        pricing_plan_data_source=pulumi.get(__ret__, 'pricing_plan_data_source'),
        tags=pulumi.get(__ret__, 'tags'),
        tracker_arn=pulumi.get(__ret__, 'tracker_arn'),
        update_time=pulumi.get(__ret__, 'update_time'))


@_utilities.lift_output_func(get_tracker)
def get_tracker_output(tracker_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrackerResult]:
    """
    Definition of AWS::Location::Tracker Resource Type
    """
    ...
