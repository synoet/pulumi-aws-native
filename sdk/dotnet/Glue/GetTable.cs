// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    public static class GetTable
    {
        /// <summary>
        /// Resource Type definition for AWS::Glue::Table
        /// </summary>
        public static Task<GetTableResult> InvokeAsync(GetTableArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTableResult>("aws-native:glue:getTable", args ?? new GetTableArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Glue::Table
        /// </summary>
        public static Output<GetTableResult> Invoke(GetTableInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTableResult>("aws-native:glue:getTable", args ?? new GetTableInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTableArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetTableArgs()
        {
        }
        public static new GetTableArgs Empty => new GetTableArgs();
    }

    public sealed class GetTableInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetTableInvokeArgs()
        {
        }
        public static new GetTableInvokeArgs Empty => new GetTableInvokeArgs();
    }


    [OutputType]
    public sealed class GetTableResult
    {
        public readonly string? Id;
        public readonly Outputs.TableOpenTableFormatInput? OpenTableFormatInput;
        public readonly Outputs.TableInput? TableInput;

        [OutputConstructor]
        private GetTableResult(
            string? id,

            Outputs.TableOpenTableFormatInput? openTableFormatInput,

            Outputs.TableInput? tableInput)
        {
            Id = id;
            OpenTableFormatInput = openTableFormatInput;
            TableInput = tableInput;
        }
    }
}
