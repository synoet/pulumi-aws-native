// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint
{
    /// <summary>
    /// Resource Type definition for AWS::Pinpoint::GCMChannel
    /// </summary>
    [Obsolete(@"GcmChannel is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:pinpoint:GcmChannel")]
    public partial class GcmChannel : global::Pulumi.CustomResource
    {
        [Output("apiKey")]
        public Output<string> ApiKey { get; private set; } = null!;

        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;


        /// <summary>
        /// Create a GcmChannel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public GcmChannel(string name, GcmChannelArgs args, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:GcmChannel", name, args ?? new GcmChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private GcmChannel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:GcmChannel", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "applicationId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing GcmChannel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static GcmChannel Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new GcmChannel(name, id, options);
        }
    }

    public sealed class GcmChannelArgs : global::Pulumi.ResourceArgs
    {
        [Input("apiKey", required: true)]
        public Input<string> ApiKey { get; set; } = null!;

        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public GcmChannelArgs()
        {
        }
        public static new GcmChannelArgs Empty => new GcmChannelArgs();
    }
}
