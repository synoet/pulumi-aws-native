// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TopicRangeConstantArgs : global::Pulumi.ResourceArgs
    {
        [Input("maximum")]
        public Input<string>? Maximum { get; set; }

        [Input("minimum")]
        public Input<string>? Minimum { get; set; }

        public TopicRangeConstantArgs()
        {
        }
        public static new TopicRangeConstantArgs Empty => new TopicRangeConstantArgs();
    }
}
