// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PinpointEmail
{
    public static class GetConfigurationSet
    {
        /// <summary>
        /// Resource Type definition for AWS::PinpointEmail::ConfigurationSet
        /// </summary>
        public static Task<GetConfigurationSetResult> InvokeAsync(GetConfigurationSetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetConfigurationSetResult>("aws-native:pinpointemail:getConfigurationSet", args ?? new GetConfigurationSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::PinpointEmail::ConfigurationSet
        /// </summary>
        public static Output<GetConfigurationSetResult> Invoke(GetConfigurationSetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetConfigurationSetResult>("aws-native:pinpointemail:getConfigurationSet", args ?? new GetConfigurationSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConfigurationSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetConfigurationSetArgs()
        {
        }
        public static new GetConfigurationSetArgs Empty => new GetConfigurationSetArgs();
    }

    public sealed class GetConfigurationSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetConfigurationSetInvokeArgs()
        {
        }
        public static new GetConfigurationSetInvokeArgs Empty => new GetConfigurationSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetConfigurationSetResult
    {
        public readonly Outputs.ConfigurationSetDeliveryOptions? DeliveryOptions;
        public readonly string? Id;
        public readonly Outputs.ConfigurationSetReputationOptions? ReputationOptions;
        public readonly Outputs.ConfigurationSetSendingOptions? SendingOptions;
        public readonly ImmutableArray<Outputs.ConfigurationSetTags> Tags;
        public readonly Outputs.ConfigurationSetTrackingOptions? TrackingOptions;

        [OutputConstructor]
        private GetConfigurationSetResult(
            Outputs.ConfigurationSetDeliveryOptions? deliveryOptions,

            string? id,

            Outputs.ConfigurationSetReputationOptions? reputationOptions,

            Outputs.ConfigurationSetSendingOptions? sendingOptions,

            ImmutableArray<Outputs.ConfigurationSetTags> tags,

            Outputs.ConfigurationSetTrackingOptions? trackingOptions)
        {
            DeliveryOptions = deliveryOptions;
            Id = id;
            ReputationOptions = reputationOptions;
            SendingOptions = sendingOptions;
            Tags = tags;
            TrackingOptions = trackingOptions;
        }
    }
}
