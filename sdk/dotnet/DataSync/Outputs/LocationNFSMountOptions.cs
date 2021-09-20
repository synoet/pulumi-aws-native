// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync.Outputs
{

    /// <summary>
    /// The NFS mount options that DataSync can use to mount your NFS share.
    /// </summary>
    [OutputType]
    public sealed class LocationNFSMountOptions
    {
        /// <summary>
        /// The specific NFS version that you want DataSync to use to mount your NFS share.
        /// </summary>
        public readonly Pulumi.AwsNative.DataSync.LocationNFSMountOptionsVersion? Version;

        [OutputConstructor]
        private LocationNFSMountOptions(Pulumi.AwsNative.DataSync.LocationNFSMountOptionsVersion? version)
        {
            Version = version;
        }
    }
}
