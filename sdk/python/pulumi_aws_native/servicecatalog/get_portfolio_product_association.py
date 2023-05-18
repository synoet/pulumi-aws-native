# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetPortfolioProductAssociationResult',
    'AwaitableGetPortfolioProductAssociationResult',
    'get_portfolio_product_association',
    'get_portfolio_product_association_output',
]

@pulumi.output_type
class GetPortfolioProductAssociationResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetPortfolioProductAssociationResult(GetPortfolioProductAssociationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPortfolioProductAssociationResult(
            id=self.id)


def get_portfolio_product_association(id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPortfolioProductAssociationResult:
    """
    Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:servicecatalog:getPortfolioProductAssociation', __args__, opts=opts, typ=GetPortfolioProductAssociationResult).value

    return AwaitableGetPortfolioProductAssociationResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_portfolio_product_association)
def get_portfolio_product_association_output(id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPortfolioProductAssociationResult]:
    """
    Resource Type definition for AWS::ServiceCatalog::PortfolioProductAssociation
    """
    ...
