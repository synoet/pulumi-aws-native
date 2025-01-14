// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CustomerProfiles.Inputs
{

    /// <summary>
    /// Configuration information about the auto-merging process.
    /// </summary>
    public sealed class DomainAutoMergingArgs : global::Pulumi.ResourceArgs
    {
        [Input("conflictResolution")]
        public Input<Inputs.DomainConflictResolutionArgs>? ConflictResolution { get; set; }

        [Input("consolidation")]
        public Input<Inputs.DomainConsolidationArgs>? Consolidation { get; set; }

        /// <summary>
        /// The flag that enables the auto-merging of duplicate profiles.
        /// </summary>
        [Input("enabled", required: true)]
        public Input<bool> Enabled { get; set; } = null!;

        /// <summary>
        /// A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.
        /// </summary>
        [Input("minAllowedConfidenceScoreForMerging")]
        public Input<double>? MinAllowedConfidenceScoreForMerging { get; set; }

        public DomainAutoMergingArgs()
        {
        }
        public static new DomainAutoMergingArgs Empty => new DomainAutoMergingArgs();
    }
}
