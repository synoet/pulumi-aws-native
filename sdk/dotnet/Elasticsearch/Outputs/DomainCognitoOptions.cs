// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Elasticsearch.Outputs
{

    [OutputType]
    public sealed class DomainCognitoOptions
    {
        public readonly bool? Enabled;
        public readonly string? IdentityPoolId;
        public readonly string? RoleArn;
        public readonly string? UserPoolId;

        [OutputConstructor]
        private DomainCognitoOptions(
            bool? enabled,

            string? identityPoolId,

            string? roleArn,

            string? userPoolId)
        {
            Enabled = enabled;
            IdentityPoolId = identityPoolId;
            RoleArn = roleArn;
            UserPoolId = userPoolId;
        }
    }
}
