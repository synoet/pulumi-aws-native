// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.BillingConductor.Outputs
{

    [OutputType]
    public sealed class CustomLineItemFlatChargeDetails
    {
        public readonly double ChargeValue;

        [OutputConstructor]
        private CustomLineItemFlatChargeDetails(double chargeValue)
        {
            ChargeValue = chargeValue;
        }
    }
}
