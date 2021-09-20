// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AnalysisAnalysisErrorType = {
    AccessDenied: "ACCESS_DENIED",
    SourceNotFound: "SOURCE_NOT_FOUND",
    DataSetNotFound: "DATA_SET_NOT_FOUND",
    InternalFailure: "INTERNAL_FAILURE",
    ParameterValueIncompatible: "PARAMETER_VALUE_INCOMPATIBLE",
    ParameterTypeInvalid: "PARAMETER_TYPE_INVALID",
    ParameterNotFound: "PARAMETER_NOT_FOUND",
    ColumnTypeMismatch: "COLUMN_TYPE_MISMATCH",
    ColumnGeographicRoleMismatch: "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    ColumnReplacementMissing: "COLUMN_REPLACEMENT_MISSING",
} as const;

export type AnalysisAnalysisErrorType = (typeof AnalysisAnalysisErrorType)[keyof typeof AnalysisAnalysisErrorType];

export const AnalysisResourceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationSuccessful: "CREATION_SUCCESSFUL",
    CreationFailed: "CREATION_FAILED",
    UpdateInProgress: "UPDATE_IN_PROGRESS",
    UpdateSuccessful: "UPDATE_SUCCESSFUL",
    UpdateFailed: "UPDATE_FAILED",
    Deleted: "DELETED",
} as const;

export type AnalysisResourceStatus = (typeof AnalysisResourceStatus)[keyof typeof AnalysisResourceStatus];

export const DashboardDashboardBehavior = {
    Enabled: "ENABLED",
    Disabled: "DISABLED",
} as const;

export type DashboardDashboardBehavior = (typeof DashboardDashboardBehavior)[keyof typeof DashboardDashboardBehavior];

export const DashboardDashboardErrorType = {
    AccessDenied: "ACCESS_DENIED",
    SourceNotFound: "SOURCE_NOT_FOUND",
    DataSetNotFound: "DATA_SET_NOT_FOUND",
    InternalFailure: "INTERNAL_FAILURE",
    ParameterValueIncompatible: "PARAMETER_VALUE_INCOMPATIBLE",
    ParameterTypeInvalid: "PARAMETER_TYPE_INVALID",
    ParameterNotFound: "PARAMETER_NOT_FOUND",
    ColumnTypeMismatch: "COLUMN_TYPE_MISMATCH",
    ColumnGeographicRoleMismatch: "COLUMN_GEOGRAPHIC_ROLE_MISMATCH",
    ColumnReplacementMissing: "COLUMN_REPLACEMENT_MISSING",
} as const;

export type DashboardDashboardErrorType = (typeof DashboardDashboardErrorType)[keyof typeof DashboardDashboardErrorType];

export const DashboardDashboardUIState = {
    Expanded: "EXPANDED",
    Collapsed: "COLLAPSED",
} as const;

export type DashboardDashboardUIState = (typeof DashboardDashboardUIState)[keyof typeof DashboardDashboardUIState];

export const DashboardResourceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationSuccessful: "CREATION_SUCCESSFUL",
    CreationFailed: "CREATION_FAILED",
    UpdateInProgress: "UPDATE_IN_PROGRESS",
    UpdateSuccessful: "UPDATE_SUCCESSFUL",
    UpdateFailed: "UPDATE_FAILED",
    Deleted: "DELETED",
} as const;

export type DashboardResourceStatus = (typeof DashboardResourceStatus)[keyof typeof DashboardResourceStatus];

export const DataSetColumnDataType = {
    String: "STRING",
    Integer: "INTEGER",
    Decimal: "DECIMAL",
    Datetime: "DATETIME",
} as const;

export type DataSetColumnDataType = (typeof DataSetColumnDataType)[keyof typeof DataSetColumnDataType];

export const DataSetDataSetImportMode = {
    Spice: "SPICE",
    DirectQuery: "DIRECT_QUERY",
} as const;

export type DataSetDataSetImportMode = (typeof DataSetDataSetImportMode)[keyof typeof DataSetDataSetImportMode];

export const DataSetGeoSpatialCountryCode = {
    Us: "US",
} as const;

export type DataSetGeoSpatialCountryCode = (typeof DataSetGeoSpatialCountryCode)[keyof typeof DataSetGeoSpatialCountryCode];

export const DataSetRowLevelPermissionFormatVersion = {
    Version1: "VERSION_1",
    Version2: "VERSION_2",
} as const;

export type DataSetRowLevelPermissionFormatVersion = (typeof DataSetRowLevelPermissionFormatVersion)[keyof typeof DataSetRowLevelPermissionFormatVersion];

