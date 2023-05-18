// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SSMContacts.Outputs
{

    /// <summary>
    /// The contacts or contact methods that the escalation plan or engagement plan is engaging.
    /// </summary>
    [OutputType]
    public sealed class PlanTargets
    {
        public readonly Outputs.PlanChannelTargetInfo? ChannelTargetInfo;
        public readonly Outputs.PlanContactTargetInfo? ContactTargetInfo;

        [OutputConstructor]
        private PlanTargets(
            Outputs.PlanChannelTargetInfo? channelTargetInfo,

            Outputs.PlanContactTargetInfo? contactTargetInfo)
        {
            ChannelTargetInfo = channelTargetInfo;
            ContactTargetInfo = contactTargetInfo;
        }
    }
}
