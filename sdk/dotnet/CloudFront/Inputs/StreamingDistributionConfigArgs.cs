// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class StreamingDistributionConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("aliases")]
        private InputList<string>? _aliases;
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        [Input("comment", required: true)]
        public Input<string> Comment { get; set; } = null!;

        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        [Input("logging")]
        public Input<Inputs.StreamingDistributionLoggingArgs>? Logging { get; set; }

        [Input("priceClass")]
        public Input<string>? PriceClass { get; set; }

        [Input("s3Origin", required: true)]
        public Input<Inputs.StreamingDistributionS3OriginArgs> S3Origin { get; set; } = null!;

        [Input("trustedSigners", required: true)]
        public Input<Inputs.StreamingDistributionTrustedSignersArgs> TrustedSigners { get; set; } = null!;

        public StreamingDistributionConfigArgs()
        {
        }
        public static new StreamingDistributionConfigArgs Empty => new StreamingDistributionConfigArgs();
    }
}