export const DataSetRowLevelPermissionPolicy = {
    GrantAccess: "GRANT_ACCESS",
    DenyAccess: "DENY_ACCESS",
} as const;

export type DataSetRowLevelPermissionPolicy = (typeof DataSetRowLevelPermissionPolicy)[keyof typeof DataSetRowLevelPermissionPolicy];

export const DataSourceDataSourceErrorInfoType = {
    AccessDenied: "ACCESS_DENIED",
    CopySourceNotFound: "COPY_SOURCE_NOT_FOUND",
    Timeout: "TIMEOUT",
    EngineVersionNotSupported: "ENGINE_VERSION_NOT_SUPPORTED",
    UnknownHost: "UNKNOWN_HOST",
    GenericSqlFailure: "GENERIC_SQL_FAILURE",
    Conflict: "CONFLICT",
    Unknown: "UNKNOWN",
} as const;

export type DataSourceDataSourceErrorInfoType = (typeof DataSourceDataSourceErrorInfoType)[keyof typeof DataSourceDataSourceErrorInfoType];

export const DataSourceDataSourceType = {
    AdobeAnalytics: "ADOBE_ANALYTICS",
    AmazonElasticsearch: "AMAZON_ELASTICSEARCH",
    Athena: "ATHENA",
    Aurora: "AURORA",
    AuroraPostgresql: "AURORA_POSTGRESQL",
    AwsIotAnalytics: "AWS_IOT_ANALYTICS",
    Github: "GITHUB",
    Jira: "JIRA",
    Mariadb: "MARIADB",
    Mysql: "MYSQL",
    Oracle: "ORACLE",
    Postgresql: "POSTGRESQL",
    Presto: "PRESTO",
    Redshift: "REDSHIFT",
    S3: "S3",
    Salesforce: "SALESFORCE",
    Servicenow: "SERVICENOW",
    Snowflake: "SNOWFLAKE",
    Spark: "SPARK",
    Sqlserver: "SQLSERVER",
    Teradata: "TERADATA",
    Twitter: "TWITTER",
    Timestream: "TIMESTREAM",
} as const;

export type DataSourceDataSourceType = (typeof DataSourceDataSourceType)[keyof typeof DataSourceDataSourceType];

export const DataSourceResourceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationSuccessful: "CREATION_SUCCESSFUL",
    CreationFailed: "CREATION_FAILED",
    UpdateInProgress: "UPDATE_IN_PROGRESS",
    UpdateSuccessful: "UPDATE_SUCCESSFUL",
    UpdateFailed: "UPDATE_FAILED",
    Deleted: "DELETED",
} as const;

export type DataSourceResourceStatus = (typeof DataSourceResourceStatus)[keyof typeof DataSourceResourceStatus];

export const TemplateResourceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationSuccessful: "CREATION_SUCCESSFUL",
    CreationFailed: "CREATION_FAILED",
    UpdateInProgress: "UPDATE_IN_PROGRESS",
    UpdateSuccessful: "UPDATE_SUCCESSFUL",
    UpdateFailed: "UPDATE_FAILED",
    Deleted: "DELETED",
} as const;

export type TemplateResourceStatus = (typeof TemplateResourceStatus)[keyof typeof TemplateResourceStatus];

export const TemplateTemplateErrorType = {
    SourceNotFound: "SOURCE_NOT_FOUND",
    DataSetNotFound: "DATA_SET_NOT_FOUND",
    InternalFailure: "INTERNAL_FAILURE",
    AccessDenied: "ACCESS_DENIED",
} as const;

export type TemplateTemplateErrorType = (typeof TemplateTemplateErrorType)[keyof typeof TemplateTemplateErrorType];

export const ThemeResourceStatus = {
    CreationInProgress: "CREATION_IN_PROGRESS",
    CreationSuccessful: "CREATION_SUCCESSFUL",
    CreationFailed: "CREATION_FAILED",
    UpdateInProgress: "UPDATE_IN_PROGRESS",
    UpdateSuccessful: "UPDATE_SUCCESSFUL",
    UpdateFailed: "UPDATE_FAILED",
    Deleted: "DELETED",
} as const;

export type ThemeResourceStatus = (typeof ThemeResourceStatus)[keyof typeof ThemeResourceStatus];

export const ThemeThemeErrorType = {
    InternalFailure: "INTERNAL_FAILURE",
} as const;

export type ThemeThemeErrorType = (typeof ThemeThemeErrorType)[keyof typeof ThemeThemeErrorType];

export const ThemeThemeType = {
    Quicksight: "QUICKSIGHT",
    Custom: "CUSTOM",
    All: "ALL",
} as const;

export type ThemeThemeType = (typeof ThemeThemeType)[keyof typeof ThemeThemeType];
