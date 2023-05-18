// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.MediaConnect
{
    /// <summary>
    /// The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    /// </summary>
    [EnumType]
    public readonly struct FlowEncryptionAlgorithm : IEquatable<FlowEncryptionAlgorithm>
    {
        private readonly string _value;

        private FlowEncryptionAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowEncryptionAlgorithm Aes128 { get; } = new FlowEncryptionAlgorithm("aes128");
        public static FlowEncryptionAlgorithm Aes192 { get; } = new FlowEncryptionAlgorithm("aes192");
        public static FlowEncryptionAlgorithm Aes256 { get; } = new FlowEncryptionAlgorithm("aes256");

        public static bool operator ==(FlowEncryptionAlgorithm left, FlowEncryptionAlgorithm right) => left.Equals(right);
        public static bool operator !=(FlowEncryptionAlgorithm left, FlowEncryptionAlgorithm right) => !left.Equals(right);

        public static explicit operator string(FlowEncryptionAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowEncryptionAlgorithm other && Equals(other);
        public bool Equals(FlowEncryptionAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    /// </summary>
    [EnumType]
    public readonly struct FlowEncryptionKeyType : IEquatable<FlowEncryptionKeyType>
    {
        private readonly string _value;

        private FlowEncryptionKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowEncryptionKeyType Speke { get; } = new FlowEncryptionKeyType("speke");
        public static FlowEncryptionKeyType StaticKey { get; } = new FlowEncryptionKeyType("static-key");
        public static FlowEncryptionKeyType SrtPassword { get; } = new FlowEncryptionKeyType("srt-password");

        public static bool operator ==(FlowEncryptionKeyType left, FlowEncryptionKeyType right) => left.Equals(right);
        public static bool operator !=(FlowEncryptionKeyType left, FlowEncryptionKeyType right) => !left.Equals(right);

        public static explicit operator string(FlowEncryptionKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowEncryptionKeyType other && Equals(other);
        public bool Equals(FlowEncryptionKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    /// </summary>
    [EnumType]
    public readonly struct FlowEntitlementEncryptionAlgorithm : IEquatable<FlowEntitlementEncryptionAlgorithm>
    {
        private readonly string _value;

        private FlowEntitlementEncryptionAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowEntitlementEncryptionAlgorithm Aes128 { get; } = new FlowEntitlementEncryptionAlgorithm("aes128");
        public static FlowEntitlementEncryptionAlgorithm Aes192 { get; } = new FlowEntitlementEncryptionAlgorithm("aes192");
        public static FlowEntitlementEncryptionAlgorithm Aes256 { get; } = new FlowEntitlementEncryptionAlgorithm("aes256");

        public static bool operator ==(FlowEntitlementEncryptionAlgorithm left, FlowEntitlementEncryptionAlgorithm right) => left.Equals(right);
        public static bool operator !=(FlowEntitlementEncryptionAlgorithm left, FlowEntitlementEncryptionAlgorithm right) => !left.Equals(right);

        public static explicit operator string(FlowEntitlementEncryptionAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowEntitlementEncryptionAlgorithm other && Equals(other);
        public bool Equals(FlowEntitlementEncryptionAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    /// </summary>
    [EnumType]
    public readonly struct FlowEntitlementEncryptionKeyType : IEquatable<FlowEntitlementEncryptionKeyType>
    {
        private readonly string _value;

        private FlowEntitlementEncryptionKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowEntitlementEncryptionKeyType Speke { get; } = new FlowEntitlementEncryptionKeyType("speke");
        public static FlowEntitlementEncryptionKeyType StaticKey { get; } = new FlowEntitlementEncryptionKeyType("static-key");

        public static bool operator ==(FlowEntitlementEncryptionKeyType left, FlowEntitlementEncryptionKeyType right) => left.Equals(right);
        public static bool operator !=(FlowEntitlementEncryptionKeyType left, FlowEntitlementEncryptionKeyType right) => !left.Equals(right);

        public static explicit operator string(FlowEntitlementEncryptionKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowEntitlementEncryptionKeyType other && Equals(other);
        public bool Equals(FlowEntitlementEncryptionKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    ///  An indication of whether the entitlement is enabled.
    /// </summary>
    [EnumType]
    public readonly struct FlowEntitlementEntitlementStatus : IEquatable<FlowEntitlementEntitlementStatus>
    {
        private readonly string _value;

        private FlowEntitlementEntitlementStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowEntitlementEntitlementStatus Enabled { get; } = new FlowEntitlementEntitlementStatus("ENABLED");
        public static FlowEntitlementEntitlementStatus Disabled { get; } = new FlowEntitlementEntitlementStatus("DISABLED");

        public static bool operator ==(FlowEntitlementEntitlementStatus left, FlowEntitlementEntitlementStatus right) => left.Equals(right);
        public static bool operator !=(FlowEntitlementEntitlementStatus left, FlowEntitlementEntitlementStatus right) => !left.Equals(right);

        public static explicit operator string(FlowEntitlementEntitlementStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowEntitlementEntitlementStatus other && Equals(other);
        public bool Equals(FlowEntitlementEntitlementStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.
    /// </summary>
    [EnumType]
    public readonly struct FlowFailoverConfigFailoverMode : IEquatable<FlowFailoverConfigFailoverMode>
    {
        private readonly string _value;

        private FlowFailoverConfigFailoverMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowFailoverConfigFailoverMode Merge { get; } = new FlowFailoverConfigFailoverMode("MERGE");
        public static FlowFailoverConfigFailoverMode Failover { get; } = new FlowFailoverConfigFailoverMode("FAILOVER");

        public static bool operator ==(FlowFailoverConfigFailoverMode left, FlowFailoverConfigFailoverMode right) => left.Equals(right);
        public static bool operator !=(FlowFailoverConfigFailoverMode left, FlowFailoverConfigFailoverMode right) => !left.Equals(right);

        public static explicit operator string(FlowFailoverConfigFailoverMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowFailoverConfigFailoverMode other && Equals(other);
        public bool Equals(FlowFailoverConfigFailoverMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FlowFailoverConfigState : IEquatable<FlowFailoverConfigState>
    {
        private readonly string _value;

        private FlowFailoverConfigState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowFailoverConfigState Enabled { get; } = new FlowFailoverConfigState("ENABLED");
        public static FlowFailoverConfigState Disabled { get; } = new FlowFailoverConfigState("DISABLED");

        public static bool operator ==(FlowFailoverConfigState left, FlowFailoverConfigState right) => left.Equals(right);
        public static bool operator !=(FlowFailoverConfigState left, FlowFailoverConfigState right) => !left.Equals(right);

        public static explicit operator string(FlowFailoverConfigState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowFailoverConfigState other && Equals(other);
        public bool Equals(FlowFailoverConfigState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    /// </summary>
    [EnumType]
    public readonly struct FlowOutputEncryptionAlgorithm : IEquatable<FlowOutputEncryptionAlgorithm>
    {
        private readonly string _value;

        private FlowOutputEncryptionAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowOutputEncryptionAlgorithm Aes128 { get; } = new FlowOutputEncryptionAlgorithm("aes128");
        public static FlowOutputEncryptionAlgorithm Aes192 { get; } = new FlowOutputEncryptionAlgorithm("aes192");
        public static FlowOutputEncryptionAlgorithm Aes256 { get; } = new FlowOutputEncryptionAlgorithm("aes256");

        public static bool operator ==(FlowOutputEncryptionAlgorithm left, FlowOutputEncryptionAlgorithm right) => left.Equals(right);
        public static bool operator !=(FlowOutputEncryptionAlgorithm left, FlowOutputEncryptionAlgorithm right) => !left.Equals(right);

        public static explicit operator string(FlowOutputEncryptionAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowOutputEncryptionAlgorithm other && Equals(other);
        public bool Equals(FlowOutputEncryptionAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    /// </summary>
    [EnumType]
    public readonly struct FlowOutputEncryptionKeyType : IEquatable<FlowOutputEncryptionKeyType>
    {
        private readonly string _value;

        private FlowOutputEncryptionKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowOutputEncryptionKeyType StaticKey { get; } = new FlowOutputEncryptionKeyType("static-key");
        public static FlowOutputEncryptionKeyType SrtPassword { get; } = new FlowOutputEncryptionKeyType("srt-password");

        public static bool operator ==(FlowOutputEncryptionKeyType left, FlowOutputEncryptionKeyType right) => left.Equals(right);
        public static bool operator !=(FlowOutputEncryptionKeyType left, FlowOutputEncryptionKeyType right) => !left.Equals(right);

        public static explicit operator string(FlowOutputEncryptionKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowOutputEncryptionKeyType other && Equals(other);
        public bool Equals(FlowOutputEncryptionKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The protocol that is used by the source or output.
    /// </summary>
    [EnumType]
    public readonly struct FlowOutputProtocol : IEquatable<FlowOutputProtocol>
    {
        private readonly string _value;

        private FlowOutputProtocol(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowOutputProtocol ZixiPush { get; } = new FlowOutputProtocol("zixi-push");
        public static FlowOutputProtocol RtpFec { get; } = new FlowOutputProtocol("rtp-fec");
        public static FlowOutputProtocol Rtp { get; } = new FlowOutputProtocol("rtp");
        public static FlowOutputProtocol ZixiPull { get; } = new FlowOutputProtocol("zixi-pull");
        public static FlowOutputProtocol Rist { get; } = new FlowOutputProtocol("rist");
        public static FlowOutputProtocol FujitsuQos { get; } = new FlowOutputProtocol("fujitsu-qos");
        public static FlowOutputProtocol SrtListener { get; } = new FlowOutputProtocol("srt-listener");
        public static FlowOutputProtocol SrtCaller { get; } = new FlowOutputProtocol("srt-caller");

        public static bool operator ==(FlowOutputProtocol left, FlowOutputProtocol right) => left.Equals(right);
        public static bool operator !=(FlowOutputProtocol left, FlowOutputProtocol right) => !left.Equals(right);

        public static explicit operator string(FlowOutputProtocol value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowOutputProtocol other && Equals(other);
        public bool Equals(FlowOutputProtocol other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of algorithm that is used for the encryption (such as aes128, aes192, or aes256).
    /// </summary>
    [EnumType]
    public readonly struct FlowSourceEncryptionAlgorithm : IEquatable<FlowSourceEncryptionAlgorithm>
    {
        private readonly string _value;

        private FlowSourceEncryptionAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowSourceEncryptionAlgorithm Aes128 { get; } = new FlowSourceEncryptionAlgorithm("aes128");
        public static FlowSourceEncryptionAlgorithm Aes192 { get; } = new FlowSourceEncryptionAlgorithm("aes192");
        public static FlowSourceEncryptionAlgorithm Aes256 { get; } = new FlowSourceEncryptionAlgorithm("aes256");

        public static bool operator ==(FlowSourceEncryptionAlgorithm left, FlowSourceEncryptionAlgorithm right) => left.Equals(right);
        public static bool operator !=(FlowSourceEncryptionAlgorithm left, FlowSourceEncryptionAlgorithm right) => !left.Equals(right);

        public static explicit operator string(FlowSourceEncryptionAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowSourceEncryptionAlgorithm other && Equals(other);
        public bool Equals(FlowSourceEncryptionAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of key that is used for the encryption. If no keyType is provided, the service will use the default setting (static-key).
    /// </summary>
    [EnumType]
    public readonly struct FlowSourceEncryptionKeyType : IEquatable<FlowSourceEncryptionKeyType>
    {
        private readonly string _value;

        private FlowSourceEncryptionKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowSourceEncryptionKeyType Speke { get; } = new FlowSourceEncryptionKeyType("speke");
        public static FlowSourceEncryptionKeyType StaticKey { get; } = new FlowSourceEncryptionKeyType("static-key");
        public static FlowSourceEncryptionKeyType SrtPassword { get; } = new FlowSourceEncryptionKeyType("srt-password");

        public static bool operator ==(FlowSourceEncryptionKeyType left, FlowSourceEncryptionKeyType right) => left.Equals(right);
        public static bool operator !=(FlowSourceEncryptionKeyType left, FlowSourceEncryptionKeyType right) => !left.Equals(right);

        public static explicit operator string(FlowSourceEncryptionKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowSourceEncryptionKeyType other && Equals(other);
        public bool Equals(FlowSourceEncryptionKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The protocol that is used by the source.
    /// </summary>
    [EnumType]
    public readonly struct FlowSourceProtocol : IEquatable<FlowSourceProtocol>
    {
        private readonly string _value;

        private FlowSourceProtocol(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FlowSourceProtocol ZixiPush { get; } = new FlowSourceProtocol("zixi-push");
        public static FlowSourceProtocol RtpFec { get; } = new FlowSourceProtocol("rtp-fec");
        public static FlowSourceProtocol Rtp { get; } = new FlowSourceProtocol("rtp");
        public static FlowSourceProtocol Rist { get; } = new FlowSourceProtocol("rist");
        public static FlowSourceProtocol FujitsuQos { get; } = new FlowSourceProtocol("fujitsu-qos");
        public static FlowSourceProtocol SrtListener { get; } = new FlowSourceProtocol("srt-listener");
        public static FlowSourceProtocol SrtCaller { get; } = new FlowSourceProtocol("srt-caller");

        public static bool operator ==(FlowSourceProtocol left, FlowSourceProtocol right) => left.Equals(right);
        public static bool operator !=(FlowSourceProtocol left, FlowSourceProtocol right) => !left.Equals(right);

        public static explicit operator string(FlowSourceProtocol value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FlowSourceProtocol other && Equals(other);
        public bool Equals(FlowSourceProtocol other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
