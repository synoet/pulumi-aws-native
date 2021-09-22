// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DocDB
{
    /// <summary>
    /// Resource Type definition for AWS::DocDB::DBSubnetGroup
    /// </summary>
    [Obsolete(@"DBSubnetGroup is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:docdb:DBSubnetGroup")]
    public partial class DBSubnetGroup : Pulumi.CustomResource
    {
        [Output("dBSubnetGroupDescription")]
        public Output<string> DBSubnetGroupDescription { get; private set; } = null!;

        [Output("dBSubnetGroupName")]
        public Output<string?> DBSubnetGroupName { get; private set; } = null!;

        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.DBSubnetGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DBSubnetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DBSubnetGroup(string name, DBSubnetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:docdb:DBSubnetGroup", name, args ?? new DBSubnetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DBSubnetGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:docdb:DBSubnetGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DBSubnetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DBSubnetGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DBSubnetGroup(name, id, options);
        }
    }

    public sealed class DBSubnetGroupArgs : Pulumi.ResourceArgs
    {
        [Input("dBSubnetGroupDescription", required: true)]
        public Input<string> DBSubnetGroupDescription { get; set; } = null!;

        [Input("dBSubnetGroupName")]
        public Input<string>? DBSubnetGroupName { get; set; }

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.DBSubnetGroupTagArgs>? _tags;
        public InputList<Inputs.DBSubnetGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DBSubnetGroupTagArgs>());
            set => _tags = value;
        }

        public DBSubnetGroupArgs()
        {
        }
    }
}
