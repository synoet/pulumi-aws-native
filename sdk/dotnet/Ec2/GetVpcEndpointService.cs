// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetVpcEndpointService
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::VPCEndpointService
        /// </summary>
        public static Task<GetVpcEndpointServiceResult> InvokeAsync(GetVpcEndpointServiceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVpcEndpointServiceResult>("aws-native:ec2:getVpcEndpointService", args ?? new GetVpcEndpointServiceArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::VPCEndpointService
        /// </summary>
        public static Output<GetVpcEndpointServiceResult> Invoke(GetVpcEndpointServiceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVpcEndpointServiceResult>("aws-native:ec2:getVpcEndpointService", args ?? new GetVpcEndpointServiceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVpcEndpointServiceArgs : global::Pulumi.InvokeArgs
    {
        [Input("serviceId", required: true)]
        public string ServiceId { get; set; } = null!;

        public GetVpcEndpointServiceArgs()
        {
        }
        public static new GetVpcEndpointServiceArgs Empty => new GetVpcEndpointServiceArgs();
    }

    public sealed class GetVpcEndpointServiceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("serviceId", required: true)]
        public Input<string> ServiceId { get; set; } = null!;

        public GetVpcEndpointServiceInvokeArgs()
        {
        }
        public static new GetVpcEndpointServiceInvokeArgs Empty => new GetVpcEndpointServiceInvokeArgs();
    }


    [OutputType]
    public sealed class GetVpcEndpointServiceResult
    {
        public readonly bool? AcceptanceRequired;
        public readonly ImmutableArray<string> GatewayLoadBalancerArns;
        public readonly ImmutableArray<string> NetworkLoadBalancerArns;
        public readonly string? PayerResponsibility;
        public readonly string? ServiceId;

        [OutputConstructor]
        private GetVpcEndpointServiceResult(
            bool? acceptanceRequired,

            ImmutableArray<string> gatewayLoadBalancerArns,

            ImmutableArray<string> networkLoadBalancerArns,

            string? payerResponsibility,

            string? serviceId)
        {
            AcceptanceRequired = acceptanceRequired;
            GatewayLoadBalancerArns = gatewayLoadBalancerArns;
            NetworkLoadBalancerArns = networkLoadBalancerArns;
            PayerResponsibility = payerResponsibility;
            ServiceId = serviceId;
        }
    }
}
