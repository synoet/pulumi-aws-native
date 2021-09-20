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

__all__ = [
    'DestinationTag',
    'DeviceProfileLoRaWANDeviceProfile',
    'DeviceProfileTag',
    'ServiceProfileLoRaWANServiceProfile',
    'ServiceProfileTag',
    'TaskDefinitionLoRaWANGatewayVersion',
    'TaskDefinitionLoRaWANUpdateGatewayTaskCreate',
    'TaskDefinitionLoRaWANUpdateGatewayTaskEntry',
    'TaskDefinitionTag',
    'TaskDefinitionUpdateWirelessGatewayTaskCreate',
    'WirelessDeviceAbpV10x',
    'WirelessDeviceAbpV11',
    'WirelessDeviceLoRaWANDevice',
    'WirelessDeviceOtaaV10x',
    'WirelessDeviceOtaaV11',
    'WirelessDeviceSessionKeysAbpV10x',
    'WirelessDeviceSessionKeysAbpV11',
    'WirelessDeviceTag',
    'WirelessGatewayLoRaWANGateway',
    'WirelessGatewayTag',
]

@pulumi.output_type
class DestinationTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class DeviceProfileLoRaWANDeviceProfile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "classBTimeout":
            suggest = "class_b_timeout"
        elif key == "classCTimeout":
            suggest = "class_c_timeout"
        elif key == "macVersion":
            suggest = "mac_version"
        elif key == "maxDutyCycle":
            suggest = "max_duty_cycle"
        elif key == "maxEirp":
            suggest = "max_eirp"
        elif key == "pingSlotDr":
            suggest = "ping_slot_dr"
        elif key == "pingSlotFreq":
            suggest = "ping_slot_freq"
        elif key == "pingSlotPeriod":
            suggest = "ping_slot_period"
        elif key == "regParamsRevision":
            suggest = "reg_params_revision"
        elif key == "rfRegion":
            suggest = "rf_region"
        elif key == "supports32BitFCnt":
            suggest = "supports32_bit_f_cnt"
        elif key == "supportsClassB":
            suggest = "supports_class_b"
        elif key == "supportsClassC":
            suggest = "supports_class_c"
        elif key == "supportsJoin":
            suggest = "supports_join"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in DeviceProfileLoRaWANDeviceProfile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        DeviceProfileLoRaWANDeviceProfile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        DeviceProfileLoRaWANDeviceProfile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 class_b_timeout: Optional[int] = None,
                 class_c_timeout: Optional[int] = None,
                 mac_version: Optional[str] = None,
                 max_duty_cycle: Optional[int] = None,
                 max_eirp: Optional[int] = None,
                 ping_slot_dr: Optional[int] = None,
                 ping_slot_freq: Optional[int] = None,
                 ping_slot_period: Optional[int] = None,
                 reg_params_revision: Optional[str] = None,
                 rf_region: Optional[str] = None,
                 supports32_bit_f_cnt: Optional[bool] = None,
                 supports_class_b: Optional[bool] = None,
                 supports_class_c: Optional[bool] = None,
                 supports_join: Optional[bool] = None):
        if class_b_timeout is not None:
            pulumi.set(__self__, "class_b_timeout", class_b_timeout)
        if class_c_timeout is not None:
            pulumi.set(__self__, "class_c_timeout", class_c_timeout)
        if mac_version is not None:
            pulumi.set(__self__, "mac_version", mac_version)
        if max_duty_cycle is not None:
            pulumi.set(__self__, "max_duty_cycle", max_duty_cycle)
        if max_eirp is not None:
            pulumi.set(__self__, "max_eirp", max_eirp)
        if ping_slot_dr is not None:
            pulumi.set(__self__, "ping_slot_dr", ping_slot_dr)
        if ping_slot_freq is not None:
            pulumi.set(__self__, "ping_slot_freq", ping_slot_freq)
        if ping_slot_period is not None:
            pulumi.set(__self__, "ping_slot_period", ping_slot_period)
        if reg_params_revision is not None:
            pulumi.set(__self__, "reg_params_revision", reg_params_revision)
        if rf_region is not None:
            pulumi.set(__self__, "rf_region", rf_region)
        if supports32_bit_f_cnt is not None:
            pulumi.set(__self__, "supports32_bit_f_cnt", supports32_bit_f_cnt)
        if supports_class_b is not None:
            pulumi.set(__self__, "supports_class_b", supports_class_b)
        if supports_class_c is not None:
            pulumi.set(__self__, "supports_class_c", supports_class_c)
        if supports_join is not None:
            pulumi.set(__self__, "supports_join", supports_join)

    @property
    @pulumi.getter(name="classBTimeout")
    def class_b_timeout(self) -> Optional[int]:
        return pulumi.get(self, "class_b_timeout")

    @property
    @pulumi.getter(name="classCTimeout")
    def class_c_timeout(self) -> Optional[int]:
        return pulumi.get(self, "class_c_timeout")

    @property
    @pulumi.getter(name="macVersion")
    def mac_version(self) -> Optional[str]:
        return pulumi.get(self, "mac_version")

    @property
    @pulumi.getter(name="maxDutyCycle")
    def max_duty_cycle(self) -> Optional[int]:
        return pulumi.get(self, "max_duty_cycle")

    @property
    @pulumi.getter(name="maxEirp")
    def max_eirp(self) -> Optional[int]:
        return pulumi.get(self, "max_eirp")

    @property
    @pulumi.getter(name="pingSlotDr")
    def ping_slot_dr(self) -> Optional[int]:
        return pulumi.get(self, "ping_slot_dr")

    @property
    @pulumi.getter(name="pingSlotFreq")
    def ping_slot_freq(self) -> Optional[int]:
        return pulumi.get(self, "ping_slot_freq")

    @property
    @pulumi.getter(name="pingSlotPeriod")
    def ping_slot_period(self) -> Optional[int]:
        return pulumi.get(self, "ping_slot_period")

    @property
    @pulumi.getter(name="regParamsRevision")
    def reg_params_revision(self) -> Optional[str]:
        return pulumi.get(self, "reg_params_revision")

    @property
    @pulumi.getter(name="rfRegion")
    def rf_region(self) -> Optional[str]:
        return pulumi.get(self, "rf_region")

    @property
    @pulumi.getter(name="supports32BitFCnt")
    def supports32_bit_f_cnt(self) -> Optional[bool]:
        return pulumi.get(self, "supports32_bit_f_cnt")

    @property
    @pulumi.getter(name="supportsClassB")
    def supports_class_b(self) -> Optional[bool]:
        return pulumi.get(self, "supports_class_b")

    @property
    @pulumi.getter(name="supportsClassC")
    def supports_class_c(self) -> Optional[bool]:
        return pulumi.get(self, "supports_class_c")

    @property
    @pulumi.getter(name="supportsJoin")
    def supports_join(self) -> Optional[bool]:
        return pulumi.get(self, "supports_join")


