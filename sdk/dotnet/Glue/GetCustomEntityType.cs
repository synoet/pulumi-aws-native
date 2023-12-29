// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    public static class GetCustomEntityType
    {
        /// <summary>
        /// Resource Type definition for AWS::Glue::CustomEntityType
        /// </summary>
        public static Task<GetCustomEntityTypeResult> InvokeAsync(GetCustomEntityTypeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCustomEntityTypeResult>("aws-native:glue:getCustomEntityType", args ?? new GetCustomEntityTypeArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Glue::CustomEntityType
        /// </summary>
        public static Output<GetCustomEntityTypeResult> Invoke(GetCustomEntityTypeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCustomEntityTypeResult>("aws-native:glue:getCustomEntityType", args ?? new GetCustomEntityTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCustomEntityTypeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetCustomEntityTypeArgs()
        {
        }
        public static new GetCustomEntityTypeArgs Empty => new GetCustomEntityTypeArgs();
    }

    public sealed class GetCustomEntityTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetCustomEntityTypeInvokeArgs()
        {
        }
        public static new GetCustomEntityTypeInvokeArgs Empty => new GetCustomEntityTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetCustomEntityTypeResult
    {
        public readonly ImmutableArray<string> ContextWords;
        public readonly string? Id;
        public readonly string? Name;
        public readonly string? RegexString;
        public readonly object? Tags;

        [OutputConstructor]
        private GetCustomEntityTypeResult(
            ImmutableArray<string> contextWords,

            string? id,

            string? name,

            string? regexString,

            object? tags)
        {
            ContextWords = contextWords;
            Id = id;
            Name = name;
            RegexString = regexString;
            Tags = tags;
        }
    }
}
