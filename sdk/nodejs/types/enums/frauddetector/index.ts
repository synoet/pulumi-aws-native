// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const DetectorDetectorVersionStatus = {
    Draft: "DRAFT",
    Active: "ACTIVE",
} as const;

/**
 * The desired detector version status for the detector
 */
export type DetectorDetectorVersionStatus = (typeof DetectorDetectorVersionStatus)[keyof typeof DetectorDetectorVersionStatus];

export const DetectorEventVariableDataSource = {
    Event: "EVENT",
} as const;

export type DetectorEventVariableDataSource = (typeof DetectorEventVariableDataSource)[keyof typeof DetectorEventVariableDataSource];

export const DetectorEventVariableDataType = {
    String: "STRING",
    Integer: "INTEGER",
    Float: "FLOAT",
    Boolean: "BOOLEAN",
} as const;

export type DetectorEventVariableDataType = (typeof DetectorEventVariableDataType)[keyof typeof DetectorEventVariableDataType];

export const DetectorEventVariableVariableType = {
    AuthCode: "AUTH_CODE",
    Avs: "AVS",
    BillingAddressL1: "BILLING_ADDRESS_L1",
    BillingAddressL2: "BILLING_ADDRESS_L2",
    BillingCity: "BILLING_CITY",
    BillingCountry: "BILLING_COUNTRY",
    BillingName: "BILLING_NAME",
    BillingPhone: "BILLING_PHONE",
    BillingState: "BILLING_STATE",
    BillingZip: "BILLING_ZIP",
    CardBin: "CARD_BIN",
    Categorical: "CATEGORICAL",
    CurrencyCode: "CURRENCY_CODE",
    EmailAddress: "EMAIL_ADDRESS",
    Fingerprint: "FINGERPRINT",
    FraudLabel: "FRAUD_LABEL",
    FreeFormText: "FREE_FORM_TEXT",
    IpAddress: "IP_ADDRESS",
    Numeric: "NUMERIC",
    OrderId: "ORDER_ID",
    PaymentType: "PAYMENT_TYPE",
    PhoneNumber: "PHONE_NUMBER",
    Price: "PRICE",
    ProductCategory: "PRODUCT_CATEGORY",
    ShippingAddressL1: "SHIPPING_ADDRESS_L1",
    ShippingAddressL2: "SHIPPING_ADDRESS_L2",
    ShippingCity: "SHIPPING_CITY",
    ShippingCountry: "SHIPPING_COUNTRY",
    ShippingName: "SHIPPING_NAME",
    ShippingPhone: "SHIPPING_PHONE",
    ShippingState: "SHIPPING_STATE",
    ShippingZip: "SHIPPING_ZIP",
    Useragent: "USERAGENT",
} as const;

export type DetectorEventVariableVariableType = (typeof DetectorEventVariableVariableType)[keyof typeof DetectorEventVariableVariableType];

export const DetectorRuleExecutionMode = {
    FirstMatched: "FIRST_MATCHED",
    AllMatched: "ALL_MATCHED",
} as const;

export type DetectorRuleExecutionMode = (typeof DetectorRuleExecutionMode)[keyof typeof DetectorRuleExecutionMode];

export const DetectorRuleLanguage = {
    Detectorpl: "DETECTORPL",
} as const;

export type DetectorRuleLanguage = (typeof DetectorRuleLanguage)[keyof typeof DetectorRuleLanguage];

export const EventTypeEventVariableDataSource = {
    Event: "EVENT",
} as const;

export type EventTypeEventVariableDataSource = (typeof EventTypeEventVariableDataSource)[keyof typeof EventTypeEventVariableDataSource];

export const EventTypeEventVariableDataType = {
    String: "STRING",
    Integer: "INTEGER",
    Float: "FLOAT",
    Boolean: "BOOLEAN",
} as const;

export type EventTypeEventVariableDataType = (typeof EventTypeEventVariableDataType)[keyof typeof EventTypeEventVariableDataType];