@pulumi.output_type
class DeviceProfileTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class ServiceProfileLoRaWANServiceProfile(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "addGwMetadata":
            suggest = "add_gw_metadata"
        elif key == "channelMask":
            suggest = "channel_mask"
        elif key == "devStatusReqFreq":
            suggest = "dev_status_req_freq"
        elif key == "dlBucketSize":
            suggest = "dl_bucket_size"
        elif key == "dlRate":
            suggest = "dl_rate"
        elif key == "dlRatePolicy":
            suggest = "dl_rate_policy"
        elif key == "drMax":
            suggest = "dr_max"
        elif key == "drMin":
            suggest = "dr_min"
        elif key == "hrAllowed":
            suggest = "hr_allowed"
        elif key == "minGwDiversity":
            suggest = "min_gw_diversity"
        elif key == "nwkGeoLoc":
            suggest = "nwk_geo_loc"
        elif key == "prAllowed":
            suggest = "pr_allowed"
        elif key == "raAllowed":
            suggest = "ra_allowed"
        elif key == "reportDevStatusBattery":
            suggest = "report_dev_status_battery"
        elif key == "reportDevStatusMargin":
            suggest = "report_dev_status_margin"
        elif key == "targetPer":
            suggest = "target_per"
        elif key == "ulBucketSize":
            suggest = "ul_bucket_size"
        elif key == "ulRate":
            suggest = "ul_rate"
        elif key == "ulRatePolicy":
            suggest = "ul_rate_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceProfileLoRaWANServiceProfile. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceProfileLoRaWANServiceProfile.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceProfileLoRaWANServiceProfile.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 add_gw_metadata: Optional[bool] = None,
                 channel_mask: Optional[str] = None,
                 dev_status_req_freq: Optional[int] = None,
                 dl_bucket_size: Optional[int] = None,
                 dl_rate: Optional[int] = None,
                 dl_rate_policy: Optional[str] = None,
                 dr_max: Optional[int] = None,
                 dr_min: Optional[int] = None,
                 hr_allowed: Optional[bool] = None,
                 min_gw_diversity: Optional[int] = None,
                 nwk_geo_loc: Optional[bool] = None,
                 pr_allowed: Optional[bool] = None,
                 ra_allowed: Optional[bool] = None,
                 report_dev_status_battery: Optional[bool] = None,
                 report_dev_status_margin: Optional[bool] = None,
                 target_per: Optional[int] = None,
                 ul_bucket_size: Optional[int] = None,
                 ul_rate: Optional[int] = None,
                 ul_rate_policy: Optional[str] = None):
        if add_gw_metadata is not None:
            pulumi.set(__self__, "add_gw_metadata", add_gw_metadata)
        if channel_mask is not None:
            pulumi.set(__self__, "channel_mask", channel_mask)
        if dev_status_req_freq is not None:
            pulumi.set(__self__, "dev_status_req_freq", dev_status_req_freq)
        if dl_bucket_size is not None:
            pulumi.set(__self__, "dl_bucket_size", dl_bucket_size)
        if dl_rate is not None:
            pulumi.set(__self__, "dl_rate", dl_rate)
        if dl_rate_policy is not None:
            pulumi.set(__self__, "dl_rate_policy", dl_rate_policy)
        if dr_max is not None:
            pulumi.set(__self__, "dr_max", dr_max)
        if dr_min is not None:
            pulumi.set(__self__, "dr_min", dr_min)
        if hr_allowed is not None:
            pulumi.set(__self__, "hr_allowed", hr_allowed)
        if min_gw_diversity is not None:
            pulumi.set(__self__, "min_gw_diversity", min_gw_diversity)
        if nwk_geo_loc is not None:
            pulumi.set(__self__, "nwk_geo_loc", nwk_geo_loc)
        if pr_allowed is not None:
            pulumi.set(__self__, "pr_allowed", pr_allowed)
        if ra_allowed is not None:
            pulumi.set(__self__, "ra_allowed", ra_allowed)
        if report_dev_status_battery is not None:
            pulumi.set(__self__, "report_dev_status_battery", report_dev_status_battery)
        if report_dev_status_margin is not None:
            pulumi.set(__self__, "report_dev_status_margin", report_dev_status_margin)
        if target_per is not None:
            pulumi.set(__self__, "target_per", target_per)
        if ul_bucket_size is not None:
            pulumi.set(__self__, "ul_bucket_size", ul_bucket_size)
        if ul_rate is not None:
            pulumi.set(__self__, "ul_rate", ul_rate)
        if ul_rate_policy is not None:
            pulumi.set(__self__, "ul_rate_policy", ul_rate_policy)

    @property
    @pulumi.getter(name="addGwMetadata")
    def add_gw_metadata(self) -> Optional[bool]:
        return pulumi.get(self, "add_gw_metadata")

    @property
    @pulumi.getter(name="channelMask")
    def channel_mask(self) -> Optional[str]:
        return pulumi.get(self, "channel_mask")

    @property
    @pulumi.getter(name="devStatusReqFreq")
    def dev_status_req_freq(self) -> Optional[int]:
        return pulumi.get(self, "dev_status_req_freq")

    @property
    @pulumi.getter(name="dlBucketSize")
    def dl_bucket_size(self) -> Optional[int]:
        return pulumi.get(self, "dl_bucket_size")

    @property
    @pulumi.getter(name="dlRate")
    def dl_rate(self) -> Optional[int]:
        return pulumi.get(self, "dl_rate")

    @property
    @pulumi.getter(name="dlRatePolicy")
    def dl_rate_policy(self) -> Optional[str]:
        return pulumi.get(self, "dl_rate_policy")

    @property
    @pulumi.getter(name="drMax")
    def dr_max(self) -> Optional[int]:
        return pulumi.get(self, "dr_max")

    @property
    @pulumi.getter(name="drMin")
    def dr_min(self) -> Optional[int]:
        return pulumi.get(self, "dr_min")

    @property
    @pulumi.getter(name="hrAllowed")
    def hr_allowed(self) -> Optional[bool]:
        return pulumi.get(self, "hr_allowed")

    @property
    @pulumi.getter(name="minGwDiversity")
    def min_gw_diversity(self) -> Optional[int]:
        return pulumi.get(self, "min_gw_diversity")

    @property
    @pulumi.getter(name="nwkGeoLoc")
    def nwk_geo_loc(self) -> Optional[bool]:
        return pulumi.get(self, "nwk_geo_loc")

    @property
    @pulumi.getter(name="prAllowed")
    def pr_allowed(self) -> Optional[bool]:
        return pulumi.get(self, "pr_allowed")

    @property
    @pulumi.getter(name="raAllowed")
    def ra_allowed(self) -> Optional[bool]:
        return pulumi.get(self, "ra_allowed")

    @property
    @pulumi.getter(name="reportDevStatusBattery")
    def report_dev_status_battery(self) -> Optional[bool]:
        return pulumi.get(self, "report_dev_status_battery")

    @property
    @pulumi.getter(name="reportDevStatusMargin")
    def report_dev_status_margin(self) -> Optional[bool]:
        return pulumi.get(self, "report_dev_status_margin")

    @property
    @pulumi.getter(name="targetPer")
    def target_per(self) -> Optional[int]:
        return pulumi.get(self, "target_per")

    @property
    @pulumi.getter(name="ulBucketSize")
    def ul_bucket_size(self) -> Optional[int]:
        return pulumi.get(self, "ul_bucket_size")

    @property
    @pulumi.getter(name="ulRate")
    def ul_rate(self) -> Optional[int]:
        return pulumi.get(self, "ul_rate")

    @property
    @pulumi.getter(name="ulRatePolicy")
    def ul_rate_policy(self) -> Optional[str]:
        return pulumi.get(self, "ul_rate_policy")


