// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecretsManager.Inputs
{

    public sealed class SecretReplicaRegionArgs : global::Pulumi.ResourceArgs
    {
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("region", required: true)]
        public Input<string> Region { get; set; } = null!;

        public SecretReplicaRegionArgs()
        {
        }
        public static new SecretReplicaRegionArgs Empty => new SecretReplicaRegionArgs();
    }
}
