# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .authorizer import *
from .certificate import *
from .policy import *
from .policy_principal_attachment import *
from .provisioning_template import *
from .thing import *
from .thing_principal_attachment import *
from .topic_rule import *
from .topic_rule_destination import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "cloudformation:IoT:Authorizer":
                return Authorizer(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:Certificate":
                return Certificate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:Policy":
                return Policy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:PolicyPrincipalAttachment":
                return PolicyPrincipalAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:ProvisioningTemplate":
                return ProvisioningTemplate(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:Thing":
                return Thing(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:ThingPrincipalAttachment":
                return ThingPrincipalAttachment(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:TopicRule":
                return TopicRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:IoT:TopicRuleDestination":
                return TopicRuleDestination(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("cloudformation", "IoT", _module_instance)

_register_module()