// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.NimbleStudio
{
    [EnumType]
    public readonly struct LaunchProfileStreamingClipboardMode : IEquatable<LaunchProfileStreamingClipboardMode>
    {
        private readonly string _value;

        private LaunchProfileStreamingClipboardMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LaunchProfileStreamingClipboardMode Enabled { get; } = new LaunchProfileStreamingClipboardMode("ENABLED");
        public static LaunchProfileStreamingClipboardMode Disabled { get; } = new LaunchProfileStreamingClipboardMode("DISABLED");

        public static bool operator ==(LaunchProfileStreamingClipboardMode left, LaunchProfileStreamingClipboardMode right) => left.Equals(right);
        public static bool operator !=(LaunchProfileStreamingClipboardMode left, LaunchProfileStreamingClipboardMode right) => !left.Equals(right);

        public static explicit operator string(LaunchProfileStreamingClipboardMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LaunchProfileStreamingClipboardMode other && Equals(other);
        public bool Equals(LaunchProfileStreamingClipboardMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct LaunchProfileStreamingInstanceType : IEquatable<LaunchProfileStreamingInstanceType>
    {
        private readonly string _value;

        private LaunchProfileStreamingInstanceType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LaunchProfileStreamingInstanceType G4dnXlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.xlarge");
        public static LaunchProfileStreamingInstanceType G4dn2xlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.2xlarge");
        public static LaunchProfileStreamingInstanceType G4dn4xlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.4xlarge");
        public static LaunchProfileStreamingInstanceType G4dn8xlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.8xlarge");
        public static LaunchProfileStreamingInstanceType G4dn12xlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.12xlarge");
        public static LaunchProfileStreamingInstanceType G4dn16xlarge { get; } = new LaunchProfileStreamingInstanceType("g4dn.16xlarge");
        public static LaunchProfileStreamingInstanceType G34xlarge { get; } = new LaunchProfileStreamingInstanceType("g3.4xlarge");
        public static LaunchProfileStreamingInstanceType G3sXlarge { get; } = new LaunchProfileStreamingInstanceType("g3s.xlarge");
        public static LaunchProfileStreamingInstanceType G5Xlarge { get; } = new LaunchProfileStreamingInstanceType("g5.xlarge");
        public static LaunchProfileStreamingInstanceType G52xlarge { get; } = new LaunchProfileStreamingInstanceType("g5.2xlarge");
        public static LaunchProfileStreamingInstanceType G54xlarge { get; } = new LaunchProfileStreamingInstanceType("g5.4xlarge");
        public static LaunchProfileStreamingInstanceType G58xlarge { get; } = new LaunchProfileStreamingInstanceType("g5.8xlarge");
        public static LaunchProfileStreamingInstanceType G516xlarge { get; } = new LaunchProfileStreamingInstanceType("g5.16xlarge");

        public static bool operator ==(LaunchProfileStreamingInstanceType left, LaunchProfileStreamingInstanceType right) => left.Equals(right);
        public static bool operator !=(LaunchProfileStreamingInstanceType left, LaunchProfileStreamingInstanceType right) => !left.Equals(right);

        public static explicit operator string(LaunchProfileStreamingInstanceType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LaunchProfileStreamingInstanceType other && Equals(other);
        public bool Equals(LaunchProfileStreamingInstanceType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct LaunchProfileStreamingSessionStorageMode : IEquatable<LaunchProfileStreamingSessionStorageMode>
    {
        private readonly string _value;

        private LaunchProfileStreamingSessionStorageMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LaunchProfileStreamingSessionStorageMode Upload { get; } = new LaunchProfileStreamingSessionStorageMode("UPLOAD");

        public static bool operator ==(LaunchProfileStreamingSessionStorageMode left, LaunchProfileStreamingSessionStorageMode right) => left.Equals(right);
        public static bool operator !=(LaunchProfileStreamingSessionStorageMode left, LaunchProfileStreamingSessionStorageMode right) => !left.Equals(right);

        public static explicit operator string(LaunchProfileStreamingSessionStorageMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LaunchProfileStreamingSessionStorageMode other && Equals(other);
        public bool Equals(LaunchProfileStreamingSessionStorageMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// &lt;p/&gt;
    /// </summary>
    [EnumType]
    public readonly struct StreamingImageEncryptionConfigurationKeyType : IEquatable<StreamingImageEncryptionConfigurationKeyType>
    {
        private readonly string _value;

        private StreamingImageEncryptionConfigurationKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StreamingImageEncryptionConfigurationKeyType CustomerManagedKey { get; } = new StreamingImageEncryptionConfigurationKeyType("CUSTOMER_MANAGED_KEY");

        public static bool operator ==(StreamingImageEncryptionConfigurationKeyType left, StreamingImageEncryptionConfigurationKeyType right) => left.Equals(right);
        public static bool operator !=(StreamingImageEncryptionConfigurationKeyType left, StreamingImageEncryptionConfigurationKeyType right) => !left.Equals(right);

        public static explicit operator string(StreamingImageEncryptionConfigurationKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StreamingImageEncryptionConfigurationKeyType other && Equals(other);
        public bool Equals(StreamingImageEncryptionConfigurationKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StudioComponentInitializationScriptRunContext : IEquatable<StudioComponentInitializationScriptRunContext>
    {
        private readonly string _value;

        private StudioComponentInitializationScriptRunContext(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StudioComponentInitializationScriptRunContext SystemInitialization { get; } = new StudioComponentInitializationScriptRunContext("SYSTEM_INITIALIZATION");
        public static StudioComponentInitializationScriptRunContext UserInitialization { get; } = new StudioComponentInitializationScriptRunContext("USER_INITIALIZATION");

        public static bool operator ==(StudioComponentInitializationScriptRunContext left, StudioComponentInitializationScriptRunContext right) => left.Equals(right);
        public static bool operator !=(StudioComponentInitializationScriptRunContext left, StudioComponentInitializationScriptRunContext right) => !left.Equals(right);

        public static explicit operator string(StudioComponentInitializationScriptRunContext value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StudioComponentInitializationScriptRunContext other && Equals(other);
        public bool Equals(StudioComponentInitializationScriptRunContext other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StudioComponentLaunchProfilePlatform : IEquatable<StudioComponentLaunchProfilePlatform>
    {
        private readonly string _value;

        private StudioComponentLaunchProfilePlatform(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StudioComponentLaunchProfilePlatform Linux { get; } = new StudioComponentLaunchProfilePlatform("LINUX");
        public static StudioComponentLaunchProfilePlatform Windows { get; } = new StudioComponentLaunchProfilePlatform("WINDOWS");

        public static bool operator ==(StudioComponentLaunchProfilePlatform left, StudioComponentLaunchProfilePlatform right) => left.Equals(right);
        public static bool operator !=(StudioComponentLaunchProfilePlatform left, StudioComponentLaunchProfilePlatform right) => !left.Equals(right);

        public static explicit operator string(StudioComponentLaunchProfilePlatform value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StudioComponentLaunchProfilePlatform other && Equals(other);
        public bool Equals(StudioComponentLaunchProfilePlatform other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StudioComponentSubtype : IEquatable<StudioComponentSubtype>
    {
        private readonly string _value;

        private StudioComponentSubtype(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StudioComponentSubtype AwsManagedMicrosoftAd { get; } = new StudioComponentSubtype("AWS_MANAGED_MICROSOFT_AD");
        public static StudioComponentSubtype AmazonFsxForWindows { get; } = new StudioComponentSubtype("AMAZON_FSX_FOR_WINDOWS");
        public static StudioComponentSubtype AmazonFsxForLustre { get; } = new StudioComponentSubtype("AMAZON_FSX_FOR_LUSTRE");
        public static StudioComponentSubtype Custom { get; } = new StudioComponentSubtype("CUSTOM");

        public static bool operator ==(StudioComponentSubtype left, StudioComponentSubtype right) => left.Equals(right);
        public static bool operator !=(StudioComponentSubtype left, StudioComponentSubtype right) => !left.Equals(right);

        public static explicit operator string(StudioComponentSubtype value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StudioComponentSubtype other && Equals(other);
        public bool Equals(StudioComponentSubtype other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct StudioComponentType : IEquatable<StudioComponentType>
    {
        private readonly string _value;

        private StudioComponentType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StudioComponentType ActiveDirectory { get; } = new StudioComponentType("ACTIVE_DIRECTORY");
        public static StudioComponentType SharedFileSystem { get; } = new StudioComponentType("SHARED_FILE_SYSTEM");
        public static StudioComponentType ComputeFarm { get; } = new StudioComponentType("COMPUTE_FARM");
        public static StudioComponentType LicenseService { get; } = new StudioComponentType("LICENSE_SERVICE");
        public static StudioComponentType Custom { get; } = new StudioComponentType("CUSTOM");

        public static bool operator ==(StudioComponentType left, StudioComponentType right) => left.Equals(right);
        public static bool operator !=(StudioComponentType left, StudioComponentType right) => !left.Equals(right);

        public static explicit operator string(StudioComponentType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StudioComponentType other && Equals(other);
        public bool Equals(StudioComponentType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// &lt;p&gt;The type of KMS key that is used to encrypt studio data.&lt;/p&gt;
    /// </summary>
    [EnumType]
    public readonly struct StudioEncryptionConfigurationKeyType : IEquatable<StudioEncryptionConfigurationKeyType>
    {
        private readonly string _value;

        private StudioEncryptionConfigurationKeyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static StudioEncryptionConfigurationKeyType AwsOwnedKey { get; } = new StudioEncryptionConfigurationKeyType("AWS_OWNED_KEY");
        public static StudioEncryptionConfigurationKeyType CustomerManagedKey { get; } = new StudioEncryptionConfigurationKeyType("CUSTOMER_MANAGED_KEY");

        public static bool operator ==(StudioEncryptionConfigurationKeyType left, StudioEncryptionConfigurationKeyType right) => left.Equals(right);
        public static bool operator !=(StudioEncryptionConfigurationKeyType left, StudioEncryptionConfigurationKeyType right) => !left.Equals(right);

        public static explicit operator string(StudioEncryptionConfigurationKeyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is StudioEncryptionConfigurationKeyType other && Equals(other);
        public bool Equals(StudioEncryptionConfigurationKeyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
