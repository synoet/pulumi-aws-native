// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceDiscovery.Inputs
{

    public sealed class PrivateDnsNamespaceSoaArgs : global::Pulumi.ResourceArgs
    {
        [Input("ttl")]
        public Input<double>? Ttl { get; set; }

        public PrivateDnsNamespaceSoaArgs()
        {
        }
        public static new PrivateDnsNamespaceSoaArgs Empty => new PrivateDnsNamespaceSoaArgs();
    }
}
