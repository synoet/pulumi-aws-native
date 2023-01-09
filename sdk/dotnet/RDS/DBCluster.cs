// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    /// <summary>
    /// The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:DBCluster")]
    public partial class DBCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        [Output("allocatedStorage")]
        public Output<int?> AllocatedStorage { get; private set; } = null!;

        /// <summary>
        /// Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
        /// </summary>
        [Output("associatedRoles")]
        public Output<ImmutableArray<Outputs.DBClusterRole>> AssociatedRoles { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
        /// </summary>
        [Output("autoMinorVersionUpgrade")]
        public Output<bool?> AutoMinorVersionUpgrade { get; private set; } = null!;

        /// <summary>
        /// A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.
        /// </summary>
        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        /// <summary>
        /// The target backtrack window, in seconds. To disable backtracking, set this value to 0.
        /// </summary>
        [Output("backtrackWindow")]
        public Output<int?> BacktrackWindow { get; private set; } = null!;

        /// <summary>
        /// The number of days for which automated backups are retained.
        /// </summary>
        [Output("backupRetentionPeriod")]
        public Output<int?> BackupRetentionPeriod { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
        /// </summary>
        [Output("copyTagsToSnapshot")]
        public Output<bool?> CopyTagsToSnapshot { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) for the DB cluster.
        /// </summary>
        [Output("dBClusterArn")]
        public Output<string> DBClusterArn { get; private set; } = null!;

        /// <summary>
        /// The DB cluster identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Output("dBClusterIdentifier")]
        public Output<string?> DBClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
        /// </summary>
        [Output("dBClusterInstanceClass")]
        public Output<string?> DBClusterInstanceClass { get; private set; } = null!;

        /// <summary>
        /// The name of the DB cluster parameter group to associate with this DB cluster.
        /// </summary>
        [Output("dBClusterParameterGroupName")]
        public Output<string?> DBClusterParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// The AWS Region-unique, immutable identifier for the DB cluster.
        /// </summary>
        [Output("dBClusterResourceId")]
        public Output<string> DBClusterResourceId { get; private set; } = null!;

        /// <summary>
        /// The name of the DB parameter group to apply to all instances of the DB cluster.
        /// </summary>
        [Output("dBInstanceParameterGroupName")]
        public Output<string?> DBInstanceParameterGroupName { get; private set; } = null!;

        /// <summary>
        /// A DB subnet group that you want to associate with this DB cluster.
        /// </summary>
        [Output("dBSubnetGroupName")]
        public Output<string?> DBSubnetGroupName { get; private set; } = null!;

        /// <summary>
        /// Reserved for future use.
        /// </summary>
        [Output("dBSystemId")]
        public Output<string?> DBSystemId { get; private set; } = null!;

        /// <summary>
        /// The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.
        /// </summary>
        [Output("databaseName")]
        public Output<string?> DatabaseName { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        /// </summary>
        [Output("deletionProtection")]
        public Output<bool?> DeletionProtection { get; private set; } = null!;

        /// <summary>
        /// The Active Directory directory ID to create the DB cluster in.
        /// </summary>
        [Output("domain")]
        public Output<string?> Domain { get; private set; } = null!;

        /// <summary>
        /// Specify the name of the IAM role to be used when making API calls to the Directory Service.
        /// </summary>
        [Output("domainIAMRoleName")]
        public Output<string?> DomainIAMRoleName { get; private set; } = null!;

        /// <summary>
        /// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
        /// </summary>
        [Output("enableCloudwatchLogsExports")]
        public Output<ImmutableArray<string>> EnableCloudwatchLogsExports { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
        /// </summary>
        [Output("enableHttpEndpoint")]
        public Output<bool?> EnableHttpEndpoint { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        /// </summary>
        [Output("enableIAMDatabaseAuthentication")]
        public Output<bool?> EnableIAMDatabaseAuthentication { get; private set; } = null!;

        [Output("endpoint")]
        public Output<Outputs.DBClusterEndpoint> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
        /// </summary>
        [Output("engine")]
        public Output<string?> Engine { get; private set; } = null!;

        /// <summary>
        /// The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.
        /// </summary>
        [Output("engineMode")]
        public Output<string?> EngineMode { get; private set; } = null!;

        /// <summary>
        /// The version number of the database engine to use.
        /// </summary>
        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        /// <summary>
        /// If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
        /// 
        /// If you aren't configuring a global database cluster, don't specify this property.
        /// </summary>
        [Output("globalClusterIdentifier")]
        public Output<string?> GlobalClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        [Output("iops")]
        public Output<int?> Iops { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to manage the master user password with AWS Secrets Manager.
        /// </summary>
        [Output("manageMasterUserPassword")]
        public Output<bool?> ManageMasterUserPassword { get; private set; } = null!;

        /// <summary>
        /// The master password for the DB instance.
        /// </summary>
        [Output("masterUserPassword")]
        public Output<string?> MasterUserPassword { get; private set; } = null!;

        /// <summary>
        /// Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
        /// </summary>
        [Output("masterUserSecret")]
        public Output<Outputs.DBClusterMasterUserSecret?> MasterUserSecret { get; private set; } = null!;

        /// <summary>
        /// The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
        /// </summary>
        [Output("masterUsername")]
        public Output<string?> MasterUsername { get; private set; } = null!;

        /// <summary>
        /// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        /// </summary>
        [Output("monitoringInterval")]
        public Output<int?> MonitoringInterval { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        /// </summary>
        [Output("monitoringRoleArn")]
        public Output<string?> MonitoringRoleArn { get; private set; } = null!;

        /// <summary>
        /// The network type of the DB cluster.
        /// </summary>
        [Output("networkType")]
        public Output<string?> NetworkType { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to turn on Performance Insights for the DB cluster.
        /// </summary>
        [Output("performanceInsightsEnabled")]
        public Output<bool?> PerformanceInsightsEnabled { get; private set; } = null!;

        /// <summary>
        /// The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
        /// </summary>
        [Output("performanceInsightsKmsKeyId")]
        public Output<string?> PerformanceInsightsKmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The amount of time, in days, to retain Performance Insights data.
        /// </summary>
        [Output("performanceInsightsRetentionPeriod")]
        public Output<int?> PerformanceInsightsRetentionPeriod { get; private set; } = null!;

        /// <summary>
        /// The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
        /// </summary>
        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        [Output("preferredBackupWindow")]
        public Output<string?> PreferredBackupWindow { get; private set; } = null!;

        /// <summary>
        /// The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether the DB cluster is publicly accessible.
        /// </summary>
        [Output("publiclyAccessible")]
        public Output<bool?> PubliclyAccessible { get; private set; } = null!;

        [Output("readEndpoint")]
        public Output<Outputs.DBClusterReadEndpoint?> ReadEndpoint { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
        /// </summary>
        [Output("replicationSourceIdentifier")]
        public Output<string?> ReplicationSourceIdentifier { get; private set; } = null!;

        /// <summary>
        /// The type of restore to be performed. You can specify one of the following values:
        /// full-copy - The new DB cluster is restored as a full copy of the source DB cluster.
        /// copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.
        /// </summary>
        [Output("restoreType")]
        public Output<string?> RestoreType { get; private set; } = null!;

        /// <summary>
        /// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
        /// </summary>
        [Output("scalingConfiguration")]
        public Output<Outputs.DBClusterScalingConfiguration?> ScalingConfiguration { get; private set; } = null!;

        /// <summary>
        /// Contains the scaling configuration of an Aurora Serverless v2 DB cluster.
        /// </summary>
        [Output("serverlessV2ScalingConfiguration")]
        public Output<Outputs.DBClusterServerlessV2ScalingConfiguration?> ServerlessV2ScalingConfiguration { get; private set; } = null!;

        /// <summary>
        /// The identifier for the DB snapshot or DB cluster snapshot to restore from.
        /// You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
        /// After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.
        /// </summary>
        [Output("snapshotIdentifier")]
        public Output<string?> SnapshotIdentifier { get; private set; } = null!;

        /// <summary>
        /// The identifier of the source DB cluster from which to restore.
        /// </summary>
        [Output("sourceDBClusterIdentifier")]
        public Output<string?> SourceDBClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.
        /// </summary>
        [Output("sourceRegion")]
        public Output<string?> SourceRegion { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the DB instance is encrypted.
        /// If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.
        /// </summary>
        [Output("storageEncrypted")]
        public Output<bool?> StorageEncrypted { get; private set; } = null!;

        /// <summary>
        /// Specifies the storage type to be associated with the DB cluster.
        /// </summary>
        [Output("storageType")]
        public Output<string?> StorageType { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DBClusterTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.
        /// </summary>
        [Output("useLatestRestorableTime")]
        public Output<bool?> UseLatestRestorableTime { get; private set; } = null!;

        /// <summary>
        /// A list of EC2 VPC security groups to associate with this DB cluster.
        /// </summary>
        [Output("vpcSecurityGroupIds")]
        public Output<ImmutableArray<string>> VpcSecurityGroupIds { get; private set; } = null!;


        /// <summary>
        /// Create a DBCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DBCluster(string name, DBClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:rds:DBCluster", name, args ?? new DBClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DBCluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:DBCluster", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing DBCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DBCluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DBCluster(name, id, options);
        }
    }

    public sealed class DBClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        [Input("allocatedStorage")]
        public Input<int>? AllocatedStorage { get; set; }

        [Input("associatedRoles")]
        private InputList<Inputs.DBClusterRoleArgs>? _associatedRoles;

        /// <summary>
        /// Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
        /// </summary>
        public InputList<Inputs.DBClusterRoleArgs> AssociatedRoles
        {
            get => _associatedRoles ?? (_associatedRoles = new InputList<Inputs.DBClusterRoleArgs>());
            set => _associatedRoles = value;
        }

        /// <summary>
        /// A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
        /// </summary>
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;

        /// <summary>
        /// A list of Availability Zones (AZs) where instances in the DB cluster can be created. For information on AWS Regions and Availability Zones, see Choosing the Regions and Availability Zones in the Amazon Aurora User Guide.
        /// </summary>
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        /// <summary>
        /// The target backtrack window, in seconds. To disable backtracking, set this value to 0.
        /// </summary>
        [Input("backtrackWindow")]
        public Input<int>? BacktrackWindow { get; set; }

        /// <summary>
        /// The number of days for which automated backups are retained.
        /// </summary>
        [Input("backupRetentionPeriod")]
        public Input<int>? BackupRetentionPeriod { get; set; }

        /// <summary>
        /// A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
        /// </summary>
        [Input("copyTagsToSnapshot")]
        public Input<bool>? CopyTagsToSnapshot { get; set; }

        /// <summary>
        /// The DB cluster identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("dBClusterIdentifier")]
        public Input<string>? DBClusterIdentifier { get; set; }

        /// <summary>
        /// The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
        /// </summary>
        [Input("dBClusterInstanceClass")]
        public Input<string>? DBClusterInstanceClass { get; set; }

        /// <summary>
        /// The name of the DB cluster parameter group to associate with this DB cluster.
        /// </summary>
        [Input("dBClusterParameterGroupName")]
        public Input<string>? DBClusterParameterGroupName { get; set; }

        /// <summary>
        /// The name of the DB parameter group to apply to all instances of the DB cluster.
        /// </summary>
        [Input("dBInstanceParameterGroupName")]
        public Input<string>? DBInstanceParameterGroupName { get; set; }

        /// <summary>
        /// A DB subnet group that you want to associate with this DB cluster.
        /// </summary>
        [Input("dBSubnetGroupName")]
        public Input<string>? DBSubnetGroupName { get; set; }

        /// <summary>
        /// Reserved for future use.
        /// </summary>
        [Input("dBSystemId")]
        public Input<string>? DBSystemId { get; set; }

        /// <summary>
        /// The name of your database. If you don't provide a name, then Amazon RDS won't create a database in this DB cluster. For naming constraints, see Naming Constraints in the Amazon RDS User Guide.
        /// </summary>
        [Input("databaseName")]
        public Input<string>? DatabaseName { get; set; }

        /// <summary>
        /// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        /// </summary>
        [Input("deletionProtection")]
        public Input<bool>? DeletionProtection { get; set; }

        /// <summary>
        /// The Active Directory directory ID to create the DB cluster in.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Specify the name of the IAM role to be used when making API calls to the Directory Service.
        /// </summary>
        [Input("domainIAMRoleName")]
        public Input<string>? DomainIAMRoleName { get; set; }

        [Input("enableCloudwatchLogsExports")]
        private InputList<string>? _enableCloudwatchLogsExports;

        /// <summary>
        /// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
        /// </summary>
        public InputList<string> EnableCloudwatchLogsExports
        {
            get => _enableCloudwatchLogsExports ?? (_enableCloudwatchLogsExports = new InputList<string>());
            set => _enableCloudwatchLogsExports = value;
        }

        /// <summary>
        /// A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
        /// </summary>
        [Input("enableHttpEndpoint")]
        public Input<bool>? EnableHttpEndpoint { get; set; }

        /// <summary>
        /// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        /// </summary>
        [Input("enableIAMDatabaseAuthentication")]
        public Input<bool>? EnableIAMDatabaseAuthentication { get; set; }

        /// <summary>
        /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// The DB engine mode of the DB cluster, either provisioned, serverless, parallelquery, global, or multimaster.
        /// </summary>
        [Input("engineMode")]
        public Input<string>? EngineMode { get; set; }

        /// <summary>
        /// The version number of the database engine to use.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
        /// 
        /// If you aren't configuring a global database cluster, don't specify this property.
        /// </summary>
        [Input("globalClusterIdentifier")]
        public Input<string>? GlobalClusterIdentifier { get; set; }

        /// <summary>
        /// The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        [Input("iops")]
        public Input<int>? Iops { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the AWS Key Management Service master key that is used to encrypt the database instances in the DB cluster, such as arn:aws:kms:us-east-1:012345678910:key/abcd1234-a123-456a-a12b-a123b4cd56ef. If you enable the StorageEncrypted property but don't specify this property, the default master key is used. If you specify this property, you must set the StorageEncrypted property to true.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// A value that indicates whether to manage the master user password with AWS Secrets Manager.
        /// </summary>
        [Input("manageMasterUserPassword")]
        public Input<bool>? ManageMasterUserPassword { get; set; }

        /// <summary>
        /// The master password for the DB instance.
        /// </summary>
        [Input("masterUserPassword")]
        public Input<string>? MasterUserPassword { get; set; }

        /// <summary>
        /// Contains the secret managed by RDS in AWS Secrets Manager for the master user password.
        /// </summary>
        [Input("masterUserSecret")]
        public Input<Inputs.DBClusterMasterUserSecretArgs>? MasterUserSecret { get; set; }

        /// <summary>
        /// The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
        /// </summary>
        [Input("masterUsername")]
        public Input<string>? MasterUsername { get; set; }

        /// <summary>
        /// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        /// </summary>
        [Input("monitoringInterval")]
        public Input<int>? MonitoringInterval { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        /// </summary>
        [Input("monitoringRoleArn")]
        public Input<string>? MonitoringRoleArn { get; set; }

        /// <summary>
        /// The network type of the DB cluster.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        /// <summary>
        /// A value that indicates whether to turn on Performance Insights for the DB cluster.
        /// </summary>
        [Input("performanceInsightsEnabled")]
        public Input<bool>? PerformanceInsightsEnabled { get; set; }

        /// <summary>
        /// The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
        /// </summary>
        [Input("performanceInsightsKmsKeyId")]
        public Input<string>? PerformanceInsightsKmsKeyId { get; set; }

        /// <summary>
        /// The amount of time, in days, to retain Performance Insights data.
        /// </summary>
        [Input("performanceInsightsRetentionPeriod")]
        public Input<int>? PerformanceInsightsRetentionPeriod { get; set; }

        /// <summary>
        /// The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        /// <summary>
        /// The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        /// <summary>
        /// A value that indicates whether the DB cluster is publicly accessible.
        /// </summary>
        [Input("publiclyAccessible")]
        public Input<bool>? PubliclyAccessible { get; set; }

        [Input("readEndpoint")]
        public Input<Inputs.DBClusterReadEndpointArgs>? ReadEndpoint { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
        /// </summary>
        [Input("replicationSourceIdentifier")]
        public Input<string>? ReplicationSourceIdentifier { get; set; }

        /// <summary>
        /// The type of restore to be performed. You can specify one of the following values:
        /// full-copy - The new DB cluster is restored as a full copy of the source DB cluster.
        /// copy-on-write - The new DB cluster is restored as a clone of the source DB cluster.
        /// </summary>
        [Input("restoreType")]
        public Input<string>? RestoreType { get; set; }

        /// <summary>
        /// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
        /// </summary>
        [Input("scalingConfiguration")]
        public Input<Inputs.DBClusterScalingConfigurationArgs>? ScalingConfiguration { get; set; }

        /// <summary>
        /// Contains the scaling configuration of an Aurora Serverless v2 DB cluster.
        /// </summary>
        [Input("serverlessV2ScalingConfiguration")]
        public Input<Inputs.DBClusterServerlessV2ScalingConfigurationArgs>? ServerlessV2ScalingConfiguration { get; set; }

        /// <summary>
        /// The identifier for the DB snapshot or DB cluster snapshot to restore from.
        /// You can use either the name or the Amazon Resource Name (ARN) to specify a DB cluster snapshot. However, you can use only the ARN to specify a DB snapshot.
        /// After you restore a DB cluster with a SnapshotIdentifier property, you must specify the same SnapshotIdentifier property for any future updates to the DB cluster. When you specify this property for an update, the DB cluster is not restored from the snapshot again, and the data in the database is not changed. However, if you don't specify the SnapshotIdentifier property, an empty DB cluster is created, and the original DB cluster is deleted. If you specify a property that is different from the previous snapshot restore property, the DB cluster is restored from the specified SnapshotIdentifier property, and the original DB cluster is deleted.
        /// </summary>
        [Input("snapshotIdentifier")]
        public Input<string>? SnapshotIdentifier { get; set; }

        /// <summary>
        /// The identifier of the source DB cluster from which to restore.
        /// </summary>
        [Input("sourceDBClusterIdentifier")]
        public Input<string>? SourceDBClusterIdentifier { get; set; }

        /// <summary>
        /// The AWS Region which contains the source DB cluster when replicating a DB cluster. For example, us-east-1.
        /// </summary>
        [Input("sourceRegion")]
        public Input<string>? SourceRegion { get; set; }

        /// <summary>
        /// Indicates whether the DB instance is encrypted.
        /// If you specify the DBClusterIdentifier, SnapshotIdentifier, or SourceDBInstanceIdentifier property, don't specify this property. The value is inherited from the cluster, snapshot, or source DB instance.
        /// </summary>
        [Input("storageEncrypted")]
        public Input<bool>? StorageEncrypted { get; set; }

        /// <summary>
        /// Specifies the storage type to be associated with the DB cluster.
        /// </summary>
        [Input("storageType")]
        public Input<string>? StorageType { get; set; }

        [Input("tags")]
        private InputList<Inputs.DBClusterTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.DBClusterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DBClusterTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// A value that indicates whether to restore the DB cluster to the latest restorable backup time. By default, the DB cluster is not restored to the latest restorable backup time.
        /// </summary>
        [Input("useLatestRestorableTime")]
        public Input<bool>? UseLatestRestorableTime { get; set; }

        [Input("vpcSecurityGroupIds")]
        private InputList<string>? _vpcSecurityGroupIds;

        /// <summary>
        /// A list of EC2 VPC security groups to associate with this DB cluster.
        /// </summary>
        public InputList<string> VpcSecurityGroupIds
        {
            get => _vpcSecurityGroupIds ?? (_vpcSecurityGroupIds = new InputList<string>());
            set => _vpcSecurityGroupIds = value;
        }

        public DBClusterArgs()
        {
        }
        public static new DBClusterArgs Empty => new DBClusterArgs();
    }
}
