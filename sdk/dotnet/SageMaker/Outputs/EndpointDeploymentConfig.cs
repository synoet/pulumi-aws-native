// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Outputs
{

    [OutputType]
    public sealed class EndpointDeploymentConfig
    {
        public readonly Outputs.EndpointAutoRollbackConfig? AutoRollbackConfiguration;
        public readonly Outputs.EndpointBlueGreenUpdatePolicy? BlueGreenUpdatePolicy;
        public readonly Outputs.EndpointRollingUpdatePolicy? RollingUpdatePolicy;

        [OutputConstructor]
        private EndpointDeploymentConfig(
            Outputs.EndpointAutoRollbackConfig? autoRollbackConfiguration,

            Outputs.EndpointBlueGreenUpdatePolicy? blueGreenUpdatePolicy,

            Outputs.EndpointRollingUpdatePolicy? rollingUpdatePolicy)
        {
            AutoRollbackConfiguration = autoRollbackConfiguration;
            BlueGreenUpdatePolicy = blueGreenUpdatePolicy;
            RollingUpdatePolicy = rollingUpdatePolicy;
        }
    }
}
