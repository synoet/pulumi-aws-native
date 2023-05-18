// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift
{
    public static class GetLocation
    {
        /// <summary>
        /// The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.
        /// </summary>
        public static Task<GetLocationResult> InvokeAsync(GetLocationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetLocationResult>("aws-native:gamelift:getLocation", args ?? new GetLocationArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::GameLift::Location resource creates an Amazon GameLift (GameLift) custom location.
        /// </summary>
        public static Output<GetLocationResult> Invoke(GetLocationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetLocationResult>("aws-native:gamelift:getLocation", args ?? new GetLocationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetLocationArgs : global::Pulumi.InvokeArgs
    {
        [Input("locationName", required: true)]
        public string LocationName { get; set; } = null!;

        public GetLocationArgs()
        {
        }
        public static new GetLocationArgs Empty => new GetLocationArgs();
    }

    public sealed class GetLocationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("locationName", required: true)]
        public Input<string> LocationName { get; set; } = null!;

        public GetLocationInvokeArgs()
        {
        }
        public static new GetLocationInvokeArgs Empty => new GetLocationInvokeArgs();
    }


    [OutputType]
    public sealed class GetLocationResult
    {
        public readonly string? LocationArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.LocationTag> Tags;

        [OutputConstructor]
        private GetLocationResult(
            string? locationArn,

            ImmutableArray<Outputs.LocationTag> tags)
        {
            LocationArn = locationArn;
            Tags = tags;
        }
    }
}
