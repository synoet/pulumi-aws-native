// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html
    /// </summary>
    public sealed class TrailInsightSelectorArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudtrail-trail-insightselector.html#cfn-cloudtrail-trail-insightselector-insighttype
        /// </summary>
        [Input("insightType")]
        public Input<string>? InsightType { get; set; }

        public TrailInsightSelectorArgs()
        {
        }
    }
}
