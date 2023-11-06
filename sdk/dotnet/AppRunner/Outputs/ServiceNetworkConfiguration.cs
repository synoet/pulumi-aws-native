// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner.Outputs
{

    /// <summary>
    /// Network configuration
    /// </summary>
    [OutputType]
    public sealed class ServiceNetworkConfiguration
    {
        public readonly Outputs.ServiceEgressConfiguration? EgressConfiguration;
        public readonly Outputs.ServiceIngressConfiguration? IngressConfiguration;
        /// <summary>
        /// App Runner service endpoint IP address type
        /// </summary>
        public readonly Pulumi.AwsNative.AppRunner.ServiceNetworkConfigurationIpAddressType? IpAddressType;

        [OutputConstructor]
        private ServiceNetworkConfiguration(
            Outputs.ServiceEgressConfiguration? egressConfiguration,

            Outputs.ServiceIngressConfiguration? ingressConfiguration,

            Pulumi.AwsNative.AppRunner.ServiceNetworkConfigurationIpAddressType? ipAddressType)
        {
            EgressConfiguration = egressConfiguration;
            IngressConfiguration = ingressConfiguration;
            IpAddressType = ipAddressType;
        }
    }
}
