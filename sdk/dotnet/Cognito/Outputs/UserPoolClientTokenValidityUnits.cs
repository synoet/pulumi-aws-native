// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Outputs
{

    [OutputType]
    public sealed class UserPoolClientTokenValidityUnits
    {
        public readonly string? AccessToken;
        public readonly string? IdToken;
        public readonly string? RefreshToken;

        [OutputConstructor]
        private UserPoolClientTokenValidityUnits(
            string? accessToken,

            string? idToken,

            string? refreshToken)
        {
            AccessToken = accessToken;
            IdToken = idToken;
            RefreshToken = refreshToken;
        }
    }
}
