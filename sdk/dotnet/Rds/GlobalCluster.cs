// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds
{
    /// <summary>
    /// Resource Type definition for AWS::RDS::GlobalCluster
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:GlobalCluster")]
    public partial class GlobalCluster : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        /// </summary>
        [Output("deletionProtection")]
        public Output<bool?> DeletionProtection { get; private set; } = null!;

        /// <summary>
        /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
        /// If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Output("engine")]
        public Output<Pulumi.AwsNative.Rds.GlobalClusterEngine?> Engine { get; private set; } = null!;

        /// <summary>
        /// The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Output("engineVersion")]
        public Output<string?> EngineVersion { get; private set; } = null!;

        /// <summary>
        /// The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        /// </summary>
        [Output("globalClusterIdentifier")]
        public Output<string?> GlobalClusterIdentifier { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        /// </summary>
        [Output("sourceDbClusterIdentifier")]
        public Output<string?> SourceDbClusterIdentifier { get; private set; } = null!;

        /// <summary>
        ///  The storage encryption setting for the new global database cluster.
        /// If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Output("storageEncrypted")]
        public Output<bool?> StorageEncrypted { get; private set; } = null!;


        /// <summary>
        /// Create a GlobalCluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GlobalCluster(string name, GlobalClusterArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:rds:GlobalCluster", name, args ?? new GlobalClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GlobalCluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:GlobalCluster", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "engine",
                    "globalClusterIdentifier",
                    "sourceDbClusterIdentifier",
                    "storageEncrypted",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GlobalCluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GlobalCluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new GlobalCluster(name, id, options);
        }
    }

    public sealed class GlobalClusterArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The deletion protection setting for the new global database. The global database can't be deleted when deletion protection is enabled.
        /// </summary>
        [Input("deletionProtection")]
        public Input<bool>? DeletionProtection { get; set; }

        /// <summary>
        /// The name of the database engine to be used for this DB cluster. Valid Values: aurora (for MySQL 5.6-compatible Aurora), aurora-mysql (for MySQL 5.7-compatible Aurora).
        /// If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Input("engine")]
        public Input<Pulumi.AwsNative.Rds.GlobalClusterEngine>? Engine { get; set; }

        /// <summary>
        /// The version number of the database engine to use. If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Input("engineVersion")]
        public Input<string>? EngineVersion { get; set; }

        /// <summary>
        /// The cluster identifier of the new global database cluster. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("globalClusterIdentifier")]
        public Input<string>? GlobalClusterIdentifier { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) to use as the primary cluster of the global database. This parameter is optional. This parameter is stored as a lowercase string.
        /// </summary>
        [Input("sourceDbClusterIdentifier")]
        public Input<string>? SourceDbClusterIdentifier { get; set; }

        /// <summary>
        ///  The storage encryption setting for the new global database cluster.
        /// If you specify the SourceDBClusterIdentifier property, don't specify this property. The value is inherited from the cluster.
        /// </summary>
        [Input("storageEncrypted")]
        public Input<bool>? StorageEncrypted { get; set; }

        public GlobalClusterArgs()
        {
        }
        public static new GlobalClusterArgs Empty => new GlobalClusterArgs();
    }
}
