// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Omics
{
    /// <summary>
    /// Definition of AWS::Omics::AnnotationStore Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:omics:AnnotationStore")]
    public partial class AnnotationStore : global::Pulumi.CustomResource
    {
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("reference")]
        public Output<Outputs.AnnotationStoreReferenceItem?> Reference { get; private set; } = null!;

        [Output("sseConfig")]
        public Output<Outputs.AnnotationStoreSseConfig?> SseConfig { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.Omics.AnnotationStoreStoreStatus> Status { get; private set; } = null!;

        [Output("statusMessage")]
        public Output<string> StatusMessage { get; private set; } = null!;

        [Output("storeArn")]
        public Output<string> StoreArn { get; private set; } = null!;

        [Output("storeFormat")]
        public Output<Pulumi.AwsNative.Omics.AnnotationStoreStoreFormat> StoreFormat { get; private set; } = null!;

        [Output("storeOptions")]
        public Output<Outputs.StoreOptionsProperties?> StoreOptions { get; private set; } = null!;

        [Output("storeSizeBytes")]
        public Output<double> StoreSizeBytes { get; private set; } = null!;

        [Output("tags")]
        public Output<Outputs.AnnotationStoreTagMap?> Tags { get; private set; } = null!;

        [Output("updateTime")]
        public Output<string> UpdateTime { get; private set; } = null!;


        /// <summary>
        /// Create a AnnotationStore resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AnnotationStore(string name, AnnotationStoreArgs args, CustomResourceOptions? options = null)
            : base("aws-native:omics:AnnotationStore", name, args ?? new AnnotationStoreArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AnnotationStore(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:omics:AnnotationStore", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing AnnotationStore resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AnnotationStore Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AnnotationStore(name, id, options);
        }
    }

    public sealed class AnnotationStoreArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("reference")]
        public Input<Inputs.AnnotationStoreReferenceItemArgs>? Reference { get; set; }

        [Input("sseConfig")]
        public Input<Inputs.AnnotationStoreSseConfigArgs>? SseConfig { get; set; }

        [Input("storeFormat", required: true)]
        public Input<Pulumi.AwsNative.Omics.AnnotationStoreStoreFormat> StoreFormat { get; set; } = null!;

        [Input("storeOptions")]
        public Input<Inputs.StoreOptionsPropertiesArgs>? StoreOptions { get; set; }

        [Input("tags")]
        public Input<Inputs.AnnotationStoreTagMapArgs>? Tags { get; set; }

        public AnnotationStoreArgs()
        {
        }
        public static new AnnotationStoreArgs Empty => new AnnotationStoreArgs();
    }
}
