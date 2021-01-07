// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.EC2.Outputs
{

    [OutputType]
    public sealed class CapacityReservationAttributes
    {
        public readonly string AvailabilityZone;
        public readonly int AvailableInstanceCount;
        public readonly string InstanceType;
        public readonly string Tenancy;
        public readonly int TotalInstanceCount;

        [OutputConstructor]
        private CapacityReservationAttributes(
            string AvailabilityZone,

            int AvailableInstanceCount,

            string InstanceType,

            string Tenancy,

            int TotalInstanceCount)
        {
            this.AvailabilityZone = AvailabilityZone;
            this.AvailableInstanceCount = AvailableInstanceCount;
            this.InstanceType = InstanceType;
            this.Tenancy = Tenancy;
            this.TotalInstanceCount = TotalInstanceCount;
        }
    }
}