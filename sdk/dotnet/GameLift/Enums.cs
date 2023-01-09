// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.GameLift
{
    /// <summary>
    /// Simple routing strategy. The alias resolves to one specific fleet. Use this type when routing to active fleets.
    /// </summary>
    [EnumType]
    public readonly struct AliasRoutingStrategyType : IEquatable<AliasRoutingStrategyType>
    {
        private readonly string _value;

        private AliasRoutingStrategyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static AliasRoutingStrategyType Simple { get; } = new AliasRoutingStrategyType("SIMPLE");
        public static AliasRoutingStrategyType Terminal { get; } = new AliasRoutingStrategyType("TERMINAL");

        public static bool operator ==(AliasRoutingStrategyType left, AliasRoutingStrategyType right) => left.Equals(right);
        public static bool operator !=(AliasRoutingStrategyType left, AliasRoutingStrategyType right) => !left.Equals(right);

        public static explicit operator string(AliasRoutingStrategyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is AliasRoutingStrategyType other && Equals(other);
        public bool Equals(AliasRoutingStrategyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The operating system that the game server binaries are built to run on. This value determines the type of fleet resources that you can use for this build. If your game build contains multiple executables, they all must run on the same operating system. If an operating system is not specified when creating a build, Amazon GameLift uses the default value (WINDOWS_2012). This value cannot be changed later.
    /// </summary>
    [EnumType]
    public readonly struct BuildOperatingSystem : IEquatable<BuildOperatingSystem>
    {
        private readonly string _value;

        private BuildOperatingSystem(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static BuildOperatingSystem AmazonLinux { get; } = new BuildOperatingSystem("AMAZON_LINUX");
        public static BuildOperatingSystem AmazonLinux2 { get; } = new BuildOperatingSystem("AMAZON_LINUX_2");
        public static BuildOperatingSystem Windows2012 { get; } = new BuildOperatingSystem("WINDOWS_2012");

        public static bool operator ==(BuildOperatingSystem left, BuildOperatingSystem right) => left.Equals(right);
        public static bool operator !=(BuildOperatingSystem left, BuildOperatingSystem right) => !left.Equals(right);

        public static explicit operator string(BuildOperatingSystem value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is BuildOperatingSystem other && Equals(other);
        public bool Equals(BuildOperatingSystem other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FleetCertificateConfigurationCertificateType : IEquatable<FleetCertificateConfigurationCertificateType>
    {
        private readonly string _value;

        private FleetCertificateConfigurationCertificateType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FleetCertificateConfigurationCertificateType Disabled { get; } = new FleetCertificateConfigurationCertificateType("DISABLED");
        public static FleetCertificateConfigurationCertificateType Generated { get; } = new FleetCertificateConfigurationCertificateType("GENERATED");

        public static bool operator ==(FleetCertificateConfigurationCertificateType left, FleetCertificateConfigurationCertificateType right) => left.Equals(right);
        public static bool operator !=(FleetCertificateConfigurationCertificateType left, FleetCertificateConfigurationCertificateType right) => !left.Equals(right);

        public static explicit operator string(FleetCertificateConfigurationCertificateType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FleetCertificateConfigurationCertificateType other && Equals(other);
        public bool Equals(FleetCertificateConfigurationCertificateType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// ComputeType to differentiate EC2 hardware managed by GameLift and Anywhere hardware managed by the customer.
    /// </summary>
    [EnumType]
    public readonly struct FleetComputeType : IEquatable<FleetComputeType>
    {
        private readonly string _value;

        private FleetComputeType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FleetComputeType Ec2 { get; } = new FleetComputeType("EC2");
        public static FleetComputeType Anywhere { get; } = new FleetComputeType("ANYWHERE");

        public static bool operator ==(FleetComputeType left, FleetComputeType right) => left.Equals(right);
        public static bool operator !=(FleetComputeType left, FleetComputeType right) => !left.Equals(right);

        public static explicit operator string(FleetComputeType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FleetComputeType other && Equals(other);
        public bool Equals(FleetComputeType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The network communication protocol used by the fleet.
    /// </summary>
    [EnumType]
    public readonly struct FleetIpPermissionProtocol : IEquatable<FleetIpPermissionProtocol>
    {
        private readonly string _value;

        private FleetIpPermissionProtocol(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FleetIpPermissionProtocol Tcp { get; } = new FleetIpPermissionProtocol("TCP");
        public static FleetIpPermissionProtocol Udp { get; } = new FleetIpPermissionProtocol("UDP");

        public static bool operator ==(FleetIpPermissionProtocol left, FleetIpPermissionProtocol right) => left.Equals(right);
        public static bool operator !=(FleetIpPermissionProtocol left, FleetIpPermissionProtocol right) => !left.Equals(right);

        public static explicit operator string(FleetIpPermissionProtocol value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FleetIpPermissionProtocol other && Equals(other);
        public bool Equals(FleetIpPermissionProtocol other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A game session protection policy to apply to all game sessions hosted on instances in this fleet. When protected, active game sessions cannot be terminated during a scale-down event. If this parameter is not set, instances in this fleet default to no protection. You can change a fleet's protection policy to affect future game sessions on the fleet. You can also set protection for individual game sessions.
    /// </summary>
    [EnumType]
    public readonly struct FleetNewGameSessionProtectionPolicy : IEquatable<FleetNewGameSessionProtectionPolicy>
    {
        private readonly string _value;

        private FleetNewGameSessionProtectionPolicy(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FleetNewGameSessionProtectionPolicy FullProtection { get; } = new FleetNewGameSessionProtectionPolicy("FullProtection");
        public static FleetNewGameSessionProtectionPolicy NoProtection { get; } = new FleetNewGameSessionProtectionPolicy("NoProtection");

        public static bool operator ==(FleetNewGameSessionProtectionPolicy left, FleetNewGameSessionProtectionPolicy right) => left.Equals(right);
        public static bool operator !=(FleetNewGameSessionProtectionPolicy left, FleetNewGameSessionProtectionPolicy right) => !left.Equals(right);

        public static explicit operator string(FleetNewGameSessionProtectionPolicy value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FleetNewGameSessionProtectionPolicy other && Equals(other);
        public bool Equals(FleetNewGameSessionProtectionPolicy other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Indicates whether to use On-Demand instances or Spot instances for this fleet. If empty, the default is ON_DEMAND. Both categories of instances use identical hardware and configurations based on the instance type selected for this fleet.
    /// </summary>
    [EnumType]
    public readonly struct FleetType : IEquatable<FleetType>
    {
        private readonly string _value;

        private FleetType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FleetType OnDemand { get; } = new FleetType("ON_DEMAND");
        public static FleetType Spot { get; } = new FleetType("SPOT");

        public static bool operator ==(FleetType left, FleetType right) => left.Equals(right);
        public static bool operator !=(FleetType left, FleetType right) => !left.Equals(right);

        public static explicit operator string(FleetType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FleetType other && Equals(other);
        public bool Equals(FleetType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The fallback balancing method to use for the game server group when Spot Instances in a Region become unavailable or are not viable for game hosting.
    /// </summary>
    [EnumType]
    public readonly struct GameServerGroupBalancingStrategy : IEquatable<GameServerGroupBalancingStrategy>
    {
        private readonly string _value;

        private GameServerGroupBalancingStrategy(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static GameServerGroupBalancingStrategy SpotOnly { get; } = new GameServerGroupBalancingStrategy("SPOT_ONLY");
        public static GameServerGroupBalancingStrategy SpotPreferred { get; } = new GameServerGroupBalancingStrategy("SPOT_PREFERRED");
        public static GameServerGroupBalancingStrategy OnDemandOnly { get; } = new GameServerGroupBalancingStrategy("ON_DEMAND_ONLY");

        public static bool operator ==(GameServerGroupBalancingStrategy left, GameServerGroupBalancingStrategy right) => left.Equals(right);
        public static bool operator !=(GameServerGroupBalancingStrategy left, GameServerGroupBalancingStrategy right) => !left.Equals(right);

        public static explicit operator string(GameServerGroupBalancingStrategy value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GameServerGroupBalancingStrategy other && Equals(other);
        public bool Equals(GameServerGroupBalancingStrategy other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of delete to perform.
    /// </summary>
    [EnumType]
    public readonly struct GameServerGroupDeleteOption : IEquatable<GameServerGroupDeleteOption>
    {
        private readonly string _value;

        private GameServerGroupDeleteOption(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static GameServerGroupDeleteOption SafeDelete { get; } = new GameServerGroupDeleteOption("SAFE_DELETE");
        public static GameServerGroupDeleteOption ForceDelete { get; } = new GameServerGroupDeleteOption("FORCE_DELETE");
        public static GameServerGroupDeleteOption Retain { get; } = new GameServerGroupDeleteOption("RETAIN");

        public static bool operator ==(GameServerGroupDeleteOption left, GameServerGroupDeleteOption right) => left.Equals(right);
        public static bool operator !=(GameServerGroupDeleteOption left, GameServerGroupDeleteOption right) => !left.Equals(right);

        public static explicit operator string(GameServerGroupDeleteOption value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GameServerGroupDeleteOption other && Equals(other);
        public bool Equals(GameServerGroupDeleteOption other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A flag that indicates whether instances in the game server group are protected from early termination.
    /// </summary>
    [EnumType]
    public readonly struct GameServerGroupGameServerProtectionPolicy : IEquatable<GameServerGroupGameServerProtectionPolicy>
    {
        private readonly string _value;

        private GameServerGroupGameServerProtectionPolicy(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static GameServerGroupGameServerProtectionPolicy NoProtection { get; } = new GameServerGroupGameServerProtectionPolicy("NO_PROTECTION");
        public static GameServerGroupGameServerProtectionPolicy FullProtection { get; } = new GameServerGroupGameServerProtectionPolicy("FULL_PROTECTION");

        public static bool operator ==(GameServerGroupGameServerProtectionPolicy left, GameServerGroupGameServerProtectionPolicy right) => left.Equals(right);
        public static bool operator !=(GameServerGroupGameServerProtectionPolicy left, GameServerGroupGameServerProtectionPolicy right) => !left.Equals(right);

        public static explicit operator string(GameServerGroupGameServerProtectionPolicy value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GameServerGroupGameServerProtectionPolicy other && Equals(other);
        public bool Equals(GameServerGroupGameServerProtectionPolicy other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
