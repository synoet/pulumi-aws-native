// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    public sealed class Ec2FleetMemoryGiBPerVCpuRequestArgs : global::Pulumi.ResourceArgs
    {
        [Input("max")]
        public Input<double>? Max { get; set; }

        [Input("min")]
        public Input<double>? Min { get; set; }

        public Ec2FleetMemoryGiBPerVCpuRequestArgs()
        {
        }
        public static new Ec2FleetMemoryGiBPerVCpuRequestArgs Empty => new Ec2FleetMemoryGiBPerVCpuRequestArgs();
    }
}
