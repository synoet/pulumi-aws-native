// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.Transfer
{
    /// <summary>
    /// Specifies the status of the agreement.
    /// </summary>
    [EnumType]
    public readonly struct AgreementStatus : IEquatable<AgreementStatus>
    {
        private readonly string _value;

        private AgreementStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AgreementStatus Active { get; } = new AgreementStatus("ACTIVE");
        public static AgreementStatus Inactive { get; } = new AgreementStatus("INACTIVE");

        public static bool operator ==(AgreementStatus left, AgreementStatus right) => left.Equals(right);
        public static bool operator !=(AgreementStatus left, AgreementStatus right) => !left.Equals(right);

        public static explicit operator string(AgreementStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AgreementStatus other && Equals(other);
        public bool Equals(AgreementStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A status description for the certificate.
    /// </summary>
    [EnumType]
    public readonly struct CertificateStatus : IEquatable<CertificateStatus>
    {
        private readonly string _value;

        private CertificateStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static CertificateStatus Active { get; } = new CertificateStatus("ACTIVE");
        public static CertificateStatus Pending { get; } = new CertificateStatus("PENDING");
        public static CertificateStatus Inactive { get; } = new CertificateStatus("INACTIVE");

        public static bool operator ==(CertificateStatus left, CertificateStatus right) => left.Equals(right);
        public static bool operator !=(CertificateStatus left, CertificateStatus right) => !left.Equals(right);

        public static explicit operator string(CertificateStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is CertificateStatus other && Equals(other);
        public bool Equals(CertificateStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Describing the type of certificate. With or without a private key.
    /// </summary>
    [EnumType]
    public readonly struct CertificateType : IEquatable<CertificateType>
    {
        private readonly string _value;

        private CertificateType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static CertificateType Certificate { get; } = new CertificateType("CERTIFICATE");
        public static CertificateType CertificateWithPrivateKey { get; } = new CertificateType("CERTIFICATE_WITH_PRIVATE_KEY");

        public static bool operator ==(CertificateType left, CertificateType right) => left.Equals(right);
        public static bool operator !=(CertificateType left, CertificateType right) => !left.Equals(right);

        public static explicit operator string(CertificateType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is CertificateType other && Equals(other);
        public bool Equals(CertificateType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specifies the usage type for the certificate.
    /// </summary>
    [EnumType]
    public readonly struct CertificateUsage : IEquatable<CertificateUsage>
    {
        private readonly string _value;

        private CertificateUsage(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static CertificateUsage Signing { get; } = new CertificateUsage("SIGNING");
        public static CertificateUsage Encryption { get; } = new CertificateUsage("ENCRYPTION");

        public static bool operator ==(CertificateUsage left, CertificateUsage right) => left.Equals(right);
        public static bool operator !=(CertificateUsage left, CertificateUsage right) => !left.Equals(right);

        public static explicit operator string(CertificateUsage value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is CertificateUsage other && Equals(other);
        public bool Equals(CertificateUsage other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Compression setting for this AS2 connector configuration.
    /// </summary>
    [EnumType]
    public readonly struct ConnectorAs2ConfigPropertiesCompression : IEquatable<ConnectorAs2ConfigPropertiesCompression>
    {
        private readonly string _value;

        private ConnectorAs2ConfigPropertiesCompression(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectorAs2ConfigPropertiesCompression Zlib { get; } = new ConnectorAs2ConfigPropertiesCompression("ZLIB");
        public static ConnectorAs2ConfigPropertiesCompression Disabled { get; } = new ConnectorAs2ConfigPropertiesCompression("DISABLED");

        public static bool operator ==(ConnectorAs2ConfigPropertiesCompression left, ConnectorAs2ConfigPropertiesCompression right) => left.Equals(right);
        public static bool operator !=(ConnectorAs2ConfigPropertiesCompression left, ConnectorAs2ConfigPropertiesCompression right) => !left.Equals(right);

        public static explicit operator string(ConnectorAs2ConfigPropertiesCompression value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectorAs2ConfigPropertiesCompression other && Equals(other);
        public bool Equals(ConnectorAs2ConfigPropertiesCompression other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Encryption algorithm for this AS2 connector configuration.
    /// </summary>
    [EnumType]
    public readonly struct ConnectorAs2ConfigPropertiesEncryptionAlgorithm : IEquatable<ConnectorAs2ConfigPropertiesEncryptionAlgorithm>
    {
        private readonly string _value;

        private ConnectorAs2ConfigPropertiesEncryptionAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectorAs2ConfigPropertiesEncryptionAlgorithm Aes128Cbc { get; } = new ConnectorAs2ConfigPropertiesEncryptionAlgorithm("AES128_CBC");
        public static ConnectorAs2ConfigPropertiesEncryptionAlgorithm Aes192Cbc { get; } = new ConnectorAs2ConfigPropertiesEncryptionAlgorithm("AES192_CBC");
        public static ConnectorAs2ConfigPropertiesEncryptionAlgorithm Aes256Cbc { get; } = new ConnectorAs2ConfigPropertiesEncryptionAlgorithm("AES256_CBC");
        public static ConnectorAs2ConfigPropertiesEncryptionAlgorithm None { get; } = new ConnectorAs2ConfigPropertiesEncryptionAlgorithm("NONE");

        public static bool operator ==(ConnectorAs2ConfigPropertiesEncryptionAlgorithm left, ConnectorAs2ConfigPropertiesEncryptionAlgorithm right) => left.Equals(right);
        public static bool operator !=(ConnectorAs2ConfigPropertiesEncryptionAlgorithm left, ConnectorAs2ConfigPropertiesEncryptionAlgorithm right) => !left.Equals(right);

        public static explicit operator string(ConnectorAs2ConfigPropertiesEncryptionAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectorAs2ConfigPropertiesEncryptionAlgorithm other && Equals(other);
        public bool Equals(ConnectorAs2ConfigPropertiesEncryptionAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// MDN Response setting for this AS2 connector configuration.
    /// </summary>
    [EnumType]
    public readonly struct ConnectorAs2ConfigPropertiesMdnResponse : IEquatable<ConnectorAs2ConfigPropertiesMdnResponse>
    {
        private readonly string _value;

        private ConnectorAs2ConfigPropertiesMdnResponse(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectorAs2ConfigPropertiesMdnResponse Sync { get; } = new ConnectorAs2ConfigPropertiesMdnResponse("SYNC");
        public static ConnectorAs2ConfigPropertiesMdnResponse None { get; } = new ConnectorAs2ConfigPropertiesMdnResponse("NONE");

        public static bool operator ==(ConnectorAs2ConfigPropertiesMdnResponse left, ConnectorAs2ConfigPropertiesMdnResponse right) => left.Equals(right);
        public static bool operator !=(ConnectorAs2ConfigPropertiesMdnResponse left, ConnectorAs2ConfigPropertiesMdnResponse right) => !left.Equals(right);

        public static explicit operator string(ConnectorAs2ConfigPropertiesMdnResponse value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectorAs2ConfigPropertiesMdnResponse other && Equals(other);
        public bool Equals(ConnectorAs2ConfigPropertiesMdnResponse other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// MDN Signing algorithm for this AS2 connector configuration.
    /// </summary>
    [EnumType]
    public readonly struct ConnectorAs2ConfigPropertiesMdnSigningAlgorithm : IEquatable<ConnectorAs2ConfigPropertiesMdnSigningAlgorithm>
    {
        private readonly string _value;

        private ConnectorAs2ConfigPropertiesMdnSigningAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm Sha256 { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("SHA256");
        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm Sha384 { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("SHA384");
        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm Sha512 { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("SHA512");
        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm Sha1 { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("SHA1");
        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm None { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("NONE");
        public static ConnectorAs2ConfigPropertiesMdnSigningAlgorithm Default { get; } = new ConnectorAs2ConfigPropertiesMdnSigningAlgorithm("DEFAULT");

        public static bool operator ==(ConnectorAs2ConfigPropertiesMdnSigningAlgorithm left, ConnectorAs2ConfigPropertiesMdnSigningAlgorithm right) => left.Equals(right);
        public static bool operator !=(ConnectorAs2ConfigPropertiesMdnSigningAlgorithm left, ConnectorAs2ConfigPropertiesMdnSigningAlgorithm right) => !left.Equals(right);

        public static explicit operator string(ConnectorAs2ConfigPropertiesMdnSigningAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectorAs2ConfigPropertiesMdnSigningAlgorithm other && Equals(other);
        public bool Equals(ConnectorAs2ConfigPropertiesMdnSigningAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Signing algorithm for this AS2 connector configuration.
    /// </summary>
    [EnumType]
    public readonly struct ConnectorAs2ConfigPropertiesSigningAlgorithm : IEquatable<ConnectorAs2ConfigPropertiesSigningAlgorithm>
    {
        private readonly string _value;

        private ConnectorAs2ConfigPropertiesSigningAlgorithm(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectorAs2ConfigPropertiesSigningAlgorithm Sha256 { get; } = new ConnectorAs2ConfigPropertiesSigningAlgorithm("SHA256");
        public static ConnectorAs2ConfigPropertiesSigningAlgorithm Sha384 { get; } = new ConnectorAs2ConfigPropertiesSigningAlgorithm("SHA384");
        public static ConnectorAs2ConfigPropertiesSigningAlgorithm Sha512 { get; } = new ConnectorAs2ConfigPropertiesSigningAlgorithm("SHA512");
        public static ConnectorAs2ConfigPropertiesSigningAlgorithm Sha1 { get; } = new ConnectorAs2ConfigPropertiesSigningAlgorithm("SHA1");
        public static ConnectorAs2ConfigPropertiesSigningAlgorithm None { get; } = new ConnectorAs2ConfigPropertiesSigningAlgorithm("NONE");

        public static bool operator ==(ConnectorAs2ConfigPropertiesSigningAlgorithm left, ConnectorAs2ConfigPropertiesSigningAlgorithm right) => left.Equals(right);
        public static bool operator !=(ConnectorAs2ConfigPropertiesSigningAlgorithm left, ConnectorAs2ConfigPropertiesSigningAlgorithm right) => !left.Equals(right);

        public static explicit operator string(ConnectorAs2ConfigPropertiesSigningAlgorithm value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectorAs2ConfigPropertiesSigningAlgorithm other && Equals(other);
        public bool Equals(ConnectorAs2ConfigPropertiesSigningAlgorithm other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Enum specifying whether the profile is local or associated with a trading partner.
    /// </summary>
    [EnumType]
    public readonly struct ProfileType : IEquatable<ProfileType>
    {
        private readonly string _value;

        private ProfileType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ProfileType Local { get; } = new ProfileType("LOCAL");
        public static ProfileType Partner { get; } = new ProfileType("PARTNER");

        public static bool operator ==(ProfileType left, ProfileType right) => left.Equals(right);
        public static bool operator !=(ProfileType left, ProfileType right) => !left.Equals(right);

        public static explicit operator string(ProfileType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ProfileType other && Equals(other);
        public bool Equals(ProfileType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A flag that indicates whether or not to overwrite an existing file of the same name. The default is FALSE.
    /// </summary>
    [EnumType]
    public readonly struct WorkflowStepCopyStepDetailsPropertiesOverwriteExisting : IEquatable<WorkflowStepCopyStepDetailsPropertiesOverwriteExisting>
    {
        private readonly string _value;

        private WorkflowStepCopyStepDetailsPropertiesOverwriteExisting(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static WorkflowStepCopyStepDetailsPropertiesOverwriteExisting True { get; } = new WorkflowStepCopyStepDetailsPropertiesOverwriteExisting("TRUE");
        public static WorkflowStepCopyStepDetailsPropertiesOverwriteExisting False { get; } = new WorkflowStepCopyStepDetailsPropertiesOverwriteExisting("FALSE");

        public static bool operator ==(WorkflowStepCopyStepDetailsPropertiesOverwriteExisting left, WorkflowStepCopyStepDetailsPropertiesOverwriteExisting right) => left.Equals(right);
        public static bool operator !=(WorkflowStepCopyStepDetailsPropertiesOverwriteExisting left, WorkflowStepCopyStepDetailsPropertiesOverwriteExisting right) => !left.Equals(right);

        public static explicit operator string(WorkflowStepCopyStepDetailsPropertiesOverwriteExisting value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is WorkflowStepCopyStepDetailsPropertiesOverwriteExisting other && Equals(other);
        public bool Equals(WorkflowStepCopyStepDetailsPropertiesOverwriteExisting other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A flag that indicates whether or not to overwrite an existing file of the same name. The default is FALSE.
    /// </summary>
    [EnumType]
    public readonly struct WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting : IEquatable<WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting>
    {
        private readonly string _value;

        private WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting True { get; } = new WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting("TRUE");
        public static WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting False { get; } = new WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting("FALSE");

        public static bool operator ==(WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting left, WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting right) => left.Equals(right);
        public static bool operator !=(WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting left, WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting right) => !left.Equals(right);

        public static explicit operator string(WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting other && Equals(other);
        public bool Equals(WorkflowStepDecryptStepDetailsPropertiesOverwriteExisting other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Specifies which encryption method to use.
    /// </summary>
    [EnumType]
    public readonly struct WorkflowStepDecryptStepDetailsPropertiesType : IEquatable<WorkflowStepDecryptStepDetailsPropertiesType>
    {
        private readonly string _value;

        private WorkflowStepDecryptStepDetailsPropertiesType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static WorkflowStepDecryptStepDetailsPropertiesType Pgp { get; } = new WorkflowStepDecryptStepDetailsPropertiesType("PGP");

        public static bool operator ==(WorkflowStepDecryptStepDetailsPropertiesType left, WorkflowStepDecryptStepDetailsPropertiesType right) => left.Equals(right);
        public static bool operator !=(WorkflowStepDecryptStepDetailsPropertiesType left, WorkflowStepDecryptStepDetailsPropertiesType right) => !left.Equals(right);

        public static explicit operator string(WorkflowStepDecryptStepDetailsPropertiesType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is WorkflowStepDecryptStepDetailsPropertiesType other && Equals(other);
        public bool Equals(WorkflowStepDecryptStepDetailsPropertiesType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct WorkflowStepType : IEquatable<WorkflowStepType>
    {
        private readonly string _value;

        private WorkflowStepType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static WorkflowStepType Copy { get; } = new WorkflowStepType("COPY");
        public static WorkflowStepType Custom { get; } = new WorkflowStepType("CUSTOM");
        public static WorkflowStepType Decrypt { get; } = new WorkflowStepType("DECRYPT");
        public static WorkflowStepType Delete { get; } = new WorkflowStepType("DELETE");
        public static WorkflowStepType Tag { get; } = new WorkflowStepType("TAG");

        public static bool operator ==(WorkflowStepType left, WorkflowStepType right) => left.Equals(right);
        public static bool operator !=(WorkflowStepType left, WorkflowStepType right) => !left.Equals(right);

        public static explicit operator string(WorkflowStepType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is WorkflowStepType other && Equals(other);
        public bool Equals(WorkflowStepType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
