// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolDomainProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-customdomainconfig
        /// </summary>
        public readonly Outputs.UserPoolDomainCustomDomainConfigType? CustomDomainConfig;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-domain
        /// </summary>
        public readonly string Domain;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-userpooldomain.html#cfn-cognito-userpooldomain-userpoolid
        /// </summary>
        public readonly string UserPoolId;

        [OutputConstructor]
        private UserPoolDomainProperties(
            Outputs.UserPoolDomainCustomDomainConfigType? CustomDomainConfig,

            string Domain,

            string UserPoolId)
        {
            this.CustomDomainConfig = CustomDomainConfig;
            this.Domain = Domain;
            this.UserPoolId = UserPoolId;
        }
    }
}