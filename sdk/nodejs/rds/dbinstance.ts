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
export class DBInstance extends pulumi.CustomResource {
    /**
     * Get an existing DBInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DBInstance {
        return new DBInstance(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rds:DBInstance';

    /**
     * Returns true if the given object is an instance of DBInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DBInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DBInstance.__pulumiType;
    }

    /**
     * The amount of storage (in gigabytes) to be initially allocated for the database instance.
     */
    public readonly allocatedStorage!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
     */
    public readonly allowMajorVersionUpgrade!: pulumi.Output<boolean | undefined>;
    /**
     * The AWS Identity and Access Management (IAM) roles associated with the DB instance.
     */
    public readonly associatedRoles!: pulumi.Output<outputs.rds.DBInstanceRole[] | undefined>;
    /**
     * A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
     */
    public readonly autoMinorVersionUpgrade!: pulumi.Output<boolean | undefined>;
    /**
     * The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
     */
    public readonly availabilityZone!: pulumi.Output<string | undefined>;
    /**
     * The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
     */
    public readonly backupRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * The identifier of the CA certificate for this DB instance.
     */
    public readonly cACertificateIdentifier!: pulumi.Output<string | undefined>;
    /**
     * For supported engines, indicates that the DB instance should be associated with the specified character set.
     */
    public readonly characterSetName!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
     */
    public readonly copyTagsToSnapshot!: pulumi.Output<boolean | undefined>;
    /**
     * The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:
     *  * The profile must exist in your account.
     *  * The profile must have an IAM role that Amazon EC2 has permissions to assume.
     *  * The instance profile name and the associated IAM role name must start with the prefix AWSRDSCustom .
     * For the list of permissions required for the IAM role, see Configure IAM and your VPC in the Amazon RDS User Guide .
     *
     * This setting is required for RDS Custom.
     */
    public readonly customIAMInstanceProfile!: pulumi.Output<string | undefined>;
    /**
     * The identifier of the DB cluster that the instance will belong to.
     */
    public readonly dBClusterIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the DB instance.
     */
    public /*out*/ readonly dBInstanceArn!: pulumi.Output<string>;
    /**
     * The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
     */
    public readonly dBInstanceClass!: pulumi.Output<string | undefined>;
    /**
     * A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
     */
    public readonly dBInstanceIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The meaning of this parameter differs according to the database engine you use.
     */
    public readonly dBName!: pulumi.Output<string | undefined>;
    /**
     * The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
     */
    public readonly dBParameterGroupName!: pulumi.Output<string | undefined>;
    /**
     * A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
     */
    public readonly dBSecurityGroups!: pulumi.Output<string[] | undefined>;
    /**
     * The name or Amazon Resource Name (ARN) of the DB snapshot that's used to restore the DB instance. If you're restoring from a shared manual DB snapshot, you must specify the ARN of the snapshot.
     */
    public readonly dBSnapshotIdentifier!: pulumi.Output<string | undefined>;
    /**
     * A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new VPC.
     */
    public readonly dBSubnetGroupName!: pulumi.Output<string | undefined>;
    /**
     * The AWS Region-unique, immutable identifier for the DB instance. This identifier is found in AWS CloudTrail log entries whenever the AWS KMS key for the DB instance is accessed.
     */
    public /*out*/ readonly dbiResourceId!: pulumi.Output<string>;
    /**
     * A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
     */
    public readonly deleteAutomatedBackups!: pulumi.Output<boolean | undefined>;
    /**
     * A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
     */
    public readonly deletionProtection!: pulumi.Output<boolean | undefined>;
    /**
     * The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
     */
    public readonly domain!: pulumi.Output<string | undefined>;
    /**
     * Specify the name of the IAM role to be used when making API calls to the Directory Service.
     */
    public readonly domainIAMRoleName!: pulumi.Output<string | undefined>;
    /**
     * The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
     */
    public readonly enableCloudwatchLogsExports!: pulumi.Output<string[] | undefined>;
    /**
     * A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
     */
    public readonly enableIAMDatabaseAuthentication!: pulumi.Output<boolean | undefined>;
    /**
     * A value that indicates whether to enable Performance Insights for the DB instance.
     */
    public readonly enablePerformanceInsights!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the connection endpoint.
     */
    public readonly endpoint!: pulumi.Output<outputs.rds.DBInstanceEndpoint | undefined>;
    /**
     * The name of the database engine that you want to use for this DB instance.
     */
    public readonly engine!: pulumi.Output<string | undefined>;
    /**
     * The version number of the database engine to use.
     */
    public readonly engineVersion!: pulumi.Output<string | undefined>;
    /**
     * The number of I/O operations per second (IOPS) that the database provisions.
     */
    public readonly iops!: pulumi.Output<number | undefined>;
    /**
     * The ARN of the AWS Key Management Service (AWS KMS) master key that's used to encrypt the DB instance.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * License model information for this DB instance.
     */
    public readonly licenseModel!: pulumi.Output<string | undefined>;
    /**
     * The password for the master user.
     */
    public readonly masterUserPassword!: pulumi.Output<string | undefined>;
    /**
     * The master user name for the DB instance.
     */
    public readonly masterUsername!: pulumi.Output<string | undefined>;
    /**
     * The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
     */
    public readonly maxAllocatedStorage!: pulumi.Output<number | undefined>;
    /**
     * The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
     */
    public readonly monitoringInterval!: pulumi.Output<number | undefined>;
    /**
     * The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
     */
    public readonly monitoringRoleArn!: pulumi.Output<string | undefined>;
    /**
     * Specifies whether the database instance is a multiple Availability Zone deployment.
     */
    public readonly multiAZ!: pulumi.Output<boolean | undefined>;
    /**
     * The name of the NCHAR character set for the Oracle DB instance. This parameter doesn't apply to RDS Custom.
     */
    public readonly ncharCharacterSetName!: pulumi.Output<string | undefined>;
    /**
     * The network type of the DB cluster.
     */
    public readonly networkType!: pulumi.Output<string | undefined>;
    /**
     * Indicates that the DB instance should be associated with the specified option group.
     */
    public readonly optionGroupName!: pulumi.Output<string | undefined>;
    /**
     * The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
     */
    public readonly performanceInsightsKMSKeyId!: pulumi.Output<string | undefined>;
    /**
     * The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
     */
    public readonly performanceInsightsRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * The port number on which the database accepts connections.
     */
    public readonly port!: pulumi.Output<string | undefined>;
    /**
     * The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
     */
    public readonly preferredBackupWindow!: pulumi.Output<string | undefined>;
    /**
     * he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
     */
    public readonly preferredMaintenanceWindow!: pulumi.Output<string | undefined>;
    /**
     * The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
     */
    public readonly processorFeatures!: pulumi.Output<outputs.rds.DBInstanceProcessorFeature[] | undefined>;
    /**
     * A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
     */
    public readonly promotionTier!: pulumi.Output<number | undefined>;
    /**
     * Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
     */
    public readonly publiclyAccessible!: pulumi.Output<boolean | undefined>;
    /**
     * The open mode of an Oracle read replica. The default is open-read-only.
     */
    public readonly replicaMode!: pulumi.Output<string | undefined>;
    /**
     * If you want to create a Read Replica DB instance, specify the ID of the source DB instance. Each DB instance can have a limited number of Read Replicas.
     */
    public readonly sourceDBInstanceIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The ID of the region that contains the source DB instance for the Read Replica.
     */
    public readonly sourceRegion!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether the DB instance is encrypted. By default, it isn't encrypted.
     */
    public readonly storageEncrypted!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the storage type to be associated with the DB instance.
     */
    public readonly storageType!: pulumi.Output<string | undefined>;
    /**
     * Tags to assign to the DB instance.
     */
    public readonly tags!: pulumi.Output<outputs.rds.DBInstanceTag[] | undefined>;
    /**
     * The ARN from the key store with which to associate the instance for TDE encryption.
     */
    public readonly tdeCredentialArn!: pulumi.Output<string | undefined>;
    /**
     * The password for the given ARN from the key store in order to access the device.
     */
    public readonly tdeCredentialPassword!: pulumi.Output<string | undefined>;
    /**
     * The time zone of the DB instance. The time zone parameter is currently supported only by Microsoft SQL Server.
     */
    public readonly timezone!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether the DB instance class of the DB instance uses its default processor features.
     */
    public readonly useDefaultProcessorFeatures!: pulumi.Output<boolean | undefined>;
    /**
     * A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
     */
    public readonly vPCSecurityGroups!: pulumi.Output<string[] | undefined>;

