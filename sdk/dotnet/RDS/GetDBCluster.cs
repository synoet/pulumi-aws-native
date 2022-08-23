// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    public static class GetDBCluster
    {
        /// <summary>
        /// The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.
        /// </summary>
        public static Task<GetDBClusterResult> InvokeAsync(GetDBClusterArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDBClusterResult>("aws-native:rds:getDBCluster", args ?? new GetDBClusterArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::RDS::DBCluster resource creates an Amazon Aurora DB cluster.
        /// </summary>
        public static Output<GetDBClusterResult> Invoke(GetDBClusterInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDBClusterResult>("aws-native:rds:getDBCluster", args ?? new GetDBClusterInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDBClusterArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The DB cluster identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("dBClusterIdentifier", required: true)]
        public string DBClusterIdentifier { get; set; } = null!;

        public GetDBClusterArgs()
        {
        }
        public static new GetDBClusterArgs Empty => new GetDBClusterArgs();
    }

    public sealed class GetDBClusterInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The DB cluster identifier. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("dBClusterIdentifier", required: true)]
        public Input<string> DBClusterIdentifier { get; set; } = null!;

        public GetDBClusterInvokeArgs()
        {
        }
        public static new GetDBClusterInvokeArgs Empty => new GetDBClusterInvokeArgs();
    }


    [OutputType]
    public sealed class GetDBClusterResult
    {
        /// <summary>
        /// The amount of storage in gibibytes (GiB) to allocate to each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        public readonly int? AllocatedStorage;
        /// <summary>
        /// Provides a list of the AWS Identity and Access Management (IAM) roles that are associated with the DB cluster. IAM roles that are associated with a DB cluster grant permission for the DB cluster to access other AWS services on your behalf.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBClusterRole> AssociatedRoles;
        /// <summary>
        /// A value that indicates whether minor engine upgrades are applied automatically to the DB cluster during the maintenance window. By default, minor engine upgrades are applied automatically.
        /// </summary>
        public readonly bool? AutoMinorVersionUpgrade;
        /// <summary>
        /// The target backtrack window, in seconds. To disable backtracking, set this value to 0.
        /// </summary>
        public readonly int? BacktrackWindow;
        /// <summary>
        /// The number of days for which automated backups are retained.
        /// </summary>
        public readonly int? BackupRetentionPeriod;
        /// <summary>
        /// A value that indicates whether to copy all tags from the DB cluster to snapshots of the DB cluster. The default is not to copy them.
        /// </summary>
        public readonly bool? CopyTagsToSnapshot;
        /// <summary>
        /// The compute and memory capacity of each DB instance in the Multi-AZ DB cluster, for example db.m6g.xlarge.
        /// </summary>
        public readonly string? DBClusterInstanceClass;
        /// <summary>
        /// The name of the DB cluster parameter group to associate with this DB cluster.
        /// </summary>
        public readonly string? DBClusterParameterGroupName;
        /// <summary>
        /// A value that indicates whether the DB cluster has deletion protection enabled. The database can't be deleted when deletion protection is enabled. By default, deletion protection is disabled.
        /// </summary>
        public readonly bool? DeletionProtection;
        /// <summary>
        /// The list of log types that need to be enabled for exporting to CloudWatch Logs. The values in the list depend on the DB engine being used. For more information, see Publishing Database Logs to Amazon CloudWatch Logs in the Amazon Aurora User Guide.
        /// </summary>
        public readonly ImmutableArray<string> EnableCloudwatchLogsExports;
        /// <summary>
        /// A value that indicates whether to enable the HTTP endpoint for an Aurora Serverless DB cluster. By default, the HTTP endpoint is disabled.
        /// </summary>
        public readonly bool? EnableHttpEndpoint;
        /// <summary>
        /// A value that indicates whether to enable mapping of AWS Identity and Access Management (IAM) accounts to database accounts. By default, mapping is disabled.
        /// </summary>
        public readonly bool? EnableIAMDatabaseAuthentication;
        public readonly Outputs.DBClusterEndpoint? Endpoint;
        /// <summary>
        /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora), and aurora-postgresql
        /// </summary>
        public readonly string? Engine;
        /// <summary>
        /// The version number of the database engine to use.
        /// </summary>
        public readonly string? EngineVersion;
        /// <summary>
        /// If you are configuring an Aurora global database cluster and want your Aurora DB cluster to be a secondary member in the global database cluster, specify the global cluster ID of the global database cluster. To define the primary database cluster of the global cluster, use the AWS::RDS::GlobalCluster resource.
        /// 
        /// If you aren't configuring a global database cluster, don't specify this property.
        /// </summary>
        public readonly string? GlobalClusterIdentifier;
        /// <summary>
        /// The amount of Provisioned IOPS (input/output operations per second) to be initially allocated for each DB instance in the Multi-AZ DB cluster.
        /// </summary>
        public readonly int? Iops;
        /// <summary>
        /// The name of the master user for the DB cluster. You must specify MasterUsername, unless you specify SnapshotIdentifier. In that case, don't specify MasterUsername.
        /// </summary>
        public readonly string? MasterUsername;
        /// <summary>
        /// The interval, in seconds, between points when Enhanced Monitoring metrics are collected for the DB cluster. To turn off collecting Enhanced Monitoring metrics, specify 0. The default is 0.
        /// </summary>
        public readonly int? MonitoringInterval;
        /// <summary>
        /// The Amazon Resource Name (ARN) for the IAM role that permits RDS to send Enhanced Monitoring metrics to Amazon CloudWatch Logs.
        /// </summary>
        public readonly string? MonitoringRoleArn;
        /// <summary>
        /// A value that indicates whether to turn on Performance Insights for the DB cluster.
        /// </summary>
        public readonly bool? PerformanceInsightsEnabled;
        /// <summary>
        /// The Amazon Web Services KMS key identifier for encryption of Performance Insights data.
        /// </summary>
        public readonly string? PerformanceInsightsKmsKeyId;
        /// <summary>
        /// The amount of time, in days, to retain Performance Insights data.
        /// </summary>
        public readonly int? PerformanceInsightsRetentionPeriod;
        /// <summary>
        /// The port number on which the instances in the DB cluster accept connections. Default: 3306 if engine is set as aurora or 5432 if set to aurora-postgresql.
        /// </summary>
        public readonly int? Port;
        /// <summary>
        /// The daily time range during which automated backups are created if automated backups are enabled using the BackupRetentionPeriod parameter. The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        public readonly string? PreferredBackupWindow;
        /// <summary>
        /// The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC). The default is a 30-minute window selected at random from an 8-hour block of time for each AWS Region, occurring on a random day of the week. To see the time blocks available, see Adjusting the Preferred DB Cluster Maintenance Window in the Amazon Aurora User Guide.
        /// </summary>
        public readonly string? PreferredMaintenanceWindow;
        public readonly Outputs.DBClusterReadEndpoint? ReadEndpoint;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the source DB instance or DB cluster if this DB cluster is created as a Read Replica.
        /// </summary>
        public readonly string? ReplicationSourceIdentifier;
        /// <summary>
        /// The ScalingConfiguration property type specifies the scaling configuration of an Aurora Serverless DB cluster.
        /// </summary>
        public readonly Outputs.DBClusterScalingConfiguration? ScalingConfiguration;
        /// <summary>
        /// Specifies the storage type to be associated with the DB cluster.
        /// </summary>
        public readonly string? StorageType;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBClusterTag> Tags;
        /// <summary>
        /// A list of EC2 VPC security groups to associate with this DB cluster.
        /// </summary>
        public readonly ImmutableArray<string> VpcSecurityGroupIds;

        [OutputConstructor]
        private GetDBClusterResult(
            int? allocatedStorage,

            ImmutableArray<Outputs.DBClusterRole> associatedRoles,

            bool? autoMinorVersionUpgrade,

            int? backtrackWindow,

            int? backupRetentionPeriod,

            bool? copyTagsToSnapshot,

            string? dBClusterInstanceClass,

            string? dBClusterParameterGroupName,

            bool? deletionProtection,

            ImmutableArray<string> enableCloudwatchLogsExports,

            bool? enableHttpEndpoint,

            bool? enableIAMDatabaseAuthentication,

            Outputs.DBClusterEndpoint? endpoint,

            string? engine,

            string? engineVersion,

            string? globalClusterIdentifier,

            int? iops,

            string? masterUsername,

            int? monitoringInterval,

            string? monitoringRoleArn,

            bool? performanceInsightsEnabled,

            string? performanceInsightsKmsKeyId,

            int? performanceInsightsRetentionPeriod,

            int? port,

            string? preferredBackupWindow,

            string? preferredMaintenanceWindow,

            Outputs.DBClusterReadEndpoint? readEndpoint,

            string? replicationSourceIdentifier,

            Outputs.DBClusterScalingConfiguration? scalingConfiguration,

            string? storageType,

            ImmutableArray<Outputs.DBClusterTag> tags,

            ImmutableArray<string> vpcSecurityGroupIds)
        {
            AllocatedStorage = allocatedStorage;
            AssociatedRoles = associatedRoles;
            AutoMinorVersionUpgrade = autoMinorVersionUpgrade;
            BacktrackWindow = backtrackWindow;
            BackupRetentionPeriod = backupRetentionPeriod;
            CopyTagsToSnapshot = copyTagsToSnapshot;
            DBClusterInstanceClass = dBClusterInstanceClass;
            DBClusterParameterGroupName = dBClusterParameterGroupName;
            DeletionProtection = deletionProtection;
            EnableCloudwatchLogsExports = enableCloudwatchLogsExports;
            EnableHttpEndpoint = enableHttpEndpoint;
            EnableIAMDatabaseAuthentication = enableIAMDatabaseAuthentication;
            Endpoint = endpoint;
            Engine = engine;
            EngineVersion = engineVersion;
            GlobalClusterIdentifier = globalClusterIdentifier;
            Iops = iops;
            MasterUsername = masterUsername;
            MonitoringInterval = monitoringInterval;
            MonitoringRoleArn = monitoringRoleArn;
            PerformanceInsightsEnabled = performanceInsightsEnabled;
            PerformanceInsightsKmsKeyId = performanceInsightsKmsKeyId;
            PerformanceInsightsRetentionPeriod = performanceInsightsRetentionPeriod;
            Port = port;
            PreferredBackupWindow = preferredBackupWindow;
            PreferredMaintenanceWindow = preferredMaintenanceWindow;
            ReadEndpoint = readEndpoint;
            ReplicationSourceIdentifier = replicationSourceIdentifier;
            ScalingConfiguration = scalingConfiguration;
            StorageType = storageType;
            Tags = tags;
            VpcSecurityGroupIds = vpcSecurityGroupIds;
        }
    }
}
