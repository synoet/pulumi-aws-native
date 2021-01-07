// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.GameLift.Outputs
{

    [OutputType]
    public sealed class MatchmakingConfigurationProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired
        /// </summary>
        public readonly bool AcceptanceRequired;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds
        /// </summary>
        public readonly int? AcceptanceTimeoutSeconds;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount
        /// </summary>
        public readonly int? AdditionalPlayerCount;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode
        /// </summary>
        public readonly string? BackfillMode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata
        /// </summary>
        public readonly string? CustomEventData;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-flexmatchmode
        /// </summary>
        public readonly string? FlexMatchMode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties
        /// </summary>
        public readonly ImmutableArray<Outputs.MatchmakingConfigurationGameProperty> GameProperties;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata
        /// </summary>
        public readonly string? GameSessionData;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns
        /// </summary>
        public readonly ImmutableArray<string> GameSessionQueueArns;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget
        /// </summary>
        public readonly string? NotificationTarget;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds
        /// </summary>
        public readonly int RequestTimeoutSeconds;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname
        /// </summary>
        public readonly string RuleSetName;

        [OutputConstructor]
        private MatchmakingConfigurationProperties(
            bool AcceptanceRequired,

            int? AcceptanceTimeoutSeconds,

            int? AdditionalPlayerCount,

            string? BackfillMode,

            string? CustomEventData,

            string? Description,

            string? FlexMatchMode,

            ImmutableArray<Outputs.MatchmakingConfigurationGameProperty> GameProperties,

            string? GameSessionData,

            ImmutableArray<string> GameSessionQueueArns,

            string Name,

            string? NotificationTarget,

            int RequestTimeoutSeconds,

            string RuleSetName)
        {
            this.AcceptanceRequired = AcceptanceRequired;
            this.AcceptanceTimeoutSeconds = AcceptanceTimeoutSeconds;
            this.AdditionalPlayerCount = AdditionalPlayerCount;
            this.BackfillMode = BackfillMode;
            this.CustomEventData = CustomEventData;
            this.Description = Description;
            this.FlexMatchMode = FlexMatchMode;
            this.GameProperties = GameProperties;
            this.GameSessionData = GameSessionData;
            this.GameSessionQueueArns = GameSessionQueueArns;
            this.Name = Name;
            this.NotificationTarget = NotificationTarget;
            this.RequestTimeoutSeconds = RequestTimeoutSeconds;
            this.RuleSetName = RuleSetName;
        }
    }
}