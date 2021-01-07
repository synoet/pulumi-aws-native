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
    public sealed class SMSChannelProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-applicationid
        /// </summary>
        public readonly string ApplicationId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-enabled
        /// </summary>
        public readonly bool? Enabled;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-senderid
        /// </summary>
        public readonly string? SenderId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-pinpoint-smschannel.html#cfn-pinpoint-smschannel-shortcode
        /// </summary>
        public readonly string? ShortCode;

        [OutputConstructor]
        private SMSChannelProperties(
            string ApplicationId,

            bool? Enabled,

            string? SenderId,

            string? ShortCode)
        {
            this.ApplicationId = ApplicationId;
            this.Enabled = Enabled;
            this.SenderId = SenderId;
            this.ShortCode = ShortCode;
        }
    }
}