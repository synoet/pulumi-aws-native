// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolClientTokenValidityUnitsArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessToken")]
        public Input<string>? AccessToken { get; set; }

        [Input("idToken")]
        public Input<string>? IdToken { get; set; }

        [Input("refreshToken")]
        public Input<string>? RefreshToken { get; set; }

        public UserPoolClientTokenValidityUnitsArgs()
        {
        }
        public static new UserPoolClientTokenValidityUnitsArgs Empty => new UserPoolClientTokenValidityUnitsArgs();
    }
}
