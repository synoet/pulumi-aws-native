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
    public sealed class BackupPlanLifecycleResourceType
    {
        public readonly double? DeleteAfterDays;
        public readonly double? MoveToColdStorageAfterDays;
        public readonly bool? OptInToArchiveForSupportedResources;

        [OutputConstructor]
        private BackupPlanLifecycleResourceType(
            double? deleteAfterDays,

            double? moveToColdStorageAfterDays,

            bool? optInToArchiveForSupportedResources)
        {
            DeleteAfterDays = deleteAfterDays;
            MoveToColdStorageAfterDays = moveToColdStorageAfterDays;
            OptInToArchiveForSupportedResources = optInToArchiveForSupportedResources;
        }
    }
}
