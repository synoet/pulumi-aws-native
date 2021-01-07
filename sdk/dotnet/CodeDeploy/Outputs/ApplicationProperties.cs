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
    public sealed class ApplicationProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname
        /// </summary>
        public readonly string? ApplicationName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform
        /// </summary>
        public readonly string? ComputePlatform;

        [OutputConstructor]
        private ApplicationProperties(
            string? ApplicationName,

            string? ComputePlatform)
        {
            this.ApplicationName = ApplicationName;
            this.ComputePlatform = ComputePlatform;
        }
    }
}