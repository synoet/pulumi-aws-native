// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    public sealed class VolumeOntapConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("copyTagsToBackups")]
        public Input<string>? CopyTagsToBackups { get; set; }

        [Input("junctionPath")]
        public Input<string>? JunctionPath { get; set; }

        [Input("ontapVolumeType")]
        public Input<string>? OntapVolumeType { get; set; }

        [Input("securityStyle")]
        public Input<string>? SecurityStyle { get; set; }

        [Input("sizeInMegabytes", required: true)]
        public Input<string> SizeInMegabytes { get; set; } = null!;

        [Input("snaplockConfiguration")]
        public Input<Inputs.VolumeSnaplockConfigurationArgs>? SnaplockConfiguration { get; set; }

        [Input("snapshotPolicy")]
        public Input<string>? SnapshotPolicy { get; set; }

        [Input("storageEfficiencyEnabled")]
        public Input<string>? StorageEfficiencyEnabled { get; set; }

        [Input("storageVirtualMachineId", required: true)]
        public Input<string> StorageVirtualMachineId { get; set; } = null!;

        [Input("tieringPolicy")]
        public Input<Inputs.VolumeTieringPolicyArgs>? TieringPolicy { get; set; }

        public VolumeOntapConfigurationArgs()
        {
        }
        public static new VolumeOntapConfigurationArgs Empty => new VolumeOntapConfigurationArgs();
    }
}
