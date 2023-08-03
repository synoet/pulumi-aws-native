// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetCaCertificate
    {
        /// <summary>
        /// Registers a CA Certificate in IoT.
        /// </summary>
        public static Task<GetCaCertificateResult> InvokeAsync(GetCaCertificateArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCaCertificateResult>("aws-native:iot:getCaCertificate", args ?? new GetCaCertificateArgs(), options.WithDefaults());

        /// <summary>
        /// Registers a CA Certificate in IoT.
        /// </summary>
        public static Output<GetCaCertificateResult> Invoke(GetCaCertificateInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCaCertificateResult>("aws-native:iot:getCaCertificate", args ?? new GetCaCertificateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCaCertificateArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetCaCertificateArgs()
        {
        }
        public static new GetCaCertificateArgs Empty => new GetCaCertificateArgs();
    }

    public sealed class GetCaCertificateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetCaCertificateInvokeArgs()
        {
        }
        public static new GetCaCertificateInvokeArgs Empty => new GetCaCertificateInvokeArgs();
    }


    [OutputType]
    public sealed class GetCaCertificateResult
    {
        public readonly string? Arn;
        public readonly Pulumi.AwsNative.IoT.CaCertificateAutoRegistrationStatus? AutoRegistrationStatus;
        public readonly string? Id;
        public readonly Outputs.CaCertificateRegistrationConfig? RegistrationConfig;
        public readonly Pulumi.AwsNative.IoT.CaCertificateStatus? Status;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.CaCertificateTag> Tags;

        [OutputConstructor]
        private GetCaCertificateResult(
            string? arn,

            Pulumi.AwsNative.IoT.CaCertificateAutoRegistrationStatus? autoRegistrationStatus,

            string? id,

            Outputs.CaCertificateRegistrationConfig? registrationConfig,

            Pulumi.AwsNative.IoT.CaCertificateStatus? status,

            ImmutableArray<Outputs.CaCertificateTag> tags)
        {
            Arn = arn;
            AutoRegistrationStatus = autoRegistrationStatus;
            Id = id;
            RegistrationConfig = registrationConfig;
            Status = status;
            Tags = tags;
        }
    }
}
