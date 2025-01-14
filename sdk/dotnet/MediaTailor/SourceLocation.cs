// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaTailor
{
    /// <summary>
    /// Definition of AWS::MediaTailor::SourceLocation Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:mediatailor:SourceLocation")]
    public partial class SourceLocation : global::Pulumi.CustomResource
    {
        [Output("accessConfiguration")]
        public Output<Outputs.SourceLocationAccessConfiguration?> AccessConfiguration { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;The ARN of the source location.&lt;/p&gt;
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("defaultSegmentDeliveryConfiguration")]
        public Output<Outputs.SourceLocationDefaultSegmentDeliveryConfiguration?> DefaultSegmentDeliveryConfiguration { get; private set; } = null!;

        [Output("httpConfiguration")]
        public Output<Outputs.SourceLocationHttpConfiguration> HttpConfiguration { get; private set; } = null!;

        /// <summary>
        /// &lt;p&gt;A list of the segment delivery configurations associated with this resource.&lt;/p&gt;
        /// </summary>
        [Output("segmentDeliveryConfigurations")]
        public Output<ImmutableArray<Outputs.SourceLocationSegmentDeliveryConfiguration>> SegmentDeliveryConfigurations { get; private set; } = null!;

        [Output("sourceLocationName")]
        public Output<string> SourceLocationName { get; private set; } = null!;

        /// <summary>
        /// The tags to assign to the source location.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.SourceLocationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SourceLocation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SourceLocation(string name, SourceLocationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:SourceLocation", name, args ?? new SourceLocationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SourceLocation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediatailor:SourceLocation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "sourceLocationName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SourceLocation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SourceLocation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SourceLocation(name, id, options);
        }
    }

    public sealed class SourceLocationArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessConfiguration")]
        public Input<Inputs.SourceLocationAccessConfigurationArgs>? AccessConfiguration { get; set; }

        [Input("defaultSegmentDeliveryConfiguration")]
        public Input<Inputs.SourceLocationDefaultSegmentDeliveryConfigurationArgs>? DefaultSegmentDeliveryConfiguration { get; set; }

        [Input("httpConfiguration", required: true)]
        public Input<Inputs.SourceLocationHttpConfigurationArgs> HttpConfiguration { get; set; } = null!;

        [Input("segmentDeliveryConfigurations")]
        private InputList<Inputs.SourceLocationSegmentDeliveryConfigurationArgs>? _segmentDeliveryConfigurations;

        /// <summary>
        /// &lt;p&gt;A list of the segment delivery configurations associated with this resource.&lt;/p&gt;
        /// </summary>
        public InputList<Inputs.SourceLocationSegmentDeliveryConfigurationArgs> SegmentDeliveryConfigurations
        {
            get => _segmentDeliveryConfigurations ?? (_segmentDeliveryConfigurations = new InputList<Inputs.SourceLocationSegmentDeliveryConfigurationArgs>());
            set => _segmentDeliveryConfigurations = value;
        }

        [Input("sourceLocationName")]
        public Input<string>? SourceLocationName { get; set; }

        [Input("tags")]
        private InputList<Inputs.SourceLocationTagArgs>? _tags;

        /// <summary>
        /// The tags to assign to the source location.
        /// </summary>
        public InputList<Inputs.SourceLocationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SourceLocationTagArgs>());
            set => _tags = value;
        }

        public SourceLocationArgs()
        {
        }
        public static new SourceLocationArgs Empty => new SourceLocationArgs();
    }
}
