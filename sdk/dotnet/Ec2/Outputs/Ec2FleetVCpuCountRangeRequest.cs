// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Outputs
{

    [OutputType]
    public sealed class Ec2FleetVCpuCountRangeRequest
    {
        public readonly int? Max;
        public readonly int? Min;

        [OutputConstructor]
        private Ec2FleetVCpuCountRangeRequest(
            int? max,

            int? min)
        {
            Max = max;
            Min = min;
        }
    }
}
