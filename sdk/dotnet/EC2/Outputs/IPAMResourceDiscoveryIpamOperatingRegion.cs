// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    /// <summary>
    /// The regions IPAM Resource Discovery is enabled for. Allows for monitoring.
    /// </summary>
    [OutputType]
    public sealed class IPAMResourceDiscoveryIpamOperatingRegion
    {
        /// <summary>
        /// The name of the region.
        /// </summary>
        public readonly string RegionName;

        [OutputConstructor]
        private IPAMResourceDiscoveryIpamOperatingRegion(string regionName)
        {
            RegionName = regionName;
        }
    }
}
