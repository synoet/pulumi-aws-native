// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TopicNamedEntityDefinitionMetricArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregation")]
        public Input<Pulumi.AwsNative.QuickSight.TopicNamedEntityAggType>? Aggregation { get; set; }

        [Input("aggregationFunctionParameters")]
        public Input<Inputs.TopicAggregationFunctionParametersArgs>? AggregationFunctionParameters { get; set; }

        public TopicNamedEntityDefinitionMetricArgs()
        {
        }
        public static new TopicNamedEntityDefinitionMetricArgs Empty => new TopicNamedEntityDefinitionMetricArgs();
    }
}
