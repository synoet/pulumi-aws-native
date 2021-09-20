// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamRedshiftDestinationConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("cloudWatchLoggingOptions")]
        public Input<Inputs.DeliveryStreamCloudWatchLoggingOptionsArgs>? CloudWatchLoggingOptions { get; set; }

        [Input("clusterJDBCURL", required: true)]
        public Input<string> ClusterJDBCURL { get; set; } = null!;

        [Input("copyCommand", required: true)]
        public Input<Inputs.DeliveryStreamCopyCommandArgs> CopyCommand { get; set; } = null!;

        [Input("password", required: true)]
        public Input<string> Password { get; set; } = null!;

        [Input("processingConfiguration")]
        public Input<Inputs.DeliveryStreamProcessingConfigurationArgs>? ProcessingConfiguration { get; set; }

        [Input("retryOptions")]
        public Input<Inputs.DeliveryStreamRedshiftRetryOptionsArgs>? RetryOptions { get; set; }

        [Input("roleARN", required: true)]
        public Input<string> RoleARN { get; set; } = null!;

        [Input("s3BackupConfiguration")]
        public Input<Inputs.DeliveryStreamS3DestinationConfigurationArgs>? S3BackupConfiguration { get; set; }

        [Input("s3BackupMode")]
        public Input<Pulumi.AwsNative.KinesisFirehose.DeliveryStreamRedshiftDestinationConfigurationS3BackupMode>? S3BackupMode { get; set; }

        [Input("s3Configuration", required: true)]
        public Input<Inputs.DeliveryStreamS3DestinationConfigurationArgs> S3Configuration { get; set; } = null!;

        [Input("username", required: true)]
        public Input<string> Username { get; set; } = null!;

        public DeliveryStreamRedshiftDestinationConfigurationArgs()
        {
        }
    }
}
