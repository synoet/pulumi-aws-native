// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeDeploy.Inputs
{

    public sealed class DeploymentGroupEcsServiceArgs : global::Pulumi.ResourceArgs
    {
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        [Input("serviceName", required: true)]
        public Input<string> ServiceName { get; set; } = null!;

        public DeploymentGroupEcsServiceArgs()
        {
        }
        public static new DeploymentGroupEcsServiceArgs Empty => new DeploymentGroupEcsServiceArgs();
    }
}
