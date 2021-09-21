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
    public sealed class ModelVpcConfig
    {
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly ImmutableArray<string> Subnets;

        [OutputConstructor]
        private ModelVpcConfig(
            ImmutableArray<string> securityGroupIds,

            ImmutableArray<string> subnets)
        {
            SecurityGroupIds = securityGroupIds;
            Subnets = subnets;
        }
    }
}
