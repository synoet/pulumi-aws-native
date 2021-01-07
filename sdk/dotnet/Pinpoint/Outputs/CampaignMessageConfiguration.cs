// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Pinpoint.Outputs
{

    [OutputType]
    public sealed class CampaignMessageConfiguration
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-admmessage
        /// </summary>
        public readonly Outputs.CampaignMessage? ADMMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-apnsmessage
        /// </summary>
        public readonly Outputs.CampaignMessage? APNSMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-baidumessage
        /// </summary>
        public readonly Outputs.CampaignMessage? BaiduMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-defaultmessage
        /// </summary>
        public readonly Outputs.CampaignMessage? DefaultMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-emailmessage
        /// </summary>
        public readonly Outputs.CampaignCampaignEmailMessage? EmailMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-gcmmessage
        /// </summary>
        public readonly Outputs.CampaignMessage? GCMMessage;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-pinpoint-campaign-messageconfiguration.html#cfn-pinpoint-campaign-messageconfiguration-smsmessage
        /// </summary>
        public readonly Outputs.CampaignCampaignSmsMessage? SMSMessage;

        [OutputConstructor]
        private CampaignMessageConfiguration(
            Outputs.CampaignMessage? ADMMessage,

            Outputs.CampaignMessage? APNSMessage,

            Outputs.CampaignMessage? BaiduMessage,

            Outputs.CampaignMessage? DefaultMessage,

            Outputs.CampaignCampaignEmailMessage? EmailMessage,

            Outputs.CampaignMessage? GCMMessage,

            Outputs.CampaignCampaignSmsMessage? SMSMessage)
        {
            this.ADMMessage = ADMMessage;
            this.APNSMessage = APNSMessage;
            this.BaiduMessage = BaiduMessage;
            this.DefaultMessage = DefaultMessage;
            this.EmailMessage = EmailMessage;
            this.GCMMessage = GCMMessage;
            this.SMSMessage = SMSMessage;
        }
    }
}