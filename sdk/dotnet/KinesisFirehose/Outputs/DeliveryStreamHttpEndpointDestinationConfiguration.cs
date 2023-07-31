// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Outputs
{

    [OutputType]
    public sealed class DeliveryStreamHttpEndpointDestinationConfiguration
    {
        public readonly Outputs.DeliveryStreamBufferingHints? BufferingHints;
        public readonly Outputs.DeliveryStreamCloudWatchLoggingOptions? CloudWatchLoggingOptions;
        public readonly Outputs.DeliveryStreamHttpEndpointConfiguration EndpointConfiguration;
        public readonly Outputs.DeliveryStreamProcessingConfiguration? ProcessingConfiguration;
        public readonly Outputs.DeliveryStreamHttpEndpointRequestConfiguration? RequestConfiguration;
        public readonly Outputs.DeliveryStreamRetryOptions? RetryOptions;
        public readonly string? RoleArn;
        public readonly string? S3BackupMode;
        public readonly Outputs.DeliveryStreamS3DestinationConfiguration S3Configuration;

        [OutputConstructor]
        private DeliveryStreamHttpEndpointDestinationConfiguration(
            Outputs.DeliveryStreamBufferingHints? bufferingHints,

            Outputs.DeliveryStreamCloudWatchLoggingOptions? cloudWatchLoggingOptions,

            Outputs.DeliveryStreamHttpEndpointConfiguration endpointConfiguration,

            Outputs.DeliveryStreamProcessingConfiguration? processingConfiguration,

            Outputs.DeliveryStreamHttpEndpointRequestConfiguration? requestConfiguration,

            Outputs.DeliveryStreamRetryOptions? retryOptions,

            string? roleArn,

            string? s3BackupMode,

            Outputs.DeliveryStreamS3DestinationConfiguration s3Configuration)
        {
            BufferingHints = bufferingHints;
            CloudWatchLoggingOptions = cloudWatchLoggingOptions;
            EndpointConfiguration = endpointConfiguration;
            ProcessingConfiguration = processingConfiguration;
            RequestConfiguration = requestConfiguration;
            RetryOptions = retryOptions;
            RoleArn = roleArn;
            S3BackupMode = s3BackupMode;
            S3Configuration = s3Configuration;
        }
    }
}
