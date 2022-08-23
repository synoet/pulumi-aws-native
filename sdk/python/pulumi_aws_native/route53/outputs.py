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
    'CidrCollectionLocation',
    'HealthCheckAlarmIdentifier',
    'HealthCheckConfigProperties',
    'HealthCheckTag',
    'HostedZoneConfig',
    'HostedZoneQueryLoggingConfig',
    'HostedZoneTag',
    'HostedZoneVPC',
    'RecordSetAliasTarget',
    'RecordSetCidrRoutingConfig',
    'RecordSetGeoLocation',
    'RecordSetGroupAliasTarget',
    'RecordSetGroupCidrRoutingConfig',
    'RecordSetGroupGeoLocation',
    'RecordSetGroupRecordSet',
]

@pulumi.output_type
class CidrCollectionLocation(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cidrList":
            suggest = "cidr_list"
        elif key == "locationName":
            suggest = "location_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CidrCollectionLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CidrCollectionLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CidrCollectionLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cidr_list: Sequence[str],
                 location_name: str):
        """
        :param Sequence[str] cidr_list: A list of CIDR blocks.
        :param str location_name: The name of the location that is associated with the CIDR collection.
        """
        pulumi.set(__self__, "cidr_list", cidr_list)
        pulumi.set(__self__, "location_name", location_name)

    @property
    @pulumi.getter(name="cidrList")
    def cidr_list(self) -> Sequence[str]:
        """
        A list of CIDR blocks.
        """
        return pulumi.get(self, "cidr_list")

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> str:
        """
        The name of the location that is associated with the CIDR collection.
        """
        return pulumi.get(self, "location_name")


@pulumi.output_type
class HealthCheckAlarmIdentifier(dict):
    """
    A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
    """
    def __init__(__self__, *,
                 name: str,
                 region: str):
        """
        A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
        :param str name: The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
        :param str region: For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "region", region)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.
        """
        return pulumi.get(self, "region")


