# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'FirewallDomainListStatus',
    'FirewallRuleGroupAssociationMutationProtection',
    'FirewallRuleGroupAssociationStatus',
    'FirewallRuleGroupFirewallRuleAction',
    'FirewallRuleGroupFirewallRuleBlockOverrideDnsType',
    'FirewallRuleGroupFirewallRuleBlockResponse',
    'FirewallRuleGroupShareStatus',
    'FirewallRuleGroupStatus',
    'OutpostResolverStatus',
    'ResolverConfigAutodefinedReverse',
    'ResolverConfigAutodefinedReverseFlag',
    'ResolverDnssecConfigValidationStatus',
    'ResolverQueryLoggingConfigAssociationError',
    'ResolverQueryLoggingConfigAssociationStatus',
    'ResolverQueryLoggingConfigShareStatus',
    'ResolverQueryLoggingConfigStatus',
    'ResolverRuleRuleType',
    'ResolverRuleTargetAddressProtocol',
]


class FirewallDomainListStatus(str, Enum):
    """
    ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    """
    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    COMPLETE_IMPORT_FAILED = "COMPLETE_IMPORT_FAILED"
    IMPORTING = "IMPORTING"
    INACTIVE_OWNER_ACCOUNT_CLOSED = "INACTIVE_OWNER_ACCOUNT_CLOSED"


class FirewallRuleGroupAssociationMutationProtection(str, Enum):
    """
    MutationProtectionStatus
    """
    ENABLED = "ENABLED"
    DISABLED = "DISABLED"


class FirewallRuleGroupAssociationStatus(str, Enum):
    """
    ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    """
    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    INACTIVE_OWNER_ACCOUNT_CLOSED = "INACTIVE_OWNER_ACCOUNT_CLOSED"


class FirewallRuleGroupFirewallRuleAction(str, Enum):
    """
    Rule Action
    """
    ALLOW = "ALLOW"
    BLOCK = "BLOCK"
    ALERT = "ALERT"


class FirewallRuleGroupFirewallRuleBlockOverrideDnsType(str, Enum):
    """
    BlockOverrideDnsType
    """
    CNAME = "CNAME"


class FirewallRuleGroupFirewallRuleBlockResponse(str, Enum):
    """
    BlockResponse
    """
    NODATA = "NODATA"
    NXDOMAIN = "NXDOMAIN"
    OVERRIDE = "OVERRIDE"


class FirewallRuleGroupShareStatus(str, Enum):
    """
    ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
    """
    NOT_SHARED = "NOT_SHARED"
    SHARED_WITH_ME = "SHARED_WITH_ME"
    SHARED_BY_ME = "SHARED_BY_ME"


class FirewallRuleGroupStatus(str, Enum):
    """
    ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    """
    COMPLETE = "COMPLETE"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    INACTIVE_OWNER_ACCOUNT_CLOSED = "INACTIVE_OWNER_ACCOUNT_CLOSED"


class OutpostResolverStatus(str, Enum):
    """
    The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.
    """
    CREATING = "CREATING"
    OPERATIONAL = "OPERATIONAL"
    DELETING = "DELETING"
    UPDATING = "UPDATING"
    ACTION_NEEDED = "ACTION_NEEDED"
    FAILED_CREATION = "FAILED_CREATION"
    FAILED_DELETION = "FAILED_DELETION"


class ResolverConfigAutodefinedReverse(str, Enum):
    """
    ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
    """
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class ResolverConfigAutodefinedReverseFlag(str, Enum):
    """
    Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
    """
    DISABLE = "DISABLE"


class ResolverDnssecConfigValidationStatus(str, Enum):
    """
    ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
    """
    ENABLING = "ENABLING"
    ENABLED = "ENABLED"
    DISABLING = "DISABLING"
    DISABLED = "DISABLED"


class ResolverQueryLoggingConfigAssociationError(str, Enum):
    """
    ResolverQueryLogConfigAssociationError
    """
    NONE = "NONE"
    DESTINATION_NOT_FOUND = "DESTINATION_NOT_FOUND"
    ACCESS_DENIED = "ACCESS_DENIED"


class ResolverQueryLoggingConfigAssociationStatus(str, Enum):
    """
    ResolverQueryLogConfigAssociationStatus
    """
    CREATING = "CREATING"
    ACTIVE = "ACTIVE"
    ACTION_NEEDED = "ACTION_NEEDED"
    DELETING = "DELETING"
    FAILED = "FAILED"
    OVERRIDDEN = "OVERRIDDEN"


class ResolverQueryLoggingConfigShareStatus(str, Enum):
    """
    ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
    """
    NOT_SHARED = "NOT_SHARED"
    SHARED_WITH_ME = "SHARED_WITH_ME"
    SHARED_BY_ME = "SHARED_BY_ME"


class ResolverQueryLoggingConfigStatus(str, Enum):
    """
    ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.
    """
    CREATING = "CREATING"
    CREATED = "CREATED"
    DELETING = "DELETING"
    FAILED = "FAILED"


class ResolverRuleRuleType(str, Enum):
    """
    When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.
    """
    FORWARD = "FORWARD"
    SYSTEM = "SYSTEM"
    RECURSIVE = "RECURSIVE"


class ResolverRuleTargetAddressProtocol(str, Enum):
    """
    The protocol that you want to use to forward DNS queries. 
    """
    DO53 = "Do53"
    DO_H = "DoH"
