// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Outputs
{

    [OutputType]
    public sealed class CampaignDataDestinationConfig0Properties
    {
        public readonly Outputs.CampaignS3Config S3Config;

        [OutputConstructor]
        private CampaignDataDestinationConfig0Properties(Outputs.CampaignS3Config s3Config)
        {
            S3Config = s3Config;
        }
    }
}
