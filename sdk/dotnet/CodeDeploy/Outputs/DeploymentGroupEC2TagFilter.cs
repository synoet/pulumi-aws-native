// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CodeDeploy.Outputs
{

    [OutputType]
    public sealed class DeploymentGroupEC2TagFilter
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key
        /// </summary>
        public readonly string? Key;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value
        /// </summary>
        public readonly string? Value;

        [OutputConstructor]
        private DeploymentGroupEC2TagFilter(
            string? Key,

            string? Type,

            string? Value)
        {
            this.Key = Key;
            this.Type = Type;
            this.Value = Value;
        }
    }
}