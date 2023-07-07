// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const ConnectorProfileAuthenticationType = {
    Oauth2: "OAUTH2",
    Apikey: "APIKEY",
    Basic: "BASIC",
    Custom: "CUSTOM",
} as const;

export type ConnectorProfileAuthenticationType = (typeof ConnectorProfileAuthenticationType)[keyof typeof ConnectorProfileAuthenticationType];

export const ConnectorProfileConnectionMode = {
    Public: "Public",
    Private: "Private",
} as const;

/**
 * Mode in which data transfer should be enabled. Private connection mode is currently enabled for Salesforce, Snowflake, Trendmicro and Singular
 */
export type ConnectorProfileConnectionMode = (typeof ConnectorProfileConnectionMode)[keyof typeof ConnectorProfileConnectionMode];

export const ConnectorProfileConnectorType = {
    Salesforce: "Salesforce",
    Pardot: "Pardot",
    Singular: "Singular",
    Slack: "Slack",
    Redshift: "Redshift",
    Marketo: "Marketo",
    Googleanalytics: "Googleanalytics",
    Zendesk: "Zendesk",
    Servicenow: "Servicenow",
    SAPOData: "SAPOData",
    Datadog: "Datadog",
    Trendmicro: "Trendmicro",
    Snowflake: "Snowflake",
    Dynatrace: "Dynatrace",
    Infornexus: "Infornexus",
    Amplitude: "Amplitude",
    Veeva: "Veeva",
    CustomConnector: "CustomConnector",
} as const;

export type ConnectorProfileConnectorType = (typeof ConnectorProfileConnectorType)[keyof typeof ConnectorProfileConnectorType];

export const ConnectorProfileOAuth2GrantType = {
    ClientCredentials: "CLIENT_CREDENTIALS",
    AuthorizationCode: "AUTHORIZATION_CODE",
    JwtBearer: "JWT_BEARER",
} as const;

export type ConnectorProfileOAuth2GrantType = (typeof ConnectorProfileOAuth2GrantType)[keyof typeof ConnectorProfileOAuth2GrantType];

export const FlowAggregationType = {
    None: "None",
    SingleFile: "SingleFile",
} as const;

export type FlowAggregationType = (typeof FlowAggregationType)[keyof typeof FlowAggregationType];

export const FlowAmplitudeConnectorOperator = {
    Between: "BETWEEN",
} as const;

export type FlowAmplitudeConnectorOperator = (typeof FlowAmplitudeConnectorOperator)[keyof typeof FlowAmplitudeConnectorOperator];

export const FlowConnectorType = {
    SAPOData: "SAPOData",
    Salesforce: "Salesforce",
    Pardot: "Pardot",
    Singular: "Singular",
    Slack: "Slack",
    Redshift: "Redshift",
    S3: "S3",
    Marketo: "Marketo",
    Googleanalytics: "Googleanalytics",
    Zendesk: "Zendesk",
    Servicenow: "Servicenow",
    Datadog: "Datadog",
    Trendmicro: "Trendmicro",
    Snowflake: "Snowflake",
    Dynatrace: "Dynatrace",
    Infornexus: "Infornexus",
    Amplitude: "Amplitude",
    Veeva: "Veeva",
    CustomConnector: "CustomConnector",
    EventBridge: "EventBridge",
    Upsolver: "Upsolver",
    LookoutMetrics: "LookoutMetrics",
} as const;

export type FlowConnectorType = (typeof FlowConnectorType)[keyof typeof FlowConnectorType];

export const FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesType = {
    Sync: "SYNC",
    Async: "ASYNC",
    Automatic: "AUTOMATIC",
} as const;

export type FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesType = (typeof FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesType)[keyof typeof FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesType];

export const FlowDataTransferApi = {
    Automatic: "AUTOMATIC",
    Bulkv2: "BULKV2",
    RestSync: "REST_SYNC",
} as const;

export type FlowDataTransferApi = (typeof FlowDataTransferApi)[keyof typeof FlowDataTransferApi];

