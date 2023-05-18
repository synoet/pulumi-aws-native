// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeArtifact
{
    public static class GetDomain
    {
        /// <summary>
        /// The resource schema to create a CodeArtifact domain.
        /// </summary>
        public static Task<GetDomainResult> InvokeAsync(GetDomainArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDomainResult>("aws-native:codeartifact:getDomain", args ?? new GetDomainArgs(), options.WithDefaults());

        /// <summary>
        /// The resource schema to create a CodeArtifact domain.
        /// </summary>
        public static Output<GetDomainResult> Invoke(GetDomainInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDomainResult>("aws-native:codeartifact:getDomain", args ?? new GetDomainInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDomainArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the domain.
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetDomainArgs()
        {
        }
        public static new GetDomainArgs Empty => new GetDomainArgs();
    }

    public sealed class GetDomainInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ARN of the domain.
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetDomainInvokeArgs()
        {
        }
        public static new GetDomainInvokeArgs Empty => new GetDomainInvokeArgs();
    }


    [OutputType]
    public sealed class GetDomainResult
    {
        /// <summary>
        /// The ARN of the domain.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The name of the domain. This field is used for GetAtt
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The 12-digit account ID of the AWS account that owns the domain. This field is used for GetAtt
        /// </summary>
        public readonly string? Owner;
        /// <summary>
        /// The access control resource policy on the provided domain.
        /// </summary>
        public readonly object? PermissionsPolicyDocument;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.DomainTag> Tags;

        [OutputConstructor]
        private GetDomainResult(
            string? arn,

            string? name,

            string? owner,

            object? permissionsPolicyDocument,

            ImmutableArray<Outputs.DomainTag> tags)
        {
            Arn = arn;
            Name = name;
            Owner = owner;
            PermissionsPolicyDocument = permissionsPolicyDocument;
            Tags = tags;
        }
    }
}
