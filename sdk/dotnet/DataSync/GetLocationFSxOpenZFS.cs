// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync
{
    public static class GetLocationFSxOpenZFS
    {
        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxOpenZFS.
        /// </summary>
        public static Task<GetLocationFSxOpenZFSResult> InvokeAsync(GetLocationFSxOpenZFSArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationFSxOpenZFSResult>("aws-native:datasync:getLocationFSxOpenZFS", args ?? new GetLocationFSxOpenZFSArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::DataSync::LocationFSxOpenZFS.
        /// </summary>
        public static Output<GetLocationFSxOpenZFSResult> Invoke(GetLocationFSxOpenZFSInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationFSxOpenZFSResult>("aws-native:datasync:getLocationFSxOpenZFS", args ?? new GetLocationFSxOpenZFSInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLocationFSxOpenZFSArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx OpenZFS file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public string LocationArn { get; set; } = null!;

        public GetLocationFSxOpenZFSArgs()
        {
        }
        public static new GetLocationFSxOpenZFSArgs Empty => new GetLocationFSxOpenZFSArgs();
    }

    public sealed class GetLocationFSxOpenZFSInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx OpenZFS file system location that is created.
        /// </summary>
        [Input("locationArn", required: true)]
        public Input<string> LocationArn { get; set; } = null!;

        public GetLocationFSxOpenZFSInvokeArgs()
        {
        }
        public static new GetLocationFSxOpenZFSInvokeArgs Empty => new GetLocationFSxOpenZFSInvokeArgs();
    }


    [OutputType]
    public sealed class GetLocationFSxOpenZFSResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon FSx OpenZFS file system location that is created.
        /// </summary>
        public readonly string? LocationArn;
        /// <summary>
        /// The URL of the FSx OpenZFS that was described.
        /// </summary>
        public readonly string? LocationUri;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.LocationFSxOpenZFSTag> Tags;

        [OutputConstructor]
        private GetLocationFSxOpenZFSResult(
            string? locationArn,

            string? locationUri,

            ImmutableArray<Outputs.LocationFSxOpenZFSTag> tags)
        {
            LocationArn = locationArn;
            LocationUri = locationUri;
            Tags = tags;
        }
    }
}
