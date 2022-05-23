// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Outputs
{

    [OutputType]
    public sealed class MeshSpec
    {
        public readonly Outputs.MeshEgressFilter? EgressFilter;
        public readonly Outputs.MeshServiceDiscovery? ServiceDiscovery;

        [OutputConstructor]
        private MeshSpec(
            Outputs.MeshEgressFilter? egressFilter,

            Outputs.MeshServiceDiscovery? serviceDiscovery)
        {
            EgressFilter = egressFilter;
            ServiceDiscovery = serviceDiscovery;
        }
    }
}
