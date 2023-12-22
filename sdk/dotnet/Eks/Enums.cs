// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.Eks
{
    /// <summary>
    /// The type of the access scope.
    /// </summary>
    [EnumType]
    public readonly struct AccessEntryAccessScopeType : IEquatable<AccessEntryAccessScopeType>
    {
        private readonly string _value;

        private AccessEntryAccessScopeType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AccessEntryAccessScopeType Namespace { get; } = new AccessEntryAccessScopeType("namespace");
        public static AccessEntryAccessScopeType Cluster { get; } = new AccessEntryAccessScopeType("cluster");

        public static bool operator ==(AccessEntryAccessScopeType left, AccessEntryAccessScopeType right) => left.Equals(right);
        public static bool operator !=(AccessEntryAccessScopeType left, AccessEntryAccessScopeType right) => !left.Equals(right);

        public static explicit operator string(AccessEntryAccessScopeType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AccessEntryAccessScopeType other && Equals(other);
        public bool Equals(AccessEntryAccessScopeType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Resolve parameter value conflicts
    /// </summary>
    [EnumType]
    public readonly struct AddonResolveConflicts : IEquatable<AddonResolveConflicts>
    {
        private readonly string _value;

        private AddonResolveConflicts(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AddonResolveConflicts None { get; } = new AddonResolveConflicts("NONE");
        public static AddonResolveConflicts Overwrite { get; } = new AddonResolveConflicts("OVERWRITE");
        public static AddonResolveConflicts Preserve { get; } = new AddonResolveConflicts("PRESERVE");

        public static bool operator ==(AddonResolveConflicts left, AddonResolveConflicts right) => left.Equals(right);
        public static bool operator !=(AddonResolveConflicts left, AddonResolveConflicts right) => !left.Equals(right);

        public static explicit operator string(AddonResolveConflicts value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AddonResolveConflicts other && Equals(other);
        public bool Equals(AddonResolveConflicts other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specify the authentication mode that should be used to create your cluster.
    /// </summary>
    [EnumType]
    public readonly struct ClusterAccessConfigAuthenticationMode : IEquatable<ClusterAccessConfigAuthenticationMode>
    {
        private readonly string _value;

        private ClusterAccessConfigAuthenticationMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ClusterAccessConfigAuthenticationMode ConfigMap { get; } = new ClusterAccessConfigAuthenticationMode("CONFIG_MAP");
        public static ClusterAccessConfigAuthenticationMode ApiAndConfigMap { get; } = new ClusterAccessConfigAuthenticationMode("API_AND_CONFIG_MAP");
        public static ClusterAccessConfigAuthenticationMode Api { get; } = new ClusterAccessConfigAuthenticationMode("API");

        public static bool operator ==(ClusterAccessConfigAuthenticationMode left, ClusterAccessConfigAuthenticationMode right) => left.Equals(right);
        public static bool operator !=(ClusterAccessConfigAuthenticationMode left, ClusterAccessConfigAuthenticationMode right) => !left.Equals(right);

        public static explicit operator string(ClusterAccessConfigAuthenticationMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ClusterAccessConfigAuthenticationMode other && Equals(other);
        public bool Equals(ClusterAccessConfigAuthenticationMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Ipv4 or Ipv6. You can only specify ipv6 for 1.21 and later clusters that use version 1.10.1 or later of the Amazon VPC CNI add-on
    /// </summary>
    [EnumType]
    public readonly struct ClusterKubernetesNetworkConfigIpFamily : IEquatable<ClusterKubernetesNetworkConfigIpFamily>
    {
        private readonly string _value;

        private ClusterKubernetesNetworkConfigIpFamily(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ClusterKubernetesNetworkConfigIpFamily Ipv4 { get; } = new ClusterKubernetesNetworkConfigIpFamily("ipv4");
        public static ClusterKubernetesNetworkConfigIpFamily Ipv6 { get; } = new ClusterKubernetesNetworkConfigIpFamily("ipv6");

        public static bool operator ==(ClusterKubernetesNetworkConfigIpFamily left, ClusterKubernetesNetworkConfigIpFamily right) => left.Equals(right);
        public static bool operator !=(ClusterKubernetesNetworkConfigIpFamily left, ClusterKubernetesNetworkConfigIpFamily right) => !left.Equals(right);

        public static explicit operator string(ClusterKubernetesNetworkConfigIpFamily value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ClusterKubernetesNetworkConfigIpFamily other && Equals(other);
        public bool Equals(ClusterKubernetesNetworkConfigIpFamily other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// name of the log type
    /// </summary>
    [EnumType]
    public readonly struct ClusterLoggingTypeConfigType : IEquatable<ClusterLoggingTypeConfigType>
    {
        private readonly string _value;

        private ClusterLoggingTypeConfigType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ClusterLoggingTypeConfigType Api { get; } = new ClusterLoggingTypeConfigType("api");
        public static ClusterLoggingTypeConfigType Audit { get; } = new ClusterLoggingTypeConfigType("audit");
        public static ClusterLoggingTypeConfigType Authenticator { get; } = new ClusterLoggingTypeConfigType("authenticator");
        public static ClusterLoggingTypeConfigType ControllerManager { get; } = new ClusterLoggingTypeConfigType("controllerManager");
        public static ClusterLoggingTypeConfigType Scheduler { get; } = new ClusterLoggingTypeConfigType("scheduler");

        public static bool operator ==(ClusterLoggingTypeConfigType left, ClusterLoggingTypeConfigType right) => left.Equals(right);
        public static bool operator !=(ClusterLoggingTypeConfigType left, ClusterLoggingTypeConfigType right) => !left.Equals(right);

        public static explicit operator string(ClusterLoggingTypeConfigType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ClusterLoggingTypeConfigType other && Equals(other);
        public bool Equals(ClusterLoggingTypeConfigType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of the identity provider configuration.
    /// </summary>
    [EnumType]
    public readonly struct IdentityProviderConfigType : IEquatable<IdentityProviderConfigType>
    {
        private readonly string _value;

        private IdentityProviderConfigType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static IdentityProviderConfigType Oidc { get; } = new IdentityProviderConfigType("oidc");

        public static bool operator ==(IdentityProviderConfigType left, IdentityProviderConfigType right) => left.Equals(right);
        public static bool operator !=(IdentityProviderConfigType left, IdentityProviderConfigType right) => !left.Equals(right);

        public static explicit operator string(IdentityProviderConfigType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is IdentityProviderConfigType other && Equals(other);
        public bool Equals(IdentityProviderConfigType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
