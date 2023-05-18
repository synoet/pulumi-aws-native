// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.MemoryDB
{
    [EnumType]
    public readonly struct ClusterDataTieringStatus : IEquatable<ClusterDataTieringStatus>
    {
        private readonly string _value;

        private ClusterDataTieringStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ClusterDataTieringStatus True { get; } = new ClusterDataTieringStatus("true");
        public static ClusterDataTieringStatus False { get; } = new ClusterDataTieringStatus("false");

        public static bool operator ==(ClusterDataTieringStatus left, ClusterDataTieringStatus right) => left.Equals(right);
        public static bool operator !=(ClusterDataTieringStatus left, ClusterDataTieringStatus right) => !left.Equals(right);

        public static explicit operator string(ClusterDataTieringStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ClusterDataTieringStatus other && Equals(other);
        public bool Equals(ClusterDataTieringStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Type of authentication strategy for this user.
    /// </summary>
    [EnumType]
    public readonly struct UserAuthenticationModePropertiesType : IEquatable<UserAuthenticationModePropertiesType>
    {
        private readonly string _value;

        private UserAuthenticationModePropertiesType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static UserAuthenticationModePropertiesType Password { get; } = new UserAuthenticationModePropertiesType("password");
        public static UserAuthenticationModePropertiesType Iam { get; } = new UserAuthenticationModePropertiesType("iam");

        public static bool operator ==(UserAuthenticationModePropertiesType left, UserAuthenticationModePropertiesType right) => left.Equals(right);
        public static bool operator !=(UserAuthenticationModePropertiesType left, UserAuthenticationModePropertiesType right) => !left.Equals(right);

        public static explicit operator string(UserAuthenticationModePropertiesType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is UserAuthenticationModePropertiesType other && Equals(other);
        public bool Equals(UserAuthenticationModePropertiesType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
