// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EKS.Inputs
{

    public sealed class ClusterProviderArgs : Pulumi.ResourceArgs
    {
        [Input("keyArn")]
        public Input<string>? KeyArn { get; set; }

        public ClusterProviderArgs()
        {
        }
    }
}
