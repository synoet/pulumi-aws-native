// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PcaConnectorAd.Outputs
{

    [OutputType]
    public sealed class TemplateValidityPeriod
    {
        public readonly double Period;
        public readonly Pulumi.AwsNative.PcaConnectorAd.TemplateValidityPeriodType PeriodType;

        [OutputConstructor]
        private TemplateValidityPeriod(
            double period,

            Pulumi.AwsNative.PcaConnectorAd.TemplateValidityPeriodType periodType)
        {
            Period = period;
            PeriodType = periodType;
        }
    }
}
