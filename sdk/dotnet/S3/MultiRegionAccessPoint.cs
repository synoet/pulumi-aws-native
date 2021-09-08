// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html
    /// </summary>
    [AwsNativeResourceType("aws-native:s3:MultiRegionAccessPoint")]
    public partial class MultiRegionAccessPoint : Pulumi.CustomResource
    {
        [Output("alias")]
        public Output<string> Alias { get; private set; } = null!;

        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-name
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration
        /// </summary>
        [Output("publicAccessBlockConfiguration")]
        public Output<Outputs.MultiRegionAccessPointPublicAccessBlockConfiguration?> PublicAccessBlockConfiguration { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-regions
        /// </summary>
        [Output("regions")]
        public Output<ImmutableArray<Outputs.MultiRegionAccessPointRegion>> Regions { get; private set; } = null!;


        /// <summary>
        /// Create a MultiRegionAccessPoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public MultiRegionAccessPoint(string name, MultiRegionAccessPointArgs args, CustomResourceOptions? options = null)
            : base("aws-native:s3:MultiRegionAccessPoint", name, args ?? new MultiRegionAccessPointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private MultiRegionAccessPoint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:s3:MultiRegionAccessPoint", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing MultiRegionAccessPoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static MultiRegionAccessPoint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new MultiRegionAccessPoint(name, id, options);
        }
    }

    public sealed class MultiRegionAccessPointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-publicaccessblockconfiguration
        /// </summary>
        [Input("publicAccessBlockConfiguration")]
        public Input<Inputs.MultiRegionAccessPointPublicAccessBlockConfigurationArgs>? PublicAccessBlockConfiguration { get; set; }

        [Input("regions", required: true)]
        private InputList<Inputs.MultiRegionAccessPointRegionArgs>? _regions;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-s3-multiregionaccesspoint.html#cfn-s3-multiregionaccesspoint-regions
        /// </summary>
        public InputList<Inputs.MultiRegionAccessPointRegionArgs> Regions
        {
            get => _regions ?? (_regions = new InputList<Inputs.MultiRegionAccessPointRegionArgs>());
            set => _regions = value;
        }

        public MultiRegionAccessPointArgs()
        {
        }
    }
}
