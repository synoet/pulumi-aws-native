// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceDiscovery.Inputs
{

    public sealed class ServiceDnsRecordArgs : global::Pulumi.ResourceArgs
    {
        [Input("ttl", required: true)]
        public Input<double> Ttl { get; set; } = null!;

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ServiceDnsRecordArgs()
        {
        }
        public static new ServiceDnsRecordArgs Empty => new ServiceDnsRecordArgs();
    }
}
