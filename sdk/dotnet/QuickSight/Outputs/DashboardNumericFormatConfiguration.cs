// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class DashboardNumericFormatConfiguration
    {
        public readonly Outputs.DashboardCurrencyDisplayFormatConfiguration? CurrencyDisplayFormatConfiguration;
        public readonly Outputs.DashboardNumberDisplayFormatConfiguration? NumberDisplayFormatConfiguration;
        public readonly Outputs.DashboardPercentageDisplayFormatConfiguration? PercentageDisplayFormatConfiguration;

        [OutputConstructor]
        private DashboardNumericFormatConfiguration(
            Outputs.DashboardCurrencyDisplayFormatConfiguration? currencyDisplayFormatConfiguration,

            Outputs.DashboardNumberDisplayFormatConfiguration? numberDisplayFormatConfiguration,

            Outputs.DashboardPercentageDisplayFormatConfiguration? percentageDisplayFormatConfiguration)
        {
            CurrencyDisplayFormatConfiguration = currencyDisplayFormatConfiguration;
            NumberDisplayFormatConfiguration = numberDisplayFormatConfiguration;
            PercentageDisplayFormatConfiguration = percentageDisplayFormatConfiguration;
        }
    }
}
