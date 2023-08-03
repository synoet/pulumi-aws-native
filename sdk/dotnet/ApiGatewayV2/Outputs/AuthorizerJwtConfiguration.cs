// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2.Outputs
{

    [OutputType]
    public sealed class AuthorizerJwtConfiguration
    {
        public readonly ImmutableArray<string> Audience;
        public readonly string? Issuer;

        [OutputConstructor]
        private AuthorizerJwtConfiguration(
            ImmutableArray<string> audience,

            string? issuer)
        {
            Audience = audience;
            Issuer = issuer;
        }
    }
}
