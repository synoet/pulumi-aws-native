// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.Route53
{
    /// <summary>
    /// A string specifying the initial status of the key signing key (KSK). You can set the value to ACTIVE or INACTIVE.
    /// </summary>
    [EnumType]
    public readonly struct KeySigningKeyStatus : IEquatable<KeySigningKeyStatus>
    {
        private readonly string _value;

        private KeySigningKeyStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static KeySigningKeyStatus Active { get; } = new KeySigningKeyStatus("ACTIVE");
        public static KeySigningKeyStatus Inactive { get; } = new KeySigningKeyStatus("INACTIVE");

        public static bool operator ==(KeySigningKeyStatus left, KeySigningKeyStatus right) => left.Equals(right);
        public static bool operator !=(KeySigningKeyStatus left, KeySigningKeyStatus right) => !left.Equals(right);

        public static explicit operator string(KeySigningKeyStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is KeySigningKeyStatus other && Equals(other);
        public bool Equals(KeySigningKeyStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