@pulumi.output_type
class ServiceProfileTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class TaskDefinitionLoRaWANGatewayVersion(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "packageVersion":
            suggest = "package_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskDefinitionLoRaWANGatewayVersion. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskDefinitionLoRaWANGatewayVersion.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskDefinitionLoRaWANGatewayVersion.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 model: Optional[str] = None,
                 package_version: Optional[str] = None,
                 station: Optional[str] = None):
        if model is not None:
            pulumi.set(__self__, "model", model)
        if package_version is not None:
            pulumi.set(__self__, "package_version", package_version)
        if station is not None:
            pulumi.set(__self__, "station", station)

    @property
    @pulumi.getter
    def model(self) -> Optional[str]:
        return pulumi.get(self, "model")

    @property
    @pulumi.getter(name="packageVersion")
    def package_version(self) -> Optional[str]:
        return pulumi.get(self, "package_version")

    @property
    @pulumi.getter
    def station(self) -> Optional[str]:
        return pulumi.get(self, "station")


@pulumi.output_type
class TaskDefinitionLoRaWANUpdateGatewayTaskCreate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "currentVersion":
            suggest = "current_version"
        elif key == "sigKeyCrc":
            suggest = "sig_key_crc"
        elif key == "updateSignature":
            suggest = "update_signature"
        elif key == "updateVersion":
            suggest = "update_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskDefinitionLoRaWANUpdateGatewayTaskCreate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskDefinitionLoRaWANUpdateGatewayTaskCreate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskDefinitionLoRaWANUpdateGatewayTaskCreate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 current_version: Optional['outputs.TaskDefinitionLoRaWANGatewayVersion'] = None,
                 sig_key_crc: Optional[int] = None,
                 update_signature: Optional[str] = None,
                 update_version: Optional['outputs.TaskDefinitionLoRaWANGatewayVersion'] = None):
        if current_version is not None:
            pulumi.set(__self__, "current_version", current_version)
        if sig_key_crc is not None:
            pulumi.set(__self__, "sig_key_crc", sig_key_crc)
        if update_signature is not None:
            pulumi.set(__self__, "update_signature", update_signature)
        if update_version is not None:
            pulumi.set(__self__, "update_version", update_version)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional['outputs.TaskDefinitionLoRaWANGatewayVersion']:
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="sigKeyCrc")
    def sig_key_crc(self) -> Optional[int]:
        return pulumi.get(self, "sig_key_crc")

    @property
    @pulumi.getter(name="updateSignature")
    def update_signature(self) -> Optional[str]:
        return pulumi.get(self, "update_signature")

    @property
    @pulumi.getter(name="updateVersion")
    def update_version(self) -> Optional['outputs.TaskDefinitionLoRaWANGatewayVersion']:
        return pulumi.get(self, "update_version")


