// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalytics.Outputs
{

    [OutputType]
    public sealed class ApplicationInputProcessingConfiguration
    {
        public readonly Outputs.ApplicationInputLambdaProcessor? InputLambdaProcessor;

        [OutputConstructor]
        private ApplicationInputProcessingConfiguration(Outputs.ApplicationInputLambdaProcessor? inputLambdaProcessor)
        {
            InputLambdaProcessor = inputLambdaProcessor;
        }
    }
}
