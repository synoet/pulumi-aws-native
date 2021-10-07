// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra
{
    /// <summary>
    /// Kendra DataSource
    /// </summary>
    [AwsNativeResourceType("aws-native:kendra:DataSource")]
    public partial class DataSource : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("dataSourceConfiguration")]
        public Output<Outputs.DataSourceConfiguration?> DataSourceConfiguration { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("indexId")]
        public Output<string> IndexId { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("roleArn")]
        public Output<string?> RoleArn { get; private set; } = null!;

        [Output("schedule")]
        public Output<string?> Schedule { get; private set; } = null!;

        /// <summary>
        /// Tags for labeling the data source
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.DataSourceTag>> Tags { get; private set; } = null!;

        [Output("type")]
        public Output<Pulumi.AwsNative.Kendra.DataSourceType> Type { get; private set; } = null!;


        /// <summary>
        /// Create a DataSource resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataSource(string name, DataSourceArgs args, CustomResourceOptions? options = null)
            : base("aws-native:kendra:DataSource", name, args ?? new DataSourceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataSource(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kendra:DataSource", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DataSource resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataSource Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataSource(name, id, options);
        }
    }

    public sealed class DataSourceArgs : Pulumi.ResourceArgs
    {
        [Input("dataSourceConfiguration")]
        public Input<Inputs.DataSourceConfigurationArgs>? DataSourceConfiguration { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("indexId", required: true)]
        public Input<string> IndexId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        [Input("schedule")]
        public Input<string>? Schedule { get; set; }

        [Input("tags")]
        private InputList<Inputs.DataSourceTagArgs>? _tags;

        /// <summary>
        /// Tags for labeling the data source
        /// </summary>
        public InputList<Inputs.DataSourceTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.DataSourceTagArgs>());
            set => _tags = value;
        }

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.Kendra.DataSourceType> Type { get; set; } = null!;

        public DataSourceArgs()
        {
        }
    }
}
