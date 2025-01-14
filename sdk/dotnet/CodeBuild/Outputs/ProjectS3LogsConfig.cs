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
    public sealed class ProjectS3LogsConfig
    {
        public readonly bool? EncryptionDisabled;
        public readonly string? Location;
        public readonly string Status;

        [OutputConstructor]
        private ProjectS3LogsConfig(
            bool? encryptionDisabled,

            string? location,

            string status)
        {
            EncryptionDisabled = encryptionDisabled;
            Location = location;
            Status = status;
        }
    }
}
