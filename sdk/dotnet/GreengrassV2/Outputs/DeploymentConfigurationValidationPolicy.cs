// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GreengrassV2.Outputs
{

    [OutputType]
    public sealed class DeploymentConfigurationValidationPolicy
    {
        public readonly int? TimeoutInSeconds;

        [OutputConstructor]
        private DeploymentConfigurationValidationPolicy(int? timeoutInSeconds)
        {
            TimeoutInSeconds = timeoutInSeconds;
        }
    }
}
