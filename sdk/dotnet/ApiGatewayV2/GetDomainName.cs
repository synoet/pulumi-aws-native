// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGatewayV2
{
    public static class GetDomainName
    {
        /// <summary>
        /// The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway). 
        ///  You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *API Gateway Developer Guide*.
        /// </summary>
        public static Task<GetDomainNameResult> InvokeAsync(GetDomainNameArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDomainNameResult>("aws-native:apigatewayv2:getDomainName", args ?? new GetDomainNameArgs(), options.WithDefaults());

        /// <summary>
        /// The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway). 
        ///  You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see [Set up Custom Domain Name for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *API Gateway Developer Guide*.
        /// </summary>
        public static Output<GetDomainNameResult> Invoke(GetDomainNameInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDomainNameResult>("aws-native:apigatewayv2:getDomainName", args ?? new GetDomainNameInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDomainNameArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        /// </summary>
        [Input("domainName", required: true)]
        public string DomainNameValue { get; set; } = null!;

        public GetDomainNameArgs()
        {
        }
        public static new GetDomainNameArgs Empty => new GetDomainNameArgs();
    }

    public sealed class GetDomainNameInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        /// </summary>
        [Input("domainName", required: true)]
        public Input<string> DomainName { get; set; } = null!;

        public GetDomainNameInvokeArgs()
        {
        }
        public static new GetDomainNameInvokeArgs Empty => new GetDomainNameInvokeArgs();
    }


    [OutputType]
    public sealed class GetDomainNameResult
    {
        /// <summary>
        /// The domain name configurations.
        /// </summary>
        public readonly ImmutableArray<Outputs.DomainNameConfiguration> DomainNameConfigurations;
        /// <summary>
        /// The mutual TLS authentication configuration for a custom domain name.
        /// </summary>
        public readonly Outputs.DomainNameMutualTlsAuthentication? MutualTlsAuthentication;
        public readonly string? RegionalDomainName;
        public readonly string? RegionalHostedZoneId;
        /// <summary>
        /// The collection of tags associated with a domain name.
        /// </summary>
        public readonly object? Tags;

        [OutputConstructor]
        private GetDomainNameResult(
            ImmutableArray<Outputs.DomainNameConfiguration> domainNameConfigurations,

            Outputs.DomainNameMutualTlsAuthentication? mutualTlsAuthentication,

            string? regionalDomainName,

            string? regionalHostedZoneId,

            object? tags)
        {
            DomainNameConfigurations = domainNameConfigurations;
            MutualTlsAuthentication = mutualTlsAuthentication;
            RegionalDomainName = regionalDomainName;
            RegionalHostedZoneId = regionalHostedZoneId;
            Tags = tags;
        }
    }
}
