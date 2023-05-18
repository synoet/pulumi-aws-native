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

__all__ = ['VerifiedAccessEndpointArgs', 'VerifiedAccessEndpoint']

@pulumi.input_type
class VerifiedAccessEndpointArgs:
    def __init__(__self__, *,
                 application_domain: pulumi.Input[str],
                 attachment_type: pulumi.Input[str],
                 domain_certificate_arn: pulumi.Input[str],
                 endpoint_domain_prefix: pulumi.Input[str],
                 endpoint_type: pulumi.Input[str],
                 verified_access_group_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 load_balancer_options: Optional[pulumi.Input['VerifiedAccessEndpointLoadBalancerOptionsArgs']] = None,
                 network_interface_options: Optional[pulumi.Input['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessEndpointTagArgs']]]] = None):
        """
        The set of arguments for constructing a VerifiedAccessEndpoint resource.
        :param pulumi.Input[str] application_domain: The DNS name for users to reach your application.
        :param pulumi.Input[str] attachment_type: The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
        :param pulumi.Input[str] domain_certificate_arn: The ARN of a public TLS/SSL certificate imported into or created with ACM.
        :param pulumi.Input[str] endpoint_domain_prefix: A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
        :param pulumi.Input[str] endpoint_type: The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
        :param pulumi.Input[str] verified_access_group_id: The ID of the AWS Verified Access group.
        :param pulumi.Input[str] description: A description for the AWS Verified Access endpoint.
        :param pulumi.Input['VerifiedAccessEndpointLoadBalancerOptionsArgs'] load_balancer_options: The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
        :param pulumi.Input['VerifiedAccessEndpointNetworkInterfaceOptionsArgs'] network_interface_options: The options for network-interface type endpoint.
        :param pulumi.Input[str] policy_document: The AWS Verified Access policy document.
        :param pulumi.Input[bool] policy_enabled: The status of the Verified Access policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The IDs of the security groups for the endpoint.
        :param pulumi.Input[Sequence[pulumi.Input['VerifiedAccessEndpointTagArgs']]] tags: An array of key-value pairs to apply to this resource.
        """
        pulumi.set(__self__, "application_domain", application_domain)
        pulumi.set(__self__, "attachment_type", attachment_type)
        pulumi.set(__self__, "domain_certificate_arn", domain_certificate_arn)
        pulumi.set(__self__, "endpoint_domain_prefix", endpoint_domain_prefix)
        pulumi.set(__self__, "endpoint_type", endpoint_type)
        pulumi.set(__self__, "verified_access_group_id", verified_access_group_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if load_balancer_options is not None:
            pulumi.set(__self__, "load_balancer_options", load_balancer_options)
        if network_interface_options is not None:
            pulumi.set(__self__, "network_interface_options", network_interface_options)
        if policy_document is not None:
            pulumi.set(__self__, "policy_document", policy_document)
        if policy_enabled is not None:
            pulumi.set(__self__, "policy_enabled", policy_enabled)
        if security_group_ids is not None:
            pulumi.set(__self__, "security_group_ids", security_group_ids)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="applicationDomain")
    def application_domain(self) -> pulumi.Input[str]:
        """
        The DNS name for users to reach your application.
        """
        return pulumi.get(self, "application_domain")

    @application_domain.setter
    def application_domain(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_domain", value)

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Input[str]:
        """
        The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
        """
        return pulumi.get(self, "attachment_type")

    @attachment_type.setter
    def attachment_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "attachment_type", value)

    @property
    @pulumi.getter(name="domainCertificateArn")
    def domain_certificate_arn(self) -> pulumi.Input[str]:
        """
        The ARN of a public TLS/SSL certificate imported into or created with ACM.
        """
        return pulumi.get(self, "domain_certificate_arn")

    @domain_certificate_arn.setter
    def domain_certificate_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_certificate_arn", value)

    @property
    @pulumi.getter(name="endpointDomainPrefix")
    def endpoint_domain_prefix(self) -> pulumi.Input[str]:
        """
        A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
        """
        return pulumi.get(self, "endpoint_domain_prefix")

    @endpoint_domain_prefix.setter
    def endpoint_domain_prefix(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_domain_prefix", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> pulumi.Input[str]:
        """
        The ID of the AWS Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_id")

    @verified_access_group_id.setter
    def verified_access_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "verified_access_group_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the AWS Verified Access endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="loadBalancerOptions")
    def load_balancer_options(self) -> Optional[pulumi.Input['VerifiedAccessEndpointLoadBalancerOptionsArgs']]:
        """
        The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
        """
        return pulumi.get(self, "load_balancer_options")

    @load_balancer_options.setter
    def load_balancer_options(self, value: Optional[pulumi.Input['VerifiedAccessEndpointLoadBalancerOptionsArgs']]):
        pulumi.set(self, "load_balancer_options", value)

    @property
    @pulumi.getter(name="networkInterfaceOptions")
    def network_interface_options(self) -> Optional[pulumi.Input['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']]:
        """
        The options for network-interface type endpoint.
        """
        return pulumi.get(self, "network_interface_options")

    @network_interface_options.setter
    def network_interface_options(self, value: Optional[pulumi.Input['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']]):
        pulumi.set(self, "network_interface_options", value)

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Verified Access policy document.
        """
        return pulumi.get(self, "policy_document")

    @policy_document.setter
    def policy_document(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_document", value)

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        The status of the Verified Access policy.
        """
        return pulumi.get(self, "policy_enabled")

    @policy_enabled.setter
    def policy_enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "policy_enabled", value)

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The IDs of the security groups for the endpoint.
        """
        return pulumi.get(self, "security_group_ids")

    @security_group_ids.setter
    def security_group_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "security_group_ids", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessEndpointTagArgs']]]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['VerifiedAccessEndpointTagArgs']]]]):
        pulumi.set(self, "tags", value)


class VerifiedAccessEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_domain: Optional[pulumi.Input[str]] = None,
                 attachment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_certificate_arn: Optional[pulumi.Input[str]] = None,
                 endpoint_domain_prefix: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointLoadBalancerOptionsArgs']]] = None,
                 network_interface_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointTagArgs']]]]] = None,
                 verified_access_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_domain: The DNS name for users to reach your application.
        :param pulumi.Input[str] attachment_type: The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
        :param pulumi.Input[str] description: A description for the AWS Verified Access endpoint.
        :param pulumi.Input[str] domain_certificate_arn: The ARN of a public TLS/SSL certificate imported into or created with ACM.
        :param pulumi.Input[str] endpoint_domain_prefix: A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
        :param pulumi.Input[str] endpoint_type: The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
        :param pulumi.Input[pulumi.InputType['VerifiedAccessEndpointLoadBalancerOptionsArgs']] load_balancer_options: The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
        :param pulumi.Input[pulumi.InputType['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']] network_interface_options: The options for network-interface type endpoint.
        :param pulumi.Input[str] policy_document: The AWS Verified Access policy document.
        :param pulumi.Input[bool] policy_enabled: The status of the Verified Access policy.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_group_ids: The IDs of the security groups for the endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointTagArgs']]]] tags: An array of key-value pairs to apply to this resource.
        :param pulumi.Input[str] verified_access_group_id: The ID of the AWS Verified Access group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VerifiedAccessEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::EC2::VerifiedAccessEndpoint resource creates an AWS EC2 Verified Access Endpoint.

        :param str resource_name: The name of the resource.
        :param VerifiedAccessEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VerifiedAccessEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_domain: Optional[pulumi.Input[str]] = None,
                 attachment_type: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_certificate_arn: Optional[pulumi.Input[str]] = None,
                 endpoint_domain_prefix: Optional[pulumi.Input[str]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 load_balancer_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointLoadBalancerOptionsArgs']]] = None,
                 network_interface_options: Optional[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointNetworkInterfaceOptionsArgs']]] = None,
                 policy_document: Optional[pulumi.Input[str]] = None,
                 policy_enabled: Optional[pulumi.Input[bool]] = None,
                 security_group_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['VerifiedAccessEndpointTagArgs']]]]] = None,
                 verified_access_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VerifiedAccessEndpointArgs.__new__(VerifiedAccessEndpointArgs)

            if application_domain is None and not opts.urn:
                raise TypeError("Missing required property 'application_domain'")
            __props__.__dict__["application_domain"] = application_domain
            if attachment_type is None and not opts.urn:
                raise TypeError("Missing required property 'attachment_type'")
            __props__.__dict__["attachment_type"] = attachment_type
            __props__.__dict__["description"] = description
            if domain_certificate_arn is None and not opts.urn:
                raise TypeError("Missing required property 'domain_certificate_arn'")
            __props__.__dict__["domain_certificate_arn"] = domain_certificate_arn
            if endpoint_domain_prefix is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_domain_prefix'")
            __props__.__dict__["endpoint_domain_prefix"] = endpoint_domain_prefix
            if endpoint_type is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint_type'")
            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["load_balancer_options"] = load_balancer_options
            __props__.__dict__["network_interface_options"] = network_interface_options
            __props__.__dict__["policy_document"] = policy_document
            __props__.__dict__["policy_enabled"] = policy_enabled
            __props__.__dict__["security_group_ids"] = security_group_ids
            __props__.__dict__["tags"] = tags
            if verified_access_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'verified_access_group_id'")
            __props__.__dict__["verified_access_group_id"] = verified_access_group_id
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["device_validation_domain"] = None
            __props__.__dict__["endpoint_domain"] = None
            __props__.__dict__["last_updated_time"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["verified_access_endpoint_id"] = None
            __props__.__dict__["verified_access_instance_id"] = None
        super(VerifiedAccessEndpoint, __self__).__init__(
            'aws-native:ec2:VerifiedAccessEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VerifiedAccessEndpoint':
        """
        Get an existing VerifiedAccessEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VerifiedAccessEndpointArgs.__new__(VerifiedAccessEndpointArgs)

        __props__.__dict__["application_domain"] = None
        __props__.__dict__["attachment_type"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["device_validation_domain"] = None
        __props__.__dict__["domain_certificate_arn"] = None
        __props__.__dict__["endpoint_domain"] = None
        __props__.__dict__["endpoint_domain_prefix"] = None
        __props__.__dict__["endpoint_type"] = None
        __props__.__dict__["last_updated_time"] = None
        __props__.__dict__["load_balancer_options"] = None
        __props__.__dict__["network_interface_options"] = None
        __props__.__dict__["policy_document"] = None
        __props__.__dict__["policy_enabled"] = None
        __props__.__dict__["security_group_ids"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["verified_access_endpoint_id"] = None
        __props__.__dict__["verified_access_group_id"] = None
        __props__.__dict__["verified_access_instance_id"] = None
        return VerifiedAccessEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationDomain")
    def application_domain(self) -> pulumi.Output[str]:
        """
        The DNS name for users to reach your application.
        """
        return pulumi.get(self, "application_domain")

    @property
    @pulumi.getter(name="attachmentType")
    def attachment_type(self) -> pulumi.Output[str]:
        """
        The type of attachment used to provide connectivity between the AWS Verified Access endpoint and the application.
        """
        return pulumi.get(self, "attachment_type")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[str]:
        """
        The creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the AWS Verified Access endpoint.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="deviceValidationDomain")
    def device_validation_domain(self) -> pulumi.Output[str]:
        """
        Returned if endpoint has a device trust provider attached.
        """
        return pulumi.get(self, "device_validation_domain")

    @property
    @pulumi.getter(name="domainCertificateArn")
    def domain_certificate_arn(self) -> pulumi.Output[str]:
        """
        The ARN of a public TLS/SSL certificate imported into or created with ACM.
        """
        return pulumi.get(self, "domain_certificate_arn")

    @property
    @pulumi.getter(name="endpointDomain")
    def endpoint_domain(self) -> pulumi.Output[str]:
        """
        A DNS name that is generated for the endpoint.
        """
        return pulumi.get(self, "endpoint_domain")

    @property
    @pulumi.getter(name="endpointDomainPrefix")
    def endpoint_domain_prefix(self) -> pulumi.Output[str]:
        """
        A custom identifier that gets prepended to a DNS name that is generated for the endpoint.
        """
        return pulumi.get(self, "endpoint_domain_prefix")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[str]:
        """
        The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.The type of AWS Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.
        """
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> pulumi.Output[str]:
        """
        The last updated time.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter(name="loadBalancerOptions")
    def load_balancer_options(self) -> pulumi.Output[Optional['outputs.VerifiedAccessEndpointLoadBalancerOptions']]:
        """
        The load balancer details if creating the AWS Verified Access endpoint as load-balancer type.
        """
        return pulumi.get(self, "load_balancer_options")

    @property
    @pulumi.getter(name="networkInterfaceOptions")
    def network_interface_options(self) -> pulumi.Output[Optional['outputs.VerifiedAccessEndpointNetworkInterfaceOptions']]:
        """
        The options for network-interface type endpoint.
        """
        return pulumi.get(self, "network_interface_options")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> pulumi.Output[Optional[str]]:
        """
        The AWS Verified Access policy document.
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter(name="policyEnabled")
    def policy_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        The status of the Verified Access policy.
        """
        return pulumi.get(self, "policy_enabled")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The IDs of the security groups for the endpoint.
        """
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The endpoint status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.VerifiedAccessEndpointTag']]]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="verifiedAccessEndpointId")
    def verified_access_endpoint_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access endpoint.
        """
        return pulumi.get(self, "verified_access_endpoint_id")

    @property
    @pulumi.getter(name="verifiedAccessGroupId")
    def verified_access_group_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access group.
        """
        return pulumi.get(self, "verified_access_group_id")

    @property
    @pulumi.getter(name="verifiedAccessInstanceId")
    def verified_access_instance_id(self) -> pulumi.Output[str]:
        """
        The ID of the AWS Verified Access instance.
        """
        return pulumi.get(self, "verified_access_instance_id")