@pulumi.output_type
class TaskDefinitionLoRaWANUpdateGatewayTaskEntry(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "currentVersion":
            suggest = "current_version"
        elif key == "updateVersion":
            suggest = "update_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskDefinitionLoRaWANUpdateGatewayTaskEntry. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskDefinitionLoRaWANUpdateGatewayTaskEntry.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskDefinitionLoRaWANUpdateGatewayTaskEntry.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 current_version: Optional['outputs.TaskDefinitionLoRaWANGatewayVersion'] = None,
                 update_version: Optional['outputs.TaskDefinitionLoRaWANGatewayVersion'] = None):
        if current_version is not None:
            pulumi.set(__self__, "current_version", current_version)
        if update_version is not None:
            pulumi.set(__self__, "update_version", update_version)

    @property
    @pulumi.getter(name="currentVersion")
    def current_version(self) -> Optional['outputs.TaskDefinitionLoRaWANGatewayVersion']:
        return pulumi.get(self, "current_version")

    @property
    @pulumi.getter(name="updateVersion")
    def update_version(self) -> Optional['outputs.TaskDefinitionLoRaWANGatewayVersion']:
        return pulumi.get(self, "update_version")


@pulumi.output_type
class TaskDefinitionTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class TaskDefinitionUpdateWirelessGatewayTaskCreate(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "loRaWAN":
            suggest = "lo_ra_wan"
        elif key == "updateDataRole":
            suggest = "update_data_role"
        elif key == "updateDataSource":
            suggest = "update_data_source"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TaskDefinitionUpdateWirelessGatewayTaskCreate. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TaskDefinitionUpdateWirelessGatewayTaskCreate.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TaskDefinitionUpdateWirelessGatewayTaskCreate.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 lo_ra_wan: Optional['outputs.TaskDefinitionLoRaWANUpdateGatewayTaskCreate'] = None,
                 update_data_role: Optional[str] = None,
                 update_data_source: Optional[str] = None):
        if lo_ra_wan is not None:
            pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if update_data_role is not None:
            pulumi.set(__self__, "update_data_role", update_data_role)
        if update_data_source is not None:
            pulumi.set(__self__, "update_data_source", update_data_source)

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> Optional['outputs.TaskDefinitionLoRaWANUpdateGatewayTaskCreate']:
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter(name="updateDataRole")
    def update_data_role(self) -> Optional[str]:
        return pulumi.get(self, "update_data_role")

    @property
    @pulumi.getter(name="updateDataSource")
    def update_data_source(self) -> Optional[str]:
        return pulumi.get(self, "update_data_source")


