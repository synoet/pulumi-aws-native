// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    /// <summary>
    /// The AWS Organizations ARN to use in the Amazon S3 Storage Lens configuration.
    /// </summary>
    public sealed class StorageLensAwsOrgArgs : global::Pulumi.ResourceArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public StorageLensAwsOrgArgs()
        {
        }
        public static new StorageLensAwsOrgArgs Empty => new StorageLensAwsOrgArgs();
    }
}
