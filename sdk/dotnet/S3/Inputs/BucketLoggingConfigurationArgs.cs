// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    public sealed class BucketLoggingConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of an Amazon S3 bucket where Amazon S3 store server access log files. You can store log files in any bucket that you own. By default, logs are stored in the bucket where the LoggingConfiguration property is defined.
        /// </summary>
        [Input("destinationBucketName")]
        public Input<string>? DestinationBucketName { get; set; }

        [Input("logFilePrefix")]
        public Input<string>? LogFilePrefix { get; set; }

        [Input("targetObjectKeyFormat")]
        public Input<Inputs.BucketTargetObjectKeyFormatArgs>? TargetObjectKeyFormat { get; set; }

        public BucketLoggingConfigurationArgs()
        {
        }
        public static new BucketLoggingConfigurationArgs Empty => new BucketLoggingConfigurationArgs();
    }
}
