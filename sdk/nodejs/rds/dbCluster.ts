// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.
 */
export class DbCluster extends pulumi.CustomResource {
    /**
     * Get an existing DbCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): DbCluster {
        return new DbCluster(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:rds:DbCluster';

    /**
     * Returns true if the given object is an instance of DbCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is DbCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === DbCluster.__pulumiType;
    }

    /**
     * The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
     */
    public readonly allocatedStorage!: pulumi.Output<number | undefined>;
    /**
     * Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
     */
    public readonly associatedRoles!: pulumi.Output<outputs.rds.DbClusterDbClusterRole[] | undefined>;
    /**
     * A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
     */
    public readonly autoMinorVersionUpgrade!: pulumi.Output<boolean | undefined>;
    /**
     * A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.
     */
    public readonly availabilityZones!: pulumi.Output<string[] | undefined>;
    /**
     * The target backtrack window, in seconds. To disable backtracking, set this value to 0.
     */
    public readonly backtrackWindow!: pulumi.Output<number | undefined>;
    /**
     * The number of days for which automated backups are retained.
     */
    public readonly backupRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
     */
    public readonly copyTagsToSnapshot!: pulumi.Output<boolean | undefined>;
    /**
     * The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.
     */
    public readonly databaseName!: pulumi.Output<string | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the DB cluster.
     */
    public /*out*/ readonly dbClusterArn!: pulumi.Output<string>;
    /**
     * The DB cluster identifier. This parameter is stored as a lowercase string.
     */
    public readonly dbClusterIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
     */
    public readonly dbClusterInstanceClass!: pulumi.Output<string | undefined>;
    /**
     * The name of the DB cluster parameter group to associate with this DB cluster.
     */
    public readonly dbClusterParameterGroupName!: pulumi.Output<string | undefined>;
    /**
     * The AWS Region-unique, immutable identifier for the DB cluster.
     */
    public /*out*/ readonly dbClusterResourceId!: pulumi.Output<string>;
    /**
     * The name of the DB parameter group to apply to all instances of the DB cluster.
     */
    public readonly dbInstanceParameterGroupName!: pulumi.Output<string | undefined>;
    /**
     * A DB subnet group that you want to associate with this DB cluster.
     */
    public readonly dbSubnetGroupName!: pulumi.Output<string | undefined>;
    /**
     * Reserved for future use.
     */
    public readonly dbSystemId!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
     */
    public readonly deletionProtection!: pulumi.Output<boolean | undefined>;
    /**
     * The Active Directory directory ID to create the DB cluster in.
     */
    public readonly domain!: pulumi.Output<string | undefined>;
    /**
     * Specify the name of the IAM role to be used when making API calls to the Directory Service.
     */
    public readonly domainIamRoleName!: pulumi.Output<string | undefined>;
    /**
     * The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
     */
    public readonly enableCloudwatchLogsExports!: pulumi.Output<string[] | undefined>;
    /**
     * A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
     */
    public readonly enableHttpEndpoint!: pulumi.Output<boolean | undefined>;
    /**
     * A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
     */
    public readonly enableIamDatabaseAuthentication!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly endpoint!: pulumi.Output<outputs.rds.DbClusterEndpoint>;
    /**
     * The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
     */
    public readonly engine!: pulumi.Output<string | undefined>;
    /**
     * The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.
     */
    public readonly engineMode!: pulumi.Output<string | undefined>;
    /**
     * The version number of the database engine to use.
     */
    public readonly engineVersion!: pulumi.Output<string | undefined>;
    /**
     * If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
     *
     * If you aren't configuring a global database cluster, don't specify this property.
     */
    public readonly globalClusterIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
     */
    public readonly iops!: pulumi.Output<number | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.
     */
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether to manage the master user password with AWS Secrets Manager.
     */
    public readonly manageMasterUserPassword!: pulumi.Output<boolean | undefined>;
    /**
     * The master password for the DB instance.
     */
    public readonly masterUserPassword!: pulumi.Output<string | undefined>;
    /**
     * Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
     */
    public readonly masterUserSecret!: pulumi.Output<outputs.rds.DbClusterMasterUserSecret | undefined>;
    /**
     * The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
     */
    public readonly masterUsername!: pulumi.Output<string | undefined>;
    /**
     * The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
     */
    public readonly monitoringInterval!: pulumi.Output<number | undefined>;
    /**
     * The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
     */
    public readonly monitoringRoleArn!: pulumi.Output<string | undefined>;
    /**
     * The network type of the DB cluster.
     */
    public readonly networkType!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether to turn on Performance Insights for the DB cluster.
     */
    public readonly performanceInsightsEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
     */
    public readonly performanceInsightsKmsKeyId!: pulumi.Output<string | undefined>;
    /**
     * The amount of time, in days, to retain Performance Insights data.
     */
    public readonly performanceInsightsRetentionPeriod!: pulumi.Output<number | undefined>;
    /**
     * The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
     */
    public readonly port!: pulumi.Output<number | undefined>;
    /**
     * The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
     */
    public readonly preferredBackupWindow!: pulumi.Output<string | undefined>;
    /**
     * The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
     */
    public readonly preferredMaintenanceWindow!: pulumi.Output<string | undefined>;
    /**
     * A value that indicates whether the DB cluster is publicly accessible.
     */
    public readonly publiclyAccessible!: pulumi.Output<boolean | undefined>;
    public readonly readEndpoint!: pulumi.Output<outputs.rds.DbClusterReadEndpoint | undefined>;
    /**
     * The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
     */
    public readonly replicationSourceIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The date and time to restore the DB cluster to. Value must be a time in Universal Coordinated Time (UTC) format. An example: 2015-03-07T23:45:00Z
     */
    public readonly restoreToTime!: pulumi.Output<string | undefined>;
    /**
     * The type of restore to be performed. You can specify one of the following values:
     * full-copy - The new DB cluster is restored as a full copy of the source DB cluster.
     * copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.
     */
    public readonly restoreType!: pulumi.Output<string | undefined>;
    /**
     * The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
     */
    public readonly scalingConfiguration!: pulumi.Output<outputs.rds.DbClusterScalingConfiguration | undefined>;
    /**
     * Contains the scaling configuration of an Aurora Serverless v2 DB cluster.
     */
    public readonly serverlessV2ScalingConfiguration!: pulumi.Output<outputs.rds.DbClusterServerlessV2ScalingConfiguration | undefined>;
    /**
     * The identifier for the DB snapshot or DB cluster snapshot to restore from.
     * You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
     * After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.
     */
    public readonly snapshotIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The identifier of the source DB cluster from which to restore.
     */
    public readonly sourceDbClusterIdentifier!: pulumi.Output<string | undefined>;
    /**
     * The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.
     */
    public readonly sourceRegion!: pulumi.Output<string | undefined>;
    /**
     * Indicates whether the DB instance is encrypted.
     * If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.
     */
    public readonly storageEncrypted!: pulumi.Output<boolean | undefined>;
    /**
     * Specifies the storage type to be associated with the DB cluster.
     */
    public readonly storageType!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.rds.DbClusterTag[] | undefined>;
    /**
     * A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.
     */
    public readonly useLatestRestorableTime!: pulumi.Output<boolean | undefined>;
    /**
     * A list of EC2 VPC security groups to associate with this DB cluster.
     */
    public readonly vpcSecurityGroupIds!: pulumi.Output<string[] | undefined>;

