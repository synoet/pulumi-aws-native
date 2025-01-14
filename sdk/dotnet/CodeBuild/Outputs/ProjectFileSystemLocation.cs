// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeBuild.Outputs
{

    [OutputType]
    public sealed class ProjectFileSystemLocation
    {
        public readonly string Identifier;
        public readonly string Location;
        public readonly string? MountOptions;
        public readonly string MountPoint;
        public readonly string Type;

        [OutputConstructor]
        private ProjectFileSystemLocation(
            string identifier,

            string location,

            string? mountOptions,

            string mountPoint,

            string type)
        {
            Identifier = identifier;
            Location = location;
            MountOptions = mountOptions;
            MountPoint = mountPoint;
            Type = type;
        }
    }
}
