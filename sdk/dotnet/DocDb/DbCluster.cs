// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DocDb
{
    /// <summary>
    /// Resource Type definition for AWS::DocDB::DBCluster
    /// </summary>
    [Obsolete(@"DbCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:docdb:DbCluster")]
    public partial class DbCluster : global::Pulumi.CustomResource
    {
        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        [Output("backupRetentionPeriod")]
        public Output<int?> BackupRetentionPeriod { get; private set; } = null!;

        [Output("clusterResourceId")]
        public Output<string> ClusterResourceId { get; private set; } = null!;

        [Output("copyTagsToSnapshot")]
        public Output<bool?> CopyTagsToSnapshot { get; private set; } = null!;

        [Output("dbClusterIdentifier")]
        public Output<string?> DbClusterIdentifier { get; private set; } = null!;

        [Output("dbClusterParameterGroupName")]
        public Output<string?> DbClusterParameterGroupName { get; private set; } = null!;

        [Output("dbSubnetGroupName")]
        public Output<string?> DbSubnetGroupName { get; private set; } = null!;

        [Output("deletionProtection")]
        public Output<bool?> DeletionProtection { get; private set; } = null!;

        [Output("enableCloudwatchLogsExports")]
        public Output<ImmutableArray<string>> EnableCloudwatchLogsExports { get; private set; } = null!;

        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("masterUserPassword")]
        public Output<string?> MasterUserPassword { get; private set; } = null!;

        [Output("masterUsername")]
        public Output<string?> MasterUsername { get; private set; } = null!;

        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        [Output("preferredBackupWindow")]
        public Output<string?> PreferredBackupWindow { get; private set; } = null!;

        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        [Output("readEndpoint")]
        public Output<string> ReadEndpoint { get; private set; } = null!;

        [Output("restoreToTime")]
        public Output<string?> RestoreToTime { get; private set; } = null!;

        [Output("restoreType")]
        public Output<string?> RestoreType { get; private set; } = null!;

        [Output("snapshotIdentifier")]
        public Output<string?> SnapshotIdentifier { get; private set; } = null!;

        [Output("sourceDbClusterIdentifier")]
        public Output<string?> SourceDbClusterIdentifier { get; private set; } = null!;

        [Output("storageEncrypted")]
        public Output<bool?> StorageEncrypted { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.DbClusterTag>> Tags { get; private set; } = null!;

        [Output("useLatestRestorableTime")]
        public Output<bool?> UseLatestRestorableTime { get; private set; } = null!;

        [Output("vpcSecurityGroupIds")]
        public Output<ImmutableArray<string>> VpcSecurityGroupIds { get; private set; } = null!;


        /// <summary>
        /// Create a DbCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DbCluster(string name, DbClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:docdb:DbCluster", name, args ?? new DbClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DbCluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:docdb:DbCluster", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DbCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DbCluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DbCluster(name, id, options);
        }
    }

    public sealed class DbClusterArgs : global::Pulumi.ResourceArgs
    {
        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        [Input("backupRetentionPeriod")]
        public Input<int>? BackupRetentionPeriod { get; set; }

        [Input("copyTagsToSnapshot")]
        public Input<bool>? CopyTagsToSnapshot { get; set; }

        [Input("dbClusterIdentifier")]
        public Input<string>? DbClusterIdentifier { get; set; }

        [Input("dbClusterParameterGroupName")]
        public Input<string>? DbClusterParameterGroupName { get; set; }

        [Input("dbSubnetGroupName")]
        public Input<string>? DbSubnetGroupName { get; set; }

        [Input("deletionProtection")]
        public Input<bool>? DeletionProtection { get; set; }

        [Input("enableCloudwatchLogsExports")]
        private InputList<string>? _enableCloudwatchLogsExports;
        public InputList<string> EnableCloudwatchLogsExports
        {
            get => _enableCloudwatchLogsExports ?? (_enableCloudwatchLogsExports = new InputList<string>());
            set => _enableCloudwatchLogsExports = value;
        }

        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("masterUserPassword")]
        public Input<string>? MasterUserPassword { get; set; }

        [Input("masterUsername")]
        public Input<string>? MasterUsername { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("preferredBackupWindow")]
        public Input<string>? PreferredBackupWindow { get; set; }

        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        [Input("restoreToTime")]
        public Input<string>? RestoreToTime { get; set; }

        [Input("restoreType")]
        public Input<string>? RestoreType { get; set; }

        [Input("snapshotIdentifier")]
        public Input<string>? SnapshotIdentifier { get; set; }

        [Input("sourceDbClusterIdentifier")]
        public Input<string>? SourceDbClusterIdentifier { get; set; }

        [Input("storageEncrypted")]
        public Input<bool>? StorageEncrypted { get; set; }

        [Input("tags")]
        private InputList<Inputs.DbClusterTagArgs>? _tags;
        public InputList<Inputs.DbClusterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DbClusterTagArgs>());
            set => _tags = value;
        }

        [Input("useLatestRestorableTime")]
        public Input<bool>? UseLatestRestorableTime { get; set; }

        [Input("vpcSecurityGroupIds")]
        private InputList<string>? _vpcSecurityGroupIds;
        public InputList<string> VpcSecurityGroupIds
        {
            get => _vpcSecurityGroupIds ?? (_vpcSecurityGroupIds = new InputList<string>());
            set => _vpcSecurityGroupIds = value;
        }

        public DbClusterArgs()
        {
        }
        public static new DbClusterArgs Empty => new DbClusterArgs();
    }
}
