// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2
{
    public static class GetListenerCertificate
    {
        /// <summary>
        /// Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate
        /// </summary>
        public static Task<GetListenerCertificateResult> InvokeAsync(GetListenerCertificateArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetListenerCertificateResult>("aws-native:elasticloadbalancingv2:getListenerCertificate", args ?? new GetListenerCertificateArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerCertificate
        /// </summary>
        public static Output<GetListenerCertificateResult> Invoke(GetListenerCertificateInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetListenerCertificateResult>("aws-native:elasticloadbalancingv2:getListenerCertificate", args ?? new GetListenerCertificateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetListenerCertificateArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetListenerCertificateArgs()
        {
        }
        public static new GetListenerCertificateArgs Empty => new GetListenerCertificateArgs();
    }

    public sealed class GetListenerCertificateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetListenerCertificateInvokeArgs()
        {
        }
        public static new GetListenerCertificateInvokeArgs Empty => new GetListenerCertificateInvokeArgs();
    }


    [OutputType]
    public sealed class GetListenerCertificateResult
    {
        public readonly ImmutableArray<Outputs.ListenerCertificateCertificate> Certificates;
        public readonly string? Id;

        [OutputConstructor]
        private GetListenerCertificateResult(
            ImmutableArray<Outputs.ListenerCertificateCertificate> certificates,

            string? id)
        {
            Certificates = certificates;
            Id = id;
        }
    }
}
