// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise
{
    /// <summary>
    /// Resource schema for AWS::IoTSiteWise::Asset
    /// </summary>
    [AwsNativeResourceType("aws-native:iotsitewise:Asset")]
    public partial class Asset : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the asset
        /// </summary>
        [Output("assetArn")]
        public Output<string> AssetArn { get; private set; } = null!;

        /// <summary>
        /// A description for the asset
        /// </summary>
        [Output("assetDescription")]
        public Output<string?> AssetDescription { get; private set; } = null!;

        [Output("assetHierarchies")]
        public Output<ImmutableArray<Outputs.AssetHierarchy>> AssetHierarchies { get; private set; } = null!;

        /// <summary>
        /// The ID of the asset
        /// </summary>
        [Output("assetId")]
        public Output<string> AssetId { get; private set; } = null!;

        /// <summary>
        /// The ID of the asset model from which to create the asset.
        /// </summary>
        [Output("assetModelId")]
        public Output<string> AssetModelId { get; private set; } = null!;

        /// <summary>
        /// A unique, friendly name for the asset.
        /// </summary>
        [Output("assetName")]
        public Output<string> AssetName { get; private set; } = null!;

        [Output("assetProperties")]
        public Output<ImmutableArray<Outputs.AssetProperty>> AssetProperties { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.AssetTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Asset resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Asset(string name, AssetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Asset", name, args ?? new AssetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Asset(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Asset", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Asset resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Asset Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Asset(name, id, options);
        }
    }

    public sealed class AssetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description for the asset
        /// </summary>
        [Input("assetDescription")]
        public Input<string>? AssetDescription { get; set; }

        [Input("assetHierarchies")]
        private InputList<Inputs.AssetHierarchyArgs>? _assetHierarchies;
        public InputList<Inputs.AssetHierarchyArgs> AssetHierarchies
        {
            get => _assetHierarchies ?? (_assetHierarchies = new InputList<Inputs.AssetHierarchyArgs>());
            set => _assetHierarchies = value;
        }

        /// <summary>
        /// The ID of the asset model from which to create the asset.
        /// </summary>
        [Input("assetModelId", required: true)]
        public Input<string> AssetModelId { get; set; } = null!;

        /// <summary>
        /// A unique, friendly name for the asset.
        /// </summary>
        [Input("assetName")]
        public Input<string>? AssetName { get; set; }

        [Input("assetProperties")]
        private InputList<Inputs.AssetPropertyArgs>? _assetProperties;
        public InputList<Inputs.AssetPropertyArgs> AssetProperties
        {
            get => _assetProperties ?? (_assetProperties = new InputList<Inputs.AssetPropertyArgs>());
            set => _assetProperties = value;
        }

        [Input("tags")]
        private InputList<Inputs.AssetTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the asset.
        /// </summary>
        public InputList<Inputs.AssetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AssetTagArgs>());
            set => _tags = value;
        }

        public AssetArgs()
        {
        }
        public static new AssetArgs Empty => new AssetArgs();
    }
}