@pulumi.output_type
class WirelessDeviceAbpV10x(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "devAddr":
            suggest = "dev_addr"
        elif key == "sessionKeys":
            suggest = "session_keys"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceAbpV10x. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceAbpV10x.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceAbpV10x.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dev_addr: str,
                 session_keys: 'outputs.WirelessDeviceSessionKeysAbpV10x'):
        pulumi.set(__self__, "dev_addr", dev_addr)
        pulumi.set(__self__, "session_keys", session_keys)

    @property
    @pulumi.getter(name="devAddr")
    def dev_addr(self) -> str:
        return pulumi.get(self, "dev_addr")

    @property
    @pulumi.getter(name="sessionKeys")
    def session_keys(self) -> 'outputs.WirelessDeviceSessionKeysAbpV10x':
        return pulumi.get(self, "session_keys")


@pulumi.output_type
class WirelessDeviceAbpV11(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "devAddr":
            suggest = "dev_addr"
        elif key == "sessionKeys":
            suggest = "session_keys"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceAbpV11. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceAbpV11.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceAbpV11.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dev_addr: str,
                 session_keys: 'outputs.WirelessDeviceSessionKeysAbpV11'):
        pulumi.set(__self__, "dev_addr", dev_addr)
        pulumi.set(__self__, "session_keys", session_keys)

    @property
    @pulumi.getter(name="devAddr")
    def dev_addr(self) -> str:
        return pulumi.get(self, "dev_addr")

    @property
    @pulumi.getter(name="sessionKeys")
    def session_keys(self) -> 'outputs.WirelessDeviceSessionKeysAbpV11':
        return pulumi.get(self, "session_keys")


