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
    public sealed class AnalysisKpiOptions
    {
        public readonly Outputs.AnalysisComparisonConfiguration? Comparison;
        public readonly Pulumi.AwsNative.QuickSight.AnalysisPrimaryValueDisplayType? PrimaryValueDisplayType;
        public readonly Outputs.AnalysisFontConfiguration? PrimaryValueFontConfiguration;
        public readonly Outputs.AnalysisProgressBarOptions? ProgressBar;
        public readonly Outputs.AnalysisSecondaryValueOptions? SecondaryValue;
        public readonly Outputs.AnalysisFontConfiguration? SecondaryValueFontConfiguration;
        public readonly Outputs.AnalysisTrendArrowOptions? TrendArrows;

        [OutputConstructor]
        private AnalysisKpiOptions(
            Outputs.AnalysisComparisonConfiguration? comparison,

            Pulumi.AwsNative.QuickSight.AnalysisPrimaryValueDisplayType? primaryValueDisplayType,

            Outputs.AnalysisFontConfiguration? primaryValueFontConfiguration,

            Outputs.AnalysisProgressBarOptions? progressBar,

            Outputs.AnalysisSecondaryValueOptions? secondaryValue,

            Outputs.AnalysisFontConfiguration? secondaryValueFontConfiguration,

            Outputs.AnalysisTrendArrowOptions? trendArrows)
        {
            Comparison = comparison;
            PrimaryValueDisplayType = primaryValueDisplayType;
            PrimaryValueFontConfiguration = primaryValueFontConfiguration;
            ProgressBar = progressBar;
            SecondaryValue = secondaryValue;
            SecondaryValueFontConfiguration = secondaryValueFontConfiguration;
            TrendArrows = trendArrows;
        }
    }
}
