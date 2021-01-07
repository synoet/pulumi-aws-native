// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.FMS.Outputs
{

    [OutputType]
    public sealed class NotificationChannelProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snsrolename
        /// </summary>
        public readonly string SnsRoleName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-fms-notificationchannel.html#cfn-fms-notificationchannel-snstopicarn
        /// </summary>
        public readonly string SnsTopicArn;

        [OutputConstructor]
        private NotificationChannelProperties(
            string SnsRoleName,

            string SnsTopicArn)
        {
            this.SnsRoleName = SnsRoleName;
            this.SnsTopicArn = SnsTopicArn;
        }
    }
}