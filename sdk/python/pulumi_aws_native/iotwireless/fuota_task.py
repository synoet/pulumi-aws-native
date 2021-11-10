# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['FuotaTaskArgs', 'FuotaTask']

@pulumi.input_type
class FuotaTaskArgs:
    def __init__(__self__, *,
                 firmware_update_image: pulumi.Input[str],
                 firmware_update_role: pulumi.Input[str],
                 lo_ra_wan: pulumi.Input['FuotaTaskLoRaWANArgs'],
                 associate_multicast_group: Optional[pulumi.Input[str]] = None,
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_multicast_group: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['FuotaTaskTagArgs']]]] = None):
        """
        The set of arguments for constructing a FuotaTask resource.
        :param pulumi.Input[str] firmware_update_image: FUOTA task firmware update image binary S3 link
        :param pulumi.Input[str] firmware_update_role: FUOTA task firmware IAM role for reading S3
        :param pulumi.Input['FuotaTaskLoRaWANArgs'] lo_ra_wan: FUOTA task LoRaWAN
        :param pulumi.Input[str] associate_multicast_group: Multicast group to associate. Only for update request.
        :param pulumi.Input[str] associate_wireless_device: Wireless device to associate. Only for update request.
        :param pulumi.Input[str] description: FUOTA task description
        :param pulumi.Input[str] disassociate_multicast_group: Multicast group to disassociate. Only for update request.
        :param pulumi.Input[str] disassociate_wireless_device: Wireless device to disassociate. Only for update request.
        :param pulumi.Input[str] name: Name of FUOTA task
        :param pulumi.Input[Sequence[pulumi.Input['FuotaTaskTagArgs']]] tags: A list of key-value pairs that contain metadata for the FUOTA task.
        """
        pulumi.set(__self__, "firmware_update_image", firmware_update_image)
        pulumi.set(__self__, "firmware_update_role", firmware_update_role)
        pulumi.set(__self__, "lo_ra_wan", lo_ra_wan)
        if associate_multicast_group is not None:
            pulumi.set(__self__, "associate_multicast_group", associate_multicast_group)
        if associate_wireless_device is not None:
            pulumi.set(__self__, "associate_wireless_device", associate_wireless_device)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if disassociate_multicast_group is not None:
            pulumi.set(__self__, "disassociate_multicast_group", disassociate_multicast_group)
        if disassociate_wireless_device is not None:
            pulumi.set(__self__, "disassociate_wireless_device", disassociate_wireless_device)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="firmwareUpdateImage")
    def firmware_update_image(self) -> pulumi.Input[str]:
        """
        FUOTA task firmware update image binary S3 link
        """
        return pulumi.get(self, "firmware_update_image")

    @firmware_update_image.setter
    def firmware_update_image(self, value: pulumi.Input[str]):
        pulumi.set(self, "firmware_update_image", value)

    @property
    @pulumi.getter(name="firmwareUpdateRole")
    def firmware_update_role(self) -> pulumi.Input[str]:
        """
        FUOTA task firmware IAM role for reading S3
        """
        return pulumi.get(self, "firmware_update_role")

    @firmware_update_role.setter
    def firmware_update_role(self, value: pulumi.Input[str]):
        pulumi.set(self, "firmware_update_role", value)

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> pulumi.Input['FuotaTaskLoRaWANArgs']:
        """
        FUOTA task LoRaWAN
        """
        return pulumi.get(self, "lo_ra_wan")

    @lo_ra_wan.setter
    def lo_ra_wan(self, value: pulumi.Input['FuotaTaskLoRaWANArgs']):
        pulumi.set(self, "lo_ra_wan", value)

    @property
    @pulumi.getter(name="associateMulticastGroup")
    def associate_multicast_group(self) -> Optional[pulumi.Input[str]]:
        """
        Multicast group to associate. Only for update request.
        """
        return pulumi.get(self, "associate_multicast_group")

    @associate_multicast_group.setter
    def associate_multicast_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associate_multicast_group", value)

    @property
    @pulumi.getter(name="associateWirelessDevice")
    def associate_wireless_device(self) -> Optional[pulumi.Input[str]]:
        """
        Wireless device to associate. Only for update request.
        """
        return pulumi.get(self, "associate_wireless_device")

    @associate_wireless_device.setter
    def associate_wireless_device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "associate_wireless_device", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        FUOTA task description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="disassociateMulticastGroup")
    def disassociate_multicast_group(self) -> Optional[pulumi.Input[str]]:
        """
        Multicast group to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_multicast_group")

    @disassociate_multicast_group.setter
    def disassociate_multicast_group(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disassociate_multicast_group", value)

    @property
    @pulumi.getter(name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> Optional[pulumi.Input[str]]:
        """
        Wireless device to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_wireless_device")

    @disassociate_wireless_device.setter
    def disassociate_wireless_device(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "disassociate_wireless_device", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of FUOTA task
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FuotaTaskTagArgs']]]]:
        """
        A list of key-value pairs that contain metadata for the FUOTA task.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FuotaTaskTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""FuotaTask is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class FuotaTask(pulumi.CustomResource):
    warnings.warn("""FuotaTask is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_multicast_group: Optional[pulumi.Input[str]] = None,
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_multicast_group: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 firmware_update_image: Optional[pulumi.Input[str]] = None,
                 firmware_update_role: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['FuotaTaskLoRaWANArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FuotaTaskTagArgs']]]]] = None,
                 __props__=None):
        """
        Create and manage FUOTA tasks.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] associate_multicast_group: Multicast group to associate. Only for update request.
        :param pulumi.Input[str] associate_wireless_device: Wireless device to associate. Only for update request.
        :param pulumi.Input[str] description: FUOTA task description
        :param pulumi.Input[str] disassociate_multicast_group: Multicast group to disassociate. Only for update request.
        :param pulumi.Input[str] disassociate_wireless_device: Wireless device to disassociate. Only for update request.
        :param pulumi.Input[str] firmware_update_image: FUOTA task firmware update image binary S3 link
        :param pulumi.Input[str] firmware_update_role: FUOTA task firmware IAM role for reading S3
        :param pulumi.Input[pulumi.InputType['FuotaTaskLoRaWANArgs']] lo_ra_wan: FUOTA task LoRaWAN
        :param pulumi.Input[str] name: Name of FUOTA task
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FuotaTaskTagArgs']]]] tags: A list of key-value pairs that contain metadata for the FUOTA task.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FuotaTaskArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create and manage FUOTA tasks.

        :param str resource_name: The name of the resource.
        :param FuotaTaskArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FuotaTaskArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associate_multicast_group: Optional[pulumi.Input[str]] = None,
                 associate_wireless_device: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 disassociate_multicast_group: Optional[pulumi.Input[str]] = None,
                 disassociate_wireless_device: Optional[pulumi.Input[str]] = None,
                 firmware_update_image: Optional[pulumi.Input[str]] = None,
                 firmware_update_role: Optional[pulumi.Input[str]] = None,
                 lo_ra_wan: Optional[pulumi.Input[pulumi.InputType['FuotaTaskLoRaWANArgs']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FuotaTaskTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""FuotaTask is deprecated: FuotaTask is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = FuotaTaskArgs.__new__(FuotaTaskArgs)

            __props__.__dict__["associate_multicast_group"] = associate_multicast_group
            __props__.__dict__["associate_wireless_device"] = associate_wireless_device
            __props__.__dict__["description"] = description
            __props__.__dict__["disassociate_multicast_group"] = disassociate_multicast_group
            __props__.__dict__["disassociate_wireless_device"] = disassociate_wireless_device
            if firmware_update_image is None and not opts.urn:
                raise TypeError("Missing required property 'firmware_update_image'")
            __props__.__dict__["firmware_update_image"] = firmware_update_image
            if firmware_update_role is None and not opts.urn:
                raise TypeError("Missing required property 'firmware_update_role'")
            __props__.__dict__["firmware_update_role"] = firmware_update_role
            if lo_ra_wan is None and not opts.urn:
                raise TypeError("Missing required property 'lo_ra_wan'")
            __props__.__dict__["lo_ra_wan"] = lo_ra_wan
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
            __props__.__dict__["fuota_task_status"] = None
        super(FuotaTask, __self__).__init__(
            'aws-native:iotwireless:FuotaTask',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'FuotaTask':
        """
        Get an existing FuotaTask resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = FuotaTaskArgs.__new__(FuotaTaskArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["associate_multicast_group"] = None
        __props__.__dict__["associate_wireless_device"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["disassociate_multicast_group"] = None
        __props__.__dict__["disassociate_wireless_device"] = None
        __props__.__dict__["firmware_update_image"] = None
        __props__.__dict__["firmware_update_role"] = None
        __props__.__dict__["fuota_task_status"] = None
        __props__.__dict__["lo_ra_wan"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return FuotaTask(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        FUOTA task arn. Returned after successful create.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associateMulticastGroup")
    def associate_multicast_group(self) -> pulumi.Output[Optional[str]]:
        """
        Multicast group to associate. Only for update request.
        """
        return pulumi.get(self, "associate_multicast_group")

    @property
    @pulumi.getter(name="associateWirelessDevice")
    def associate_wireless_device(self) -> pulumi.Output[Optional[str]]:
        """
        Wireless device to associate. Only for update request.
        """
        return pulumi.get(self, "associate_wireless_device")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        FUOTA task description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="disassociateMulticastGroup")
    def disassociate_multicast_group(self) -> pulumi.Output[Optional[str]]:
        """
        Multicast group to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_multicast_group")

    @property
    @pulumi.getter(name="disassociateWirelessDevice")
    def disassociate_wireless_device(self) -> pulumi.Output[Optional[str]]:
        """
        Wireless device to disassociate. Only for update request.
        """
        return pulumi.get(self, "disassociate_wireless_device")

    @property
    @pulumi.getter(name="firmwareUpdateImage")
    def firmware_update_image(self) -> pulumi.Output[str]:
        """
        FUOTA task firmware update image binary S3 link
        """
        return pulumi.get(self, "firmware_update_image")

    @property
    @pulumi.getter(name="firmwareUpdateRole")
    def firmware_update_role(self) -> pulumi.Output[str]:
        """
        FUOTA task firmware IAM role for reading S3
        """
        return pulumi.get(self, "firmware_update_role")

    @property
    @pulumi.getter(name="fuotaTaskStatus")
    def fuota_task_status(self) -> pulumi.Output[str]:
        """
        FUOTA task status. Returned after successful read.
        """
        return pulumi.get(self, "fuota_task_status")

    @property
    @pulumi.getter(name="loRaWAN")
    def lo_ra_wan(self) -> pulumi.Output['outputs.FuotaTaskLoRaWAN']:
        """
        FUOTA task LoRaWAN
        """
        return pulumi.get(self, "lo_ra_wan")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of FUOTA task
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.FuotaTaskTag']]]:
        """
        A list of key-value pairs that contain metadata for the FUOTA task.
        """
        return pulumi.get(self, "tags")

