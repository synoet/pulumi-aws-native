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
    public sealed class AnalysisVisualCustomActionOperation
    {
        public readonly Outputs.AnalysisCustomActionFilterOperation? FilterOperation;
        public readonly Outputs.AnalysisCustomActionNavigationOperation? NavigationOperation;
        public readonly Outputs.AnalysisCustomActionSetParametersOperation? SetParametersOperation;
        public readonly Outputs.AnalysisCustomActionUrlOperation? UrlOperation;

        [OutputConstructor]
        private AnalysisVisualCustomActionOperation(
            Outputs.AnalysisCustomActionFilterOperation? filterOperation,

            Outputs.AnalysisCustomActionNavigationOperation? navigationOperation,

            Outputs.AnalysisCustomActionSetParametersOperation? setParametersOperation,

            Outputs.AnalysisCustomActionUrlOperation? urlOperation)
        {
            FilterOperation = filterOperation;
            NavigationOperation = navigationOperation;
            SetParametersOperation = setParametersOperation;
            UrlOperation = urlOperation;
        }
    }
}
