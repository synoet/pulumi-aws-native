# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .destination import *
from .log_group import *
from .log_stream import *
from .metric_filter import *
from .subscription_filter import *
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
            if typ == "cloudformation:Logs:Destination":
                return Destination(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:Logs:LogGroup":
                return LogGroup(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:Logs:LogStream":
                return LogStream(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:Logs:MetricFilter":
                return MetricFilter(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:Logs:SubscriptionFilter":
                return SubscriptionFilter(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("cloudformation", "Logs", _module_instance)

_register_module()
