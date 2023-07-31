// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Outputs
{

    [OutputType]
    public sealed class CampaignTemplateConfiguration
    {
        public readonly Outputs.CampaignTemplate? EmailTemplate;
        public readonly Outputs.CampaignTemplate? PushTemplate;
        public readonly Outputs.CampaignTemplate? SmsTemplate;
        public readonly Outputs.CampaignTemplate? VoiceTemplate;

        [OutputConstructor]
        private CampaignTemplateConfiguration(
            Outputs.CampaignTemplate? emailTemplate,

            Outputs.CampaignTemplate? pushTemplate,

            Outputs.CampaignTemplate? smsTemplate,

            Outputs.CampaignTemplate? voiceTemplate)
        {
            EmailTemplate = emailTemplate;
            PushTemplate = pushTemplate;
            SmsTemplate = smsTemplate;
            VoiceTemplate = voiceTemplate;
        }
    }
}
