// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.
 */
export function getDbInstance(args: GetDbInstanceArgs, opts?: pulumi.InvokeOptions): Promise<GetDbInstanceResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:rds:getDbInstance", {
        "dbInstanceIdentifier": args.dbInstanceIdentifier,
    }, opts);
}

export interface GetDbInstanceArgs {
    /**
     * A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
     */
    dbInstanceIdentifier: string;
}

export interface GetDbInstanceResult {
    /**
     * The amount of storage (in gigabytes) to be initially allocated for the database instance.
     */
    readonly allocatedStorage?: string;
    /**
     * The AWS Identity and Access Management (IAM) roles associated with the DB instance.
     */
    readonly associatedRoles?: outputs.rds.DbInstanceDbInstanceRole[];
    /**
     * A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
     */
    readonly autoMinorVersionUpgrade?: boolean;
    /**
     * The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
     */
    readonly availabilityZone?: string;
    /**
     * The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
     */
    readonly backupRetentionPeriod?: number;
    /**
     * The identifier of the CA certificate for this DB instance.
     */
    readonly caCertificateIdentifier?: string;
    /**
     * Returns the details of the DB instance's server certificate.
     */
    readonly certificateDetails?: outputs.rds.DbInstanceCertificateDetails;
    /**
     * A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
     */
    readonly copyTagsToSnapshot?: boolean;
    /**
     * The identifier for the RDS for MySQL Multi-AZ DB cluster snapshot to restore from. For more information on Multi-AZ DB clusters, see Multi-AZ deployments with two readable standby DB instances in the Amazon RDS User Guide .
     *
     * Constraints:
     *  * Must match the identifier of an existing Multi-AZ DB cluster snapshot.
     *  * Can't be specified when DBSnapshotIdentifier is specified.
     *  * Must be specified when DBSnapshotIdentifier isn't specified.
     *  * If you are restoring from a shared manual Multi-AZ DB cluster snapshot, the DBClusterSnapshotIdentifier must be the ARN of the shared snapshot.
     *  * Can't be the identifier of an Aurora DB cluster snapshot.
     *  * Can't be the identifier of an RDS for PostgreSQL Multi-AZ DB cluster snapshot.
     */
    readonly dbClusterSnapshotIdentifier?: string;
    /**
     * The Amazon Resource Name (ARN) for the DB instance.
     */
    readonly dbInstanceArn?: string;
    /**
     * The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
     */
    readonly dbInstanceClass?: string;
    /**
     * The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
     */
    readonly dbParameterGroupName?: string;
    /**
     * A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
     */
    readonly dbSecurityGroups?: string[];
    /**
     * The Oracle system ID (Oracle SID) for a container database (CDB). The Oracle SID is also the name of the CDB. This setting is valid for RDS Custom only.
     */
    readonly dbSystemId?: string;
    /**
     * The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
     */
    readonly dbiResourceId?: string;
    /**
     * A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
     */
    readonly deletionProtection?: boolean;
    /**
     * The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
     */
    readonly domain?: string;
    /**
     * The ARN for the Secrets Manager secret with the credentials for the user joining the domain.
     */
    readonly domainAuthSecretArn?: string;
    /**
     * The IPv4 DNS IP addresses of your primary and secondary Active Directory domain controllers.
     */
    readonly domainDnsIps?: string[];
    /**
     * The fully qualified domain name (FQDN) of an Active Directory domain.
     */
    readonly domainFqdn?: string;
    /**
     * Specify the name of the IAM role to be used when making API calls to the Directory Service.
     */
    readonly domainIamRoleName?: string;
    /**
     * The Active Directory organizational unit for your DB instance to join.
     */
    readonly domainOu?: string;
    /**
     * The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
     */
    readonly enableCloudwatchLogsExports?: string[];
    /**
     * A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
     */
    readonly enableIamDatabaseAuthentication?: boolean;
    /**
     * A value that indicates whether to enable Performance Insights for the DB instance.
     */
    readonly enablePerformanceInsights?: boolean;
    /**
     * Specifies the connection endpoint.
     */
    readonly endpoint?: outputs.rds.DbInstanceEndpoint;
    /**
     * The name of the database engine that you want to use for this DB instance.
     */
    readonly engine?: string;
    /**
     * The version number of the database engine to use.
     */
    readonly engineVersion?: string;
    /**
     * The number of I/O operations per second (IOPS) that the database provisions.
     */
    readonly iops?: number;
    /**
     * License model information for this DB instance.
     */
    readonly licenseModel?: string;
    /**
     * A value that indicates whether to manage the master user password with AWS Secrets Manager.
     */
    readonly manageMasterUserPassword?: boolean;
    /**
     * Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
     */
    readonly masterUserSecret?: outputs.rds.DbInstanceMasterUserSecret;
    /**
     * The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
     */
    readonly maxAllocatedStorage?: number;
    /**
     * The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
     */
    readonly monitoringInterval?: number;
    /**
     * The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
     */
    readonly monitoringRoleArn?: string;
    /**
     * Specifies whether the database instance is a multiple Availability Zone deployment.
     */
    readonly multiAz?: boolean;
    /**
     * The network type of the DB cluster.
     */
    readonly networkType?: string;
    /**
     * Indicates that the DB instance should be associated with the specified option group.
     */
    readonly optionGroupName?: string;
    /**
     * The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
     */
    readonly performanceInsightsKmsKeyId?: string;
    /**
     * The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
     */
    readonly performanceInsightsRetentionPeriod?: number;
    /**
     * The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
     */
    readonly preferredBackupWindow?: string;
    /**
     * he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
     */
    readonly preferredMaintenanceWindow?: string;
    /**
     * The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
     */
    readonly processorFeatures?: outputs.rds.DbInstanceProcessorFeature[];
    /**
     * A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
     */
    readonly promotionTier?: number;
    /**
     * Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
     */
    readonly publiclyAccessible?: boolean;
    /**
     * The open mode of an Oracle read replica. The default is open-read-only.
     */
    readonly replicaMode?: string;
    /**
     * The identifier of the Multi-AZ DB cluster that will act as the source for the read replica. Each DB cluster can have up to 15 read replicas.
     */
    readonly sourceDbClusterIdentifier?: string;
    /**
     * Specifies the storage throughput for the DB instance.
     */
    readonly storageThroughput?: number;
    /**
     * Specifies the storage type to be associated with the DB instance.
     */
    readonly storageType?: string;
    /**
     * Tags to assign to the DB instance.
     */
    readonly tags?: outputs.rds.DbInstanceTag[];
    /**
     * The ARN from the key store with which to associate the instance for TDE encryption.
     */
    readonly tdeCredentialArn?: string;
    /**
     * A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
     */
    readonly vpcSecurityGroups?: string[];
}
/**
 * The AWS::RDS::DBInstance resource creates an Amazon RDS DB instance.
 */
export function getDbInstanceOutput(args: GetDbInstanceOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDbInstanceResult> {
    return pulumi.output(args).apply((a: any) => getDbInstance(a, opts))
}

export interface GetDbInstanceOutputArgs {
    /**
     * A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
     */
    dbInstanceIdentifier: pulumi.Input<string>;
}
