// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Inputs
{

    public sealed class ApplicationOutputLambdaOutputArgs : Pulumi.ResourceArgs
    {
        [Input("resourceARN", required: true)]
        public Input<string> ResourceARN { get; set; } = null!;

        public ApplicationOutputLambdaOutputArgs()
        {
        }
    }
}
