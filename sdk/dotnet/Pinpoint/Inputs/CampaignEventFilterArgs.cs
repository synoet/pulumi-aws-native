// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Inputs
{

    public sealed class CampaignEventFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("dimensions")]
        public Input<Inputs.CampaignEventDimensionsArgs>? Dimensions { get; set; }

        [Input("filterType")]
        public Input<string>? FilterType { get; set; }

        public CampaignEventFilterArgs()
        {
        }
        public static new CampaignEventFilterArgs Empty => new CampaignEventFilterArgs();
    }
}
