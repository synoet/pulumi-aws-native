// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisVideo
{
    public static class GetStream
    {
        /// <summary>
        /// Resource Type Definition for AWS::KinesisVideo::Stream
        /// </summary>
        public static Task<GetStreamResult> InvokeAsync(GetStreamArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStreamResult>("aws-native:kinesisvideo:getStream", args ?? new GetStreamArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type Definition for AWS::KinesisVideo::Stream
        /// </summary>
        public static Output<GetStreamResult> Invoke(GetStreamInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStreamResult>("aws-native:kinesisvideo:getStream", args ?? new GetStreamInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStreamArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Kinesis Video stream.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetStreamArgs()
        {
        }
        public static new GetStreamArgs Empty => new GetStreamArgs();
    }

    public sealed class GetStreamInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the Kinesis Video stream.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetStreamInvokeArgs()
        {
        }
        public static new GetStreamInvokeArgs Empty => new GetStreamInvokeArgs();
    }


    [OutputType]
    public sealed class GetStreamResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Kinesis Video stream.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The number of hours till which Kinesis Video will retain the data in the stream
        /// </summary>
        public readonly int? DataRetentionInHours;
        /// <summary>
        /// The name of the device that is writing to the stream.
        /// </summary>
        public readonly string? DeviceName;
        /// <summary>
        /// AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        /// </summary>
        public readonly string? KmsKeyId;
        /// <summary>
        /// The media type of the stream. Consumers of the stream can use this information when processing the stream.
        /// </summary>
        public readonly string? MediaType;
        /// <summary>
        /// An array of key-value pairs associated with the Kinesis Video Stream.
        /// </summary>
        public readonly ImmutableArray<Outputs.StreamTag> Tags;

        [OutputConstructor]
        private GetStreamResult(
            string? arn,

            int? dataRetentionInHours,

            string? deviceName,

            string? kmsKeyId,

            string? mediaType,

            ImmutableArray<Outputs.StreamTag> tags)
        {
            Arn = arn;
            DataRetentionInHours = dataRetentionInHours;
            DeviceName = deviceName;
            KmsKeyId = kmsKeyId;
            MediaType = mediaType;
            Tags = tags;
        }
    }
}
