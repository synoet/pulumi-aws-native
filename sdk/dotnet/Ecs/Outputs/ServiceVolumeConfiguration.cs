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
    public sealed class ServiceVolumeConfiguration
    {
        public readonly Outputs.ServiceManagedEbsVolumeConfiguration? ManagedEbsVolume;
        public readonly string Name;

        [OutputConstructor]
        private ServiceVolumeConfiguration(
            Outputs.ServiceManagedEbsVolumeConfiguration? managedEbsVolume,

            string name)
        {
            ManagedEbsVolume = managedEbsVolume;
            Name = name;
        }
    }
}