@pulumi.output_type
class HealthCheckConfigProperties(dict):
    """
    A complex type that contains information about the health check.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "alarmIdentifier":
            suggest = "alarm_identifier"
        elif key == "childHealthChecks":
            suggest = "child_health_checks"
        elif key == "enableSNI":
            suggest = "enable_sni"
        elif key == "failureThreshold":
            suggest = "failure_threshold"
        elif key == "fullyQualifiedDomainName":
            suggest = "fully_qualified_domain_name"
        elif key == "healthThreshold":
            suggest = "health_threshold"
        elif key == "iPAddress":
            suggest = "i_p_address"
        elif key == "insufficientDataHealthStatus":
            suggest = "insufficient_data_health_status"
        elif key == "measureLatency":
            suggest = "measure_latency"
        elif key == "requestInterval":
            suggest = "request_interval"
        elif key == "resourcePath":
            suggest = "resource_path"
        elif key == "routingControlArn":
            suggest = "routing_control_arn"
        elif key == "searchString":
            suggest = "search_string"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HealthCheckConfigProperties. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HealthCheckConfigProperties.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HealthCheckConfigProperties.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 type: 'HealthCheckConfigPropertiesType',
                 alarm_identifier: Optional['outputs.HealthCheckAlarmIdentifier'] = None,
                 child_health_checks: Optional[Sequence[str]] = None,
                 enable_sni: Optional[bool] = None,
                 failure_threshold: Optional[int] = None,
                 fully_qualified_domain_name: Optional[str] = None,
                 health_threshold: Optional[int] = None,
                 i_p_address: Optional[str] = None,
                 insufficient_data_health_status: Optional['HealthCheckConfigPropertiesInsufficientDataHealthStatus'] = None,
                 inverted: Optional[bool] = None,
                 measure_latency: Optional[bool] = None,
                 port: Optional[int] = None,
                 regions: Optional[Sequence[str]] = None,
                 request_interval: Optional[int] = None,
                 resource_path: Optional[str] = None,
                 routing_control_arn: Optional[str] = None,
                 search_string: Optional[str] = None):
        """
        A complex type that contains information about the health check.
        """
        pulumi.set(__self__, "type", type)
        if alarm_identifier is not None:
            pulumi.set(__self__, "alarm_identifier", alarm_identifier)
        if child_health_checks is not None:
            pulumi.set(__self__, "child_health_checks", child_health_checks)
        if enable_sni is not None:
            pulumi.set(__self__, "enable_sni", enable_sni)
        if failure_threshold is not None:
            pulumi.set(__self__, "failure_threshold", failure_threshold)
        if fully_qualified_domain_name is not None:
            pulumi.set(__self__, "fully_qualified_domain_name", fully_qualified_domain_name)
        if health_threshold is not None:
            pulumi.set(__self__, "health_threshold", health_threshold)
        if i_p_address is not None:
            pulumi.set(__self__, "i_p_address", i_p_address)
        if insufficient_data_health_status is not None:
            pulumi.set(__self__, "insufficient_data_health_status", insufficient_data_health_status)
        if inverted is not None:
            pulumi.set(__self__, "inverted", inverted)
        if measure_latency is not None:
            pulumi.set(__self__, "measure_latency", measure_latency)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if regions is not None:
            pulumi.set(__self__, "regions", regions)
        if request_interval is not None:
            pulumi.set(__self__, "request_interval", request_interval)
        if resource_path is not None:
            pulumi.set(__self__, "resource_path", resource_path)
        if routing_control_arn is not None:
            pulumi.set(__self__, "routing_control_arn", routing_control_arn)
        if search_string is not None:
            pulumi.set(__self__, "search_string", search_string)

    @property
    @pulumi.getter
    def type(self) -> 'HealthCheckConfigPropertiesType':
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="alarmIdentifier")
    def alarm_identifier(self) -> Optional['outputs.HealthCheckAlarmIdentifier']:
        return pulumi.get(self, "alarm_identifier")

    @property
    @pulumi.getter(name="childHealthChecks")
    def child_health_checks(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "child_health_checks")

    @property
    @pulumi.getter(name="enableSNI")
    def enable_sni(self) -> Optional[bool]:
        return pulumi.get(self, "enable_sni")

    @property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[int]:
        return pulumi.get(self, "failure_threshold")

    @property
    @pulumi.getter(name="fullyQualifiedDomainName")
    def fully_qualified_domain_name(self) -> Optional[str]:
        return pulumi.get(self, "fully_qualified_domain_name")

    @property
    @pulumi.getter(name="healthThreshold")
    def health_threshold(self) -> Optional[int]:
        return pulumi.get(self, "health_threshold")

    @property
    @pulumi.getter(name="iPAddress")
    def i_p_address(self) -> Optional[str]:
        return pulumi.get(self, "i_p_address")

    @property
    @pulumi.getter(name="insufficientDataHealthStatus")
    def insufficient_data_health_status(self) -> Optional['HealthCheckConfigPropertiesInsufficientDataHealthStatus']:
        return pulumi.get(self, "insufficient_data_health_status")

    @property
    @pulumi.getter
    def inverted(self) -> Optional[bool]:
        return pulumi.get(self, "inverted")

    @property
    @pulumi.getter(name="measureLatency")
    def measure_latency(self) -> Optional[bool]:
        return pulumi.get(self, "measure_latency")

    @property
    @pulumi.getter
    def port(self) -> Optional[int]:
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def regions(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "regions")

    @property
    @pulumi.getter(name="requestInterval")
    def request_interval(self) -> Optional[int]:
        return pulumi.get(self, "request_interval")

    @property
    @pulumi.getter(name="resourcePath")
    def resource_path(self) -> Optional[str]:
        return pulumi.get(self, "resource_path")

    @property
    @pulumi.getter(name="routingControlArn")
    def routing_control_arn(self) -> Optional[str]:
        return pulumi.get(self, "routing_control_arn")

    @property
    @pulumi.getter(name="searchString")
    def search_string(self) -> Optional[str]:
        return pulumi.get(self, "search_string")


@pulumi.output_type
class HealthCheckTag(dict):
    """
    A key-value pair to associate with a resource.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A key-value pair to associate with a resource.
        :param str key: The key name of the tag.
        :param str value: The value for the tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class HostedZoneConfig(dict):
    """
    A complex type that contains an optional comment.

    If you don't want to specify a comment, omit the HostedZoneConfig and Comment elements.
    """
    def __init__(__self__, *,
                 comment: Optional[str] = None):
        """
        A complex type that contains an optional comment.

        If you don't want to specify a comment, omit the HostedZoneConfig and Comment elements.
        :param str comment: Any comments that you want to include about the hosted zone.
        """
        if comment is not None:
            pulumi.set(__self__, "comment", comment)

    @property
    @pulumi.getter
    def comment(self) -> Optional[str]:
        """
        Any comments that you want to include about the hosted zone.
        """
        return pulumi.get(self, "comment")


