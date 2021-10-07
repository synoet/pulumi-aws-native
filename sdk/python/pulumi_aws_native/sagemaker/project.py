# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['ProjectArgs', 'Project']

@pulumi.input_type
class ProjectArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 service_catalog_provisioning_details: Any,
                 project_description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]] = None):
        """
        The set of arguments for constructing a Project resource.
        :param Any service_catalog_provisioning_details: Input ServiceCatalog Provisioning Details
        :param pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "service_catalog_provisioning_details", service_catalog_provisioning_details)
        if project_description is not None:
            pulumi.set(__self__, "project_description", project_description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> Any:
        """
        Input ServiceCatalog Provisioning Details
        """
        return pulumi.get(self, "service_catalog_provisioning_details")

    @service_catalog_provisioning_details.setter
    def service_catalog_provisioning_details(self, value: Any):
        pulumi.set(self, "service_catalog_provisioning_details", value)

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project_description")

    @project_description.setter
    def project_description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ProjectTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Project(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_description: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_catalog_provisioning_details: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SageMaker::Project

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param Any service_catalog_provisioning_details: Input ServiceCatalog Provisioning Details
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SageMaker::Project

        :param str resource_name: The name of the resource.
        :param ProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 project_description: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 service_catalog_provisioning_details: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ProjectTagArgs']]]]] = None,
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
            __props__ = ProjectArgs.__new__(ProjectArgs)

            __props__.__dict__["project_description"] = project_description
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if service_catalog_provisioning_details is None and not opts.urn:
                raise TypeError("Missing required property 'service_catalog_provisioning_details'")
            __props__.__dict__["service_catalog_provisioning_details"] = service_catalog_provisioning_details
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["project_arn"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["project_status"] = None
            __props__.__dict__["service_catalog_provisioned_product_details"] = None
        super(Project, __self__).__init__(
            'aws-native:sagemaker:Project',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Project':
        """
        Get an existing Project resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectArgs.__new__(ProjectArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["project_arn"] = None
        __props__.__dict__["project_description"] = None
        __props__.__dict__["project_id"] = None
        __props__.__dict__["project_name"] = None
        __props__.__dict__["project_status"] = None
        __props__.__dict__["service_catalog_provisioned_product_details"] = None
        __props__.__dict__["service_catalog_provisioning_details"] = None
        __props__.__dict__["tags"] = None
        return Project(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The time at which the project was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="projectArn")
    def project_arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_arn")

    @property
    @pulumi.getter(name="projectDescription")
    def project_description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "project_description")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project_name")

    @property
    @pulumi.getter(name="projectStatus")
    def project_status(self) -> pulumi.Output['ProjectStatus']:
        """
        The status of a project.
        """
        return pulumi.get(self, "project_status")

    @property
    @pulumi.getter(name="serviceCatalogProvisionedProductDetails")
    def service_catalog_provisioned_product_details(self) -> pulumi.Output[Any]:
        """
        Provisioned ServiceCatalog  Details
        """
        return pulumi.get(self, "service_catalog_provisioned_product_details")

    @property
    @pulumi.getter(name="serviceCatalogProvisioningDetails")
    def service_catalog_provisioning_details(self) -> pulumi.Output[Any]:
        """
        Input ServiceCatalog Provisioning Details
        """
        return pulumi.get(self, "service_catalog_provisioning_details")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ProjectTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

