// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchService.Inputs
{

    public sealed class DomainCognitoOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("identityPoolId")]
        public Input<string>? IdentityPoolId { get; set; }

        [Input("roleArn")]
        public Input<string>? RoleArn { get; set; }

        [Input("userPoolId")]
        public Input<string>? UserPoolId { get; set; }

        public DomainCognitoOptionsArgs()
        {
        }
        public static new DomainCognitoOptionsArgs Empty => new DomainCognitoOptionsArgs();
    }
}
