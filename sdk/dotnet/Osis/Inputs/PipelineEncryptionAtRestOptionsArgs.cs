// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Osis.Inputs
{

    /// <summary>
    /// Key-value pairs to configure encryption at rest.
    /// </summary>
    public sealed class PipelineEncryptionAtRestOptionsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The KMS key to use for encrypting data. By default an AWS owned key is used
        /// </summary>
        [Input("kmsKeyArn", required: true)]
        public Input<string> KmsKeyArn { get; set; } = null!;

        public PipelineEncryptionAtRestOptionsArgs()
        {
        }
        public static new PipelineEncryptionAtRestOptionsArgs Empty => new PipelineEncryptionAtRestOptionsArgs();
    }
}
