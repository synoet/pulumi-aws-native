// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EFS.Inputs
{

    public sealed class AccessPointCreationInfoArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the POSIX group ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        /// </summary>
        [Input("ownerGid", required: true)]
        public Input<string> OwnerGid { get; set; } = null!;

        /// <summary>
        /// Specifies the POSIX user ID to apply to the RootDirectory. Accepts values from 0 to 2^32 (4294967295).
        /// </summary>
        [Input("ownerUid", required: true)]
        public Input<string> OwnerUid { get; set; } = null!;

        /// <summary>
        /// Specifies the POSIX permissions to apply to the RootDirectory, in the format of an octal number representing the file's mode bits.
        /// </summary>
        [Input("permissions", required: true)]
        public Input<string> Permissions { get; set; } = null!;

        public AccessPointCreationInfoArgs()
        {
        }
        public static new AccessPointCreationInfoArgs Empty => new AccessPointCreationInfoArgs();
    }
}
