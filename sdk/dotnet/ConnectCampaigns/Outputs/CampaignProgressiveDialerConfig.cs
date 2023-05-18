// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ConnectCampaigns.Outputs
{

    /// <summary>
    /// Progressive Dialer config
    /// </summary>
    [OutputType]
    public sealed class CampaignProgressiveDialerConfig
    {
        /// <summary>
        /// The bandwidth allocation of a queue resource.
        /// </summary>
        public readonly double BandwidthAllocation;

        [OutputConstructor]
        private CampaignProgressiveDialerConfig(double bandwidthAllocation)
        {
            BandwidthAllocation = bandwidthAllocation;
        }
    }
}
