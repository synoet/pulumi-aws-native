// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Comprehend.Inputs
{

    public sealed class DocumentClassifierOutputDataConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("s3Uri")]
        public Input<string>? S3Uri { get; set; }

        public DocumentClassifierOutputDataConfigArgs()
        {
        }
        public static new DocumentClassifierOutputDataConfigArgs Empty => new DocumentClassifierOutputDataConfigArgs();
    }
}