export const FlowDatadogConnectorOperator = {
    Projection: "PROJECTION",
    Between: "BETWEEN",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowDatadogConnectorOperator = (typeof FlowDatadogConnectorOperator)[keyof typeof FlowDatadogConnectorOperator];

export const FlowDynatraceConnectorOperator = {
    Projection: "PROJECTION",
    Between: "BETWEEN",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowDynatraceConnectorOperator = (typeof FlowDynatraceConnectorOperator)[keyof typeof FlowDynatraceConnectorOperator];

export const FlowFileType = {
    Csv: "CSV",
    Json: "JSON",
    Parquet: "PARQUET",
} as const;

export type FlowFileType = (typeof FlowFileType)[keyof typeof FlowFileType];

export const FlowGoogleAnalyticsConnectorOperator = {
    Projection: "PROJECTION",
    Between: "BETWEEN",
} as const;

export type FlowGoogleAnalyticsConnectorOperator = (typeof FlowGoogleAnalyticsConnectorOperator)[keyof typeof FlowGoogleAnalyticsConnectorOperator];

export const FlowInforNexusConnectorOperator = {
    Projection: "PROJECTION",
    Between: "BETWEEN",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowInforNexusConnectorOperator = (typeof FlowInforNexusConnectorOperator)[keyof typeof FlowInforNexusConnectorOperator];

export const FlowMarketoConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowMarketoConnectorOperator = (typeof FlowMarketoConnectorOperator)[keyof typeof FlowMarketoConnectorOperator];

export const FlowOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    GreaterThan: "GREATER_THAN",
    Contains: "CONTAINS",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowOperator = (typeof FlowOperator)[keyof typeof FlowOperator];

export const FlowOperatorPropertiesKeys = {
    Value: "VALUE",
    Values: "VALUES",
    DataType: "DATA_TYPE",
    UpperBound: "UPPER_BOUND",
    LowerBound: "LOWER_BOUND",
    SourceDataType: "SOURCE_DATA_TYPE",
    DestinationDataType: "DESTINATION_DATA_TYPE",
    ValidationAction: "VALIDATION_ACTION",
    MaskValue: "MASK_VALUE",
    MaskLength: "MASK_LENGTH",
    TruncateLength: "TRUNCATE_LENGTH",
    MathOperationFieldsOrder: "MATH_OPERATION_FIELDS_ORDER",
    ConcatFormat: "CONCAT_FORMAT",
    SubfieldCategoryMap: "SUBFIELD_CATEGORY_MAP",
    ExcludeSourceFieldsList: "EXCLUDE_SOURCE_FIELDS_LIST",
    IncludeNewFields: "INCLUDE_NEW_FIELDS",
    OrderedPartitionKeysList: "ORDERED_PARTITION_KEYS_LIST",
} as const;

export type FlowOperatorPropertiesKeys = (typeof FlowOperatorPropertiesKeys)[keyof typeof FlowOperatorPropertiesKeys];

export const FlowPardotConnectorOperator = {
    Projection: "PROJECTION",
    EqualTo: "EQUAL_TO",
    NoOp: "NO_OP",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
} as const;

export type FlowPardotConnectorOperator = (typeof FlowPardotConnectorOperator)[keyof typeof FlowPardotConnectorOperator];

export const FlowPathPrefix = {
    ExecutionId: "EXECUTION_ID",
    SchemaVersion: "SCHEMA_VERSION",
} as const;

export type FlowPathPrefix = (typeof FlowPathPrefix)[keyof typeof FlowPathPrefix];

export const FlowPrefixFormat = {
    Year: "YEAR",
    Month: "MONTH",
    Day: "DAY",
    Hour: "HOUR",
    Minute: "MINUTE",
} as const;

export type FlowPrefixFormat = (typeof FlowPrefixFormat)[keyof typeof FlowPrefixFormat];

export const FlowPrefixType = {
    Filename: "FILENAME",
    Path: "PATH",
    PathAndFilename: "PATH_AND_FILENAME",
} as const;

export type FlowPrefixType = (typeof FlowPrefixType)[keyof typeof FlowPrefixType];

export const FlowS3ConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowS3ConnectorOperator = (typeof FlowS3ConnectorOperator)[keyof typeof FlowS3ConnectorOperator];

export const FlowS3InputFormatConfigS3InputFileType = {
    Csv: "CSV",
    Json: "JSON",
} as const;

export type FlowS3InputFormatConfigS3InputFileType = (typeof FlowS3InputFormatConfigS3InputFileType)[keyof typeof FlowS3InputFormatConfigS3InputFileType];

export const FlowSAPODataConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    Contains: "CONTAINS",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowSAPODataConnectorOperator = (typeof FlowSAPODataConnectorOperator)[keyof typeof FlowSAPODataConnectorOperator];

export const FlowSalesforceConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    Contains: "CONTAINS",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowSalesforceConnectorOperator = (typeof FlowSalesforceConnectorOperator)[keyof typeof FlowSalesforceConnectorOperator];

export const FlowScheduledTriggerPropertiesDataPullMode = {
    Incremental: "Incremental",
    Complete: "Complete",
} as const;

export type FlowScheduledTriggerPropertiesDataPullMode = (typeof FlowScheduledTriggerPropertiesDataPullMode)[keyof typeof FlowScheduledTriggerPropertiesDataPullMode];

export const FlowServiceNowConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    Contains: "CONTAINS",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowServiceNowConnectorOperator = (typeof FlowServiceNowConnectorOperator)[keyof typeof FlowServiceNowConnectorOperator];

export const FlowSingularConnectorOperator = {
    Projection: "PROJECTION",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowSingularConnectorOperator = (typeof FlowSingularConnectorOperator)[keyof typeof FlowSingularConnectorOperator];

export const FlowSlackConnectorOperator = {
    Projection: "PROJECTION",
    Between: "BETWEEN",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowSlackConnectorOperator = (typeof FlowSlackConnectorOperator)[keyof typeof FlowSlackConnectorOperator];

export const FlowStatus = {
    Active: "Active",
    Suspended: "Suspended",
} as const;

/**
 * Flow activation status for Scheduled- and Event-triggered flows
 */
export type FlowStatus = (typeof FlowStatus)[keyof typeof FlowStatus];

export const FlowTaskType = {
    Arithmetic: "Arithmetic",
    Filter: "Filter",
    Map: "Map",
    MapAll: "Map_all",
    Mask: "Mask",
    Merge: "Merge",
    Passthrough: "Passthrough",
    Truncate: "Truncate",
    Validate: "Validate",
    Partition: "Partition",
} as const;

export type FlowTaskType = (typeof FlowTaskType)[keyof typeof FlowTaskType];

export const FlowTrendmicroConnectorOperator = {
    Projection: "PROJECTION",
    EqualTo: "EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowTrendmicroConnectorOperator = (typeof FlowTrendmicroConnectorOperator)[keyof typeof FlowTrendmicroConnectorOperator];

export const FlowTriggerType = {
    Scheduled: "Scheduled",
    Event: "Event",
    OnDemand: "OnDemand",
} as const;

export type FlowTriggerType = (typeof FlowTriggerType)[keyof typeof FlowTriggerType];

export const FlowVeevaConnectorOperator = {
    Projection: "PROJECTION",
    LessThan: "LESS_THAN",
    GreaterThan: "GREATER_THAN",
    Between: "BETWEEN",
    LessThanOrEqualTo: "LESS_THAN_OR_EQUAL_TO",
    GreaterThanOrEqualTo: "GREATER_THAN_OR_EQUAL_TO",
    EqualTo: "EQUAL_TO",
    NotEqualTo: "NOT_EQUAL_TO",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowVeevaConnectorOperator = (typeof FlowVeevaConnectorOperator)[keyof typeof FlowVeevaConnectorOperator];

export const FlowWriteOperationType = {
    Insert: "INSERT",
    Upsert: "UPSERT",
    Update: "UPDATE",
    Delete: "DELETE",
} as const;

export type FlowWriteOperationType = (typeof FlowWriteOperationType)[keyof typeof FlowWriteOperationType];

export const FlowZendeskConnectorOperator = {
    Projection: "PROJECTION",
    GreaterThan: "GREATER_THAN",
    Addition: "ADDITION",
    Multiplication: "MULTIPLICATION",
    Division: "DIVISION",
    Subtraction: "SUBTRACTION",
    MaskAll: "MASK_ALL",
    MaskFirstN: "MASK_FIRST_N",
    MaskLastN: "MASK_LAST_N",
    ValidateNonNull: "VALIDATE_NON_NULL",
    ValidateNonZero: "VALIDATE_NON_ZERO",
    ValidateNonNegative: "VALIDATE_NON_NEGATIVE",
    ValidateNumeric: "VALIDATE_NUMERIC",
    NoOp: "NO_OP",
} as const;

export type FlowZendeskConnectorOperator = (typeof FlowZendeskConnectorOperator)[keyof typeof FlowZendeskConnectorOperator];
