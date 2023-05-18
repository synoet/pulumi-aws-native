// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync.Outputs
{

    /// <summary>
    /// SMB protocol configuration for FSx ONTAP file system.
    /// </summary>
    [OutputType]
    public sealed class LocationFSxONTAPSMB
    {
        /// <summary>
        /// The name of the Windows domain that the SMB server belongs to.
        /// </summary>
        public readonly string? Domain;
        public readonly Outputs.LocationFSxONTAPSmbMountOptions MountOptions;
        /// <summary>
        /// The password of the user who can mount the share and has the permissions to access files and folders in the SMB share.
        /// </summary>
        public readonly string Password;
        /// <summary>
        /// The user who can mount the share, has the permissions to access files and folders in the SMB share.
        /// </summary>
        public readonly string User;

        [OutputConstructor]
        private LocationFSxONTAPSMB(
            string? domain,

            Outputs.LocationFSxONTAPSmbMountOptions mountOptions,

            string password,

            string user)
        {
            Domain = domain;
            MountOptions = mountOptions;
            Password = password;
            User = user;
        }
    }
}
