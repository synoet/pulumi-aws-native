// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisCustomActionURLOperationArgs : global::Pulumi.ResourceArgs
    {
        [Input("uRLTarget", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.AnalysisURLTargetConfiguration> URLTarget { get; set; } = null!;

        [Input("uRLTemplate", required: true)]
        public Input<string> URLTemplate { get; set; } = null!;

        public AnalysisCustomActionURLOperationArgs()
        {
        }
        public static new AnalysisCustomActionURLOperationArgs Empty => new AnalysisCustomActionURLOperationArgs();
    }
}
