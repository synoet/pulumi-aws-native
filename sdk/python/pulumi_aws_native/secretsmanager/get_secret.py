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
    'GetSecretResult',
    'AwaitableGetSecretResult',
    'get_secret',
    'get_secret_output',
]

@pulumi.output_type
class GetSecretResult:
    def __init__(__self__, description=None, generate_secret_string=None, id=None, kms_key_id=None, replica_regions=None, secret_string=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if generate_secret_string and not isinstance(generate_secret_string, dict):
            raise TypeError("Expected argument 'generate_secret_string' to be a dict")
        pulumi.set(__self__, "generate_secret_string", generate_secret_string)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kms_key_id and not isinstance(kms_key_id, str):
            raise TypeError("Expected argument 'kms_key_id' to be a str")
        pulumi.set(__self__, "kms_key_id", kms_key_id)
        if replica_regions and not isinstance(replica_regions, list):
            raise TypeError("Expected argument 'replica_regions' to be a list")
        pulumi.set(__self__, "replica_regions", replica_regions)
        if secret_string and not isinstance(secret_string, str):
            raise TypeError("Expected argument 'secret_string' to be a str")
        pulumi.set(__self__, "secret_string", secret_string)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="generateSecretString")
    def generate_secret_string(self) -> Optional['outputs.SecretGenerateSecretString']:
        return pulumi.get(self, "generate_secret_string")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kmsKeyId")
    def kms_key_id(self) -> Optional[str]:
        return pulumi.get(self, "kms_key_id")

    @property
    @pulumi.getter(name="replicaRegions")
    def replica_regions(self) -> Optional[Sequence['outputs.SecretReplicaRegion']]:
        return pulumi.get(self, "replica_regions")

    @property
    @pulumi.getter(name="secretString")
    def secret_string(self) -> Optional[str]:
        return pulumi.get(self, "secret_string")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SecretTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetSecretResult(GetSecretResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecretResult(
            description=self.description,
            generate_secret_string=self.generate_secret_string,
            id=self.id,
            kms_key_id=self.kms_key_id,
            replica_regions=self.replica_regions,
            secret_string=self.secret_string,
            tags=self.tags)


def get_secret(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecretResult:
    """
    Resource Type definition for AWS::SecretsManager::Secret
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:secretsmanager:getSecret', __args__, opts=opts, typ=GetSecretResult).value

    return AwaitableGetSecretResult(
        description=__ret__.description,
        generate_secret_string=__ret__.generate_secret_string,
        id=__ret__.id,
        kms_key_id=__ret__.kms_key_id,
        replica_regions=__ret__.replica_regions,
        secret_string=__ret__.secret_string,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_secret)
def get_secret_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecretResult]:
    """
    Resource Type definition for AWS::SecretsManager::Secret
    """
    ...
