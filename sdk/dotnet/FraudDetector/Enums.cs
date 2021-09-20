// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.ComponentModel;
using Pulumi;

namespace Pulumi.AwsNative.FraudDetector
{
    /// <summary>
    /// The desired detector version status for the detector
    /// </summary>
    [EnumType]
    public readonly struct DetectorDetectorVersionStatus : IEquatable<DetectorDetectorVersionStatus>
    {
        private readonly string _value;

        private DetectorDetectorVersionStatus(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorDetectorVersionStatus Draft { get; } = new DetectorDetectorVersionStatus("DRAFT");
        public static DetectorDetectorVersionStatus Active { get; } = new DetectorDetectorVersionStatus("ACTIVE");

        public static bool operator ==(DetectorDetectorVersionStatus left, DetectorDetectorVersionStatus right) => left.Equals(right);
        public static bool operator !=(DetectorDetectorVersionStatus left, DetectorDetectorVersionStatus right) => !left.Equals(right);

        public static explicit operator string(DetectorDetectorVersionStatus value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorDetectorVersionStatus other && Equals(other);
        public bool Equals(DetectorDetectorVersionStatus other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DetectorEventVariableDataSource : IEquatable<DetectorEventVariableDataSource>
    {
        private readonly string _value;

        private DetectorEventVariableDataSource(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorEventVariableDataSource Event { get; } = new DetectorEventVariableDataSource("EVENT");

        public static bool operator ==(DetectorEventVariableDataSource left, DetectorEventVariableDataSource right) => left.Equals(right);
        public static bool operator !=(DetectorEventVariableDataSource left, DetectorEventVariableDataSource right) => !left.Equals(right);

        public static explicit operator string(DetectorEventVariableDataSource value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorEventVariableDataSource other && Equals(other);
        public bool Equals(DetectorEventVariableDataSource other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DetectorEventVariableDataType : IEquatable<DetectorEventVariableDataType>
    {
        private readonly string _value;

        private DetectorEventVariableDataType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorEventVariableDataType String { get; } = new DetectorEventVariableDataType("STRING");
        public static DetectorEventVariableDataType Integer { get; } = new DetectorEventVariableDataType("INTEGER");
        public static DetectorEventVariableDataType Float { get; } = new DetectorEventVariableDataType("FLOAT");
        public static DetectorEventVariableDataType Boolean { get; } = new DetectorEventVariableDataType("BOOLEAN");

        public static bool operator ==(DetectorEventVariableDataType left, DetectorEventVariableDataType right) => left.Equals(right);
        public static bool operator !=(DetectorEventVariableDataType left, DetectorEventVariableDataType right) => !left.Equals(right);

        public static explicit operator string(DetectorEventVariableDataType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorEventVariableDataType other && Equals(other);
        public bool Equals(DetectorEventVariableDataType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DetectorEventVariableVariableType : IEquatable<DetectorEventVariableVariableType>
    {
        private readonly string _value;

        private DetectorEventVariableVariableType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorEventVariableVariableType AuthCode { get; } = new DetectorEventVariableVariableType("AUTH_CODE");
        public static DetectorEventVariableVariableType Avs { get; } = new DetectorEventVariableVariableType("AVS");
        public static DetectorEventVariableVariableType BillingAddressL1 { get; } = new DetectorEventVariableVariableType("BILLING_ADDRESS_L1");
        public static DetectorEventVariableVariableType BillingAddressL2 { get; } = new DetectorEventVariableVariableType("BILLING_ADDRESS_L2");
        public static DetectorEventVariableVariableType BillingCity { get; } = new DetectorEventVariableVariableType("BILLING_CITY");
        public static DetectorEventVariableVariableType BillingCountry { get; } = new DetectorEventVariableVariableType("BILLING_COUNTRY");
        public static DetectorEventVariableVariableType BillingName { get; } = new DetectorEventVariableVariableType("BILLING_NAME");
        public static DetectorEventVariableVariableType BillingPhone { get; } = new DetectorEventVariableVariableType("BILLING_PHONE");
        public static DetectorEventVariableVariableType BillingState { get; } = new DetectorEventVariableVariableType("BILLING_STATE");
        public static DetectorEventVariableVariableType BillingZip { get; } = new DetectorEventVariableVariableType("BILLING_ZIP");
        public static DetectorEventVariableVariableType CardBin { get; } = new DetectorEventVariableVariableType("CARD_BIN");
        public static DetectorEventVariableVariableType Categorical { get; } = new DetectorEventVariableVariableType("CATEGORICAL");
        public static DetectorEventVariableVariableType CurrencyCode { get; } = new DetectorEventVariableVariableType("CURRENCY_CODE");
        public static DetectorEventVariableVariableType EmailAddress { get; } = new DetectorEventVariableVariableType("EMAIL_ADDRESS");
        public static DetectorEventVariableVariableType Fingerprint { get; } = new DetectorEventVariableVariableType("FINGERPRINT");
        public static DetectorEventVariableVariableType FraudLabel { get; } = new DetectorEventVariableVariableType("FRAUD_LABEL");
        public static DetectorEventVariableVariableType FreeFormText { get; } = new DetectorEventVariableVariableType("FREE_FORM_TEXT");
        public static DetectorEventVariableVariableType IpAddress { get; } = new DetectorEventVariableVariableType("IP_ADDRESS");
        public static DetectorEventVariableVariableType Numeric { get; } = new DetectorEventVariableVariableType("NUMERIC");
        public static DetectorEventVariableVariableType OrderId { get; } = new DetectorEventVariableVariableType("ORDER_ID");
        public static DetectorEventVariableVariableType PaymentType { get; } = new DetectorEventVariableVariableType("PAYMENT_TYPE");
        public static DetectorEventVariableVariableType PhoneNumber { get; } = new DetectorEventVariableVariableType("PHONE_NUMBER");
        public static DetectorEventVariableVariableType Price { get; } = new DetectorEventVariableVariableType("PRICE");
        public static DetectorEventVariableVariableType ProductCategory { get; } = new DetectorEventVariableVariableType("PRODUCT_CATEGORY");
        public static DetectorEventVariableVariableType ShippingAddressL1 { get; } = new DetectorEventVariableVariableType("SHIPPING_ADDRESS_L1");
        public static DetectorEventVariableVariableType ShippingAddressL2 { get; } = new DetectorEventVariableVariableType("SHIPPING_ADDRESS_L2");
        public static DetectorEventVariableVariableType ShippingCity { get; } = new DetectorEventVariableVariableType("SHIPPING_CITY");
        public static DetectorEventVariableVariableType ShippingCountry { get; } = new DetectorEventVariableVariableType("SHIPPING_COUNTRY");
        public static DetectorEventVariableVariableType ShippingName { get; } = new DetectorEventVariableVariableType("SHIPPING_NAME");
        public static DetectorEventVariableVariableType ShippingPhone { get; } = new DetectorEventVariableVariableType("SHIPPING_PHONE");
        public static DetectorEventVariableVariableType ShippingState { get; } = new DetectorEventVariableVariableType("SHIPPING_STATE");
        public static DetectorEventVariableVariableType ShippingZip { get; } = new DetectorEventVariableVariableType("SHIPPING_ZIP");
        public static DetectorEventVariableVariableType Useragent { get; } = new DetectorEventVariableVariableType("USERAGENT");

        public static bool operator ==(DetectorEventVariableVariableType left, DetectorEventVariableVariableType right) => left.Equals(right);
        public static bool operator !=(DetectorEventVariableVariableType left, DetectorEventVariableVariableType right) => !left.Equals(right);

        public static explicit operator string(DetectorEventVariableVariableType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorEventVariableVariableType other && Equals(other);
        public bool Equals(DetectorEventVariableVariableType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DetectorRuleExecutionMode : IEquatable<DetectorRuleExecutionMode>
    {
        private readonly string _value;

        private DetectorRuleExecutionMode(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorRuleExecutionMode FirstMatched { get; } = new DetectorRuleExecutionMode("FIRST_MATCHED");
        public static DetectorRuleExecutionMode AllMatched { get; } = new DetectorRuleExecutionMode("ALL_MATCHED");

        public static bool operator ==(DetectorRuleExecutionMode left, DetectorRuleExecutionMode right) => left.Equals(right);
        public static bool operator !=(DetectorRuleExecutionMode left, DetectorRuleExecutionMode right) => !left.Equals(right);

        public static explicit operator string(DetectorRuleExecutionMode value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorRuleExecutionMode other && Equals(other);
        public bool Equals(DetectorRuleExecutionMode other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct DetectorRuleLanguage : IEquatable<DetectorRuleLanguage>
    {
        private readonly string _value;

        private DetectorRuleLanguage(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static DetectorRuleLanguage Detectorpl { get; } = new DetectorRuleLanguage("DETECTORPL");

        public static bool operator ==(DetectorRuleLanguage left, DetectorRuleLanguage right) => left.Equals(right);
        public static bool operator !=(DetectorRuleLanguage left, DetectorRuleLanguage right) => !left.Equals(right);

        public static explicit operator string(DetectorRuleLanguage value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is DetectorRuleLanguage other && Equals(other);
        public bool Equals(DetectorRuleLanguage other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EventTypeEventVariableDataSource : IEquatable<EventTypeEventVariableDataSource>
    {
        private readonly string _value;

        private EventTypeEventVariableDataSource(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EventTypeEventVariableDataSource Event { get; } = new EventTypeEventVariableDataSource("EVENT");

        public static bool operator ==(EventTypeEventVariableDataSource left, EventTypeEventVariableDataSource right) => left.Equals(right);
        public static bool operator !=(EventTypeEventVariableDataSource left, EventTypeEventVariableDataSource right) => !left.Equals(right);

        public static explicit operator string(EventTypeEventVariableDataSource value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EventTypeEventVariableDataSource other && Equals(other);
        public bool Equals(EventTypeEventVariableDataSource other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EventTypeEventVariableDataType : IEquatable<EventTypeEventVariableDataType>
    {
        private readonly string _value;

        private EventTypeEventVariableDataType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EventTypeEventVariableDataType String { get; } = new EventTypeEventVariableDataType("STRING");
        public static EventTypeEventVariableDataType Integer { get; } = new EventTypeEventVariableDataType("INTEGER");
        public static EventTypeEventVariableDataType Float { get; } = new EventTypeEventVariableDataType("FLOAT");
        public static EventTypeEventVariableDataType Boolean { get; } = new EventTypeEventVariableDataType("BOOLEAN");

        public static bool operator ==(EventTypeEventVariableDataType left, EventTypeEventVariableDataType right) => left.Equals(right);
        public static bool operator !=(EventTypeEventVariableDataType left, EventTypeEventVariableDataType right) => !left.Equals(right);

        public static explicit operator string(EventTypeEventVariableDataType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EventTypeEventVariableDataType other && Equals(other);
        public bool Equals(EventTypeEventVariableDataType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    [EnumType]
    public readonly struct EventTypeEventVariableVariableType : IEquatable<EventTypeEventVariableVariableType>
    {
        private readonly string _value;

        private EventTypeEventVariableVariableType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static EventTypeEventVariableVariableType AuthCode { get; } = new EventTypeEventVariableVariableType("AUTH_CODE");
        public static EventTypeEventVariableVariableType Avs { get; } = new EventTypeEventVariableVariableType("AVS");
        public static EventTypeEventVariableVariableType BillingAddressL1 { get; } = new EventTypeEventVariableVariableType("BILLING_ADDRESS_L1");
        public static EventTypeEventVariableVariableType BillingAddressL2 { get; } = new EventTypeEventVariableVariableType("BILLING_ADDRESS_L2");
        public static EventTypeEventVariableVariableType BillingCity { get; } = new EventTypeEventVariableVariableType("BILLING_CITY");
        public static EventTypeEventVariableVariableType BillingCountry { get; } = new EventTypeEventVariableVariableType("BILLING_COUNTRY");
        public static EventTypeEventVariableVariableType BillingName { get; } = new EventTypeEventVariableVariableType("BILLING_NAME");
        public static EventTypeEventVariableVariableType BillingPhone { get; } = new EventTypeEventVariableVariableType("BILLING_PHONE");
        public static EventTypeEventVariableVariableType BillingState { get; } = new EventTypeEventVariableVariableType("BILLING_STATE");
        public static EventTypeEventVariableVariableType BillingZip { get; } = new EventTypeEventVariableVariableType("BILLING_ZIP");
        public static EventTypeEventVariableVariableType CardBin { get; } = new EventTypeEventVariableVariableType("CARD_BIN");
        public static EventTypeEventVariableVariableType Categorical { get; } = new EventTypeEventVariableVariableType("CATEGORICAL");
        public static EventTypeEventVariableVariableType CurrencyCode { get; } = new EventTypeEventVariableVariableType("CURRENCY_CODE");
        public static EventTypeEventVariableVariableType EmailAddress { get; } = new EventTypeEventVariableVariableType("EMAIL_ADDRESS");
        public static EventTypeEventVariableVariableType Fingerprint { get; } = new EventTypeEventVariableVariableType("FINGERPRINT");
        public static EventTypeEventVariableVariableType FraudLabel { get; } = new EventTypeEventVariableVariableType("FRAUD_LABEL");
        public static EventTypeEventVariableVariableType FreeFormText { get; } = new EventTypeEventVariableVariableType("FREE_FORM_TEXT");
        public static EventTypeEventVariableVariableType IpAddress { get; } = new EventTypeEventVariableVariableType("IP_ADDRESS");
        public static EventTypeEventVariableVariableType Numeric { get; } = new EventTypeEventVariableVariableType("NUMERIC");
        public static EventTypeEventVariableVariableType OrderId { get; } = new EventTypeEventVariableVariableType("ORDER_ID");
        public static EventTypeEventVariableVariableType PaymentType { get; } = new EventTypeEventVariableVariableType("PAYMENT_TYPE");
        public static EventTypeEventVariableVariableType PhoneNumber { get; } = new EventTypeEventVariableVariableType("PHONE_NUMBER");
        public static EventTypeEventVariableVariableType Price { get; } = new EventTypeEventVariableVariableType("PRICE");
        public static EventTypeEventVariableVariableType ProductCategory { get; } = new EventTypeEventVariableVariableType("PRODUCT_CATEGORY");
        public static EventTypeEventVariableVariableType ShippingAddressL1 { get; } = new EventTypeEventVariableVariableType("SHIPPING_ADDRESS_L1");
        public static EventTypeEventVariableVariableType ShippingAddressL2 { get; } = new EventTypeEventVariableVariableType("SHIPPING_ADDRESS_L2");
        public static EventTypeEventVariableVariableType ShippingCity { get; } = new EventTypeEventVariableVariableType("SHIPPING_CITY");
        public static EventTypeEventVariableVariableType ShippingCountry { get; } = new EventTypeEventVariableVariableType("SHIPPING_COUNTRY");
        public static EventTypeEventVariableVariableType ShippingName { get; } = new EventTypeEventVariableVariableType("SHIPPING_NAME");
        public static EventTypeEventVariableVariableType ShippingPhone { get; } = new EventTypeEventVariableVariableType("SHIPPING_PHONE");
        public static EventTypeEventVariableVariableType ShippingState { get; } = new EventTypeEventVariableVariableType("SHIPPING_STATE");
        public static EventTypeEventVariableVariableType ShippingZip { get; } = new EventTypeEventVariableVariableType("SHIPPING_ZIP");
        public static EventTypeEventVariableVariableType Useragent { get; } = new EventTypeEventVariableVariableType("USERAGENT");

        public static bool operator ==(EventTypeEventVariableVariableType left, EventTypeEventVariableVariableType right) => left.Equals(right);
        public static bool operator !=(EventTypeEventVariableVariableType left, EventTypeEventVariableVariableType right) => !left.Equals(right);

        public static explicit operator string(EventTypeEventVariableVariableType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is EventTypeEventVariableVariableType other && Equals(other);
        public bool Equals(EventTypeEventVariableVariableType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The source of the data.
    /// </summary>
    [EnumType]
    public readonly struct VariableDataSource : IEquatable<VariableDataSource>
    {
        private readonly string _value;

        private VariableDataSource(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static VariableDataSource Event { get; } = new VariableDataSource("EVENT");
        public static VariableDataSource ExternalModelScore { get; } = new VariableDataSource("EXTERNAL_MODEL_SCORE");

        public static bool operator ==(VariableDataSource left, VariableDataSource right) => left.Equals(right);
        public static bool operator !=(VariableDataSource left, VariableDataSource right) => !left.Equals(right);

        public static explicit operator string(VariableDataSource value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is VariableDataSource other && Equals(other);
        public bool Equals(VariableDataSource other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The data type.
    /// </summary>
    [EnumType]
    public readonly struct VariableDataType : IEquatable<VariableDataType>
    {
        private readonly string _value;

        private VariableDataType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static VariableDataType String { get; } = new VariableDataType("STRING");
        public static VariableDataType Integer { get; } = new VariableDataType("INTEGER");
        public static VariableDataType Float { get; } = new VariableDataType("FLOAT");
        public static VariableDataType Boolean { get; } = new VariableDataType("BOOLEAN");

        public static bool operator ==(VariableDataType left, VariableDataType right) => left.Equals(right);
        public static bool operator !=(VariableDataType left, VariableDataType right) => !left.Equals(right);

        public static explicit operator string(VariableDataType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is VariableDataType other && Equals(other);
        public bool Equals(VariableDataType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }

    /// <summary>
    /// The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
    /// </summary>
    [EnumType]
    public readonly struct VariableVariableType : IEquatable<VariableVariableType>
    {
        private readonly string _value;

        private VariableVariableType(string value)
        {
            _value = value ?? throw new ArgumentNullException(nameof(value));
        }

        public static VariableVariableType AuthCode { get; } = new VariableVariableType("AUTH_CODE");
        public static VariableVariableType Avs { get; } = new VariableVariableType("AVS");
        public static VariableVariableType BillingAddressL1 { get; } = new VariableVariableType("BILLING_ADDRESS_L1");
        public static VariableVariableType BillingAddressL2 { get; } = new VariableVariableType("BILLING_ADDRESS_L2");
        public static VariableVariableType BillingCity { get; } = new VariableVariableType("BILLING_CITY");
        public static VariableVariableType BillingCountry { get; } = new VariableVariableType("BILLING_COUNTRY");
        public static VariableVariableType BillingName { get; } = new VariableVariableType("BILLING_NAME");
        public static VariableVariableType BillingPhone { get; } = new VariableVariableType("BILLING_PHONE");
        public static VariableVariableType BillingState { get; } = new VariableVariableType("BILLING_STATE");
        public static VariableVariableType BillingZip { get; } = new VariableVariableType("BILLING_ZIP");
        public static VariableVariableType CardBin { get; } = new VariableVariableType("CARD_BIN");
        public static VariableVariableType Categorical { get; } = new VariableVariableType("CATEGORICAL");
        public static VariableVariableType CurrencyCode { get; } = new VariableVariableType("CURRENCY_CODE");
        public static VariableVariableType EmailAddress { get; } = new VariableVariableType("EMAIL_ADDRESS");
        public static VariableVariableType Fingerprint { get; } = new VariableVariableType("FINGERPRINT");
        public static VariableVariableType FraudLabel { get; } = new VariableVariableType("FRAUD_LABEL");
        public static VariableVariableType FreeFormText { get; } = new VariableVariableType("FREE_FORM_TEXT");
        public static VariableVariableType IpAddress { get; } = new VariableVariableType("IP_ADDRESS");
        public static VariableVariableType Numeric { get; } = new VariableVariableType("NUMERIC");
        public static VariableVariableType OrderId { get; } = new VariableVariableType("ORDER_ID");
        public static VariableVariableType PaymentType { get; } = new VariableVariableType("PAYMENT_TYPE");
        public static VariableVariableType PhoneNumber { get; } = new VariableVariableType("PHONE_NUMBER");
        public static VariableVariableType Price { get; } = new VariableVariableType("PRICE");
        public static VariableVariableType ProductCategory { get; } = new VariableVariableType("PRODUCT_CATEGORY");
        public static VariableVariableType ShippingAddressL1 { get; } = new VariableVariableType("SHIPPING_ADDRESS_L1");
        public static VariableVariableType ShippingAddressL2 { get; } = new VariableVariableType("SHIPPING_ADDRESS_L2");
        public static VariableVariableType ShippingCity { get; } = new VariableVariableType("SHIPPING_CITY");
        public static VariableVariableType ShippingCountry { get; } = new VariableVariableType("SHIPPING_COUNTRY");
        public static VariableVariableType ShippingName { get; } = new VariableVariableType("SHIPPING_NAME");
        public static VariableVariableType ShippingPhone { get; } = new VariableVariableType("SHIPPING_PHONE");
        public static VariableVariableType ShippingState { get; } = new VariableVariableType("SHIPPING_STATE");
        public static VariableVariableType ShippingZip { get; } = new VariableVariableType("SHIPPING_ZIP");
        public static VariableVariableType Useragent { get; } = new VariableVariableType("USERAGENT");

        public static bool operator ==(VariableVariableType left, VariableVariableType right) => left.Equals(right);
        public static bool operator !=(VariableVariableType left, VariableVariableType right) => !left.Equals(right);

        public static explicit operator string(VariableVariableType value) => value._value;

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override bool Equals(object? obj) => obj is VariableVariableType other && Equals(other);
        public bool Equals(VariableVariableType other) => string.Equals(_value, other._value, StringComparison.Ordinal);

        [EditorBrowsable(EditorBrowsableState.Never)]
        public override int GetHashCode() => _value?.GetHashCode() ?? 0;

        public override string ToString() => _value;
    }
}
