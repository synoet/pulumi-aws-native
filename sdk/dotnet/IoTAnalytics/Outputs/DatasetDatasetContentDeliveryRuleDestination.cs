// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Outputs
{

    [OutputType]
    public sealed class DatasetDatasetContentDeliveryRuleDestination
    {
        public readonly Outputs.DatasetIotEventsDestinationConfiguration? IotEventsDestinationConfiguration;
        public readonly Outputs.DatasetS3DestinationConfiguration? S3DestinationConfiguration;

        [OutputConstructor]
        private DatasetDatasetContentDeliveryRuleDestination(
            Outputs.DatasetIotEventsDestinationConfiguration? iotEventsDestinationConfiguration,

            Outputs.DatasetS3DestinationConfiguration? s3DestinationConfiguration)
        {
            IotEventsDestinationConfiguration = iotEventsDestinationConfiguration;
            S3DestinationConfiguration = s3DestinationConfiguration;
        }
    }
}
