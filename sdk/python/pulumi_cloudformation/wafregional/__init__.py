# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .byte_match_set import *
from .geo_match_set import *
from .ip_set import *
from .rate_based_rule import *
from .regex_pattern_set import *
from .rule import *
from .size_constraint_set import *
from .sql_injection_match_set import *
from .web_acl import *
from .web_aclassociation import *
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
            if typ == "cloudformation:WAFRegional:ByteMatchSet":
                return ByteMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:GeoMatchSet":
                return GeoMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:IPSet":
                return IPSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:RateBasedRule":
                return RateBasedRule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:RegexPatternSet":
                return RegexPatternSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:Rule":
                return Rule(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:SizeConstraintSet":
                return SizeConstraintSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:SqlInjectionMatchSet":
                return SqlInjectionMatchSet(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:WebACL":
                return WebACL(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:WebACLAssociation":
                return WebACLAssociation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "cloudformation:WAFRegional:XssMatchSet":
                return XssMatchSet(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("cloudformation", "WAFRegional", _module_instance)

_register_module()
