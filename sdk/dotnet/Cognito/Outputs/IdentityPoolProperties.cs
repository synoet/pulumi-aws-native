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
    public sealed class IdentityPoolProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowclassicflow
        /// </summary>
        public readonly bool? AllowClassicFlow;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-allowunauthenticatedidentities
        /// </summary>
        public readonly bool AllowUnauthenticatedIdentities;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoevents
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? CognitoEvents;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitoidentityproviders
        /// </summary>
        public readonly ImmutableArray<Outputs.IdentityPoolCognitoIdentityProvider> CognitoIdentityProviders;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-cognitostreams
        /// </summary>
        public readonly Outputs.IdentityPoolCognitoStreams? CognitoStreams;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-developerprovidername
        /// </summary>
        public readonly string? DeveloperProviderName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-identitypoolname
        /// </summary>
        public readonly string? IdentityPoolName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-openidconnectproviderarns
        /// </summary>
        public readonly ImmutableArray<string> OpenIdConnectProviderARNs;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-pushsync
        /// </summary>
        public readonly Outputs.IdentityPoolPushSync? PushSync;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-samlproviderarns
        /// </summary>
        public readonly ImmutableArray<string> SamlProviderARNs;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cognito-identitypool.html#cfn-cognito-identitypool-supportedloginproviders
        /// </summary>
        public readonly Union<System.Text.Json.JsonElement, string>? SupportedLoginProviders;

        [OutputConstructor]
        private IdentityPoolProperties(
            bool? AllowClassicFlow,

            bool AllowUnauthenticatedIdentities,

            Union<System.Text.Json.JsonElement, string>? CognitoEvents,

            ImmutableArray<Outputs.IdentityPoolCognitoIdentityProvider> CognitoIdentityProviders,

            Outputs.IdentityPoolCognitoStreams? CognitoStreams,

            string? DeveloperProviderName,

            string? IdentityPoolName,

            ImmutableArray<string> OpenIdConnectProviderARNs,

            Outputs.IdentityPoolPushSync? PushSync,

            ImmutableArray<string> SamlProviderARNs,

            Union<System.Text.Json.JsonElement, string>? SupportedLoginProviders)
        {
            this.AllowClassicFlow = AllowClassicFlow;
            this.AllowUnauthenticatedIdentities = AllowUnauthenticatedIdentities;
            this.CognitoEvents = CognitoEvents;
            this.CognitoIdentityProviders = CognitoIdentityProviders;
            this.CognitoStreams = CognitoStreams;
            this.DeveloperProviderName = DeveloperProviderName;
            this.IdentityPoolName = IdentityPoolName;
            this.OpenIdConnectProviderARNs = OpenIdConnectProviderARNs;
            this.PushSync = PushSync;
            this.SamlProviderARNs = SamlProviderARNs;
            this.SupportedLoginProviders = SupportedLoginProviders;
        }
    }
}