# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .application import *
from .application_output import *
from .application_reference_data_source import *
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
            if typ == "cloudformation:KinesisAnalytics:Application":
                return Application(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:KinesisAnalytics:ApplicationOutput":
                return ApplicationOutput(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:KinesisAnalytics:ApplicationReferenceDataSource":
                return ApplicationReferenceDataSource(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("cloudformation", "KinesisAnalytics", _module_instance)

_register_module()
