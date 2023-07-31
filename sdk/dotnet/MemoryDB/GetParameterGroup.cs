// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MemoryDB
{
    public static class GetParameterGroup
    {
        /// <summary>
        /// The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.
        /// </summary>
        public static Task<GetParameterGroupResult> InvokeAsync(GetParameterGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetParameterGroupResult>("aws-native:memorydb:getParameterGroup", args ?? new GetParameterGroupArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::MemoryDB::ParameterGroup resource creates an Amazon MemoryDB ParameterGroup.
        /// </summary>
        public static Output<GetParameterGroupResult> Invoke(GetParameterGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetParameterGroupResult>("aws-native:memorydb:getParameterGroup", args ?? new GetParameterGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetParameterGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the parameter group.
        /// </summary>
        [Input("parameterGroupName", required: true)]
        public string ParameterGroupName { get; set; } = null!;

        public GetParameterGroupArgs()
        {
        }
        public static new GetParameterGroupArgs Empty => new GetParameterGroupArgs();
    }

    public sealed class GetParameterGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the parameter group.
        /// </summary>
        [Input("parameterGroupName", required: true)]
        public Input<string> ParameterGroupName { get; set; } = null!;

        public GetParameterGroupInvokeArgs()
        {
        }
        public static new GetParameterGroupInvokeArgs Empty => new GetParameterGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetParameterGroupResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the parameter group.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// An array of key-value pairs to apply to this parameter group.
        /// </summary>
        public readonly ImmutableArray<Outputs.ParameterGroupTag> Tags;

        [OutputConstructor]
        private GetParameterGroupResult(
            string? arn,

            ImmutableArray<Outputs.ParameterGroupTag> tags)
        {
            Arn = arn;
            Tags = tags;
        }
    }
}
