// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolRiskConfigurationAttachmentNotifyConfigurationType
    {
        public readonly Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? BlockEmail;
        public readonly string? From;
        public readonly Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? MfaEmail;
        public readonly Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? NoActionEmail;
        public readonly string? ReplyTo;
        public readonly string SourceArn;

        [OutputConstructor]
        private UserPoolRiskConfigurationAttachmentNotifyConfigurationType(
            Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? blockEmail,

            string? from,

            Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? mfaEmail,

            Outputs.UserPoolRiskConfigurationAttachmentNotifyEmailType? noActionEmail,

            string? replyTo,

            string sourceArn)
        {
            BlockEmail = blockEmail;
            From = from;
            MfaEmail = mfaEmail;
            NoActionEmail = noActionEmail;
            ReplyTo = replyTo;
            SourceArn = sourceArn;
        }
    }
}
