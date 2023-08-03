// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.SsmIncidents
{
    /// <summary>
    /// The account type to use when starting the SSM automation document.
    /// </summary>
    [EnumType]
    public readonly struct ResponsePlanSsmAutomationTargetAccount : IEquatable<ResponsePlanSsmAutomationTargetAccount>
    {
        private readonly string _value;

        private ResponsePlanSsmAutomationTargetAccount(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResponsePlanSsmAutomationTargetAccount ImpactedAccount { get; } = new ResponsePlanSsmAutomationTargetAccount("IMPACTED_ACCOUNT");
        public static ResponsePlanSsmAutomationTargetAccount ResponsePlanOwnerAccount { get; } = new ResponsePlanSsmAutomationTargetAccount("RESPONSE_PLAN_OWNER_ACCOUNT");

        public static bool operator ==(ResponsePlanSsmAutomationTargetAccount left, ResponsePlanSsmAutomationTargetAccount right) => left.Equals(right);
        public static bool operator !=(ResponsePlanSsmAutomationTargetAccount left, ResponsePlanSsmAutomationTargetAccount right) => !left.Equals(right);

        public static explicit operator string(ResponsePlanSsmAutomationTargetAccount value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResponsePlanSsmAutomationTargetAccount other && Equals(other);
        public bool Equals(ResponsePlanSsmAutomationTargetAccount other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The variable types used as dynamic parameter value when starting the SSM automation document.
    /// </summary>
    [EnumType]
    public readonly struct ResponsePlanVariableType : IEquatable<ResponsePlanVariableType>
    {
        private readonly string _value;

        private ResponsePlanVariableType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static ResponsePlanVariableType IncidentRecordArn { get; } = new ResponsePlanVariableType("INCIDENT_RECORD_ARN");
        public static ResponsePlanVariableType InvolvedResources { get; } = new ResponsePlanVariableType("INVOLVED_RESOURCES");

        public static bool operator ==(ResponsePlanVariableType left, ResponsePlanVariableType right) => left.Equals(right);
        public static bool operator !=(ResponsePlanVariableType left, ResponsePlanVariableType right) => !left.Equals(right);

        public static explicit operator string(ResponsePlanVariableType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is ResponsePlanVariableType other && Equals(other);
        public bool Equals(ResponsePlanVariableType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
