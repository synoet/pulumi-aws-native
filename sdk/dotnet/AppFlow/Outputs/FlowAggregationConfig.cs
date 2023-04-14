// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Outputs
{

    [OutputType]
    public sealed class FlowAggregationConfig
    {
        public readonly Pulumi.AwsNative.AppFlow.FlowAggregationType? AggregationType;
        public readonly int? TargetFileSize;

        [OutputConstructor]
        private FlowAggregationConfig(
            Pulumi.AwsNative.AppFlow.FlowAggregationType? aggregationType,

            int? targetFileSize)
        {
            AggregationType = aggregationType;
            TargetFileSize = targetFileSize;
        }
    }
}
