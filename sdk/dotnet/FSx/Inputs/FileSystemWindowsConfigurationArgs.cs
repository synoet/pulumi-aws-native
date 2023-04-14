// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    public sealed class FileSystemWindowsConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("activeDirectoryId")]
        public Input<string>? ActiveDirectoryId { get; set; }

        [Input("aliases")]
        private InputList<string>? _aliases;
        public InputList<string> Aliases
        {
            get => _aliases ?? (_aliases = new InputList<string>());
            set => _aliases = value;
        }

        [Input("auditLogConfiguration")]
        public Input<Inputs.FileSystemAuditLogConfigurationArgs>? AuditLogConfiguration { get; set; }

        [Input("automaticBackupRetentionDays")]
        public Input<int>? AutomaticBackupRetentionDays { get; set; }

        [Input("copyTagsToBackups")]
        public Input<bool>? CopyTagsToBackups { get; set; }

        [Input("dailyAutomaticBackupStartTime")]
        public Input<string>? DailyAutomaticBackupStartTime { get; set; }

        [Input("deploymentType")]
        public Input<string>? DeploymentType { get; set; }

        [Input("preferredSubnetId")]
        public Input<string>? PreferredSubnetId { get; set; }

        [Input("selfManagedActiveDirectoryConfiguration")]
        public Input<Inputs.FileSystemSelfManagedActiveDirectoryConfigurationArgs>? SelfManagedActiveDirectoryConfiguration { get; set; }

        [Input("throughputCapacity", required: true)]
        public Input<int> ThroughputCapacity { get; set; } = null!;

        [Input("weeklyMaintenanceStartTime")]
        public Input<string>? WeeklyMaintenanceStartTime { get; set; }

        public FileSystemWindowsConfigurationArgs()
        {
        }
        public static new FileSystemWindowsConfigurationArgs Empty => new FileSystemWindowsConfigurationArgs();
    }
}
