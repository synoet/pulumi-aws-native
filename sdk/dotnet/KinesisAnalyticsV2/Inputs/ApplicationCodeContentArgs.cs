// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Inputs
{

    /// <summary>
    /// Specifies either the application code, or the location of the application code, for a Flink-based Kinesis Data Analytics application.
    /// </summary>
    public sealed class ApplicationCodeContentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Information about the Amazon S3 bucket that contains the application code.
        /// </summary>
        [Input("s3ContentLocation")]
        public Input<Inputs.ApplicationS3ContentLocationArgs>? S3ContentLocation { get; set; }

        /// <summary>
        /// The text-format code for a Flink-based Kinesis Data Analytics application.
        /// </summary>
        [Input("textContent")]
        public Input<string>? TextContent { get; set; }

        /// <summary>
        /// The zip-format code for a Flink-based Kinesis Data Analytics application.
        /// </summary>
        [Input("zipFileContent")]
        public Input<string>? ZipFileContent { get; set; }

        public ApplicationCodeContentArgs()
        {
        }
    }
}
