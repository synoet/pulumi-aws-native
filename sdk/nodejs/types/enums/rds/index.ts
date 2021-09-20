// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const DBProxyAuthFormatAuthScheme = {
    Secrets: "SECRETS",
} as const;

/**
 * The type of authentication that the proxy uses for connections from the proxy to the underlying database. 
 */
export type DBProxyAuthFormatAuthScheme = (typeof DBProxyAuthFormatAuthScheme)[keyof typeof DBProxyAuthFormatAuthScheme];

export const DBProxyAuthFormatIAMAuth = {
    Disabled: "DISABLED",
    Required: "REQUIRED",
} as const;

/**
 * Whether to require or disallow AWS Identity and Access Management (IAM) authentication for connections to the proxy. 
 */
export type DBProxyAuthFormatIAMAuth = (typeof DBProxyAuthFormatIAMAuth)[keyof typeof DBProxyAuthFormatIAMAuth];

export const DBProxyEndpointTargetRole = {
    ReadWrite: "READ_WRITE",
    ReadOnly: "READ_ONLY",
} as const;

/**
 * A value that indicates whether the DB proxy endpoint can be used for read/write or read-only operations.
 */
export type DBProxyEndpointTargetRole = (typeof DBProxyEndpointTargetRole)[keyof typeof DBProxyEndpointTargetRole];

export const DBProxyEngineFamily = {
    Mysql: "MYSQL",
    Postgresql: "POSTGRESQL",
} as const;

/**
 * The kinds of databases that the proxy can connect to.
 */
export type DBProxyEngineFamily = (typeof DBProxyEngineFamily)[keyof typeof DBProxyEngineFamily];

export const DBProxyTargetGroupTargetGroupName = {
    Default: "default",
} as const;

/**
 * The identifier for the DBProxyTargetGroup
 */
export type DBProxyTargetGroupTargetGroupName = (typeof DBProxyTargetGroupTargetGroupName)[keyof typeof DBProxyTargetGroupTargetGroupName];

export const GlobalClusterEngine = {
    Aurora: "aurora",
    AuroraMysql: "aurora-mysql",
    AuroraPostgresql: "aurora-postgresql",
} as const;

/**
 * The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
 * If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
 */
export type GlobalClusterEngine = (typeof GlobalClusterEngine)[keyof typeof GlobalClusterEngine];
