# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCoreNetworkResult',
    'AwaitableGetCoreNetworkResult',
    'get_core_network',
    'get_core_network_output',
]

@pulumi.output_type
class GetCoreNetworkResult:
    def __init__(__self__, core_network_arn=None, core_network_id=None, created_at=None, description=None, edges=None, owner_account=None, policy_document=None, segments=None, state=None, tags=None):
        if core_network_arn and not isinstance(core_network_arn, str):
            raise TypeError("Expected argument 'core_network_arn' to be a str")
        pulumi.set(__self__, "core_network_arn", core_network_arn)
        if core_network_id and not isinstance(core_network_id, str):
            raise TypeError("Expected argument 'core_network_id' to be a str")
        pulumi.set(__self__, "core_network_id", core_network_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if edges and not isinstance(edges, list):
            raise TypeError("Expected argument 'edges' to be a list")
        pulumi.set(__self__, "edges", edges)
        if owner_account and not isinstance(owner_account, str):
            raise TypeError("Expected argument 'owner_account' to be a str")
        pulumi.set(__self__, "owner_account", owner_account)
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)
        if segments and not isinstance(segments, list):
            raise TypeError("Expected argument 'segments' to be a list")
        pulumi.set(__self__, "segments", segments)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="coreNetworkArn")
    def core_network_arn(self) -> Optional[str]:
        """
        The ARN (Amazon resource name) of core network
        """
        return pulumi.get(self, "core_network_arn")

    @property
    @pulumi.getter(name="coreNetworkId")
    def core_network_id(self) -> Optional[str]:
        """
        The Id of core network
        """
        return pulumi.get(self, "core_network_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The creation time of core network
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of core network
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def edges(self) -> Optional[Sequence['outputs.CoreNetworkEdge']]:
        """
        The edges within a core network.
        """
        return pulumi.get(self, "edges")

    @property
    @pulumi.getter(name="ownerAccount")
    def owner_account(self) -> Optional[str]:
        """
        Owner of the core network
        """
        return pulumi.get(self, "owner_account")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        """
        Live policy document for the core network, you must provide PolicyDocument in Json Format
        """
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter
    def segments(self) -> Optional[Sequence['outputs.CoreNetworkSegment']]:
        """
        The segments within a core network.
        """
        return pulumi.get(self, "segments")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of core network
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.CoreNetworkTag']]:
        """
        The tags for the global network.
        """
        return pulumi.get(self, "tags")


class AwaitableGetCoreNetworkResult(GetCoreNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCoreNetworkResult(
            core_network_arn=self.core_network_arn,
            core_network_id=self.core_network_id,
            created_at=self.created_at,
            description=self.description,
            edges=self.edges,
            owner_account=self.owner_account,
            policy_document=self.policy_document,
            segments=self.segments,
            state=self.state,
            tags=self.tags)


def get_core_network(core_network_id: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCoreNetworkResult:
    """
    AWS::NetworkManager::CoreNetwork Resource Type Definition.


    :param str core_network_id: The Id of core network
    """
    __args__ = dict()
    __args__['coreNetworkId'] = core_network_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:networkmanager:getCoreNetwork', __args__, opts=opts, typ=GetCoreNetworkResult).value

    return AwaitableGetCoreNetworkResult(
        core_network_arn=__ret__.core_network_arn,
        core_network_id=__ret__.core_network_id,
        created_at=__ret__.created_at,
        description=__ret__.description,
        edges=__ret__.edges,
        owner_account=__ret__.owner_account,
        policy_document=__ret__.policy_document,
        segments=__ret__.segments,
        state=__ret__.state,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_core_network)
def get_core_network_output(core_network_id: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCoreNetworkResult]:
    """
    AWS::NetworkManager::CoreNetwork Resource Type Definition.


    :param str core_network_id: The Id of core network
    """
    ...
