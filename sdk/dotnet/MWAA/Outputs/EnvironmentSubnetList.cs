// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.MWAA.Outputs
{

    [OutputType]
    public sealed class EnvironmentSubnetList
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mwaa-environment-subnetlist.html#cfn-mwaa-environment-subnetlist-subnetlist
        /// </summary>
        public readonly ImmutableArray<string> SubnetList;

        [OutputConstructor]
        private EnvironmentSubnetList(ImmutableArray<string> SubnetList)
        {
            this.SubnetList = SubnetList;
        }
    }
}