    /**
     * Create a DbCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DbClusterArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["allocatedStorage"] = args ? args.allocatedStorage : undefined;
            resourceInputs["associatedRoles"] = args ? args.associatedRoles : undefined;
            resourceInputs["autoMinorVersionUpgrade"] = args ? args.autoMinorVersionUpgrade : undefined;
            resourceInputs["availabilityZones"] = args ? args.availabilityZones : undefined;
            resourceInputs["backtrackWindow"] = args ? args.backtrackWindow : undefined;
            resourceInputs["backupRetentionPeriod"] = args ? args.backupRetentionPeriod : undefined;
            resourceInputs["copyTagsToSnapshot"] = args ? args.copyTagsToSnapshot : undefined;
            resourceInputs["databaseName"] = args ? args.databaseName : undefined;
            resourceInputs["dbClusterIdentifier"] = args ? args.dbClusterIdentifier : undefined;
            resourceInputs["dbClusterInstanceClass"] = args ? args.dbClusterInstanceClass : undefined;
            resourceInputs["dbClusterParameterGroupName"] = args ? args.dbClusterParameterGroupName : undefined;
            resourceInputs["dbInstanceParameterGroupName"] = args ? args.dbInstanceParameterGroupName : undefined;
            resourceInputs["dbSubnetGroupName"] = args ? args.dbSubnetGroupName : undefined;
            resourceInputs["dbSystemId"] = args ? args.dbSystemId : undefined;
            resourceInputs["deletionProtection"] = args ? args.deletionProtection : undefined;
            resourceInputs["domain"] = args ? args.domain : undefined;
            resourceInputs["domainIamRoleName"] = args ? args.domainIamRoleName : undefined;
            resourceInputs["enableCloudwatchLogsExports"] = args ? args.enableCloudwatchLogsExports : undefined;
            resourceInputs["enableHttpEndpoint"] = args ? args.enableHttpEndpoint : undefined;
            resourceInputs["enableIamDatabaseAuthentication"] = args ? args.enableIamDatabaseAuthentication : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["engineMode"] = args ? args.engineMode : undefined;
            resourceInputs["engineVersion"] = args ? args.engineVersion : undefined;
            resourceInputs["globalClusterIdentifier"] = args ? args.globalClusterIdentifier : undefined;
            resourceInputs["iops"] = args ? args.iops : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["manageMasterUserPassword"] = args ? args.manageMasterUserPassword : undefined;
            resourceInputs["masterUserPassword"] = args ? args.masterUserPassword : undefined;
            resourceInputs["masterUserSecret"] = args ? args.masterUserSecret : undefined;
            resourceInputs["masterUsername"] = args ? args.masterUsername : undefined;
            resourceInputs["monitoringInterval"] = args ? args.monitoringInterval : undefined;
            resourceInputs["monitoringRoleArn"] = args ? args.monitoringRoleArn : undefined;
            resourceInputs["networkType"] = args ? args.networkType : undefined;
            resourceInputs["performanceInsightsEnabled"] = args ? args.performanceInsightsEnabled : undefined;
            resourceInputs["performanceInsightsKmsKeyId"] = args ? args.performanceInsightsKmsKeyId : undefined;
            resourceInputs["performanceInsightsRetentionPeriod"] = args ? args.performanceInsightsRetentionPeriod : undefined;
            resourceInputs["port"] = args ? args.port : undefined;
            resourceInputs["preferredBackupWindow"] = args ? args.preferredBackupWindow : undefined;
            resourceInputs["preferredMaintenanceWindow"] = args ? args.preferredMaintenanceWindow : undefined;
            resourceInputs["publiclyAccessible"] = args ? args.publiclyAccessible : undefined;
            resourceInputs["readEndpoint"] = args ? args.readEndpoint : undefined;
            resourceInputs["replicationSourceIdentifier"] = args ? args.replicationSourceIdentifier : undefined;
            resourceInputs["restoreToTime"] = args ? args.restoreToTime : undefined;
            resourceInputs["restoreType"] = args ? args.restoreType : undefined;
            resourceInputs["scalingConfiguration"] = args ? args.scalingConfiguration : undefined;
            resourceInputs["serverlessV2ScalingConfiguration"] = args ? args.serverlessV2ScalingConfiguration : undefined;
            resourceInputs["snapshotIdentifier"] = args ? args.snapshotIdentifier : undefined;
            resourceInputs["sourceDbClusterIdentifier"] = args ? args.sourceDbClusterIdentifier : undefined;
            resourceInputs["sourceRegion"] = args ? args.sourceRegion : undefined;
            resourceInputs["storageEncrypted"] = args ? args.storageEncrypted : undefined;
            resourceInputs["storageType"] = args ? args.storageType : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["useLatestRestorableTime"] = args ? args.useLatestRestorableTime : undefined;
            resourceInputs["vpcSecurityGroupIds"] = args ? args.vpcSecurityGroupIds : undefined;
            resourceInputs["dbClusterArn"] = undefined /*out*/;
            resourceInputs["dbClusterResourceId"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
        } else {
            resourceInputs["allocatedStorage"] = undefined /*out*/;
            resourceInputs["associatedRoles"] = undefined /*out*/;
            resourceInputs["autoMinorVersionUpgrade"] = undefined /*out*/;
            resourceInputs["availabilityZones"] = undefined /*out*/;
            resourceInputs["backtrackWindow"] = undefined /*out*/;
            resourceInputs["backupRetentionPeriod"] = undefined /*out*/;
            resourceInputs["copyTagsToSnapshot"] = undefined /*out*/;
            resourceInputs["databaseName"] = undefined /*out*/;
            resourceInputs["dbClusterArn"] = undefined /*out*/;
            resourceInputs["dbClusterIdentifier"] = undefined /*out*/;
            resourceInputs["dbClusterInstanceClass"] = undefined /*out*/;
            resourceInputs["dbClusterParameterGroupName"] = undefined /*out*/;
            resourceInputs["dbClusterResourceId"] = undefined /*out*/;
            resourceInputs["dbInstanceParameterGroupName"] = undefined /*out*/;
            resourceInputs["dbSubnetGroupName"] = undefined /*out*/;
            resourceInputs["dbSystemId"] = undefined /*out*/;
            resourceInputs["deletionProtection"] = undefined /*out*/;
            resourceInputs["domain"] = undefined /*out*/;
            resourceInputs["domainIamRoleName"] = undefined /*out*/;
            resourceInputs["enableCloudwatchLogsExports"] = undefined /*out*/;
            resourceInputs["enableHttpEndpoint"] = undefined /*out*/;
            resourceInputs["enableIamDatabaseAuthentication"] = undefined /*out*/;
            resourceInputs["endpoint"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["engineMode"] = undefined /*out*/;
            resourceInputs["engineVersion"] = undefined /*out*/;
            resourceInputs["globalClusterIdentifier"] = undefined /*out*/;
            resourceInputs["iops"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["manageMasterUserPassword"] = undefined /*out*/;
            resourceInputs["masterUserPassword"] = undefined /*out*/;
            resourceInputs["masterUserSecret"] = undefined /*out*/;
            resourceInputs["masterUsername"] = undefined /*out*/;
            resourceInputs["monitoringInterval"] = undefined /*out*/;
            resourceInputs["monitoringRoleArn"] = undefined /*out*/;
            resourceInputs["networkType"] = undefined /*out*/;
            resourceInputs["performanceInsightsEnabled"] = undefined /*out*/;
            resourceInputs["performanceInsightsKmsKeyId"] = undefined /*out*/;
            resourceInputs["performanceInsightsRetentionPeriod"] = undefined /*out*/;
            resourceInputs["port"] = undefined /*out*/;
            resourceInputs["preferredBackupWindow"] = undefined /*out*/;
            resourceInputs["preferredMaintenanceWindow"] = undefined /*out*/;
            resourceInputs["publiclyAccessible"] = undefined /*out*/;
            resourceInputs["readEndpoint"] = undefined /*out*/;
            resourceInputs["replicationSourceIdentifier"] = undefined /*out*/;
            resourceInputs["restoreToTime"] = undefined /*out*/;
            resourceInputs["restoreType"] = undefined /*out*/;
            resourceInputs["scalingConfiguration"] = undefined /*out*/;
            resourceInputs["serverlessV2ScalingConfiguration"] = undefined /*out*/;
            resourceInputs["snapshotIdentifier"] = undefined /*out*/;
            resourceInputs["sourceDbClusterIdentifier"] = undefined /*out*/;
            resourceInputs["sourceRegion"] = undefined /*out*/;
            resourceInputs["storageEncrypted"] = undefined /*out*/;
            resourceInputs["storageType"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
            resourceInputs["useLatestRestorableTime"] = undefined /*out*/;
            resourceInputs["vpcSecurityGroupIds"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["availabilityZones[*]", "databaseName", "dbClusterIdentifier", "dbSubnetGroupName", "dbSystemId", "engineMode", "kmsKeyId", "publiclyAccessible", "restoreToTime", "restoreType", "snapshotIdentifier", "sourceDbClusterIdentifier", "sourceRegion", "storageEncrypted", "useLatestRestorableTime"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(DbCluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a DbCluster resource.
 */
export interface DbClusterArgs {
    /**
     * The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
     */
    allocatedStorage?: pulumi.Input<number>;
    /**
     * Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
     */
    associatedRoles?: pulumi.Input<pulumi.Input<inputs.rds.DbClusterDbClusterRoleArgs>[]>;
    /**
     * A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
     */
    autoMinorVersionUpgrade?: pulumi.Input<boolean>;
    /**
     * A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.
     */
    availabilityZones?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The target backtrack window, in seconds. To disable backtracking, set this value to 0.
     */
    backtrackWindow?: pulumi.Input<number>;
    /**
     * The number of days for which automated backups are retained.
     */
    backupRetentionPeriod?: pulumi.Input<number>;
    /**
     * A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
     */
    copyTagsToSnapshot?: pulumi.Input<boolean>;
    /**
     * The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.
     */
    databaseName?: pulumi.Input<string>;
    /**
     * The DB cluster identifier. This parameter is stored as a lowercase string.
     */
    dbClusterIdentifier?: pulumi.Input<string>;
    /**
     * The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
     */
    dbClusterInstanceClass?: pulumi.Input<string>;
    /**
     * The name of the DB cluster parameter group to associate with this DB cluster.
     */
    dbClusterParameterGroupName?: pulumi.Input<string>;
    /**
     * The name of the DB parameter group to apply to all instances of the DB cluster.
     */
    dbInstanceParameterGroupName?: pulumi.Input<string>;
    /**
     * A DB subnet group that you want to associate with this DB cluster.
     */
    dbSubnetGroupName?: pulumi.Input<string>;
    /**
     * Reserved for future use.
     */
    dbSystemId?: pulumi.Input<string>;
    /**
     * A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
     */
    deletionProtection?: pulumi.Input<boolean>;
    /**
     * The Active Directory directory ID to create the DB cluster in.
     */
    domain?: pulumi.Input<string>;
    /**
     * Specify the name of the IAM role to be used when making API calls to the Directory Service.
     */
    domainIamRoleName?: pulumi.Input<string>;
    /**
     * The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
     */
    enableCloudwatchLogsExports?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
     */
    enableHttpEndpoint?: pulumi.Input<boolean>;
    /**
     * A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
     */
    enableIamDatabaseAuthentication?: pulumi.Input<boolean>;
    /**
     * The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
     */
    engine?: pulumi.Input<string>;
    /**
     * The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.
     */
    engineMode?: pulumi.Input<string>;
    /**
     * The version number of the database engine to use.
     */
    engineVersion?: pulumi.Input<string>;
    /**
     * If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
     *
     * If you aren't configuring a global database cluster, don't specify this property.
     */
    globalClusterIdentifier?: pulumi.Input<string>;
    /**
     * The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
     */
    iops?: pulumi.Input<number>;
    /**
     * The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.
     */
    kmsKeyId?: pulumi.Input<string>;
    /**
     * A value that indicates whether to manage the master user password with AWS Secrets Manager.
     */
    manageMasterUserPassword?: pulumi.Input<boolean>;
    /**
     * The master password for the DB instance.
     */
    masterUserPassword?: pulumi.Input<string>;
    /**
     * Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
     */
    masterUserSecret?: pulumi.Input<inputs.rds.DbClusterMasterUserSecretArgs>;
    /**
     * The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
     */
    masterUsername?: pulumi.Input<string>;
    /**
     * The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
     */
    monitoringInterval?: pulumi.Input<number>;
    /**
     * The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
     */
    monitoringRoleArn?: pulumi.Input<string>;
    /**
     * The network type of the DB cluster.
     */
    networkType?: pulumi.Input<string>;
    /**
     * A value that indicates whether to turn on Performance Insights for the DB cluster.
     */
    performanceInsightsEnabled?: pulumi.Input<boolean>;
    /**
     * The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
     */
    performanceInsightsKmsKeyId?: pulumi.Input<string>;
    /**
     * The amount of time, in days, to retain Performance Insights data.
     */
    performanceInsightsRetentionPeriod?: pulumi.Input<number>;
    /**
     * The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
     */
    port?: pulumi.Input<number>;
    /**
     * The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
     */
    preferredBackupWindow?: pulumi.Input<string>;
    /**
     * The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
     */
    preferredMaintenanceWindow?: pulumi.Input<string>;
    /**
     * A value that indicates whether the DB cluster is publicly accessible.
     */
    publiclyAccessible?: pulumi.Input<boolean>;
    readEndpoint?: pulumi.Input<inputs.rds.DbClusterReadEndpointArgs>;
    /**
     * The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
     */
    replicationSourceIdentifier?: pulumi.Input<string>;
    /**
     * The date and time to restore the DB cluster to. Value must be a time in Universal Coordinated Time (UTC) format. An example: 2015-03-07T23:45:00Z
     */
    restoreToTime?: pulumi.Input<string>;
    /**
     * The type of restore to be performed. You can specify one of the following values:
     * full-copy - The new DB cluster is restored as a full copy of the source DB cluster.
     * copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.
     */
    restoreType?: pulumi.Input<string>;
    /**
     * The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
     */
    scalingConfiguration?: pulumi.Input<inputs.rds.DbClusterScalingConfigurationArgs>;
    /**
     * Contains the scaling configuration of an Aurora Serverless v2 DB cluster.
     */
    serverlessV2ScalingConfiguration?: pulumi.Input<inputs.rds.DbClusterServerlessV2ScalingConfigurationArgs>;
    /**
     * The identifier for the DB snapshot or DB cluster snapshot to restore from.
     * You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
     * After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.
     */
    snapshotIdentifier?: pulumi.Input<string>;
    /**
     * The identifier of the source DB cluster from which to restore.
     */
    sourceDbClusterIdentifier?: pulumi.Input<string>;
    /**
     * The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.
     */
    sourceRegion?: pulumi.Input<string>;
    /**
     * Indicates whether the DB instance is encrypted.
     * If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.
     */
    storageEncrypted?: pulumi.Input<boolean>;
    /**
     * Specifies the storage type to be associated with the DB cluster.
     */
    storageType?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.rds.DbClusterTagArgs>[]>;
    /**
     * A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.
     */
    useLatestRestorableTime?: pulumi.Input<boolean>;
    /**
     * A list of EC2 VPC security groups to associate with this DB cluster.
     */
    vpcSecurityGroupIds?: pulumi.Input<pulumi.Input<string>[]>;
}
