// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.RDS
{
    /// <summary>
    /// The type of authentication that the proxy uses for connections from the proxy to the underlying database. 
    /// </summary>
    [EnumType]
    public readonly struct DBProxyAuthFormatAuthScheme : IEquatable<DBProxyAuthFormatAuthScheme>
    {
        private readonly string _value;

        private DBProxyAuthFormatAuthScheme(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DBProxyAuthFormatAuthScheme Secrets { get; } = new DBProxyAuthFormatAuthScheme("SECRETS");

        public static bool operator ==(DBProxyAuthFormatAuthScheme left, DBProxyAuthFormatAuthScheme right) => left.Equals(right);
        public static bool operator !=(DBProxyAuthFormatAuthScheme left, DBProxyAuthFormatAuthScheme right) => !left.Equals(right);

        public static explicit operator string(DBProxyAuthFormatAuthScheme value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DBProxyAuthFormatAuthScheme other && Equals(other);
        public bool Equals(DBProxyAuthFormatAuthScheme other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// Whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. 
    /// </summary>
    [EnumType]
    public readonly struct DBProxyAuthFormatIAMAuth : IEquatable<DBProxyAuthFormatIAMAuth>
    {
        private readonly string _value;

        private DBProxyAuthFormatIAMAuth(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DBProxyAuthFormatIAMAuth Disabled { get; } = new DBProxyAuthFormatIAMAuth("DISABLED");
        public static DBProxyAuthFormatIAMAuth Required { get; } = new DBProxyAuthFormatIAMAuth("REQUIRED");

        public static bool operator ==(DBProxyAuthFormatIAMAuth left, DBProxyAuthFormatIAMAuth right) => left.Equals(right);
        public static bool operator !=(DBProxyAuthFormatIAMAuth left, DBProxyAuthFormatIAMAuth right) => !left.Equals(right);

        public static explicit operator string(DBProxyAuthFormatIAMAuth value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DBProxyAuthFormatIAMAuth other && Equals(other);
        public bool Equals(DBProxyAuthFormatIAMAuth other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
    /// </summary>
    [EnumType]
    public readonly struct DBProxyEndpointTargetRole : IEquatable<DBProxyEndpointTargetRole>
    {
        private readonly string _value;

        private DBProxyEndpointTargetRole(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DBProxyEndpointTargetRole ReadWrite { get; } = new DBProxyEndpointTargetRole("READ_WRITE");
        public static DBProxyEndpointTargetRole ReadOnly { get; } = new DBProxyEndpointTargetRole("READ_ONLY");

        public static bool operator ==(DBProxyEndpointTargetRole left, DBProxyEndpointTargetRole right) => left.Equals(right);
        public static bool operator !=(DBProxyEndpointTargetRole left, DBProxyEndpointTargetRole right) => !left.Equals(right);

        public static explicit operator string(DBProxyEndpointTargetRole value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DBProxyEndpointTargetRole other && Equals(other);
        public bool Equals(DBProxyEndpointTargetRole other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The kinds of databases that the proxy can connect to.
    /// </summary>
    [EnumType]
    public readonly struct DBProxyEngineFamily : IEquatable<DBProxyEngineFamily>
    {
        private readonly string _value;

        private DBProxyEngineFamily(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DBProxyEngineFamily Mysql { get; } = new DBProxyEngineFamily("MYSQL");
        public static DBProxyEngineFamily Postgresql { get; } = new DBProxyEngineFamily("POSTGRESQL");

        public static bool operator ==(DBProxyEngineFamily left, DBProxyEngineFamily right) => left.Equals(right);
        public static bool operator !=(DBProxyEngineFamily left, DBProxyEngineFamily right) => !left.Equals(right);

        public static explicit operator string(DBProxyEngineFamily value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DBProxyEngineFamily other && Equals(other);
        public bool Equals(DBProxyEngineFamily other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The identifier for the DBProxyTargetGroup
    /// </summary>
    [EnumType]
    public readonly struct DBProxyTargetGroupTargetGroupName : IEquatable<DBProxyTargetGroupTargetGroupName>
    {
        private readonly string _value;

        private DBProxyTargetGroupTargetGroupName(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DBProxyTargetGroupTargetGroupName Default { get; } = new DBProxyTargetGroupTargetGroupName("default");

        public static bool operator ==(DBProxyTargetGroupTargetGroupName left, DBProxyTargetGroupTargetGroupName right) => left.Equals(right);
        public static bool operator !=(DBProxyTargetGroupTargetGroupName left, DBProxyTargetGroupTargetGroupName right) => !left.Equals(right);

        public static explicit operator string(DBProxyTargetGroupTargetGroupName value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DBProxyTargetGroupTargetGroupName other && Equals(other);
        public bool Equals(DBProxyTargetGroupTargetGroupName other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The type of source that will be generating the events. For example, if you want to be notified of events generated by a DB instance, you would set this parameter to db-instance. if this value is not specified, all events are returned.
    /// </summary>
    [EnumType]
    public readonly struct EventSubscriptionSourceType : IEquatable<EventSubscriptionSourceType>
    {
        private readonly string _value;

        private EventSubscriptionSourceType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EventSubscriptionSourceType CustomEngineVersion { get; } = new EventSubscriptionSourceType("custom-engine-version");
        public static EventSubscriptionSourceType DbCluster { get; } = new EventSubscriptionSourceType("db-cluster");
        public static EventSubscriptionSourceType DbClusterSnapshot { get; } = new EventSubscriptionSourceType("db-cluster-snapshot");
        public static EventSubscriptionSourceType DbInstance { get; } = new EventSubscriptionSourceType("db-instance");
        public static EventSubscriptionSourceType DbProxy { get; } = new EventSubscriptionSourceType("db-proxy");
        public static EventSubscriptionSourceType DbParameterGroup { get; } = new EventSubscriptionSourceType("db-parameter-group");
        public static EventSubscriptionSourceType DbSecurityGroup { get; } = new EventSubscriptionSourceType("db-security-group");
        public static EventSubscriptionSourceType DbSnapshot { get; } = new EventSubscriptionSourceType("db-snapshot");

        public static bool operator ==(EventSubscriptionSourceType left, EventSubscriptionSourceType right) => left.Equals(right);
        public static bool operator !=(EventSubscriptionSourceType left, EventSubscriptionSourceType right) => !left.Equals(right);

        public static explicit operator string(EventSubscriptionSourceType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EventSubscriptionSourceType other && Equals(other);
        public bool Equals(EventSubscriptionSourceType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
    /// If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
    /// </summary>
    [EnumType]
    public readonly struct GlobalClusterEngine : IEquatable<GlobalClusterEngine>
    {
        private readonly string _value;

        private GlobalClusterEngine(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static GlobalClusterEngine Aurora { get; } = new GlobalClusterEngine("aurora");
        public static GlobalClusterEngine AuroraMysql { get; } = new GlobalClusterEngine("aurora-mysql");
        public static GlobalClusterEngine AuroraPostgresql { get; } = new GlobalClusterEngine("aurora-postgresql");

        public static bool operator ==(GlobalClusterEngine left, GlobalClusterEngine right) => left.Equals(right);
        public static bool operator !=(GlobalClusterEngine left, GlobalClusterEngine right) => !left.Equals(right);

        public static explicit operator string(GlobalClusterEngine value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is GlobalClusterEngine other && Equals(other);
        public bool Equals(GlobalClusterEngine other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
