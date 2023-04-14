// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class PipelineLambdaArgs : global::Pulumi.ResourceArgs
    {
        [Input("batchSize", required: true)]
        public Input<int> BatchSize { get; set; } = null!;

        [Input("lambdaName", required: true)]
        public Input<string> LambdaName { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("next")]
        public Input<string>? Next { get; set; }

        public PipelineLambdaArgs()
        {
        }
        public static new PipelineLambdaArgs Empty => new PipelineLambdaArgs();
    }
}
