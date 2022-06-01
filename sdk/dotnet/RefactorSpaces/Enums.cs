// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.RefactorSpaces
{
    [EnumType]
    public readonly struct ApplicationApiGatewayEndpointType : IEquatable<ApplicationApiGatewayEndpointType>
    {
        private readonly string _value;

        private ApplicationApiGatewayEndpointType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ApplicationApiGatewayEndpointType Regional { get; } = new ApplicationApiGatewayEndpointType("REGIONAL");
        public static ApplicationApiGatewayEndpointType Private { get; } = new ApplicationApiGatewayEndpointType("PRIVATE");

        public static bool operator ==(ApplicationApiGatewayEndpointType left, ApplicationApiGatewayEndpointType right) => left.Equals(right);
        public static bool operator !=(ApplicationApiGatewayEndpointType left, ApplicationApiGatewayEndpointType right) => !left.Equals(right);

        public static explicit operator string(ApplicationApiGatewayEndpointType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ApplicationApiGatewayEndpointType other && Equals(other);
        public bool Equals(ApplicationApiGatewayEndpointType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ApplicationProxyType : IEquatable<ApplicationProxyType>
    {
        private readonly string _value;

        private ApplicationProxyType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ApplicationProxyType ApiGateway { get; } = new ApplicationProxyType("API_GATEWAY");

        public static bool operator ==(ApplicationProxyType left, ApplicationProxyType right) => left.Equals(right);
        public static bool operator !=(ApplicationProxyType left, ApplicationProxyType right) => !left.Equals(right);

        public static explicit operator string(ApplicationProxyType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ApplicationProxyType other && Equals(other);
        public bool Equals(ApplicationProxyType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EnvironmentNetworkFabricType : IEquatable<EnvironmentNetworkFabricType>
    {
        private readonly string _value;

        private EnvironmentNetworkFabricType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EnvironmentNetworkFabricType TransitGateway { get; } = new EnvironmentNetworkFabricType("TRANSIT_GATEWAY");

        public static bool operator ==(EnvironmentNetworkFabricType left, EnvironmentNetworkFabricType right) => left.Equals(right);
        public static bool operator !=(EnvironmentNetworkFabricType left, EnvironmentNetworkFabricType right) => !left.Equals(right);

        public static explicit operator string(EnvironmentNetworkFabricType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EnvironmentNetworkFabricType other && Equals(other);
        public bool Equals(EnvironmentNetworkFabricType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RouteActivationState : IEquatable<RouteActivationState>
    {
        private readonly string _value;

        private RouteActivationState(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RouteActivationState Inactive { get; } = new RouteActivationState("INACTIVE");
        public static RouteActivationState Active { get; } = new RouteActivationState("ACTIVE");

        public static bool operator ==(RouteActivationState left, RouteActivationState right) => left.Equals(right);
        public static bool operator !=(RouteActivationState left, RouteActivationState right) => !left.Equals(right);

        public static explicit operator string(RouteActivationState value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RouteActivationState other && Equals(other);
        public bool Equals(RouteActivationState other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RouteMethod : IEquatable<RouteMethod>
    {
        private readonly string _value;

        private RouteMethod(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RouteMethod Delete { get; } = new RouteMethod("DELETE");
        public static RouteMethod Get { get; } = new RouteMethod("GET");
        public static RouteMethod Head { get; } = new RouteMethod("HEAD");
        public static RouteMethod Options { get; } = new RouteMethod("OPTIONS");
        public static RouteMethod Patch { get; } = new RouteMethod("PATCH");
        public static RouteMethod Post { get; } = new RouteMethod("POST");
        public static RouteMethod Put { get; } = new RouteMethod("PUT");

        public static bool operator ==(RouteMethod left, RouteMethod right) => left.Equals(right);
        public static bool operator !=(RouteMethod left, RouteMethod right) => !left.Equals(right);

        public static explicit operator string(RouteMethod value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RouteMethod other && Equals(other);
        public bool Equals(RouteMethod other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct RouteType : IEquatable<RouteType>
    {
        private readonly string _value;

        private RouteType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static RouteType Default { get; } = new RouteType("DEFAULT");
        public static RouteType UriPath { get; } = new RouteType("URI_PATH");

        public static bool operator ==(RouteType left, RouteType right) => left.Equals(right);
        public static bool operator !=(RouteType left, RouteType right) => !left.Equals(right);

        public static explicit operator string(RouteType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is RouteType other && Equals(other);
        public bool Equals(RouteType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct ServiceEndpointType : IEquatable<ServiceEndpointType>
    {
        private readonly string _value;

        private ServiceEndpointType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ServiceEndpointType Lambda { get; } = new ServiceEndpointType("LAMBDA");
        public static ServiceEndpointType Url { get; } = new ServiceEndpointType("URL");

        public static bool operator ==(ServiceEndpointType left, ServiceEndpointType right) => left.Equals(right);
        public static bool operator !=(ServiceEndpointType left, ServiceEndpointType right) => !left.Equals(right);

        public static explicit operator string(ServiceEndpointType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ServiceEndpointType other && Equals(other);
        public bool Equals(ServiceEndpointType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
