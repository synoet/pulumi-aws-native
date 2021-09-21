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
    /// Resource Type definition for AWS::ElastiCache::SubnetGroup
    /// </summary>
    [Obsolete(@"SubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:elasticache:SubnetGroup")]
    public partial class SubnetGroup : Pulumi.CustomResource
    {
        [Output("cacheSubnetGroupName")]
        public Output<string?> CacheSubnetGroupName { get; private set; } = null!;

        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.SubnetGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SubnetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubnetGroup(string name, SubnetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:SubnetGroup", name, args ?? new SubnetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SubnetGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:SubnetGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubnetGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SubnetGroup(name, id, options);
        }
    }

    public sealed class SubnetGroupArgs : Pulumi.ResourceArgs
    {
        [Input("cacheSubnetGroupName")]
        public Input<string>? CacheSubnetGroupName { get; set; }

        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.SubnetGroupTagArgs>? _tags;
        public InputList<Inputs.SubnetGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SubnetGroupTagArgs>());
            set => _tags = value;
        }

        public SubnetGroupArgs()
        {
        }
    }
}
