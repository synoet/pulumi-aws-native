// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Backup.Outputs
{

    [OutputType]
    public sealed class BackupPlanBackupRuleResourceType
    {
        public readonly double? CompletionWindowMinutes;
        public readonly ImmutableArray<Outputs.BackupPlanCopyActionResourceType> CopyActions;
        public readonly bool? EnableContinuousBackup;
        public readonly Outputs.BackupPlanLifecycleResourceType? Lifecycle;
        public readonly object? RecoveryPointTags;
        public readonly string RuleName;
        public readonly string? ScheduleExpression;
        public readonly string? ScheduleExpressionTimezone;
        public readonly double? StartWindowMinutes;
        public readonly string TargetBackupVault;

        [OutputConstructor]
        private BackupPlanBackupRuleResourceType(
            double? completionWindowMinutes,

            ImmutableArray<Outputs.BackupPlanCopyActionResourceType> copyActions,

            bool? enableContinuousBackup,

            Outputs.BackupPlanLifecycleResourceType? lifecycle,

            object? recoveryPointTags,

            string ruleName,

            string? scheduleExpression,

            string? scheduleExpressionTimezone,

            double? startWindowMinutes,

            string targetBackupVault)
        {
            CompletionWindowMinutes = completionWindowMinutes;
            CopyActions = copyActions;
            EnableContinuousBackup = enableContinuousBackup;
            Lifecycle = lifecycle;
            RecoveryPointTags = recoveryPointTags;
            RuleName = ruleName;
            ScheduleExpression = scheduleExpression;
            ScheduleExpressionTimezone = scheduleExpressionTimezone;
            StartWindowMinutes = startWindowMinutes;
            TargetBackupVault = targetBackupVault;
        }
    }
}