@pulumi.output_type
class WirelessDeviceLoRaWANDevice(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "abpV10x":
            suggest = "abp_v10x"
        elif key == "abpV11":
            suggest = "abp_v11"
        elif key == "devEui":
            suggest = "dev_eui"
        elif key == "deviceProfileId":
            suggest = "device_profile_id"
        elif key == "otaaV10x":
            suggest = "otaa_v10x"
        elif key == "otaaV11":
            suggest = "otaa_v11"
        elif key == "serviceProfileId":
            suggest = "service_profile_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceLoRaWANDevice. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceLoRaWANDevice.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceLoRaWANDevice.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 abp_v10x: Optional['outputs.WirelessDeviceAbpV10x'] = None,
                 abp_v11: Optional['outputs.WirelessDeviceAbpV11'] = None,
                 dev_eui: Optional[str] = None,
                 device_profile_id: Optional[str] = None,
                 otaa_v10x: Optional['outputs.WirelessDeviceOtaaV10x'] = None,
                 otaa_v11: Optional['outputs.WirelessDeviceOtaaV11'] = None,
                 service_profile_id: Optional[str] = None):
        if abp_v10x is not None:
            pulumi.set(__self__, "abp_v10x", abp_v10x)
        if abp_v11 is not None:
            pulumi.set(__self__, "abp_v11", abp_v11)
        if dev_eui is not None:
            pulumi.set(__self__, "dev_eui", dev_eui)
        if device_profile_id is not None:
            pulumi.set(__self__, "device_profile_id", device_profile_id)
        if otaa_v10x is not None:
            pulumi.set(__self__, "otaa_v10x", otaa_v10x)
        if otaa_v11 is not None:
            pulumi.set(__self__, "otaa_v11", otaa_v11)
        if service_profile_id is not None:
            pulumi.set(__self__, "service_profile_id", service_profile_id)

    @property
    @pulumi.getter(name="abpV10x")
    def abp_v10x(self) -> Optional['outputs.WirelessDeviceAbpV10x']:
        return pulumi.get(self, "abp_v10x")

    @property
    @pulumi.getter(name="abpV11")
    def abp_v11(self) -> Optional['outputs.WirelessDeviceAbpV11']:
        return pulumi.get(self, "abp_v11")

    @property
    @pulumi.getter(name="devEui")
    def dev_eui(self) -> Optional[str]:
        return pulumi.get(self, "dev_eui")

    @property
    @pulumi.getter(name="deviceProfileId")
    def device_profile_id(self) -> Optional[str]:
        return pulumi.get(self, "device_profile_id")

    @property
    @pulumi.getter(name="otaaV10x")
    def otaa_v10x(self) -> Optional['outputs.WirelessDeviceOtaaV10x']:
        return pulumi.get(self, "otaa_v10x")

    @property
    @pulumi.getter(name="otaaV11")
    def otaa_v11(self) -> Optional['outputs.WirelessDeviceOtaaV11']:
        return pulumi.get(self, "otaa_v11")

    @property
    @pulumi.getter(name="serviceProfileId")
    def service_profile_id(self) -> Optional[str]:
        return pulumi.get(self, "service_profile_id")


@pulumi.output_type
class WirelessDeviceOtaaV10x(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appEui":
            suggest = "app_eui"
        elif key == "appKey":
            suggest = "app_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceOtaaV10x. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceOtaaV10x.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceOtaaV10x.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_eui: str,
                 app_key: str):
        pulumi.set(__self__, "app_eui", app_eui)
        pulumi.set(__self__, "app_key", app_key)

    @property
    @pulumi.getter(name="appEui")
    def app_eui(self) -> str:
        return pulumi.get(self, "app_eui")

    @property
    @pulumi.getter(name="appKey")
    def app_key(self) -> str:
        return pulumi.get(self, "app_key")


