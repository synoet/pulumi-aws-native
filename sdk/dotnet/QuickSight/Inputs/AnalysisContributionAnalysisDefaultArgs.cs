// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisContributionAnalysisDefaultArgs : global::Pulumi.ResourceArgs
    {
        [Input("contributorDimensions", required: true)]
        private InputList<Inputs.AnalysisColumnIdentifierArgs>? _contributorDimensions;
        public InputList<Inputs.AnalysisColumnIdentifierArgs> ContributorDimensions
        {
            get => _contributorDimensions ?? (_contributorDimensions = new InputList<Inputs.AnalysisColumnIdentifierArgs>());
            set => _contributorDimensions = value;
        }

        [Input("measureFieldId", required: true)]
        public Input<string> MeasureFieldId { get; set; } = null!;

        public AnalysisContributionAnalysisDefaultArgs()
        {
        }
        public static new AnalysisContributionAnalysisDefaultArgs Empty => new AnalysisContributionAnalysisDefaultArgs();
    }
}
