// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisVisibleRangeOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("percentRange")]
        public Input<Inputs.AnalysisPercentVisibleRangeArgs>? PercentRange { get; set; }

        public AnalysisVisibleRangeOptionsArgs()
        {
        }
        public static new AnalysisVisibleRangeOptionsArgs Empty => new AnalysisVisibleRangeOptionsArgs();
    }
}
