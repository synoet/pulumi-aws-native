// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Inputs
{

    public sealed class ApplicationApplicationSnapshotConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("snapshotsEnabled", required: true)]
        public Input<bool> SnapshotsEnabled { get; set; } = null!;

        public ApplicationApplicationSnapshotConfigurationArgs()
        {
        }
    }
}
