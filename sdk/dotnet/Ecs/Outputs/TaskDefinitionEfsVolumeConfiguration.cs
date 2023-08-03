// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs.Outputs
{

    [OutputType]
    public sealed class TaskDefinitionEfsVolumeConfiguration
    {
        public readonly Outputs.TaskDefinitionAuthorizationConfig? AuthorizationConfig;
        public readonly string FilesystemId;
        public readonly string? RootDirectory;
        public readonly Pulumi.AwsNative.Ecs.TaskDefinitionEfsVolumeConfigurationTransitEncryption? TransitEncryption;
        public readonly int? TransitEncryptionPort;

        [OutputConstructor]
        private TaskDefinitionEfsVolumeConfiguration(
            Outputs.TaskDefinitionAuthorizationConfig? authorizationConfig,

            string filesystemId,

            string? rootDirectory,

            Pulumi.AwsNative.Ecs.TaskDefinitionEfsVolumeConfigurationTransitEncryption? transitEncryption,

            int? transitEncryptionPort)
        {
            AuthorizationConfig = authorizationConfig;
            FilesystemId = filesystemId;
            RootDirectory = rootDirectory;
            TransitEncryption = transitEncryption;
            TransitEncryptionPort = transitEncryptionPort;
        }
    }
}
