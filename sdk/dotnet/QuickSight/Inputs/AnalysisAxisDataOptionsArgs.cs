// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisAxisDataOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("dateAxisOptions")]
        public Input<Inputs.AnalysisDateAxisOptionsArgs>? DateAxisOptions { get; set; }

        [Input("numericAxisOptions")]
        public Input<Inputs.AnalysisNumericAxisOptionsArgs>? NumericAxisOptions { get; set; }

        public AnalysisAxisDataOptionsArgs()
        {
        }
        public static new AnalysisAxisDataOptionsArgs Empty => new AnalysisAxisDataOptionsArgs();
    }
}
