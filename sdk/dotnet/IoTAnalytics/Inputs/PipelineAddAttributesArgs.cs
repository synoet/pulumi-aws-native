// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class PipelineAddAttributesArgs : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        public Input<object>? Attributes { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("next")]
        public Input<string>? Next { get; set; }

        public PipelineAddAttributesArgs()
        {
        }
    }
}