@pulumi.output_type
class HostedZoneQueryLoggingConfig(dict):
    """
    A complex type that contains information about a configuration for DNS query logging.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "cloudWatchLogsLogGroupArn":
            suggest = "cloud_watch_logs_log_group_arn"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostedZoneQueryLoggingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostedZoneQueryLoggingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostedZoneQueryLoggingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 cloud_watch_logs_log_group_arn: str):
        """
        A complex type that contains information about a configuration for DNS query logging.
        :param str cloud_watch_logs_log_group_arn: The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.
        """
        pulumi.set(__self__, "cloud_watch_logs_log_group_arn", cloud_watch_logs_log_group_arn)

    @property
    @pulumi.getter(name="cloudWatchLogsLogGroupArn")
    def cloud_watch_logs_log_group_arn(self) -> str:
        """
        The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.
        """
        return pulumi.get(self, "cloud_watch_logs_log_group_arn")


@pulumi.output_type
class HostedZoneTag(dict):
    """
    A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.
        :param str key: The key name of the tag.
        :param str value: The value for the tag.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        The key name of the tag.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        The value for the tag.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class HostedZoneVPC(dict):
    """
    A complex type that contains information about an Amazon VPC. Route 53 Resolver uses the records in the private hosted zone to route traffic in that VPC.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vPCId":
            suggest = "v_pc_id"
        elif key == "vPCRegion":
            suggest = "v_pc_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in HostedZoneVPC. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        HostedZoneVPC.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        HostedZoneVPC.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 v_pc_id: str,
                 v_pc_region: str):
        """
        A complex type that contains information about an Amazon VPC. Route 53 Resolver uses the records in the private hosted zone to route traffic in that VPC.
        :param str v_pc_id: The ID of an Amazon VPC.
        :param str v_pc_region: The region that an Amazon VPC was created in. See https://docs.aws.amazon.com/general/latest/gr/rande.html for a list of up to date regions.
        """
        pulumi.set(__self__, "v_pc_id", v_pc_id)
        pulumi.set(__self__, "v_pc_region", v_pc_region)

    @property
    @pulumi.getter(name="vPCId")
    def v_pc_id(self) -> str:
        """
        The ID of an Amazon VPC.
        """
        return pulumi.get(self, "v_pc_id")

    @property
    @pulumi.getter(name="vPCRegion")
    def v_pc_region(self) -> str:
        """
        The region that an Amazon VPC was created in. See https://docs.aws.amazon.com/general/latest/gr/rande.html for a list of up to date regions.
        """
        return pulumi.get(self, "v_pc_region")


@pulumi.output_type
class RecordSetAliasTarget(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dNSName":
            suggest = "d_ns_name"
        elif key == "hostedZoneId":
            suggest = "hosted_zone_id"
        elif key == "evaluateTargetHealth":
            suggest = "evaluate_target_health"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetAliasTarget. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetAliasTarget.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetAliasTarget.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 d_ns_name: str,
                 hosted_zone_id: str,
                 evaluate_target_health: Optional[bool] = None):
        pulumi.set(__self__, "d_ns_name", d_ns_name)
        pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if evaluate_target_health is not None:
            pulumi.set(__self__, "evaluate_target_health", evaluate_target_health)

    @property
    @pulumi.getter(name="dNSName")
    def d_ns_name(self) -> str:
        return pulumi.get(self, "d_ns_name")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> str:
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[bool]:
        return pulumi.get(self, "evaluate_target_health")


@pulumi.output_type
class RecordSetCidrRoutingConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "collectionId":
            suggest = "collection_id"
        elif key == "locationName":
            suggest = "location_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetCidrRoutingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetCidrRoutingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetCidrRoutingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 collection_id: str,
                 location_name: str):
        pulumi.set(__self__, "collection_id", collection_id)
        pulumi.set(__self__, "location_name", location_name)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> str:
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> str:
        return pulumi.get(self, "location_name")


@pulumi.output_type
class RecordSetGeoLocation(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "continentCode":
            suggest = "continent_code"
        elif key == "countryCode":
            suggest = "country_code"
        elif key == "subdivisionCode":
            suggest = "subdivision_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetGeoLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetGeoLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetGeoLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 continent_code: Optional[str] = None,
                 country_code: Optional[str] = None,
                 subdivision_code: Optional[str] = None):
        if continent_code is not None:
            pulumi.set(__self__, "continent_code", continent_code)
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if subdivision_code is not None:
            pulumi.set(__self__, "subdivision_code", subdivision_code)

    @property
    @pulumi.getter(name="continentCode")
    def continent_code(self) -> Optional[str]:
        return pulumi.get(self, "continent_code")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[str]:
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter(name="subdivisionCode")
    def subdivision_code(self) -> Optional[str]:
        return pulumi.get(self, "subdivision_code")


@pulumi.output_type
class RecordSetGroupAliasTarget(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dNSName":
            suggest = "d_ns_name"
        elif key == "hostedZoneId":
            suggest = "hosted_zone_id"
        elif key == "evaluateTargetHealth":
            suggest = "evaluate_target_health"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetGroupAliasTarget. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetGroupAliasTarget.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetGroupAliasTarget.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 d_ns_name: str,
                 hosted_zone_id: str,
                 evaluate_target_health: Optional[bool] = None):
        pulumi.set(__self__, "d_ns_name", d_ns_name)
        pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if evaluate_target_health is not None:
            pulumi.set(__self__, "evaluate_target_health", evaluate_target_health)

    @property
    @pulumi.getter(name="dNSName")
    def d_ns_name(self) -> str:
        return pulumi.get(self, "d_ns_name")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> str:
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="evaluateTargetHealth")
    def evaluate_target_health(self) -> Optional[bool]:
        return pulumi.get(self, "evaluate_target_health")


@pulumi.output_type
class RecordSetGroupCidrRoutingConfig(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "collectionId":
            suggest = "collection_id"
        elif key == "locationName":
            suggest = "location_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetGroupCidrRoutingConfig. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetGroupCidrRoutingConfig.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetGroupCidrRoutingConfig.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 collection_id: str,
                 location_name: str):
        pulumi.set(__self__, "collection_id", collection_id)
        pulumi.set(__self__, "location_name", location_name)

    @property
    @pulumi.getter(name="collectionId")
    def collection_id(self) -> str:
        return pulumi.get(self, "collection_id")

    @property
    @pulumi.getter(name="locationName")
    def location_name(self) -> str:
        return pulumi.get(self, "location_name")


@pulumi.output_type
class RecordSetGroupGeoLocation(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "continentCode":
            suggest = "continent_code"
        elif key == "countryCode":
            suggest = "country_code"
        elif key == "subdivisionCode":
            suggest = "subdivision_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetGroupGeoLocation. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetGroupGeoLocation.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetGroupGeoLocation.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 continent_code: Optional[str] = None,
                 country_code: Optional[str] = None,
                 subdivision_code: Optional[str] = None):
        if continent_code is not None:
            pulumi.set(__self__, "continent_code", continent_code)
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if subdivision_code is not None:
            pulumi.set(__self__, "subdivision_code", subdivision_code)

    @property
    @pulumi.getter(name="continentCode")
    def continent_code(self) -> Optional[str]:
        return pulumi.get(self, "continent_code")

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[str]:
        return pulumi.get(self, "country_code")

    @property
    @pulumi.getter(name="subdivisionCode")
    def subdivision_code(self) -> Optional[str]:
        return pulumi.get(self, "subdivision_code")


@pulumi.output_type
class RecordSetGroupRecordSet(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "aliasTarget":
            suggest = "alias_target"
        elif key == "cidrRoutingConfig":
            suggest = "cidr_routing_config"
        elif key == "geoLocation":
            suggest = "geo_location"
        elif key == "healthCheckId":
            suggest = "health_check_id"
        elif key == "hostedZoneId":
            suggest = "hosted_zone_id"
        elif key == "hostedZoneName":
            suggest = "hosted_zone_name"
        elif key == "multiValueAnswer":
            suggest = "multi_value_answer"
        elif key == "resourceRecords":
            suggest = "resource_records"
        elif key == "setIdentifier":
            suggest = "set_identifier"
        elif key == "tTL":
            suggest = "t_tl"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RecordSetGroupRecordSet. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RecordSetGroupRecordSet.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RecordSetGroupRecordSet.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 type: str,
                 alias_target: Optional['outputs.RecordSetGroupAliasTarget'] = None,
                 cidr_routing_config: Optional['outputs.RecordSetGroupCidrRoutingConfig'] = None,
                 failover: Optional[str] = None,
                 geo_location: Optional['outputs.RecordSetGroupGeoLocation'] = None,
                 health_check_id: Optional[str] = None,
                 hosted_zone_id: Optional[str] = None,
                 hosted_zone_name: Optional[str] = None,
                 multi_value_answer: Optional[bool] = None,
                 region: Optional[str] = None,
                 resource_records: Optional[Sequence[str]] = None,
                 set_identifier: Optional[str] = None,
                 t_tl: Optional[str] = None,
                 weight: Optional[int] = None):
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)
        if alias_target is not None:
            pulumi.set(__self__, "alias_target", alias_target)
        if cidr_routing_config is not None:
            pulumi.set(__self__, "cidr_routing_config", cidr_routing_config)
        if failover is not None:
            pulumi.set(__self__, "failover", failover)
        if geo_location is not None:
            pulumi.set(__self__, "geo_location", geo_location)
        if health_check_id is not None:
            pulumi.set(__self__, "health_check_id", health_check_id)
        if hosted_zone_id is not None:
            pulumi.set(__self__, "hosted_zone_id", hosted_zone_id)
        if hosted_zone_name is not None:
            pulumi.set(__self__, "hosted_zone_name", hosted_zone_name)
        if multi_value_answer is not None:
            pulumi.set(__self__, "multi_value_answer", multi_value_answer)
        if region is not None:
            pulumi.set(__self__, "region", region)
        if resource_records is not None:
            pulumi.set(__self__, "resource_records", resource_records)
        if set_identifier is not None:
            pulumi.set(__self__, "set_identifier", set_identifier)
        if t_tl is not None:
            pulumi.set(__self__, "t_tl", t_tl)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="aliasTarget")
    def alias_target(self) -> Optional['outputs.RecordSetGroupAliasTarget']:
        return pulumi.get(self, "alias_target")

    @property
    @pulumi.getter(name="cidrRoutingConfig")
    def cidr_routing_config(self) -> Optional['outputs.RecordSetGroupCidrRoutingConfig']:
        return pulumi.get(self, "cidr_routing_config")

    @property
    @pulumi.getter
    def failover(self) -> Optional[str]:
        return pulumi.get(self, "failover")

    @property
    @pulumi.getter(name="geoLocation")
    def geo_location(self) -> Optional['outputs.RecordSetGroupGeoLocation']:
        return pulumi.get(self, "geo_location")

    @property
    @pulumi.getter(name="healthCheckId")
    def health_check_id(self) -> Optional[str]:
        return pulumi.get(self, "health_check_id")

    @property
    @pulumi.getter(name="hostedZoneId")
    def hosted_zone_id(self) -> Optional[str]:
        return pulumi.get(self, "hosted_zone_id")

    @property
    @pulumi.getter(name="hostedZoneName")
    def hosted_zone_name(self) -> Optional[str]:
        return pulumi.get(self, "hosted_zone_name")

    @property
    @pulumi.getter(name="multiValueAnswer")
    def multi_value_answer(self) -> Optional[bool]:
        return pulumi.get(self, "multi_value_answer")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceRecords")
    def resource_records(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_records")

    @property
    @pulumi.getter(name="setIdentifier")
    def set_identifier(self) -> Optional[str]:
        return pulumi.get(self, "set_identifier")

    @property
    @pulumi.getter(name="tTL")
    def t_tl(self) -> Optional[str]:
        return pulumi.get(self, "t_tl")

    @property
    @pulumi.getter
    def weight(self) -> Optional[int]:
        return pulumi.get(self, "weight")


