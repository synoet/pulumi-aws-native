// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    /// <summary>
    /// Information about the targets to which audit notifications are sent.
    /// </summary>
    public sealed class AccountAuditConfigurationAuditNotificationTargetConfigurationsArgs : global::Pulumi.ResourceArgs
    {
        [Input("sns")]
        public Input<Inputs.AccountAuditConfigurationAuditNotificationTargetArgs>? Sns { get; set; }

        public AccountAuditConfigurationAuditNotificationTargetConfigurationsArgs()
        {
        }
        public static new AccountAuditConfigurationAuditNotificationTargetConfigurationsArgs Empty => new AccountAuditConfigurationAuditNotificationTargetConfigurationsArgs();
    }
}
