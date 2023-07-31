// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Inputs
{

    public sealed class CampaignInAppMessageButtonArgs : global::Pulumi.ResourceArgs
    {
        [Input("android")]
        public Input<Inputs.CampaignOverrideButtonConfigurationArgs>? Android { get; set; }

        [Input("defaultConfig")]
        public Input<Inputs.CampaignDefaultButtonConfigurationArgs>? DefaultConfig { get; set; }

        [Input("ios")]
        public Input<Inputs.CampaignOverrideButtonConfigurationArgs>? Ios { get; set; }

        [Input("web")]
        public Input<Inputs.CampaignOverrideButtonConfigurationArgs>? Web { get; set; }

        public CampaignInAppMessageButtonArgs()
        {
        }
        public static new CampaignInAppMessageButtonArgs Empty => new CampaignInAppMessageButtonArgs();
    }
}
