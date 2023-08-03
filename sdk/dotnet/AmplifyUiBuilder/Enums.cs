// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.AmplifyUiBuilder
{
    [EnumType]
    public readonly struct FormActionType : IEquatable<FormActionType>
    {
        private readonly string _value;

        private FormActionType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FormActionType Create { get; } = new FormActionType("create");
        public static FormActionType Update { get; } = new FormActionType("update");

        public static bool operator ==(FormActionType left, FormActionType right) => left.Equals(right);
        public static bool operator !=(FormActionType left, FormActionType right) => !left.Equals(right);

        public static explicit operator string(FormActionType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FormActionType other && Equals(other);
        public bool Equals(FormActionType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FormButtonsPosition : IEquatable<FormButtonsPosition>
    {
        private readonly string _value;

        private FormButtonsPosition(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FormButtonsPosition Top { get; } = new FormButtonsPosition("top");
        public static FormButtonsPosition Bottom { get; } = new FormButtonsPosition("bottom");
        public static FormButtonsPosition TopAndBottom { get; } = new FormButtonsPosition("top_and_bottom");

        public static bool operator ==(FormButtonsPosition left, FormButtonsPosition right) => left.Equals(right);
        public static bool operator !=(FormButtonsPosition left, FormButtonsPosition right) => !left.Equals(right);

        public static explicit operator string(FormButtonsPosition value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FormButtonsPosition other && Equals(other);
        public bool Equals(FormButtonsPosition other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FormDataSourceType : IEquatable<FormDataSourceType>
    {
        private readonly string _value;

        private FormDataSourceType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FormDataSourceType DataStore { get; } = new FormDataSourceType("DataStore");
        public static FormDataSourceType Custom { get; } = new FormDataSourceType("Custom");

        public static bool operator ==(FormDataSourceType left, FormDataSourceType right) => left.Equals(right);
        public static bool operator !=(FormDataSourceType left, FormDataSourceType right) => !left.Equals(right);

        public static explicit operator string(FormDataSourceType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FormDataSourceType other && Equals(other);
        public bool Equals(FormDataSourceType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FormFixedPosition : IEquatable<FormFixedPosition>
    {
        private readonly string _value;

        private FormFixedPosition(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FormFixedPosition First { get; } = new FormFixedPosition("first");

        public static bool operator ==(FormFixedPosition left, FormFixedPosition right) => left.Equals(right);
        public static bool operator !=(FormFixedPosition left, FormFixedPosition right) => !left.Equals(right);

        public static explicit operator string(FormFixedPosition value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FormFixedPosition other && Equals(other);
        public bool Equals(FormFixedPosition other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct FormLabelDecorator : IEquatable<FormLabelDecorator>
    {
        private readonly string _value;

        private FormLabelDecorator(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static FormLabelDecorator Required { get; } = new FormLabelDecorator("required");
        public static FormLabelDecorator Optional { get; } = new FormLabelDecorator("optional");
        public static FormLabelDecorator None { get; } = new FormLabelDecorator("none");

        public static bool operator ==(FormLabelDecorator left, FormLabelDecorator right) => left.Equals(right);
        public static bool operator !=(FormLabelDecorator left, FormLabelDecorator right) => !left.Equals(right);

        public static explicit operator string(FormLabelDecorator value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is FormLabelDecorator other && Equals(other);
        public bool Equals(FormLabelDecorator other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
