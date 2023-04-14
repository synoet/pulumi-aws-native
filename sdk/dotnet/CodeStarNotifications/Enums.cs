// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.CodeStarNotifications
{
    [EnumType]
    public readonly struct NotificationRuleDetailType : IEquatable<NotificationRuleDetailType>
    {
        private readonly string _value;

        private NotificationRuleDetailType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static NotificationRuleDetailType Basic { get; } = new NotificationRuleDetailType("BASIC");
        public static NotificationRuleDetailType Full { get; } = new NotificationRuleDetailType("FULL");

        public static bool operator ==(NotificationRuleDetailType left, NotificationRuleDetailType right) => left.Equals(right);
        public static bool operator !=(NotificationRuleDetailType left, NotificationRuleDetailType right) => !left.Equals(right);

        public static explicit operator string(NotificationRuleDetailType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is NotificationRuleDetailType other && Equals(other);
        public bool Equals(NotificationRuleDetailType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct NotificationRuleStatus : IEquatable<NotificationRuleStatus>
    {
        private readonly string _value;

        private NotificationRuleStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static NotificationRuleStatus Enabled { get; } = new NotificationRuleStatus("ENABLED");
        public static NotificationRuleStatus Disabled { get; } = new NotificationRuleStatus("DISABLED");

        public static bool operator ==(NotificationRuleStatus left, NotificationRuleStatus right) => left.Equals(right);
        public static bool operator !=(NotificationRuleStatus left, NotificationRuleStatus right) => !left.Equals(right);

        public static explicit operator string(NotificationRuleStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is NotificationRuleStatus other && Equals(other);
        public bool Equals(NotificationRuleStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
