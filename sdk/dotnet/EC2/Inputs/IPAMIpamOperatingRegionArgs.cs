// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    /// <summary>
    /// The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
    /// </summary>
    public sealed class IPAMIpamOperatingRegionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the region.
        /// </summary>
        [Input("regionName", required: true)]
        public Input<string> RegionName { get; set; } = null!;

        public IPAMIpamOperatingRegionArgs()
        {
        }
        public static new IPAMIpamOperatingRegionArgs Empty => new IPAMIpamOperatingRegionArgs();
    }
}
