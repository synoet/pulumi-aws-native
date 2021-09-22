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

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 certificate: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 endpoint_details: Optional[pulumi.Input['ServerEndpointDetailsArgs']] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 identity_provider_details: Optional[pulumi.Input['ServerIdentityProviderDetailsArgs']] = None,
                 identity_provider_type: Optional[pulumi.Input[str]] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 protocol_details: Optional[pulumi.Input['ServerProtocolDetailsArgs']] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input['ServerProtocolArgs']]]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]] = None,
                 workflow_details: Optional[pulumi.Input['ServerWorkflowDetailsArgs']] = None):
        """
        The set of arguments for constructing a Server resource.
        """
        if certificate is not None:
            pulumi.set(__self__, "certificate", certificate)
        if domain is not None:
            pulumi.set(__self__, "domain", domain)
        if endpoint_details is not None:
            pulumi.set(__self__, "endpoint_details", endpoint_details)
        if endpoint_type is not None:
            pulumi.set(__self__, "endpoint_type", endpoint_type)
        if identity_provider_details is not None:
            pulumi.set(__self__, "identity_provider_details", identity_provider_details)
        if identity_provider_type is not None:
            pulumi.set(__self__, "identity_provider_type", identity_provider_type)
        if logging_role is not None:
            pulumi.set(__self__, "logging_role", logging_role)
        if protocol_details is not None:
            pulumi.set(__self__, "protocol_details", protocol_details)
        if protocols is not None:
            pulumi.set(__self__, "protocols", protocols)
        if security_policy_name is not None:
            pulumi.set(__self__, "security_policy_name", security_policy_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if workflow_details is not None:
            pulumi.set(__self__, "workflow_details", workflow_details)

    @property
    @pulumi.getter
    def certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter
    def domain(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "domain")

    @domain.setter
    def domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain", value)

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> Optional[pulumi.Input['ServerEndpointDetailsArgs']]:
        return pulumi.get(self, "endpoint_details")

    @endpoint_details.setter
    def endpoint_details(self, value: Optional[pulumi.Input['ServerEndpointDetailsArgs']]):
        pulumi.set(self, "endpoint_details", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> Optional[pulumi.Input['ServerIdentityProviderDetailsArgs']]:
        return pulumi.get(self, "identity_provider_details")

    @identity_provider_details.setter
    def identity_provider_details(self, value: Optional[pulumi.Input['ServerIdentityProviderDetailsArgs']]):
        pulumi.set(self, "identity_provider_details", value)

    @property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "identity_provider_type")

    @identity_provider_type.setter
    def identity_provider_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "identity_provider_type", value)

    @property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "logging_role")

    @logging_role.setter
    def logging_role(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logging_role", value)

    @property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> Optional[pulumi.Input['ServerProtocolDetailsArgs']]:
        return pulumi.get(self, "protocol_details")

    @protocol_details.setter
    def protocol_details(self, value: Optional[pulumi.Input['ServerProtocolDetailsArgs']]):
        pulumi.set(self, "protocol_details", value)

    @property
    @pulumi.getter
    def protocols(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerProtocolArgs']]]]:
        return pulumi.get(self, "protocols")

    @protocols.setter
    def protocols(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerProtocolArgs']]]]):
        pulumi.set(self, "protocols", value)

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "security_policy_name")

    @security_policy_name.setter
    def security_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_policy_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerTagArgs']]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(self) -> Optional[pulumi.Input['ServerWorkflowDetailsArgs']]:
        return pulumi.get(self, "workflow_details")

    @workflow_details.setter
    def workflow_details(self, value: Optional[pulumi.Input['ServerWorkflowDetailsArgs']]):
        pulumi.set(self, "workflow_details", value)


warnings.warn("""Server is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Server(pulumi.CustomResource):
    warnings.warn("""Server is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 endpoint_details: Optional[pulumi.Input[pulumi.InputType['ServerEndpointDetailsArgs']]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 identity_provider_details: Optional[pulumi.Input[pulumi.InputType['ServerIdentityProviderDetailsArgs']]] = None,
                 identity_provider_type: Optional[pulumi.Input[str]] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 protocol_details: Optional[pulumi.Input[pulumi.InputType['ServerProtocolDetailsArgs']]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerProtocolArgs']]]]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerTagArgs']]]]] = None,
                 workflow_details: Optional[pulumi.Input[pulumi.InputType['ServerWorkflowDetailsArgs']]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Transfer::Server

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ServerArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Transfer::Server

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 domain: Optional[pulumi.Input[str]] = None,
                 endpoint_details: Optional[pulumi.Input[pulumi.InputType['ServerEndpointDetailsArgs']]] = None,
                 endpoint_type: Optional[pulumi.Input[str]] = None,
                 identity_provider_details: Optional[pulumi.Input[pulumi.InputType['ServerIdentityProviderDetailsArgs']]] = None,
                 identity_provider_type: Optional[pulumi.Input[str]] = None,
                 logging_role: Optional[pulumi.Input[str]] = None,
                 protocol_details: Optional[pulumi.Input[pulumi.InputType['ServerProtocolDetailsArgs']]] = None,
                 protocols: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerProtocolArgs']]]]] = None,
                 security_policy_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerTagArgs']]]]] = None,
                 workflow_details: Optional[pulumi.Input[pulumi.InputType['ServerWorkflowDetailsArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Server is deprecated: Server is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["certificate"] = certificate
            __props__.__dict__["domain"] = domain
            __props__.__dict__["endpoint_details"] = endpoint_details
            __props__.__dict__["endpoint_type"] = endpoint_type
            __props__.__dict__["identity_provider_details"] = identity_provider_details
            __props__.__dict__["identity_provider_type"] = identity_provider_type
            __props__.__dict__["logging_role"] = logging_role
            __props__.__dict__["protocol_details"] = protocol_details
            __props__.__dict__["protocols"] = protocols
            __props__.__dict__["security_policy_name"] = security_policy_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["workflow_details"] = workflow_details
            __props__.__dict__["arn"] = None
            __props__.__dict__["server_id"] = None
        super(Server, __self__).__init__(
            'aws-native:transfer:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerArgs.__new__(ServerArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["certificate"] = None
        __props__.__dict__["domain"] = None
        __props__.__dict__["endpoint_details"] = None
        __props__.__dict__["endpoint_type"] = None
        __props__.__dict__["identity_provider_details"] = None
        __props__.__dict__["identity_provider_type"] = None
        __props__.__dict__["logging_role"] = None
        __props__.__dict__["protocol_details"] = None
        __props__.__dict__["protocols"] = None
        __props__.__dict__["security_policy_name"] = None
        __props__.__dict__["server_id"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["workflow_details"] = None
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def domain(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "domain")

    @property
    @pulumi.getter(name="endpointDetails")
    def endpoint_details(self) -> pulumi.Output[Optional['outputs.ServerEndpointDetails']]:
        return pulumi.get(self, "endpoint_details")

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "endpoint_type")

    @property
    @pulumi.getter(name="identityProviderDetails")
    def identity_provider_details(self) -> pulumi.Output[Optional['outputs.ServerIdentityProviderDetails']]:
        return pulumi.get(self, "identity_provider_details")

    @property
    @pulumi.getter(name="identityProviderType")
    def identity_provider_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "identity_provider_type")

    @property
    @pulumi.getter(name="loggingRole")
    def logging_role(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "logging_role")

    @property
    @pulumi.getter(name="protocolDetails")
    def protocol_details(self) -> pulumi.Output[Optional['outputs.ServerProtocolDetails']]:
        return pulumi.get(self, "protocol_details")

    @property
    @pulumi.getter
    def protocols(self) -> pulumi.Output[Optional[Sequence['outputs.ServerProtocol']]]:
        return pulumi.get(self, "protocols")

    @property
    @pulumi.getter(name="securityPolicyName")
    def security_policy_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "security_policy_name")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ServerTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="workflowDetails")
    def workflow_details(self) -> pulumi.Output[Optional['outputs.ServerWorkflowDetails']]:
        return pulumi.get(self, "workflow_details")

