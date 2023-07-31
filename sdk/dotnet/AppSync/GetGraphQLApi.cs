// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppSync
{
    public static class GetGraphQLApi
    {
        /// <summary>
        /// Resource Type definition for AWS::AppSync::GraphQLApi
        /// </summary>
        public static Task<GetGraphQLApiResult> InvokeAsync(GetGraphQLApiArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetGraphQLApiResult>("aws-native:appsync:getGraphQLApi", args ?? new GetGraphQLApiArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppSync::GraphQLApi
        /// </summary>
        public static Output<GetGraphQLApiResult> Invoke(GetGraphQLApiInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetGraphQLApiResult>("aws-native:appsync:getGraphQLApi", args ?? new GetGraphQLApiInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetGraphQLApiArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetGraphQLApiArgs()
        {
        }
        public static new GetGraphQLApiArgs Empty => new GetGraphQLApiArgs();
    }

    public sealed class GetGraphQLApiInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetGraphQLApiInvokeArgs()
        {
        }
        public static new GetGraphQLApiInvokeArgs Empty => new GetGraphQLApiInvokeArgs();
    }


    [OutputType]
    public sealed class GetGraphQLApiResult
    {
        public readonly ImmutableArray<Outputs.GraphQLApiAdditionalAuthenticationProvider> AdditionalAuthenticationProviders;
        public readonly string? ApiId;
        public readonly string? Arn;
        public readonly string? AuthenticationType;
        public readonly string? GraphQlDns;
        public readonly string? GraphQlUrl;
        public readonly string? Id;
        public readonly Outputs.GraphQLApiLambdaAuthorizerConfig? LambdaAuthorizerConfig;
        public readonly Outputs.GraphQLApiLogConfig? LogConfig;
        public readonly string? MergedApiExecutionRoleArn;
        public readonly string? Name;
        public readonly Outputs.GraphQLApiOpenIDConnectConfig? OpenIdConnectConfig;
        public readonly string? OwnerContact;
        public readonly string? RealtimeDns;
        public readonly string? RealtimeUrl;
        public readonly ImmutableArray<Outputs.GraphQLApiTag> Tags;
        public readonly Outputs.GraphQLApiUserPoolConfig? UserPoolConfig;
        public readonly bool? XrayEnabled;

        [OutputConstructor]
        private GetGraphQLApiResult(
            ImmutableArray<Outputs.GraphQLApiAdditionalAuthenticationProvider> additionalAuthenticationProviders,

            string? apiId,

            string? arn,

            string? authenticationType,

            string? graphQlDns,

            string? graphQlUrl,

            string? id,

            Outputs.GraphQLApiLambdaAuthorizerConfig? lambdaAuthorizerConfig,

            Outputs.GraphQLApiLogConfig? logConfig,

            string? mergedApiExecutionRoleArn,

            string? name,

            Outputs.GraphQLApiOpenIDConnectConfig? openIdConnectConfig,

            string? ownerContact,

            string? realtimeDns,

            string? realtimeUrl,

            ImmutableArray<Outputs.GraphQLApiTag> tags,

            Outputs.GraphQLApiUserPoolConfig? userPoolConfig,

            bool? xrayEnabled)
        {
            AdditionalAuthenticationProviders = additionalAuthenticationProviders;
            ApiId = apiId;
            Arn = arn;
            AuthenticationType = authenticationType;
            GraphQlDns = graphQlDns;
            GraphQlUrl = graphQlUrl;
            Id = id;
            LambdaAuthorizerConfig = lambdaAuthorizerConfig;
            LogConfig = logConfig;
            MergedApiExecutionRoleArn = mergedApiExecutionRoleArn;
            Name = name;
            OpenIdConnectConfig = openIdConnectConfig;
            OwnerContact = ownerContact;
            RealtimeDns = realtimeDns;
            RealtimeUrl = realtimeUrl;
            Tags = tags;
            UserPoolConfig = userPoolConfig;
            XrayEnabled = xrayEnabled;
        }
    }
}
