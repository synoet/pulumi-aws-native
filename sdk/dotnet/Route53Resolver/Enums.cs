// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.Route53Resolver
{
    /// <summary>
    /// ResolverFirewallDomainList, possible values are COMPLETE, DELETING, UPDATING, COMPLETE_IMPORT_FAILED, IMPORTING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    /// </summary>
    [EnumType]
    public readonly struct FirewallDomainListStatus : IEquatable<FirewallDomainListStatus>
    {
        private readonly string _value;

        private FirewallDomainListStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallDomainListStatus Complete { get; } = new FirewallDomainListStatus("COMPLETE");
        public static FirewallDomainListStatus Deleting { get; } = new FirewallDomainListStatus("DELETING");
        public static FirewallDomainListStatus Updating { get; } = new FirewallDomainListStatus("UPDATING");
        public static FirewallDomainListStatus CompleteImportFailed { get; } = new FirewallDomainListStatus("COMPLETE_IMPORT_FAILED");
        public static FirewallDomainListStatus Importing { get; } = new FirewallDomainListStatus("IMPORTING");
        public static FirewallDomainListStatus InactiveOwnerAccountClosed { get; } = new FirewallDomainListStatus("INACTIVE_OWNER_ACCOUNT_CLOSED");

        public static bool operator ==(FirewallDomainListStatus left, FirewallDomainListStatus right) => left.Equals(right);
        public static bool operator !=(FirewallDomainListStatus left, FirewallDomainListStatus right) => !left.Equals(right);

        public static explicit operator string(FirewallDomainListStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallDomainListStatus other && Equals(other);
        public bool Equals(FirewallDomainListStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// MutationProtectionStatus
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupAssociationMutationProtection : IEquatable<FirewallRuleGroupAssociationMutationProtection>
    {
        private readonly string _value;

        private FirewallRuleGroupAssociationMutationProtection(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupAssociationMutationProtection Enabled { get; } = new FirewallRuleGroupAssociationMutationProtection("ENABLED");
        public static FirewallRuleGroupAssociationMutationProtection Disabled { get; } = new FirewallRuleGroupAssociationMutationProtection("DISABLED");

        public static bool operator ==(FirewallRuleGroupAssociationMutationProtection left, FirewallRuleGroupAssociationMutationProtection right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupAssociationMutationProtection left, FirewallRuleGroupAssociationMutationProtection right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupAssociationMutationProtection value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupAssociationMutationProtection other && Equals(other);
        public bool Equals(FirewallRuleGroupAssociationMutationProtection other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupAssociationStatus : IEquatable<FirewallRuleGroupAssociationStatus>
    {
        private readonly string _value;

        private FirewallRuleGroupAssociationStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupAssociationStatus Complete { get; } = new FirewallRuleGroupAssociationStatus("COMPLETE");
        public static FirewallRuleGroupAssociationStatus Deleting { get; } = new FirewallRuleGroupAssociationStatus("DELETING");
        public static FirewallRuleGroupAssociationStatus Updating { get; } = new FirewallRuleGroupAssociationStatus("UPDATING");
        public static FirewallRuleGroupAssociationStatus InactiveOwnerAccountClosed { get; } = new FirewallRuleGroupAssociationStatus("INACTIVE_OWNER_ACCOUNT_CLOSED");

        public static bool operator ==(FirewallRuleGroupAssociationStatus left, FirewallRuleGroupAssociationStatus right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupAssociationStatus left, FirewallRuleGroupAssociationStatus right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupAssociationStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupAssociationStatus other && Equals(other);
        public bool Equals(FirewallRuleGroupAssociationStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Rule Action
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupFirewallRuleAction : IEquatable<FirewallRuleGroupFirewallRuleAction>
    {
        private readonly string _value;

        private FirewallRuleGroupFirewallRuleAction(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupFirewallRuleAction Allow { get; } = new FirewallRuleGroupFirewallRuleAction("ALLOW");
        public static FirewallRuleGroupFirewallRuleAction Block { get; } = new FirewallRuleGroupFirewallRuleAction("BLOCK");
        public static FirewallRuleGroupFirewallRuleAction Alert { get; } = new FirewallRuleGroupFirewallRuleAction("ALERT");

        public static bool operator ==(FirewallRuleGroupFirewallRuleAction left, FirewallRuleGroupFirewallRuleAction right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupFirewallRuleAction left, FirewallRuleGroupFirewallRuleAction right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupFirewallRuleAction value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupFirewallRuleAction other && Equals(other);
        public bool Equals(FirewallRuleGroupFirewallRuleAction other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// BlockOverrideDnsType
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupFirewallRuleBlockOverrideDnsType : IEquatable<FirewallRuleGroupFirewallRuleBlockOverrideDnsType>
    {
        private readonly string _value;

        private FirewallRuleGroupFirewallRuleBlockOverrideDnsType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupFirewallRuleBlockOverrideDnsType Cname { get; } = new FirewallRuleGroupFirewallRuleBlockOverrideDnsType("CNAME");

        public static bool operator ==(FirewallRuleGroupFirewallRuleBlockOverrideDnsType left, FirewallRuleGroupFirewallRuleBlockOverrideDnsType right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupFirewallRuleBlockOverrideDnsType left, FirewallRuleGroupFirewallRuleBlockOverrideDnsType right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupFirewallRuleBlockOverrideDnsType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupFirewallRuleBlockOverrideDnsType other && Equals(other);
        public bool Equals(FirewallRuleGroupFirewallRuleBlockOverrideDnsType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// BlockResponse
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupFirewallRuleBlockResponse : IEquatable<FirewallRuleGroupFirewallRuleBlockResponse>
    {
        private readonly string _value;

        private FirewallRuleGroupFirewallRuleBlockResponse(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupFirewallRuleBlockResponse Nodata { get; } = new FirewallRuleGroupFirewallRuleBlockResponse("NODATA");
        public static FirewallRuleGroupFirewallRuleBlockResponse Nxdomain { get; } = new FirewallRuleGroupFirewallRuleBlockResponse("NXDOMAIN");
        public static FirewallRuleGroupFirewallRuleBlockResponse Override { get; } = new FirewallRuleGroupFirewallRuleBlockResponse("OVERRIDE");

        public static bool operator ==(FirewallRuleGroupFirewallRuleBlockResponse left, FirewallRuleGroupFirewallRuleBlockResponse right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupFirewallRuleBlockResponse left, FirewallRuleGroupFirewallRuleBlockResponse right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupFirewallRuleBlockResponse value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupFirewallRuleBlockResponse other && Equals(other);
        public bool Equals(FirewallRuleGroupFirewallRuleBlockResponse other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupShareStatus : IEquatable<FirewallRuleGroupShareStatus>
    {
        private readonly string _value;

        private FirewallRuleGroupShareStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupShareStatus NotShared { get; } = new FirewallRuleGroupShareStatus("NOT_SHARED");
        public static FirewallRuleGroupShareStatus SharedWithMe { get; } = new FirewallRuleGroupShareStatus("SHARED_WITH_ME");
        public static FirewallRuleGroupShareStatus SharedByMe { get; } = new FirewallRuleGroupShareStatus("SHARED_BY_ME");

        public static bool operator ==(FirewallRuleGroupShareStatus left, FirewallRuleGroupShareStatus right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupShareStatus left, FirewallRuleGroupShareStatus right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupShareStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupShareStatus other && Equals(other);
        public bool Equals(FirewallRuleGroupShareStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverFirewallRuleGroupAssociation, possible values are COMPLETE, DELETING, UPDATING, and INACTIVE_OWNER_ACCOUNT_CLOSED.
    /// </summary>
    [EnumType]
    public readonly struct FirewallRuleGroupStatus : IEquatable<FirewallRuleGroupStatus>
    {
        private readonly string _value;

        private FirewallRuleGroupStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallRuleGroupStatus Complete { get; } = new FirewallRuleGroupStatus("COMPLETE");
        public static FirewallRuleGroupStatus Deleting { get; } = new FirewallRuleGroupStatus("DELETING");
        public static FirewallRuleGroupStatus Updating { get; } = new FirewallRuleGroupStatus("UPDATING");
        public static FirewallRuleGroupStatus InactiveOwnerAccountClosed { get; } = new FirewallRuleGroupStatus("INACTIVE_OWNER_ACCOUNT_CLOSED");

        public static bool operator ==(FirewallRuleGroupStatus left, FirewallRuleGroupStatus right) => left.Equals(right);
        public static bool operator !=(FirewallRuleGroupStatus left, FirewallRuleGroupStatus right) => !left.Equals(right);

        public static explicit operator string(FirewallRuleGroupStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallRuleGroupStatus other && Equals(other);
        public bool Equals(FirewallRuleGroupStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The OutpostResolver status, possible values are CREATING, OPERATIONAL, UPDATING, DELETING, ACTION_NEEDED, FAILED_CREATION and FAILED_DELETION.
    /// </summary>
    [EnumType]
    public readonly struct OutpostResolverStatus : IEquatable<OutpostResolverStatus>
    {
        private readonly string _value;

        private OutpostResolverStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static OutpostResolverStatus Creating { get; } = new OutpostResolverStatus("CREATING");
        public static OutpostResolverStatus Operational { get; } = new OutpostResolverStatus("OPERATIONAL");
        public static OutpostResolverStatus Deleting { get; } = new OutpostResolverStatus("DELETING");
        public static OutpostResolverStatus Updating { get; } = new OutpostResolverStatus("UPDATING");
        public static OutpostResolverStatus ActionNeeded { get; } = new OutpostResolverStatus("ACTION_NEEDED");
        public static OutpostResolverStatus FailedCreation { get; } = new OutpostResolverStatus("FAILED_CREATION");
        public static OutpostResolverStatus FailedDeletion { get; } = new OutpostResolverStatus("FAILED_DELETION");

        public static bool operator ==(OutpostResolverStatus left, OutpostResolverStatus right) => left.Equals(right);
        public static bool operator !=(OutpostResolverStatus left, OutpostResolverStatus right) => !left.Equals(right);

        public static explicit operator string(OutpostResolverStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is OutpostResolverStatus other && Equals(other);
        public bool Equals(OutpostResolverStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverAutodefinedReverseStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
    /// </summary>
    [EnumType]
    public readonly struct ResolverConfigAutodefinedReverse : IEquatable<ResolverConfigAutodefinedReverse>
    {
        private readonly string _value;

        private ResolverConfigAutodefinedReverse(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverConfigAutodefinedReverse Enabling { get; } = new ResolverConfigAutodefinedReverse("ENABLING");
        public static ResolverConfigAutodefinedReverse Enabled { get; } = new ResolverConfigAutodefinedReverse("ENABLED");
        public static ResolverConfigAutodefinedReverse Disabling { get; } = new ResolverConfigAutodefinedReverse("DISABLING");
        public static ResolverConfigAutodefinedReverse Disabled { get; } = new ResolverConfigAutodefinedReverse("DISABLED");

        public static bool operator ==(ResolverConfigAutodefinedReverse left, ResolverConfigAutodefinedReverse right) => left.Equals(right);
        public static bool operator !=(ResolverConfigAutodefinedReverse left, ResolverConfigAutodefinedReverse right) => !left.Equals(right);

        public static explicit operator string(ResolverConfigAutodefinedReverse value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverConfigAutodefinedReverse other && Equals(other);
        public bool Equals(ResolverConfigAutodefinedReverse other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Represents the desired status of AutodefinedReverse. The only supported value on creation is DISABLE. Deletion of this resource will return AutodefinedReverse to its default value (ENABLED).
    /// </summary>
    [EnumType]
    public readonly struct ResolverConfigAutodefinedReverseFlag : IEquatable<ResolverConfigAutodefinedReverseFlag>
    {
        private readonly string _value;

        private ResolverConfigAutodefinedReverseFlag(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverConfigAutodefinedReverseFlag Disable { get; } = new ResolverConfigAutodefinedReverseFlag("DISABLE");

        public static bool operator ==(ResolverConfigAutodefinedReverseFlag left, ResolverConfigAutodefinedReverseFlag right) => left.Equals(right);
        public static bool operator !=(ResolverConfigAutodefinedReverseFlag left, ResolverConfigAutodefinedReverseFlag right) => !left.Equals(right);

        public static explicit operator string(ResolverConfigAutodefinedReverseFlag value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverConfigAutodefinedReverseFlag other && Equals(other);
        public bool Equals(ResolverConfigAutodefinedReverseFlag other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverDNSSECValidationStatus, possible values are ENABLING, ENABLED, DISABLING AND DISABLED.
    /// </summary>
    [EnumType]
    public readonly struct ResolverDnssecConfigValidationStatus : IEquatable<ResolverDnssecConfigValidationStatus>
    {
        private readonly string _value;

        private ResolverDnssecConfigValidationStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverDnssecConfigValidationStatus Enabling { get; } = new ResolverDnssecConfigValidationStatus("ENABLING");
        public static ResolverDnssecConfigValidationStatus Enabled { get; } = new ResolverDnssecConfigValidationStatus("ENABLED");
        public static ResolverDnssecConfigValidationStatus Disabling { get; } = new ResolverDnssecConfigValidationStatus("DISABLING");
        public static ResolverDnssecConfigValidationStatus Disabled { get; } = new ResolverDnssecConfigValidationStatus("DISABLED");

        public static bool operator ==(ResolverDnssecConfigValidationStatus left, ResolverDnssecConfigValidationStatus right) => left.Equals(right);
        public static bool operator !=(ResolverDnssecConfigValidationStatus left, ResolverDnssecConfigValidationStatus right) => !left.Equals(right);

        public static explicit operator string(ResolverDnssecConfigValidationStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverDnssecConfigValidationStatus other && Equals(other);
        public bool Equals(ResolverDnssecConfigValidationStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverQueryLogConfigAssociationError
    /// </summary>
    [EnumType]
    public readonly struct ResolverQueryLoggingConfigAssociationError : IEquatable<ResolverQueryLoggingConfigAssociationError>
    {
        private readonly string _value;

        private ResolverQueryLoggingConfigAssociationError(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverQueryLoggingConfigAssociationError None { get; } = new ResolverQueryLoggingConfigAssociationError("NONE");
        public static ResolverQueryLoggingConfigAssociationError DestinationNotFound { get; } = new ResolverQueryLoggingConfigAssociationError("DESTINATION_NOT_FOUND");
        public static ResolverQueryLoggingConfigAssociationError AccessDenied { get; } = new ResolverQueryLoggingConfigAssociationError("ACCESS_DENIED");

        public static bool operator ==(ResolverQueryLoggingConfigAssociationError left, ResolverQueryLoggingConfigAssociationError right) => left.Equals(right);
        public static bool operator !=(ResolverQueryLoggingConfigAssociationError left, ResolverQueryLoggingConfigAssociationError right) => !left.Equals(right);

        public static explicit operator string(ResolverQueryLoggingConfigAssociationError value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverQueryLoggingConfigAssociationError other && Equals(other);
        public bool Equals(ResolverQueryLoggingConfigAssociationError other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverQueryLogConfigAssociationStatus
    /// </summary>
    [EnumType]
    public readonly struct ResolverQueryLoggingConfigAssociationStatus : IEquatable<ResolverQueryLoggingConfigAssociationStatus>
    {
        private readonly string _value;

        private ResolverQueryLoggingConfigAssociationStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverQueryLoggingConfigAssociationStatus Creating { get; } = new ResolverQueryLoggingConfigAssociationStatus("CREATING");
        public static ResolverQueryLoggingConfigAssociationStatus Active { get; } = new ResolverQueryLoggingConfigAssociationStatus("ACTIVE");
        public static ResolverQueryLoggingConfigAssociationStatus ActionNeeded { get; } = new ResolverQueryLoggingConfigAssociationStatus("ACTION_NEEDED");
        public static ResolverQueryLoggingConfigAssociationStatus Deleting { get; } = new ResolverQueryLoggingConfigAssociationStatus("DELETING");
        public static ResolverQueryLoggingConfigAssociationStatus Failed { get; } = new ResolverQueryLoggingConfigAssociationStatus("FAILED");
        public static ResolverQueryLoggingConfigAssociationStatus Overridden { get; } = new ResolverQueryLoggingConfigAssociationStatus("OVERRIDDEN");

        public static bool operator ==(ResolverQueryLoggingConfigAssociationStatus left, ResolverQueryLoggingConfigAssociationStatus right) => left.Equals(right);
        public static bool operator !=(ResolverQueryLoggingConfigAssociationStatus left, ResolverQueryLoggingConfigAssociationStatus right) => !left.Equals(right);

        public static explicit operator string(ResolverQueryLoggingConfigAssociationStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverQueryLoggingConfigAssociationStatus other && Equals(other);
        public bool Equals(ResolverQueryLoggingConfigAssociationStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ShareStatus, possible values are NOT_SHARED, SHARED_WITH_ME, SHARED_BY_ME.
    /// </summary>
    [EnumType]
    public readonly struct ResolverQueryLoggingConfigShareStatus : IEquatable<ResolverQueryLoggingConfigShareStatus>
    {
        private readonly string _value;

        private ResolverQueryLoggingConfigShareStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverQueryLoggingConfigShareStatus NotShared { get; } = new ResolverQueryLoggingConfigShareStatus("NOT_SHARED");
        public static ResolverQueryLoggingConfigShareStatus SharedWithMe { get; } = new ResolverQueryLoggingConfigShareStatus("SHARED_WITH_ME");
        public static ResolverQueryLoggingConfigShareStatus SharedByMe { get; } = new ResolverQueryLoggingConfigShareStatus("SHARED_BY_ME");

        public static bool operator ==(ResolverQueryLoggingConfigShareStatus left, ResolverQueryLoggingConfigShareStatus right) => left.Equals(right);
        public static bool operator !=(ResolverQueryLoggingConfigShareStatus left, ResolverQueryLoggingConfigShareStatus right) => !left.Equals(right);

        public static explicit operator string(ResolverQueryLoggingConfigShareStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverQueryLoggingConfigShareStatus other && Equals(other);
        public bool Equals(ResolverQueryLoggingConfigShareStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ResolverQueryLogConfigStatus, possible values are CREATING, CREATED, DELETED AND FAILED.
    /// </summary>
    [EnumType]
    public readonly struct ResolverQueryLoggingConfigStatus : IEquatable<ResolverQueryLoggingConfigStatus>
    {
        private readonly string _value;

        private ResolverQueryLoggingConfigStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverQueryLoggingConfigStatus Creating { get; } = new ResolverQueryLoggingConfigStatus("CREATING");
        public static ResolverQueryLoggingConfigStatus Created { get; } = new ResolverQueryLoggingConfigStatus("CREATED");
        public static ResolverQueryLoggingConfigStatus Deleting { get; } = new ResolverQueryLoggingConfigStatus("DELETING");
        public static ResolverQueryLoggingConfigStatus Failed { get; } = new ResolverQueryLoggingConfigStatus("FAILED");

        public static bool operator ==(ResolverQueryLoggingConfigStatus left, ResolverQueryLoggingConfigStatus right) => left.Equals(right);
        public static bool operator !=(ResolverQueryLoggingConfigStatus left, ResolverQueryLoggingConfigStatus right) => !left.Equals(right);

        public static explicit operator string(ResolverQueryLoggingConfigStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverQueryLoggingConfigStatus other && Equals(other);
        public bool Equals(ResolverQueryLoggingConfigStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// When you want to forward DNS queries for specified domain name to resolvers on your network, specify FORWARD. When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify SYSTEM.
    /// </summary>
    [EnumType]
    public readonly struct ResolverRuleRuleType : IEquatable<ResolverRuleRuleType>
    {
        private readonly string _value;

        private ResolverRuleRuleType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverRuleRuleType Forward { get; } = new ResolverRuleRuleType("FORWARD");
        public static ResolverRuleRuleType System { get; } = new ResolverRuleRuleType("SYSTEM");
        public static ResolverRuleRuleType Recursive { get; } = new ResolverRuleRuleType("RECURSIVE");

        public static bool operator ==(ResolverRuleRuleType left, ResolverRuleRuleType right) => left.Equals(right);
        public static bool operator !=(ResolverRuleRuleType left, ResolverRuleRuleType right) => !left.Equals(right);

        public static explicit operator string(ResolverRuleRuleType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverRuleRuleType other && Equals(other);
        public bool Equals(ResolverRuleRuleType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The protocol that you want to use to forward DNS queries. 
    /// </summary>
    [EnumType]
    public readonly struct ResolverRuleTargetAddressProtocol : IEquatable<ResolverRuleTargetAddressProtocol>
    {
        private readonly string _value;

        private ResolverRuleTargetAddressProtocol(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResolverRuleTargetAddressProtocol Do53 { get; } = new ResolverRuleTargetAddressProtocol("Do53");
        public static ResolverRuleTargetAddressProtocol DoH { get; } = new ResolverRuleTargetAddressProtocol("DoH");

        public static bool operator ==(ResolverRuleTargetAddressProtocol left, ResolverRuleTargetAddressProtocol right) => left.Equals(right);
        public static bool operator !=(ResolverRuleTargetAddressProtocol left, ResolverRuleTargetAddressProtocol right) => !left.Equals(right);

        public static explicit operator string(ResolverRuleTargetAddressProtocol value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResolverRuleTargetAddressProtocol other && Equals(other);
        public bool Equals(ResolverRuleTargetAddressProtocol other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
