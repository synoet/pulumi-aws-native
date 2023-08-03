// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Neptune
{
    public static class GetDbSubnetGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::Neptune::DBSubnetGroup
        /// </summary>
        public static Task<GetDbSubnetGroupResult> InvokeAsync(GetDbSubnetGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDbSubnetGroupResult>("aws-native:neptune:getDbSubnetGroup", args ?? new GetDbSubnetGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Neptune::DBSubnetGroup
        /// </summary>
        public static Output<GetDbSubnetGroupResult> Invoke(GetDbSubnetGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDbSubnetGroupResult>("aws-native:neptune:getDbSubnetGroup", args ?? new GetDbSubnetGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDbSubnetGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDbSubnetGroupArgs()
        {
        }
        public static new GetDbSubnetGroupArgs Empty => new GetDbSubnetGroupArgs();
    }

    public sealed class GetDbSubnetGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDbSubnetGroupInvokeArgs()
        {
        }
        public static new GetDbSubnetGroupInvokeArgs Empty => new GetDbSubnetGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetDbSubnetGroupResult
    {
        public readonly string? DbSubnetGroupDescription;
        public readonly string? Id;
        public readonly ImmutableArray<string> SubnetIds;
        public readonly ImmutableArray<Outputs.DbSubnetGroupTag> Tags;

        [OutputConstructor]
        private GetDbSubnetGroupResult(
            string? dbSubnetGroupDescription,

            string? id,

            ImmutableArray<string> subnetIds,

            ImmutableArray<Outputs.DbSubnetGroupTag> tags)
        {
            DbSubnetGroupDescription = dbSubnetGroupDescription;
            Id = id;
            SubnetIds = subnetIds;
            Tags = tags;
        }
    }
}
