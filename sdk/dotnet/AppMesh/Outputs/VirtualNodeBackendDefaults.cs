// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AppMesh.Outputs
{

    [OutputType]
    public sealed class VirtualNodeBackendDefaults
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appmesh-virtualnode-backenddefaults.html#cfn-appmesh-virtualnode-backenddefaults-clientpolicy
        /// </summary>
        public readonly Outputs.VirtualNodeClientPolicy? ClientPolicy;

        [OutputConstructor]
        private VirtualNodeBackendDefaults(Outputs.VirtualNodeClientPolicy? ClientPolicy)
        {
            this.ClientPolicy = ClientPolicy;
        }
    }
}