// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.Events
{
    [EnumType]
    public readonly struct ApiDestinationHttpMethod : IEquatable<ApiDestinationHttpMethod>
    {
        private readonly string _value;

        private ApiDestinationHttpMethod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ApiDestinationHttpMethod Get { get; } = new ApiDestinationHttpMethod("GET");
        public static ApiDestinationHttpMethod Head { get; } = new ApiDestinationHttpMethod("HEAD");
        public static ApiDestinationHttpMethod Post { get; } = new ApiDestinationHttpMethod("POST");
        public static ApiDestinationHttpMethod Options { get; } = new ApiDestinationHttpMethod("OPTIONS");
        public static ApiDestinationHttpMethod Put { get; } = new ApiDestinationHttpMethod("PUT");
        public static ApiDestinationHttpMethod Delete { get; } = new ApiDestinationHttpMethod("DELETE");
        public static ApiDestinationHttpMethod Patch { get; } = new ApiDestinationHttpMethod("PATCH");

        public static bool operator ==(ApiDestinationHttpMethod left, ApiDestinationHttpMethod right) => left.Equals(right);
        public static bool operator !=(ApiDestinationHttpMethod left, ApiDestinationHttpMethod right) => !left.Equals(right);

        public static explicit operator string(ApiDestinationHttpMethod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ApiDestinationHttpMethod other && Equals(other);
        public bool Equals(ApiDestinationHttpMethod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConnectionAuthorizationType : IEquatable<ConnectionAuthorizationType>
    {
        private readonly string _value;

        private ConnectionAuthorizationType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectionAuthorizationType ApiKey { get; } = new ConnectionAuthorizationType("API_KEY");
        public static ConnectionAuthorizationType Basic { get; } = new ConnectionAuthorizationType("BASIC");
        public static ConnectionAuthorizationType OauthClientCredentials { get; } = new ConnectionAuthorizationType("OAUTH_CLIENT_CREDENTIALS");

        public static bool operator ==(ConnectionAuthorizationType left, ConnectionAuthorizationType right) => left.Equals(right);
        public static bool operator !=(ConnectionAuthorizationType left, ConnectionAuthorizationType right) => !left.Equals(right);

        public static explicit operator string(ConnectionAuthorizationType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectionAuthorizationType other && Equals(other);
        public bool Equals(ConnectionAuthorizationType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ConnectionOAuthParametersHttpMethod : IEquatable<ConnectionOAuthParametersHttpMethod>
    {
        private readonly string _value;

        private ConnectionOAuthParametersHttpMethod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ConnectionOAuthParametersHttpMethod Get { get; } = new ConnectionOAuthParametersHttpMethod("GET");
        public static ConnectionOAuthParametersHttpMethod Post { get; } = new ConnectionOAuthParametersHttpMethod("POST");
        public static ConnectionOAuthParametersHttpMethod Put { get; } = new ConnectionOAuthParametersHttpMethod("PUT");

        public static bool operator ==(ConnectionOAuthParametersHttpMethod left, ConnectionOAuthParametersHttpMethod right) => left.Equals(right);
        public static bool operator !=(ConnectionOAuthParametersHttpMethod left, ConnectionOAuthParametersHttpMethod right) => !left.Equals(right);

        public static explicit operator string(ConnectionOAuthParametersHttpMethod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ConnectionOAuthParametersHttpMethod other && Equals(other);
        public bool Equals(ConnectionOAuthParametersHttpMethod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EndpointReplicationState : IEquatable<EndpointReplicationState>
    {
        private readonly string _value;

        private EndpointReplicationState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EndpointReplicationState Enabled { get; } = new EndpointReplicationState("ENABLED");
        public static EndpointReplicationState Disabled { get; } = new EndpointReplicationState("DISABLED");

        public static bool operator ==(EndpointReplicationState left, EndpointReplicationState right) => left.Equals(right);
        public static bool operator !=(EndpointReplicationState left, EndpointReplicationState right) => !left.Equals(right);

        public static explicit operator string(EndpointReplicationState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EndpointReplicationState other && Equals(other);
        public bool Equals(EndpointReplicationState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EndpointState : IEquatable<EndpointState>
    {
        private readonly string _value;

        private EndpointState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EndpointState Active { get; } = new EndpointState("ACTIVE");
        public static EndpointState Creating { get; } = new EndpointState("CREATING");
        public static EndpointState Updating { get; } = new EndpointState("UPDATING");
        public static EndpointState Deleting { get; } = new EndpointState("DELETING");
        public static EndpointState CreateFailed { get; } = new EndpointState("CREATE_FAILED");
        public static EndpointState UpdateFailed { get; } = new EndpointState("UPDATE_FAILED");

        public static bool operator ==(EndpointState left, EndpointState right) => left.Equals(right);
        public static bool operator !=(EndpointState left, EndpointState right) => !left.Equals(right);

        public static explicit operator string(EndpointState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EndpointState other && Equals(other);
        public bool Equals(EndpointState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The state of the rule.
    /// </summary>
    [EnumType]
    public readonly struct RuleState : IEquatable<RuleState>
    {
        private readonly string _value;

        private RuleState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RuleState Disabled { get; } = new RuleState("DISABLED");
        public static RuleState Enabled { get; } = new RuleState("ENABLED");
        public static RuleState EnabledWithAllCloudtrailManagementEvents { get; } = new RuleState("ENABLED_WITH_ALL_CLOUDTRAIL_MANAGEMENT_EVENTS");

        public static bool operator ==(RuleState left, RuleState right) => left.Equals(right);
        public static bool operator !=(RuleState left, RuleState right) => !left.Equals(right);

        public static explicit operator string(RuleState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RuleState other && Equals(other);
        public bool Equals(RuleState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