@pulumi.output_type
class WirelessDeviceOtaaV11(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appKey":
            suggest = "app_key"
        elif key == "joinEui":
            suggest = "join_eui"
        elif key == "nwkKey":
            suggest = "nwk_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceOtaaV11. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceOtaaV11.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceOtaaV11.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_key: str,
                 join_eui: str,
                 nwk_key: str):
        pulumi.set(__self__, "app_key", app_key)
        pulumi.set(__self__, "join_eui", join_eui)
        pulumi.set(__self__, "nwk_key", nwk_key)

    @property
    @pulumi.getter(name="appKey")
    def app_key(self) -> str:
        return pulumi.get(self, "app_key")

    @property
    @pulumi.getter(name="joinEui")
    def join_eui(self) -> str:
        return pulumi.get(self, "join_eui")

    @property
    @pulumi.getter(name="nwkKey")
    def nwk_key(self) -> str:
        return pulumi.get(self, "nwk_key")


@pulumi.output_type
class WirelessDeviceSessionKeysAbpV10x(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appSKey":
            suggest = "app_s_key"
        elif key == "nwkSKey":
            suggest = "nwk_s_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceSessionKeysAbpV10x. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceSessionKeysAbpV10x.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceSessionKeysAbpV10x.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_s_key: str,
                 nwk_s_key: str):
        pulumi.set(__self__, "app_s_key", app_s_key)
        pulumi.set(__self__, "nwk_s_key", nwk_s_key)

    @property
    @pulumi.getter(name="appSKey")
    def app_s_key(self) -> str:
        return pulumi.get(self, "app_s_key")

    @property
    @pulumi.getter(name="nwkSKey")
    def nwk_s_key(self) -> str:
        return pulumi.get(self, "nwk_s_key")


@pulumi.output_type
class WirelessDeviceSessionKeysAbpV11(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appSKey":
            suggest = "app_s_key"
        elif key == "fNwkSIntKey":
            suggest = "f_nwk_s_int_key"
        elif key == "nwkSEncKey":
            suggest = "nwk_s_enc_key"
        elif key == "sNwkSIntKey":
            suggest = "s_nwk_s_int_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessDeviceSessionKeysAbpV11. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessDeviceSessionKeysAbpV11.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessDeviceSessionKeysAbpV11.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_s_key: str,
                 f_nwk_s_int_key: str,
                 nwk_s_enc_key: str,
                 s_nwk_s_int_key: str):
        pulumi.set(__self__, "app_s_key", app_s_key)
        pulumi.set(__self__, "f_nwk_s_int_key", f_nwk_s_int_key)
        pulumi.set(__self__, "nwk_s_enc_key", nwk_s_enc_key)
        pulumi.set(__self__, "s_nwk_s_int_key", s_nwk_s_int_key)

    @property
    @pulumi.getter(name="appSKey")
    def app_s_key(self) -> str:
        return pulumi.get(self, "app_s_key")

    @property
    @pulumi.getter(name="fNwkSIntKey")
    def f_nwk_s_int_key(self) -> str:
        return pulumi.get(self, "f_nwk_s_int_key")

    @property
    @pulumi.getter(name="nwkSEncKey")
    def nwk_s_enc_key(self) -> str:
        return pulumi.get(self, "nwk_s_enc_key")

    @property
    @pulumi.getter(name="sNwkSIntKey")
    def s_nwk_s_int_key(self) -> str:
        return pulumi.get(self, "s_nwk_s_int_key")


@pulumi.output_type
class WirelessDeviceTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


@pulumi.output_type
class WirelessGatewayLoRaWANGateway(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "gatewayEui":
            suggest = "gateway_eui"
        elif key == "rfRegion":
            suggest = "rf_region"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WirelessGatewayLoRaWANGateway. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WirelessGatewayLoRaWANGateway.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WirelessGatewayLoRaWANGateway.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 gateway_eui: str,
                 rf_region: str):
        pulumi.set(__self__, "gateway_eui", gateway_eui)
        pulumi.set(__self__, "rf_region", rf_region)

    @property
    @pulumi.getter(name="gatewayEui")
    def gateway_eui(self) -> str:
        return pulumi.get(self, "gateway_eui")

    @property
    @pulumi.getter(name="rfRegion")
    def rf_region(self) -> str:
        return pulumi.get(self, "rf_region")


@pulumi.output_type
class WirelessGatewayTag(dict):
    def __init__(__self__, *,
                 key: Optional[str] = None,
                 value: Optional[str] = None):
        if key is not None:
            pulumi.set(__self__, "key", key)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[str]:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        return pulumi.get(self, "value")