export const EventTypeEventVariableVariableType = {
    AuthCode: "AUTH_CODE",
    Avs: "AVS",
    BillingAddressL1: "BILLING_ADDRESS_L1",
    BillingAddressL2: "BILLING_ADDRESS_L2",
    BillingCity: "BILLING_CITY",
    BillingCountry: "BILLING_COUNTRY",
    BillingName: "BILLING_NAME",
    BillingPhone: "BILLING_PHONE",
    BillingState: "BILLING_STATE",
    BillingZip: "BILLING_ZIP",
    CardBin: "CARD_BIN",
    Categorical: "CATEGORICAL",
    CurrencyCode: "CURRENCY_CODE",
    EmailAddress: "EMAIL_ADDRESS",
    Fingerprint: "FINGERPRINT",
    FraudLabel: "FRAUD_LABEL",
    FreeFormText: "FREE_FORM_TEXT",
    IpAddress: "IP_ADDRESS",
    Numeric: "NUMERIC",
    OrderId: "ORDER_ID",
    PaymentType: "PAYMENT_TYPE",
    PhoneNumber: "PHONE_NUMBER",
    Price: "PRICE",
    ProductCategory: "PRODUCT_CATEGORY",
    ShippingAddressL1: "SHIPPING_ADDRESS_L1",
    ShippingAddressL2: "SHIPPING_ADDRESS_L2",
    ShippingCity: "SHIPPING_CITY",
    ShippingCountry: "SHIPPING_COUNTRY",
    ShippingName: "SHIPPING_NAME",
    ShippingPhone: "SHIPPING_PHONE",
    ShippingState: "SHIPPING_STATE",
    ShippingZip: "SHIPPING_ZIP",
    Useragent: "USERAGENT",
} as const;

export type EventTypeEventVariableVariableType = (typeof EventTypeEventVariableVariableType)[keyof typeof EventTypeEventVariableVariableType];

export const VariableDataSource = {
    Event: "EVENT",
    ExternalModelScore: "EXTERNAL_MODEL_SCORE",
} as const;

/**
 * The source of the data.
 */
export type VariableDataSource = (typeof VariableDataSource)[keyof typeof VariableDataSource];

export const VariableDataType = {
    String: "STRING",
    Integer: "INTEGER",
    Float: "FLOAT",
    Boolean: "BOOLEAN",
} as const;

/**
 * The data type.
 */
export type VariableDataType = (typeof VariableDataType)[keyof typeof VariableDataType];

export const VariableVariableType = {
    AuthCode: "AUTH_CODE",
    Avs: "AVS",
    BillingAddressL1: "BILLING_ADDRESS_L1",
    BillingAddressL2: "BILLING_ADDRESS_L2",
    BillingCity: "BILLING_CITY",
    BillingCountry: "BILLING_COUNTRY",
    BillingName: "BILLING_NAME",
    BillingPhone: "BILLING_PHONE",
    BillingState: "BILLING_STATE",
    BillingZip: "BILLING_ZIP",
    CardBin: "CARD_BIN",
    Categorical: "CATEGORICAL",
    CurrencyCode: "CURRENCY_CODE",
    EmailAddress: "EMAIL_ADDRESS",
    Fingerprint: "FINGERPRINT",
    FraudLabel: "FRAUD_LABEL",
    FreeFormText: "FREE_FORM_TEXT",
    IpAddress: "IP_ADDRESS",
    Numeric: "NUMERIC",
    OrderId: "ORDER_ID",
    PaymentType: "PAYMENT_TYPE",
    PhoneNumber: "PHONE_NUMBER",
    Price: "PRICE",
    ProductCategory: "PRODUCT_CATEGORY",
    ShippingAddressL1: "SHIPPING_ADDRESS_L1",
    ShippingAddressL2: "SHIPPING_ADDRESS_L2",
    ShippingCity: "SHIPPING_CITY",
    ShippingCountry: "SHIPPING_COUNTRY",
    ShippingName: "SHIPPING_NAME",
    ShippingPhone: "SHIPPING_PHONE",
    ShippingState: "SHIPPING_STATE",
    ShippingZip: "SHIPPING_ZIP",
    Useragent: "USERAGENT",
} as const;

/**
 * The variable type. For more information see https://docs.aws.amazon.com/frauddetector/latest/ug/create-a-variable.html#variable-types
 */
export type VariableVariableType = (typeof VariableVariableType)[keyof typeof VariableVariableType];
