// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DeviceFarm
{
    public static class GetVPCEConfiguration
    {
        /// <summary>
        /// AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
        /// </summary>
        public static Task<GetVPCEConfigurationResult> InvokeAsync(GetVPCEConfigurationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetVPCEConfigurationResult>("aws-native:devicefarm:getVPCEConfiguration", args ?? new GetVPCEConfigurationArgs(), options.WithDefaults());

        /// <summary>
        /// AWS::DeviceFarm::VPCEConfiguration creates a new Device Farm VPCE Configuration
        /// </summary>
        public static Output<GetVPCEConfigurationResult> Invoke(GetVPCEConfigurationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetVPCEConfigurationResult>("aws-native:devicefarm:getVPCEConfiguration", args ?? new GetVPCEConfigurationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetVPCEConfigurationArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetVPCEConfigurationArgs()
        {
        }
        public static new GetVPCEConfigurationArgs Empty => new GetVPCEConfigurationArgs();
    }

    public sealed class GetVPCEConfigurationInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetVPCEConfigurationInvokeArgs()
        {
        }
        public static new GetVPCEConfigurationInvokeArgs Empty => new GetVPCEConfigurationInvokeArgs();
    }


    [OutputType]
    public sealed class GetVPCEConfigurationResult
    {
        public readonly string? Arn;
        public readonly string? ServiceDnsName;
        public readonly ImmutableArray<Outputs.VPCEConfigurationTag> Tags;
        public readonly string? VpceConfigurationDescription;
        public readonly string? VpceConfigurationName;
        public readonly string? VpceServiceName;

        [OutputConstructor]
        private GetVPCEConfigurationResult(
            string? arn,

            string? serviceDnsName,

            ImmutableArray<Outputs.VPCEConfigurationTag> tags,

            string? vpceConfigurationDescription,

            string? vpceConfigurationName,

            string? vpceServiceName)
        {
            Arn = arn;
            ServiceDnsName = serviceDnsName;
            Tags = tags;
            VpceConfigurationDescription = vpceConfigurationDescription;
            VpceConfigurationName = vpceConfigurationName;
            VpceServiceName = vpceServiceName;
        }
    }
}
