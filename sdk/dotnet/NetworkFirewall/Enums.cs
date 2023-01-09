// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.NetworkFirewall
{
    [EnumType]
    public readonly struct FirewallPolicyOverrideAction : IEquatable<FirewallPolicyOverrideAction>
    {
        private readonly string _value;

        private FirewallPolicyOverrideAction(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallPolicyOverrideAction DropToAlert { get; } = new FirewallPolicyOverrideAction("DROP_TO_ALERT");

        public static bool operator ==(FirewallPolicyOverrideAction left, FirewallPolicyOverrideAction right) => left.Equals(right);
        public static bool operator !=(FirewallPolicyOverrideAction left, FirewallPolicyOverrideAction right) => !left.Equals(right);

        public static explicit operator string(FirewallPolicyOverrideAction value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallPolicyOverrideAction other && Equals(other);
        public bool Equals(FirewallPolicyOverrideAction other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FirewallPolicyRuleOrder : IEquatable<FirewallPolicyRuleOrder>
    {
        private readonly string _value;

        private FirewallPolicyRuleOrder(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallPolicyRuleOrder DefaultActionOrder { get; } = new FirewallPolicyRuleOrder("DEFAULT_ACTION_ORDER");
        public static FirewallPolicyRuleOrder StrictOrder { get; } = new FirewallPolicyRuleOrder("STRICT_ORDER");

        public static bool operator ==(FirewallPolicyRuleOrder left, FirewallPolicyRuleOrder right) => left.Equals(right);
        public static bool operator !=(FirewallPolicyRuleOrder left, FirewallPolicyRuleOrder right) => !left.Equals(right);

        public static explicit operator string(FirewallPolicyRuleOrder value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallPolicyRuleOrder other && Equals(other);
        public bool Equals(FirewallPolicyRuleOrder other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FirewallPolicyStreamExceptionPolicy : IEquatable<FirewallPolicyStreamExceptionPolicy>
    {
        private readonly string _value;

        private FirewallPolicyStreamExceptionPolicy(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FirewallPolicyStreamExceptionPolicy Drop { get; } = new FirewallPolicyStreamExceptionPolicy("DROP");
        public static FirewallPolicyStreamExceptionPolicy Continue { get; } = new FirewallPolicyStreamExceptionPolicy("CONTINUE");

        public static bool operator ==(FirewallPolicyStreamExceptionPolicy left, FirewallPolicyStreamExceptionPolicy right) => left.Equals(right);
        public static bool operator !=(FirewallPolicyStreamExceptionPolicy left, FirewallPolicyStreamExceptionPolicy right) => !left.Equals(right);

        public static explicit operator string(FirewallPolicyStreamExceptionPolicy value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FirewallPolicyStreamExceptionPolicy other && Equals(other);
        public bool Equals(FirewallPolicyStreamExceptionPolicy other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct LoggingConfigurationLogDestinationConfigLogDestinationType : IEquatable<LoggingConfigurationLogDestinationConfigLogDestinationType>
    {
        private readonly string _value;

        private LoggingConfigurationLogDestinationConfigLogDestinationType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LoggingConfigurationLogDestinationConfigLogDestinationType S3 { get; } = new LoggingConfigurationLogDestinationConfigLogDestinationType("S3");
        public static LoggingConfigurationLogDestinationConfigLogDestinationType CloudWatchLogs { get; } = new LoggingConfigurationLogDestinationConfigLogDestinationType("CloudWatchLogs");
        public static LoggingConfigurationLogDestinationConfigLogDestinationType KinesisDataFirehose { get; } = new LoggingConfigurationLogDestinationConfigLogDestinationType("KinesisDataFirehose");

        public static bool operator ==(LoggingConfigurationLogDestinationConfigLogDestinationType left, LoggingConfigurationLogDestinationConfigLogDestinationType right) => left.Equals(right);
        public static bool operator !=(LoggingConfigurationLogDestinationConfigLogDestinationType left, LoggingConfigurationLogDestinationConfigLogDestinationType right) => !left.Equals(right);

        public static explicit operator string(LoggingConfigurationLogDestinationConfigLogDestinationType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LoggingConfigurationLogDestinationConfigLogDestinationType other && Equals(other);
        public bool Equals(LoggingConfigurationLogDestinationConfigLogDestinationType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct LoggingConfigurationLogDestinationConfigLogType : IEquatable<LoggingConfigurationLogDestinationConfigLogType>
    {
        private readonly string _value;

        private LoggingConfigurationLogDestinationConfigLogType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static LoggingConfigurationLogDestinationConfigLogType Alert { get; } = new LoggingConfigurationLogDestinationConfigLogType("ALERT");
        public static LoggingConfigurationLogDestinationConfigLogType Flow { get; } = new LoggingConfigurationLogDestinationConfigLogType("FLOW");

        public static bool operator ==(LoggingConfigurationLogDestinationConfigLogType left, LoggingConfigurationLogDestinationConfigLogType right) => left.Equals(right);
        public static bool operator !=(LoggingConfigurationLogDestinationConfigLogType left, LoggingConfigurationLogDestinationConfigLogType right) => !left.Equals(right);

        public static explicit operator string(LoggingConfigurationLogDestinationConfigLogType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is LoggingConfigurationLogDestinationConfigLogType other && Equals(other);
        public bool Equals(LoggingConfigurationLogDestinationConfigLogType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupGeneratedRulesType : IEquatable<RuleGroupGeneratedRulesType>
    {
        private readonly string _value;

        private RuleGroupGeneratedRulesType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupGeneratedRulesType Allowlist { get; } = new RuleGroupGeneratedRulesType("ALLOWLIST");
        public static RuleGroupGeneratedRulesType Denylist { get; } = new RuleGroupGeneratedRulesType("DENYLIST");

        public static bool operator ==(RuleGroupGeneratedRulesType left, RuleGroupGeneratedRulesType right) => left.Equals(right);
        public static bool operator !=(RuleGroupGeneratedRulesType left, RuleGroupGeneratedRulesType right) => !left.Equals(right);

        public static explicit operator string(RuleGroupGeneratedRulesType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupGeneratedRulesType other && Equals(other);
        public bool Equals(RuleGroupGeneratedRulesType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupHeaderDirection : IEquatable<RuleGroupHeaderDirection>
    {
        private readonly string _value;

        private RuleGroupHeaderDirection(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupHeaderDirection Forward { get; } = new RuleGroupHeaderDirection("FORWARD");
        public static RuleGroupHeaderDirection Any { get; } = new RuleGroupHeaderDirection("ANY");

        public static bool operator ==(RuleGroupHeaderDirection left, RuleGroupHeaderDirection right) => left.Equals(right);
        public static bool operator !=(RuleGroupHeaderDirection left, RuleGroupHeaderDirection right) => !left.Equals(right);

        public static explicit operator string(RuleGroupHeaderDirection value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupHeaderDirection other && Equals(other);
        public bool Equals(RuleGroupHeaderDirection other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupHeaderProtocol : IEquatable<RuleGroupHeaderProtocol>
    {
        private readonly string _value;

        private RuleGroupHeaderProtocol(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupHeaderProtocol Ip { get; } = new RuleGroupHeaderProtocol("IP");
        public static RuleGroupHeaderProtocol Tcp { get; } = new RuleGroupHeaderProtocol("TCP");
        public static RuleGroupHeaderProtocol Udp { get; } = new RuleGroupHeaderProtocol("UDP");
        public static RuleGroupHeaderProtocol Icmp { get; } = new RuleGroupHeaderProtocol("ICMP");
        public static RuleGroupHeaderProtocol Http { get; } = new RuleGroupHeaderProtocol("HTTP");
        public static RuleGroupHeaderProtocol Ftp { get; } = new RuleGroupHeaderProtocol("FTP");
        public static RuleGroupHeaderProtocol Tls { get; } = new RuleGroupHeaderProtocol("TLS");
        public static RuleGroupHeaderProtocol Smb { get; } = new RuleGroupHeaderProtocol("SMB");
        public static RuleGroupHeaderProtocol Dns { get; } = new RuleGroupHeaderProtocol("DNS");
        public static RuleGroupHeaderProtocol Dcerpc { get; } = new RuleGroupHeaderProtocol("DCERPC");
        public static RuleGroupHeaderProtocol Ssh { get; } = new RuleGroupHeaderProtocol("SSH");
        public static RuleGroupHeaderProtocol Smtp { get; } = new RuleGroupHeaderProtocol("SMTP");
        public static RuleGroupHeaderProtocol Imap { get; } = new RuleGroupHeaderProtocol("IMAP");
        public static RuleGroupHeaderProtocol Msn { get; } = new RuleGroupHeaderProtocol("MSN");
        public static RuleGroupHeaderProtocol Krb5 { get; } = new RuleGroupHeaderProtocol("KRB5");
        public static RuleGroupHeaderProtocol Ikev2 { get; } = new RuleGroupHeaderProtocol("IKEV2");
        public static RuleGroupHeaderProtocol Tftp { get; } = new RuleGroupHeaderProtocol("TFTP");
        public static RuleGroupHeaderProtocol Ntp { get; } = new RuleGroupHeaderProtocol("NTP");
        public static RuleGroupHeaderProtocol Dhcp { get; } = new RuleGroupHeaderProtocol("DHCP");

        public static bool operator ==(RuleGroupHeaderProtocol left, RuleGroupHeaderProtocol right) => left.Equals(right);
        public static bool operator !=(RuleGroupHeaderProtocol left, RuleGroupHeaderProtocol right) => !left.Equals(right);

        public static explicit operator string(RuleGroupHeaderProtocol value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupHeaderProtocol other && Equals(other);
        public bool Equals(RuleGroupHeaderProtocol other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupRuleOrder : IEquatable<RuleGroupRuleOrder>
    {
        private readonly string _value;

        private RuleGroupRuleOrder(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupRuleOrder DefaultActionOrder { get; } = new RuleGroupRuleOrder("DEFAULT_ACTION_ORDER");
        public static RuleGroupRuleOrder StrictOrder { get; } = new RuleGroupRuleOrder("STRICT_ORDER");

        public static bool operator ==(RuleGroupRuleOrder left, RuleGroupRuleOrder right) => left.Equals(right);
        public static bool operator !=(RuleGroupRuleOrder left, RuleGroupRuleOrder right) => !left.Equals(right);

        public static explicit operator string(RuleGroupRuleOrder value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupRuleOrder other && Equals(other);
        public bool Equals(RuleGroupRuleOrder other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupStatefulRuleAction : IEquatable<RuleGroupStatefulRuleAction>
    {
        private readonly string _value;

        private RuleGroupStatefulRuleAction(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupStatefulRuleAction Pass { get; } = new RuleGroupStatefulRuleAction("PASS");
        public static RuleGroupStatefulRuleAction Drop { get; } = new RuleGroupStatefulRuleAction("DROP");
        public static RuleGroupStatefulRuleAction Alert { get; } = new RuleGroupStatefulRuleAction("ALERT");

        public static bool operator ==(RuleGroupStatefulRuleAction left, RuleGroupStatefulRuleAction right) => left.Equals(right);
        public static bool operator !=(RuleGroupStatefulRuleAction left, RuleGroupStatefulRuleAction right) => !left.Equals(right);

        public static explicit operator string(RuleGroupStatefulRuleAction value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupStatefulRuleAction other && Equals(other);
        public bool Equals(RuleGroupStatefulRuleAction other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupTCPFlag : IEquatable<RuleGroupTCPFlag>
    {
        private readonly string _value;

        private RuleGroupTCPFlag(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupTCPFlag Fin { get; } = new RuleGroupTCPFlag("FIN");
        public static RuleGroupTCPFlag Syn { get; } = new RuleGroupTCPFlag("SYN");
        public static RuleGroupTCPFlag Rst { get; } = new RuleGroupTCPFlag("RST");
        public static RuleGroupTCPFlag Psh { get; } = new RuleGroupTCPFlag("PSH");
        public static RuleGroupTCPFlag Ack { get; } = new RuleGroupTCPFlag("ACK");
        public static RuleGroupTCPFlag Urg { get; } = new RuleGroupTCPFlag("URG");
        public static RuleGroupTCPFlag Ece { get; } = new RuleGroupTCPFlag("ECE");
        public static RuleGroupTCPFlag Cwr { get; } = new RuleGroupTCPFlag("CWR");

        public static bool operator ==(RuleGroupTCPFlag left, RuleGroupTCPFlag right) => left.Equals(right);
        public static bool operator !=(RuleGroupTCPFlag left, RuleGroupTCPFlag right) => !left.Equals(right);

        public static explicit operator string(RuleGroupTCPFlag value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupTCPFlag other && Equals(other);
        public bool Equals(RuleGroupTCPFlag other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupTargetType : IEquatable<RuleGroupTargetType>
    {
        private readonly string _value;

        private RuleGroupTargetType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupTargetType TlsSni { get; } = new RuleGroupTargetType("TLS_SNI");
        public static RuleGroupTargetType HttpHost { get; } = new RuleGroupTargetType("HTTP_HOST");

        public static bool operator ==(RuleGroupTargetType left, RuleGroupTargetType right) => left.Equals(right);
        public static bool operator !=(RuleGroupTargetType left, RuleGroupTargetType right) => !left.Equals(right);

        public static explicit operator string(RuleGroupTargetType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupTargetType other && Equals(other);
        public bool Equals(RuleGroupTargetType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RuleGroupTypeEnum : IEquatable<RuleGroupTypeEnum>
    {
        private readonly string _value;

        private RuleGroupTypeEnum(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleGroupTypeEnum Stateless { get; } = new RuleGroupTypeEnum("STATELESS");
        public static RuleGroupTypeEnum Stateful { get; } = new RuleGroupTypeEnum("STATEFUL");

        public static bool operator ==(RuleGroupTypeEnum left, RuleGroupTypeEnum right) => left.Equals(right);
        public static bool operator !=(RuleGroupTypeEnum left, RuleGroupTypeEnum right) => !left.Equals(right);

        public static explicit operator string(RuleGroupTypeEnum value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleGroupTypeEnum other && Equals(other);
        public bool Equals(RuleGroupTypeEnum other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
