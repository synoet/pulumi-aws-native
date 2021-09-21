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
    /// Resource Type definition for AWS::Pinpoint::APNSChannel
    /// </summary>
    [Obsolete(@"APNSChannel is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:pinpoint:APNSChannel")]
    public partial class APNSChannel : Pulumi.CustomResource
    {
        [Output("applicationId")]
        public Output<string> ApplicationId { get; private set; } = null!;

        [Output("bundleId")]
        public Output<string?> BundleId { get; private set; } = null!;

        [Output("certificate")]
        public Output<string?> Certificate { get; private set; } = null!;

        [Output("defaultAuthenticationMethod")]
        public Output<string?> DefaultAuthenticationMethod { get; private set; } = null!;

        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("privateKey")]
        public Output<string?> PrivateKey { get; private set; } = null!;

        [Output("teamId")]
        public Output<string?> TeamId { get; private set; } = null!;

        [Output("tokenKey")]
        public Output<string?> TokenKey { get; private set; } = null!;

        [Output("tokenKeyId")]
        public Output<string?> TokenKeyId { get; private set; } = null!;


        /// <summary>
        /// Create a APNSChannel resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public APNSChannel(string name, APNSChannelArgs args, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:APNSChannel", name, args ?? new APNSChannelArgs(), MakeResourceOptions(options, ""))
        {
        }

        private APNSChannel(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:pinpoint:APNSChannel", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing APNSChannel resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static APNSChannel Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new APNSChannel(name, id, options);
        }
    }

    public sealed class APNSChannelArgs : Pulumi.ResourceArgs
    {
        [Input("applicationId", required: true)]
        public Input<string> ApplicationId { get; set; } = null!;

        [Input("bundleId")]
        public Input<string>? BundleId { get; set; }

        [Input("certificate")]
        public Input<string>? Certificate { get; set; }

        [Input("defaultAuthenticationMethod")]
        public Input<string>? DefaultAuthenticationMethod { get; set; }

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        [Input("tokenKey")]
        public Input<string>? TokenKey { get; set; }

        [Input("tokenKeyId")]
        public Input<string>? TokenKeyId { get; set; }

        public APNSChannelArgs()
        {
        }
    }
}
