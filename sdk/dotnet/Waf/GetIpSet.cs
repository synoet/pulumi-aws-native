// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Waf
{
    public static class GetIpSet
    {
        /// <summary>
        /// Resource Type definition for AWS::WAF::IPSet
        /// </summary>
        public static Task<GetIpSetResult> InvokeAsync(GetIpSetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetIpSetResult>("aws-native:waf:getIpSet", args ?? new GetIpSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::WAF::IPSet
        /// </summary>
        public static Output<GetIpSetResult> Invoke(GetIpSetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetIpSetResult>("aws-native:waf:getIpSet", args ?? new GetIpSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetIpSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetIpSetArgs()
        {
        }
        public static new GetIpSetArgs Empty => new GetIpSetArgs();
    }

    public sealed class GetIpSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetIpSetInvokeArgs()
        {
        }
        public static new GetIpSetInvokeArgs Empty => new GetIpSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetIpSetResult
    {
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.IpSetIpSetDescriptor> IpSetDescriptors;

        [OutputConstructor]
        private GetIpSetResult(
            string? id,

            ImmutableArray<Outputs.IpSetIpSetDescriptor> ipSetDescriptors)
        {
            Id = id;
            IpSetDescriptors = ipSetDescriptors;
        }
    }
}
