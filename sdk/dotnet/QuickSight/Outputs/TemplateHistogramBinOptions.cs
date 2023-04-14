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
    public sealed class TemplateHistogramBinOptions
    {
        public readonly Outputs.TemplateBinCountOptions? BinCount;
        public readonly Outputs.TemplateBinWidthOptions? BinWidth;
        public readonly Pulumi.AwsNative.QuickSight.TemplateHistogramBinType? SelectedBinType;
        public readonly double? StartValue;

        [OutputConstructor]
        private TemplateHistogramBinOptions(
            Outputs.TemplateBinCountOptions? binCount,

            Outputs.TemplateBinWidthOptions? binWidth,

            Pulumi.AwsNative.QuickSight.TemplateHistogramBinType? selectedBinType,

            double? startValue)
        {
            BinCount = binCount;
            BinWidth = binWidth;
            SelectedBinType = selectedBinType;
            StartValue = startValue;
        }
    }
}
