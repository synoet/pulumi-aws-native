// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Msk.Inputs
{

    public sealed class ClusterVpcConnectivityClientAuthenticationArgs : global::Pulumi.ResourceArgs
    {
        [Input("sasl")]
        public Input<Inputs.ClusterVpcConnectivitySaslArgs>? Sasl { get; set; }

        [Input("tls")]
        public Input<Inputs.ClusterVpcConnectivityTlsArgs>? Tls { get; set; }

        public ClusterVpcConnectivityClientAuthenticationArgs()
        {
        }
        public static new ClusterVpcConnectivityClientAuthenticationArgs Empty => new ClusterVpcConnectivityClientAuthenticationArgs();
    }
}
