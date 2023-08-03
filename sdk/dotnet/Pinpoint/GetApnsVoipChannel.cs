// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint
{
    public static class GetApnsVoipChannel
    {
        /// <summary>
        /// Resource Type definition for AWS::Pinpoint::APNSVoipChannel
        /// </summary>
        public static Task<GetApnsVoipChannelResult> InvokeAsync(GetApnsVoipChannelArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetApnsVoipChannelResult>("aws-native:pinpoint:getApnsVoipChannel", args ?? new GetApnsVoipChannelArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Pinpoint::APNSVoipChannel
        /// </summary>
        public static Output<GetApnsVoipChannelResult> Invoke(GetApnsVoipChannelInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetApnsVoipChannelResult>("aws-native:pinpoint:getApnsVoipChannel", args ?? new GetApnsVoipChannelInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetApnsVoipChannelArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetApnsVoipChannelArgs()
        {
        }
        public static new GetApnsVoipChannelArgs Empty => new GetApnsVoipChannelArgs();
    }

    public sealed class GetApnsVoipChannelInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetApnsVoipChannelInvokeArgs()
        {
        }
        public static new GetApnsVoipChannelInvokeArgs Empty => new GetApnsVoipChannelInvokeArgs();
    }


    [OutputType]
    public sealed class GetApnsVoipChannelResult
    {
        public readonly string? BundleId;
        public readonly string? Certificate;
        public readonly string? DefaultAuthenticationMethod;
        public readonly bool? Enabled;
        public readonly string? Id;
        public readonly string? PrivateKey;
        public readonly string? TeamId;
        public readonly string? TokenKey;
        public readonly string? TokenKeyId;

        [OutputConstructor]
        private GetApnsVoipChannelResult(
            string? bundleId,

            string? certificate,

            string? defaultAuthenticationMethod,

            bool? enabled,

            string? id,

            string? privateKey,

            string? teamId,

            string? tokenKey,

            string? tokenKeyId)
        {
            BundleId = bundleId;
            Certificate = certificate;
            DefaultAuthenticationMethod = defaultAuthenticationMethod;
            Enabled = enabled;
            Id = id;
            PrivateKey = privateKey;
            TeamId = teamId;
            TokenKey = tokenKey;
            TokenKeyId = tokenKeyId;
        }
    }
}
