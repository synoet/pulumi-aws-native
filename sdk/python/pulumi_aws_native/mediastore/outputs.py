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

__all__ = [
    'ContainerCorsRule',
    'ContainerMetricPolicy',
    'ContainerMetricPolicyRule',
    'ContainerTag',
]

@pulumi.output_type
class ContainerCorsRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowedHeaders":
            suggest = "allowed_headers"
        elif key == "allowedMethods":
            suggest = "allowed_methods"
        elif key == "allowedOrigins":
            suggest = "allowed_origins"
        elif key == "exposeHeaders":
            suggest = "expose_headers"
        elif key == "maxAgeSeconds":
            suggest = "max_age_seconds"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerCorsRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerCorsRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerCorsRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allowed_headers: Optional[Sequence[str]] = None,
                 allowed_methods: Optional[Sequence[str]] = None,
                 allowed_origins: Optional[Sequence[str]] = None,
                 expose_headers: Optional[Sequence[str]] = None,
                 max_age_seconds: Optional[int] = None):
        if allowed_headers is not None:
            pulumi.set(__self__, "allowed_headers", allowed_headers)
        if allowed_methods is not None:
            pulumi.set(__self__, "allowed_methods", allowed_methods)
        if allowed_origins is not None:
            pulumi.set(__self__, "allowed_origins", allowed_origins)
        if expose_headers is not None:
            pulumi.set(__self__, "expose_headers", expose_headers)
        if max_age_seconds is not None:
            pulumi.set(__self__, "max_age_seconds", max_age_seconds)

    @property
    @pulumi.getter(name="allowedHeaders")
    def allowed_headers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_headers")

    @property
    @pulumi.getter(name="allowedMethods")
    def allowed_methods(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_methods")

    @property
    @pulumi.getter(name="allowedOrigins")
    def allowed_origins(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "allowed_origins")

    @property
    @pulumi.getter(name="exposeHeaders")
    def expose_headers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "expose_headers")

    @property
    @pulumi.getter(name="maxAgeSeconds")
    def max_age_seconds(self) -> Optional[int]:
        return pulumi.get(self, "max_age_seconds")


@pulumi.output_type
class ContainerMetricPolicy(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "containerLevelMetrics":
            suggest = "container_level_metrics"
        elif key == "metricPolicyRules":
            suggest = "metric_policy_rules"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerMetricPolicy. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerMetricPolicy.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerMetricPolicy.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 container_level_metrics: str,
                 metric_policy_rules: Optional[Sequence['outputs.ContainerMetricPolicyRule']] = None):
        pulumi.set(__self__, "container_level_metrics", container_level_metrics)
        if metric_policy_rules is not None:
            pulumi.set(__self__, "metric_policy_rules", metric_policy_rules)

    @property
    @pulumi.getter(name="containerLevelMetrics")
    def container_level_metrics(self) -> str:
        return pulumi.get(self, "container_level_metrics")

    @property
    @pulumi.getter(name="metricPolicyRules")
    def metric_policy_rules(self) -> Optional[Sequence['outputs.ContainerMetricPolicyRule']]:
        return pulumi.get(self, "metric_policy_rules")


@pulumi.output_type
class ContainerMetricPolicyRule(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "objectGroup":
            suggest = "object_group"
        elif key == "objectGroupName":
            suggest = "object_group_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerMetricPolicyRule. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerMetricPolicyRule.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerMetricPolicyRule.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 object_group: str,
                 object_group_name: str):
        pulumi.set(__self__, "object_group", object_group)
        pulumi.set(__self__, "object_group_name", object_group_name)

    @property
    @pulumi.getter(name="objectGroup")
    def object_group(self) -> str:
        return pulumi.get(self, "object_group")

    @property
    @pulumi.getter(name="objectGroupName")
    def object_group_name(self) -> str:
        return pulumi.get(self, "object_group_name")


@pulumi.output_type
class ContainerTag(dict):
    def __init__(__self__, *,
                 key: str,
                 value: str):
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        return pulumi.get(self, "value")