    /**
     * Create a DBInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DBInstanceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["allocatedStorage"] = args ? args.allocatedStorage : undefined;
            resourceInputs["allowMajorVersionUpgrade"] = args ? args.allowMajorVersionUpgrade : undefined;
            resourceInputs["associatedRoles"] = args ? args.associatedRoles : undefined;
            resourceInputs["autoMinorVersionUpgrade"] = args ? args.autoMinorVersionUpgrade : undefined;
            resourceInputs["availabilityZone"] = args ? args.availabilityZone : undefined;
            resourceInputs["backupRetentionPeriod"] = args ? args.backupRetentionPeriod : undefined;
            resourceInputs["cACertificateIdentifier"] = args ? args.cACertificateIdentifier : undefined;
            resourceInputs["characterSetName"] = args ? args.characterSetName : undefined;
            resourceInputs["copyTagsToSnapshot"] = args ? args.copyTagsToSnapshot : undefined;
            resourceInputs["customIAMInstanceProfile"] = args ? args.customIAMInstanceProfile : undefined;
            resourceInputs["dBClusterIdentifier"] = args ? args.dBClusterIdentifier : undefined;
            resourceInputs["dBInstanceClass"] = args ? args.dBInstanceClass : undefined;
            resourceInputs["dBInstanceIdentifier"] = args ? args.dBInstanceIdentifier : undefined;
            resourceInputs["dBName"] = args ? args.dBName : undefined;
            resourceInputs["dBParameterGroupName"] = args ? args.dBParameterGroupName : undefined;
            resourceInputs["dBSecurityGroups"] = args ? args.dBSecurityGroups : undefined;
            resourceInputs["dBSnapshotIdentifier"] = args ? args.dBSnapshotIdentifier : undefined;
            resourceInputs["dBSubnetGroupName"] = args ? args.dBSubnetGroupName : undefined;
            resourceInputs["deleteAutomatedBackups"] = args ? args.deleteAutomatedBackups : undefined;
            resourceInputs["deletionProtection"] = args ? args.deletionProtection : undefined;
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["domainIAMRoleName"] = args ? args.domainIAMRoleName : undefined;
            resourceInputs["enableCloudwatchLogsExports"] = args ? args.enableCloudwatchLogsExports : undefined;
            resourceInputs["enableIAMDatabaseAuthentication"] = args ? args.enableIAMDatabaseAuthentication : undefined;
            resourceInputs["enablePerformanceInsights"] = args ? args.enablePerformanceInsights : undefined;
            resourceInputs["endpoint"] = args ? args.endpoint : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["iops"] = args ? args.iops : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["licenseModel"] = args ? args.licenseModel : undefined;
            resourceInputs["masterUserPassword"] = args ? args.masterUserPassword : undefined;
            resourceInputs["masterUsername"] = args ? args.masterUsername : undefined;
            resourceInputs["maxAllocatedStorage"] = args ? args.maxAllocatedStorage : undefined;
            resourceInputs["monitoringInterval"] = args ? args.monitoringInterval : undefined;
            resourceInputs["monitoringRoleArn"] = args ? args.monitoringRoleArn : undefined;
            resourceInputs["multiAZ"] = args ? args.multiAZ : undefined;
            resourceInputs["ncharCharacterSetName"] = args ? args.ncharCharacterSetName : undefined;
            resourceInputs["networkType"] = args ? args.networkType : undefined;
            resourceInputs["optionGroupName"] = args ? args.optionGroupName : undefined;
            resourceInputs["performanceInsightsKMSKeyId"] = args ? args.performanceInsightsKMSKeyId : undefined;
            resourceInputs["performanceInsightsRetentionPeriod"] = args ? args.performanceInsightsRetentionPeriod : undefined;
            resourceInputs["port"] = args ? args.port : undefined;
            resourceInputs["preferredBackupWindow"] = args ? args.preferredBackupWindow : undefined;
            resourceInputs["preferredMaintenanceWindow"] = args ? args.preferredMaintenanceWindow : undefined;
            resourceInputs["processorFeatures"] = args ? args.processorFeatures : undefined;
            resourceInputs["promotionTier"] = args ? args.promotionTier : undefined;
            resourceInputs["publiclyAccessible"] = args ? args.publiclyAccessible : undefined;
            resourceInputs["replicaMode"] = args ? args.replicaMode : undefined;
            resourceInputs["sourceDBInstanceIdentifier"] = args ? args.sourceDBInstanceIdentifier : undefined;
            resourceInputs["sourceRegion"] = args ? args.sourceRegion : undefined;
            resourceInputs["storageEncrypted"] = args ? args.storageEncrypted : undefined;
            resourceInputs["storageType"] = args ? args.storageType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["tdeCredentialArn"] = args ? args.tdeCredentialArn : undefined;
            resourceInputs["tdeCredentialPassword"] = args ? args.tdeCredentialPassword : undefined;
            resourceInputs["timezone"] = args ? args.timezone : undefined;
            resourceInputs["useDefaultProcessorFeatures"] = args ? args.useDefaultProcessorFeatures : undefined;
            resourceInputs["vPCSecurityGroups"] = args ? args.vPCSecurityGroups : undefined;
            resourceInputs["dBInstanceArn"] = undefined /*out*/;
            resourceInputs["dbiResourceId"] = undefined /*out*/;
        } else {
            resourceInputs["allocatedStorage"] = undefined /*out*/;
            resourceInputs["allowMajorVersionUpgrade"] = undefined /*out*/;
            resourceInputs["associatedRoles"] = undefined /*out*/;
            resourceInputs["autoMinorVersionUpgrade"] = undefined /*out*/;
            resourceInputs["availabilityZone"] = undefined /*out*/;
            resourceInputs["backupRetentionPeriod"] = undefined /*out*/;
            resourceInputs["cACertificateIdentifier"] = undefined /*out*/;
            resourceInputs["characterSetName"] = undefined /*out*/;
            resourceInputs["copyTagsToSnapshot"] = undefined /*out*/;
            resourceInputs["customIAMInstanceProfile"] = undefined /*out*/;
            resourceInputs["dBClusterIdentifier"] = undefined /*out*/;
            resourceInputs["dBInstanceArn"] = undefined /*out*/;
            resourceInputs["dBInstanceClass"] = undefined /*out*/;
            resourceInputs["dBInstanceIdentifier"] = undefined /*out*/;
            resourceInputs["dBName"] = undefined /*out*/;
            resourceInputs["dBParameterGroupName"] = undefined /*out*/;
            resourceInputs["dBSecurityGroups"] = undefined /*out*/;
            resourceInputs["dBSnapshotIdentifier"] = undefined /*out*/;
            resourceInputs["dBSubnetGroupName"] = undefined /*out*/;
            resourceInputs["dbiResourceId"] = undefined /*out*/;
            resourceInputs["deleteAutomatedBackups"] = undefined /*out*/;
            resourceInputs["deletionProtection"] = undefined /*out*/;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["domainIAMRoleName"] = undefined /*out*/;
            resourceInputs["enableCloudwatchLogsExports"] = undefined /*out*/;
            resourceInputs["enableIAMDatabaseAuthentication"] = undefined /*out*/;
            resourceInputs["enablePerformanceInsights"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["iops"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["licenseModel"] = undefined /*out*/;
            resourceInputs["masterUserPassword"] = undefined /*out*/;
            resourceInputs["masterUsername"] = undefined /*out*/;
            resourceInputs["maxAllocatedStorage"] = undefined /*out*/;
            resourceInputs["monitoringInterval"] = undefined /*out*/;
            resourceInputs["monitoringRoleArn"] = undefined /*out*/;
            resourceInputs["multiAZ"] = undefined /*out*/;
            resourceInputs["ncharCharacterSetName"] = undefined /*out*/;
            resourceInputs["networkType"] = undefined /*out*/;
            resourceInputs["optionGroupName"] = undefined /*out*/;
            resourceInputs["performanceInsightsKMSKeyId"] = undefined /*out*/;
            resourceInputs["performanceInsightsRetentionPeriod"] = undefined /*out*/;
            resourceInputs["port"] = undefined /*out*/;
            resourceInputs["preferredBackupWindow"] = undefined /*out*/;
            resourceInputs["preferredMaintenanceWindow"] = undefined /*out*/;
            resourceInputs["processorFeatures"] = undefined /*out*/;
            resourceInputs["promotionTier"] = undefined /*out*/;
            resourceInputs["publiclyAccessible"] = undefined /*out*/;
            resourceInputs["replicaMode"] = undefined /*out*/;
            resourceInputs["sourceDBInstanceIdentifier"] = undefined /*out*/;
            resourceInputs["sourceRegion"] = undefined /*out*/;
            resourceInputs["storageEncrypted"] = undefined /*out*/;
            resourceInputs["storageType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["tdeCredentialArn"] = undefined /*out*/;
            resourceInputs["tdeCredentialPassword"] = undefined /*out*/;
            resourceInputs["timezone"] = undefined /*out*/;
            resourceInputs["useDefaultProcessorFeatures"] = undefined /*out*/;
            resourceInputs["vPCSecurityGroups"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(DBInstance.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DBInstance resource.
 */
export interface DBInstanceArgs {
    /**
     * The amount of storage (in gigabytes) to be initially allocated for the database instance.
     */
    allocatedStorage?: pulumi.Input<string>;
    /**
     * A value that indicates whether major version upgrades are allowed. Changing this parameter doesn't result in an outage and the change is asynchronously applied as soon as possible.
     */
    allowMajorVersionUpgrade?: pulumi.Input<boolean>;
    /**
     * The AWS Identity and Access Management (IAM) roles associated with the DB instance.
     */
    associatedRoles?: pulumi.Input<pulumi.Input<inputs.rds.DBInstanceRoleArgs>[]>;
    /**
     * A value that indicates whether minor engine upgrades are applied automatically to the DB instance during the maintenance window. By default, minor engine upgrades are applied automatically.
     */
    autoMinorVersionUpgrade?: pulumi.Input<boolean>;
    /**
     * The Availability Zone (AZ) where the database will be created. For information on AWS Regions and Availability Zones.
     */
    availabilityZone?: pulumi.Input<string>;
    /**
     * The number of days for which automated backups are retained. Setting this parameter to a positive number enables backups. Setting this parameter to 0 disables automated backups.
     */
    backupRetentionPeriod?: pulumi.Input<number>;
    /**
     * The identifier of the CA certificate for this DB instance.
     */
    cACertificateIdentifier?: pulumi.Input<string>;
    /**
     * For supported engines, indicates that the DB instance should be associated with the specified character set.
     */
    characterSetName?: pulumi.Input<string>;
    /**
     * A value that indicates whether to copy tags from the DB instance to snapshots of the DB instance. By default, tags are not copied.
     */
    copyTagsToSnapshot?: pulumi.Input<boolean>;
    /**
     * The instance profile associated with the underlying Amazon EC2 instance of an RDS Custom DB instance. The instance profile must meet the following requirements:
     *  * The profile must exist in your account.
     *  * The profile must have an IAM role that Amazon EC2 has permissions to assume.
     *  * The instance profile name and the associated IAM role name must start with the prefix AWSRDSCustom .
     * For the list of permissions required for the IAM role, see Configure IAM and your VPC in the Amazon RDS User Guide .
     *
     * This setting is required for RDS Custom.
     */
    customIAMInstanceProfile?: pulumi.Input<string>;
    /**
     * The identifier of the DB cluster that the instance will belong to.
     */
    dBClusterIdentifier?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of the DB instance, for example, db.m4.large. Not all DB instance classes are available in all AWS Regions, or for all database engines.
     */
    dBInstanceClass?: pulumi.Input<string>;
    /**
     * A name for the DB instance. If you specify a name, AWS CloudFormation converts it to lowercase. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the DB instance.
     */
    dBInstanceIdentifier?: pulumi.Input<string>;
    /**
     * The meaning of this parameter differs according to the database engine you use.
     */
    dBName?: pulumi.Input<string>;
    /**
     * The name of an existing DB parameter group or a reference to an AWS::RDS::DBParameterGroup resource created in the template.
     */
    dBParameterGroupName?: pulumi.Input<string>;
    /**
     * A list of the DB security groups to assign to the DB instance. The list can include both the name of existing DB security groups or references to AWS::RDS::DBSecurityGroup resources created in the template.
     */
    dBSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name or Amazon Resource Name (ARN) of the DB snapshot that's used to restore the DB instance. If you're restoring from a shared manual DB snapshot, you must specify the ARN of the snapshot.
     */
    dBSnapshotIdentifier?: pulumi.Input<string>;
    /**
     * A DB subnet group to associate with the DB instance. If you update this value, the new subnet group must be a subnet group in a new VPC.
     */
    dBSubnetGroupName?: pulumi.Input<string>;
    /**
     * A value that indicates whether to remove automated backups immediately after the DB instance is deleted. This parameter isn't case-sensitive. The default is to remove automated backups immediately after the DB instance is deleted.
     */
    deleteAutomatedBackups?: pulumi.Input<boolean>;
    /**
     * A value that indicates whether the DB instance has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * The Active Directory directory ID to create the DB instance in. Currently, only MySQL, Microsoft SQL Server, Oracle, and PostgreSQL DB instances can be created in an Active Directory Domain.
     */
    domain?: pulumi.Input<string>;
    /**
     * Specify the name of the IAM role to be used when making API calls to the Directory Service.
     */
    domainIAMRoleName?: pulumi.Input<string>;
    /**
     * The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used.
     */
    enableCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
     */
    enableIAMDatabaseAuthentication?: pulumi.Input<boolean>;
    /**
     * A value that indicates whether to enable Performance Insights for the DB instance.
     */
    enablePerformanceInsights?: pulumi.Input<boolean>;
    /**
     * Specifies the connection endpoint.
     */
    endpoint?: pulumi.Input<inputs.rds.DBInstanceEndpointArgs>;
    /**
     * The name of the database engine that you want to use for this DB instance.
     */
    engine?: pulumi.Input<string>;
    /**
     * The version number of the database engine to use.
     */
    engineVersion?: pulumi.Input<string>;
    /**
     * The number of I/O operations per second (IOPS) that the database provisions.
     */
    iops?: pulumi.Input<number>;
    /**
     * The ARN of the AWS Key Management Service (AWS KMS) master key that's used to encrypt the DB instance.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * License model information for this DB instance.
     */
    licenseModel?: pulumi.Input<string>;
    /**
     * The password for the master user.
     */
    masterUserPassword?: pulumi.Input<string>;
    /**
     * The master user name for the DB instance.
     */
    masterUsername?: pulumi.Input<string>;
    /**
     * The upper limit to which Amazon RDS can automatically scale the storage of the DB instance.
     */
    maxAllocatedStorage?: pulumi.Input<number>;
    /**
     * The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB instance. To disable collecting Enhanced Monitoring metrics, specify 0. The default is 0.
     */
    monitoringInterval?: pulumi.Input<number>;
    /**
     * The ARN for the IAM role that permits RDS to send enhanced monitoring metrics to Amazon CloudWatch Logs.
     */
    monitoringRoleArn?: pulumi.Input<string>;
    /**
     * Specifies whether the database instance is a multiple Availability Zone deployment.
     */
    multiAZ?: pulumi.Input<boolean>;
    /**
     * The name of the NCHAR character set for the Oracle DB instance. This parameter doesn't apply to RDS Custom.
     */
    ncharCharacterSetName?: pulumi.Input<string>;
    /**
     * The network type of the DB cluster.
     */
    networkType?: pulumi.Input<string>;
    /**
     * Indicates that the DB instance should be associated with the specified option group.
     */
    optionGroupName?: pulumi.Input<string>;
    /**
     * The AWS KMS key identifier for encryption of Performance Insights data. The KMS key ID is the Amazon Resource Name (ARN), KMS key identifier, or the KMS key alias for the KMS encryption key.
     */
    performanceInsightsKMSKeyId?: pulumi.Input<string>;
    /**
     * The amount of time, in days, to retain Performance Insights data. Valid values are 7 or 731 (2 years).
     */
    performanceInsightsRetentionPeriod?: pulumi.Input<number>;
    /**
     * The port number on which the database accepts connections.
     */
    port?: pulumi.Input<string>;
    /**
     * The daily time range during which automated backups are created if automated backups are enabled, using the BackupRetentionPeriod parameter.
     */
    preferredBackupWindow?: pulumi.Input<string>;
    /**
     * he weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).
     */
    preferredMaintenanceWindow?: pulumi.Input<string>;
    /**
     * The number of CPU cores and the number of threads per core for the DB instance class of the DB instance.
     */
    processorFeatures?: pulumi.Input<pulumi.Input<inputs.rds.DBInstanceProcessorFeatureArgs>[]>;
    /**
     * A value that specifies the order in which an Aurora Replica is promoted to the primary instance after a failure of the existing primary instance.
     */
    promotionTier?: pulumi.Input<number>;
    /**
     * Indicates whether the DB instance is an internet-facing instance. If you specify true, AWS CloudFormation creates an instance with a publicly resolvable DNS name, which resolves to a public IP address. If you specify false, AWS CloudFormation creates an internal instance with a DNS name that resolves to a private IP address.
     */
    publiclyAccessible?: pulumi.Input<boolean>;
    /**
     * The open mode of an Oracle read replica. The default is open-read-only.
     */
    replicaMode?: pulumi.Input<string>;
    /**
     * If you want to create a Read Replica DB instance, specify the ID of the source DB instance. Each DB instance can have a limited number of Read Replicas.
     */
    sourceDBInstanceIdentifier?: pulumi.Input<string>;
    /**
     * The ID of the region that contains the source DB instance for the Read Replica.
     */
    sourceRegion?: pulumi.Input<string>;
    /**
     * A value that indicates whether the DB instance is encrypted. By default, it isn't encrypted.
     */
    storageEncrypted?: pulumi.Input<boolean>;
    /**
     * Specifies the storage type to be associated with the DB instance.
     */
    storageType?: pulumi.Input<string>;
    /**
     * Tags to assign to the DB instance.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.rds.DBInstanceTagArgs>[]>;
    /**
     * The ARN from the key store with which to associate the instance for TDE encryption.
     */
    tdeCredentialArn?: pulumi.Input<string>;
    /**
     * The password for the given ARN from the key store in order to access the device.
     */
    tdeCredentialPassword?: pulumi.Input<string>;
    /**
     * The time zone of the DB instance. The time zone parameter is currently supported only by Microsoft SQL Server.
     */
    timezone?: pulumi.Input<string>;
    /**
     * A value that indicates whether the DB instance class of the DB instance uses its default processor features.
     */
    useDefaultProcessorFeatures?: pulumi.Input<boolean>;
    /**
     * A list of the VPC security group IDs to assign to the DB instance. The list can include both the physical IDs of existing VPC security groups and references to AWS::EC2::SecurityGroup resources created in the template.
     */
    vPCSecurityGroups?: pulumi.Input<pulumi.Input<string>[]>;
}
