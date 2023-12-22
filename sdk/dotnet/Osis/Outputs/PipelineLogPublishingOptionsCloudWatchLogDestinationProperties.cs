// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Osis.Outputs
{

    /// <summary>
    /// The destination for OpenSearch Ingestion Service logs sent to Amazon CloudWatch.
    /// </summary>
    [OutputType]
    public sealed class PipelineLogPublishingOptionsCloudWatchLogDestinationProperties
    {
        public readonly string LogGroup;

        [OutputConstructor]
        private PipelineLogPublishingOptionsCloudWatchLogDestinationProperties(string logGroup)
        {
            LogGroup = logGroup;
        }
    }
}
