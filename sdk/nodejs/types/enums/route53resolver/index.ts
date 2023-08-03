// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const FirewallDomainListStatus = {
    Complete: "COMPLETE",
    Deleting: "DELETING",
    Updating: "UPDATING",
    CompleteImportFailed: "COMPLETE_IMPORT_FAILED",
    Importing: "IMPORTING",
    InactiveOwnerAccountClosed: "INACTIVE_OWNER_ACCOUNT_CLOSED",
} as const;

/**
 * ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
 */
export type FirewallDomainListStatus = (typeof FirewallDomainListStatus)[keyof typeof FirewallDomainListStatus];

export const FirewallRuleGroupAssociationMutationProtection = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

/**
 * MutationProtectionStatus
 */
export type FirewallRuleGroupAssociationMutationProtection = (typeof FirewallRuleGroupAssociationMutationProtection)[keyof typeof FirewallRuleGroupAssociationMutationProtection];

export const FirewallRuleGroupAssociationStatus = {
    Complete: "COMPLETE",
    Deleting: "DELETING",
    Updating: "UPDATING",
    InactiveOwnerAccountClosed: "INACTIVE_OWNER_ACCOUNT_CLOSED",
} as const;

/**
 * ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
 */
export type FirewallRuleGroupAssociationStatus = (typeof FirewallRuleGroupAssociationStatus)[keyof typeof FirewallRuleGroupAssociationStatus];

export const FirewallRuleGroupFirewallRuleAction = {
    Allow: "ALLOW",
    Block: "BLOCK",
    Alert: "ALERT",
} as const;

/**
 * Rule Action
 */
export type FirewallRuleGroupFirewallRuleAction = (typeof FirewallRuleGroupFirewallRuleAction)[keyof typeof FirewallRuleGroupFirewallRuleAction];

export const FirewallRuleGroupFirewallRuleBlockOverrideDnsType = {
    Cname: "CNAME",
} as const;

/**
 * BlockOverrideDnsType
 */
export type FirewallRuleGroupFirewallRuleBlockOverrideDnsType = (typeof FirewallRuleGroupFirewallRuleBlockOverrideDnsType)[keyof typeof FirewallRuleGroupFirewallRuleBlockOverrideDnsType];

export const FirewallRuleGroupFirewallRuleBlockResponse = {
    Nodata: "NODATA",
    Nxdomain: "NXDOMAIN",
    Override: "OVERRIDE",
} as const;

/**
 * BlockResponse
 */
export type FirewallRuleGroupFirewallRuleBlockResponse = (typeof FirewallRuleGroupFirewallRuleBlockResponse)[keyof typeof FirewallRuleGroupFirewallRuleBlockResponse];

export const FirewallRuleGroupShareStatus = {
    NotShared: "NOT_SHARED",
    SharedWithMe: "SHARED_WITH_ME",
    SharedByMe: "SHARED_BY_ME",
} as const;

/**
 * ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
 */
export type FirewallRuleGroupShareStatus = (typeof FirewallRuleGroupShareStatus)[keyof typeof FirewallRuleGroupShareStatus];

export const FirewallRuleGroupStatus = {
    Complete: "COMPLETE",
    Deleting: "DELETING",
    Updating: "UPDATING",
    InactiveOwnerAccountClosed: "INACTIVE_OWNER_ACCOUNT_CLOSED",
} as const;

/**
 * ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
 */
export type FirewallRuleGroupStatus = (typeof FirewallRuleGroupStatus)[keyof typeof FirewallRuleGroupStatus];

export const ResolverConfigAutodefinedReverse = {
    Enabling: "ENABLING",
    Enabled: "ENABLED",
    Disabling: "DISABLING",
    Disabled: "DISABLED",
} as const;

/**
 * ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
 */
export type ResolverConfigAutodefinedReverse = (typeof ResolverConfigAutodefinedReverse)[keyof typeof ResolverConfigAutodefinedReverse];

export const ResolverConfigAutodefinedReverseFlag = {
    Disable: "DISABLE",
} as const;

/**
 * Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
 */
export type ResolverConfigAutodefinedReverseFlag = (typeof ResolverConfigAutodefinedReverseFlag)[keyof typeof ResolverConfigAutodefinedReverseFlag];

export const ResolverDnssecConfigValidationStatus = {
    Enabling: "ENABLING",
    Enabled: "ENABLED",
    Disabling: "DISABLING",
    Disabled: "DISABLED",
} as const;

/**
 * ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
 */
export type ResolverDnssecConfigValidationStatus = (typeof ResolverDnssecConfigValidationStatus)[keyof typeof ResolverDnssecConfigValidationStatus];

export const ResolverQueryLoggingConfigAssociationError = {
    None: "NONE",
    DestinationNotFound: "DESTINATION_NOT_FOUND",
    AccessDenied: "ACCESS_DENIED",
} as const;

/**
 * ResolverQueryLogConfigAssociationError
 */
export type ResolverQueryLoggingConfigAssociationError = (typeof ResolverQueryLoggingConfigAssociationError)[keyof typeof ResolverQueryLoggingConfigAssociationError];

export const ResolverQueryLoggingConfigAssociationStatus = {
    Creating: "CREATING",
    Active: "ACTIVE",
    ActionNeeded: "ACTION_NEEDED",
    Deleting: "DELETING",
    Failed: "FAILED",
    Overridden: "OVERRIDDEN",
} as const;

/**
 * ResolverQueryLogConfigAssociationStatus
 */
export type ResolverQueryLoggingConfigAssociationStatus = (typeof ResolverQueryLoggingConfigAssociationStatus)[keyof typeof ResolverQueryLoggingConfigAssociationStatus];

export const ResolverQueryLoggingConfigShareStatus = {
    NotShared: "NOT_SHARED",
    SharedWithMe: "SHARED_WITH_ME",
    SharedByMe: "SHARED_BY_ME",
} as const;

/**
 * ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
 */
export type ResolverQueryLoggingConfigShareStatus = (typeof ResolverQueryLoggingConfigShareStatus)[keyof typeof ResolverQueryLoggingConfigShareStatus];

export const ResolverQueryLoggingConfigStatus = {
    Creating: "CREATING",
    Created: "CREATED",
    Deleting: "DELETING",
    Failed: "FAILED",
} as const;

/**
 * ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.
 */
export type ResolverQueryLoggingConfigStatus = (typeof ResolverQueryLoggingConfigStatus)[keyof typeof ResolverQueryLoggingConfigStatus];

export const ResolverRuleRuleType = {
    Forward: "FORWARD",
    System: "SYSTEM",
    Recursive: "RECURSIVE",
} as const;

/**
 * When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.
 */
export type ResolverRuleRuleType = (typeof ResolverRuleRuleType)[keyof typeof ResolverRuleRuleType];
