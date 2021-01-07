# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .byte_match_set import *
from .ip_set import *
from .rule import *
from .size_constraint_set import *
from .sql_injection_match_set import *
from .web_acl import *
from .xss_match_set import *
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
            if typ == "cloudformation:WAF:ByteMatchSet":
                return ByteMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:IPSet":
                return IPSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:Rule":
                return Rule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:SizeConstraintSet":
                return SizeConstraintSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:SqlInjectionMatchSet":
                return SqlInjectionMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:WebACL":
                return WebACL(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAF:XssMatchSet":
                return XssMatchSet(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("cloudformation", "WAF", _module_instance)

_register_module()