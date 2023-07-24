// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.KMS
{
    /// <summary>
    /// The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is AWS_KMS, which means that AWS KMS creates the key material.
    /// </summary>
    [EnumType]
    public readonly struct KeyOrigin : IEquatable<KeyOrigin>
    {
        private readonly string _value;

        private KeyOrigin(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static KeyOrigin AwsKms { get; } = new KeyOrigin("AWS_KMS");
        public static KeyOrigin External { get; } = new KeyOrigin("EXTERNAL");

        public static bool operator ==(KeyOrigin left, KeyOrigin right) => left.Equals(right);
        public static bool operator !=(KeyOrigin left, KeyOrigin right) => !left.Equals(right);

        public static explicit operator string(KeyOrigin value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is KeyOrigin other && Equals(other);
        public bool Equals(KeyOrigin other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
    /// </summary>
    [EnumType]
    public readonly struct KeySpec : IEquatable<KeySpec>
    {
        private readonly string _value;

        private KeySpec(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static KeySpec SymmetricDefault { get; } = new KeySpec("SYMMETRIC_DEFAULT");
        public static KeySpec Rsa2048 { get; } = new KeySpec("RSA_2048");
        public static KeySpec Rsa3072 { get; } = new KeySpec("RSA_3072");
        public static KeySpec Rsa4096 { get; } = new KeySpec("RSA_4096");
        public static KeySpec EccNistP256 { get; } = new KeySpec("ECC_NIST_P256");
        public static KeySpec EccNistP384 { get; } = new KeySpec("ECC_NIST_P384");
        public static KeySpec EccNistP521 { get; } = new KeySpec("ECC_NIST_P521");
        public static KeySpec EccSecgP256k1 { get; } = new KeySpec("ECC_SECG_P256K1");
        public static KeySpec Hmac224 { get; } = new KeySpec("HMAC_224");
        public static KeySpec Hmac256 { get; } = new KeySpec("HMAC_256");
        public static KeySpec Hmac384 { get; } = new KeySpec("HMAC_384");
        public static KeySpec Hmac512 { get; } = new KeySpec("HMAC_512");
        public static KeySpec Sm2 { get; } = new KeySpec("SM2");

        public static bool operator ==(KeySpec left, KeySpec right) => left.Equals(right);
        public static bool operator !=(KeySpec left, KeySpec right) => !left.Equals(right);

        public static explicit operator string(KeySpec value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is KeySpec other && Equals(other);
        public bool Equals(KeySpec other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
    /// </summary>
    [EnumType]
    public readonly struct KeyUsage : IEquatable<KeyUsage>
    {
        private readonly string _value;

        private KeyUsage(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static KeyUsage EncryptDecrypt { get; } = new KeyUsage("ENCRYPT_DECRYPT");
        public static KeyUsage SignVerify { get; } = new KeyUsage("SIGN_VERIFY");
        public static KeyUsage GenerateVerifyMac { get; } = new KeyUsage("GENERATE_VERIFY_MAC");

        public static bool operator ==(KeyUsage left, KeyUsage right) => left.Equals(right);
        public static bool operator !=(KeyUsage left, KeyUsage right) => !left.Equals(right);

        public static explicit operator string(KeyUsage value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is KeyUsage other && Equals(other);
        public bool Equals(KeyUsage other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
