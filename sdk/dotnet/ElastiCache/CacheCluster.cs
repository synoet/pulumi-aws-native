// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    /// <summary>
    /// Resource Type definition for AWS::ElastiCache::CacheCluster
    /// </summary>
    [Obsolete(@"CacheCluster is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:elasticache:CacheCluster")]
    public partial class CacheCluster : global::Pulumi.CustomResource
    {
        [Output("autoMinorVersionUpgrade")]
        public Output<bool?> AutoMinorVersionUpgrade { get; private set; } = null!;

        [Output("azMode")]
        public Output<string?> AzMode { get; private set; } = null!;

        [Output("cacheNodeType")]
        public Output<string> CacheNodeType { get; private set; } = null!;

        [Output("cacheParameterGroupName")]
        public Output<string?> CacheParameterGroupName { get; private set; } = null!;

        [Output("cacheSecurityGroupNames")]
        public Output<ImmutableArray<string>> CacheSecurityGroupNames { get; private set; } = null!;

        [Output("cacheSubnetGroupName")]
        public Output<string?> CacheSubnetGroupName { get; private set; } = null!;

        [Output("clusterName")]
        public Output<string?> ClusterName { get; private set; } = null!;

        [Output("configurationEndpointAddress")]
        public Output<string?> ConfigurationEndpointAddress { get; private set; } = null!;

        [Output("configurationEndpointPort")]
        public Output<string?> ConfigurationEndpointPort { get; private set; } = null!;

        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        [Output("ipDiscovery")]
        public Output<string?> IpDiscovery { get; private set; } = null!;

        [Output("logDeliveryConfigurations")]
        public Output<ImmutableArray<Outputs.CacheClusterLogDeliveryConfigurationRequest>> LogDeliveryConfigurations { get; private set; } = null!;

        [Output("networkType")]
        public Output<string?> NetworkType { get; private set; } = null!;

        [Output("notificationTopicArn")]
        public Output<string?> NotificationTopicArn { get; private set; } = null!;

        [Output("numCacheNodes")]
        public Output<int> NumCacheNodes { get; private set; } = null!;

        [Output("port")]
        public Output<int?> Port { get; private set; } = null!;

        [Output("preferredAvailabilityZone")]
        public Output<string?> PreferredAvailabilityZone { get; private set; } = null!;

        [Output("preferredAvailabilityZones")]
        public Output<ImmutableArray<string>> PreferredAvailabilityZones { get; private set; } = null!;

        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        [Output("redisEndpointAddress")]
        public Output<string?> RedisEndpointAddress { get; private set; } = null!;

        [Output("redisEndpointPort")]
        public Output<string?> RedisEndpointPort { get; private set; } = null!;

        [Output("snapshotArns")]
        public Output<ImmutableArray<string>> SnapshotArns { get; private set; } = null!;

        [Output("snapshotName")]
        public Output<string?> SnapshotName { get; private set; } = null!;

        [Output("snapshotRetentionLimit")]
        public Output<int?> SnapshotRetentionLimit { get; private set; } = null!;

        [Output("snapshotWindow")]
        public Output<string?> SnapshotWindow { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.CacheClusterTag>> Tags { get; private set; } = null!;

        [Output("transitEncryptionEnabled")]
        public Output<bool?> TransitEncryptionEnabled { get; private set; } = null!;

        [Output("vpcSecurityGroupIds")]
        public Output<ImmutableArray<string>> VpcSecurityGroupIds { get; private set; } = null!;


        /// <summary>
        /// Create a CacheCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CacheCluster(string name, CacheClusterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:CacheCluster", name, args ?? new CacheClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CacheCluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:CacheCluster", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "cacheSubnetGroupName",
                    "clusterName",
                    "engine",
                    "networkType",
                    "port",
                    "snapshotArns[*]",
                    "snapshotName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CacheCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CacheCluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CacheCluster(name, id, options);
        }
    }

    public sealed class CacheClusterArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoMinorVersionUpgrade")]
        public Input<bool>? AutoMinorVersionUpgrade { get; set; }

        [Input("azMode")]
        public Input<string>? AzMode { get; set; }

        [Input("cacheNodeType", required: true)]
        public Input<string> CacheNodeType { get; set; } = null!;

        [Input("cacheParameterGroupName")]
        public Input<string>? CacheParameterGroupName { get; set; }

        [Input("cacheSecurityGroupNames")]
        private InputList<string>? _cacheSecurityGroupNames;
        public InputList<string> CacheSecurityGroupNames
        {
            get => _cacheSecurityGroupNames ?? (_cacheSecurityGroupNames = new InputList<string>());
            set => _cacheSecurityGroupNames = value;
        }

        [Input("cacheSubnetGroupName")]
        public Input<string>? CacheSubnetGroupName { get; set; }

        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        [Input("configurationEndpointAddress")]
        public Input<string>? ConfigurationEndpointAddress { get; set; }

        [Input("configurationEndpointPort")]
        public Input<string>? ConfigurationEndpointPort { get; set; }

        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        [Input("ipDiscovery")]
        public Input<string>? IpDiscovery { get; set; }

        [Input("logDeliveryConfigurations")]
        private InputList<Inputs.CacheClusterLogDeliveryConfigurationRequestArgs>? _logDeliveryConfigurations;
        public InputList<Inputs.CacheClusterLogDeliveryConfigurationRequestArgs> LogDeliveryConfigurations
        {
            get => _logDeliveryConfigurations ?? (_logDeliveryConfigurations = new InputList<Inputs.CacheClusterLogDeliveryConfigurationRequestArgs>());
            set => _logDeliveryConfigurations = value;
        }

        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        [Input("notificationTopicArn")]
        public Input<string>? NotificationTopicArn { get; set; }

        [Input("numCacheNodes", required: true)]
        public Input<int> NumCacheNodes { get; set; } = null!;

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("preferredAvailabilityZone")]
        public Input<string>? PreferredAvailabilityZone { get; set; }

        [Input("preferredAvailabilityZones")]
        private InputList<string>? _preferredAvailabilityZones;
        public InputList<string> PreferredAvailabilityZones
        {
            get => _preferredAvailabilityZones ?? (_preferredAvailabilityZones = new InputList<string>());
            set => _preferredAvailabilityZones = value;
        }

        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        [Input("redisEndpointAddress")]
        public Input<string>? RedisEndpointAddress { get; set; }

        [Input("redisEndpointPort")]
        public Input<string>? RedisEndpointPort { get; set; }

        [Input("snapshotArns")]
        private InputList<string>? _snapshotArns;
        public InputList<string> SnapshotArns
        {
            get => _snapshotArns ?? (_snapshotArns = new InputList<string>());
            set => _snapshotArns = value;
        }

        [Input("snapshotName")]
        public Input<string>? SnapshotName { get; set; }

        [Input("snapshotRetentionLimit")]
        public Input<int>? SnapshotRetentionLimit { get; set; }

        [Input("snapshotWindow")]
        public Input<string>? SnapshotWindow { get; set; }

        [Input("tags")]
        private InputList<Inputs.CacheClusterTagArgs>? _tags;
        public InputList<Inputs.CacheClusterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CacheClusterTagArgs>());
            set => _tags = value;
        }

        [Input("transitEncryptionEnabled")]
        public Input<bool>? TransitEncryptionEnabled { get; set; }

        [Input("vpcSecurityGroupIds")]
        private InputList<string>? _vpcSecurityGroupIds;
        public InputList<string> VpcSecurityGroupIds
        {
            get => _vpcSecurityGroupIds ?? (_vpcSecurityGroupIds = new InputList<string>());
            set => _vpcSecurityGroupIds = value;
        }

        public CacheClusterArgs()
        {
        }
        public static new CacheClusterArgs Empty => new CacheClusterArgs();
    }
}
