// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    public static class GetDBParameterGroup
    {
        /// <summary>
        /// The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family
        /// </summary>
        public static Task<GetDBParameterGroupResult> InvokeAsync(GetDBParameterGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDBParameterGroupResult>("aws-native:rds:getDBParameterGroup", args ?? new GetDBParameterGroupArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::RDS::DBParameterGroup resource creates a custom parameter group for an RDS database family
        /// </summary>
        public static Output<GetDBParameterGroupResult> Invoke(GetDBParameterGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDBParameterGroupResult>("aws-native:rds:getDBParameterGroup", args ?? new GetDBParameterGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDBParameterGroupArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies the name of the DB parameter group
        /// </summary>
        [Input("dbParameterGroupName", required: true)]
        public string DbParameterGroupName { get; set; } = null!;

        public GetDBParameterGroupArgs()
        {
        }
        public static new GetDBParameterGroupArgs Empty => new GetDBParameterGroupArgs();
    }

    public sealed class GetDBParameterGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Specifies the name of the DB parameter group
        /// </summary>
        [Input("dbParameterGroupName", required: true)]
        public Input<string> DbParameterGroupName { get; set; } = null!;

        public GetDBParameterGroupInvokeArgs()
        {
        }
        public static new GetDBParameterGroupInvokeArgs Empty => new GetDBParameterGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetDBParameterGroupResult
    {
        /// <summary>
        /// An array of parameter names and values for the parameter update.
        /// </summary>
        public readonly object? Parameters;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.DBParameterGroupTag> Tags;

        [OutputConstructor]
        private GetDBParameterGroupResult(
            object? parameters,

            ImmutableArray<Outputs.DBParameterGroupTag> tags)
        {
            Parameters = parameters;
            Tags = tags;
        }
    }
}
