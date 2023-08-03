// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds
{
    public static class GetDbSecurityGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::RDS::DBSecurityGroup
        /// </summary>
        public static Task<GetDbSecurityGroupResult> InvokeAsync(GetDbSecurityGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDbSecurityGroupResult>("aws-native:rds:getDbSecurityGroup", args ?? new GetDbSecurityGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::RDS::DBSecurityGroup
        /// </summary>
        public static Output<GetDbSecurityGroupResult> Invoke(GetDbSecurityGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDbSecurityGroupResult>("aws-native:rds:getDbSecurityGroup", args ?? new GetDbSecurityGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDbSecurityGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDbSecurityGroupArgs()
        {
        }
        public static new GetDbSecurityGroupArgs Empty => new GetDbSecurityGroupArgs();
    }

    public sealed class GetDbSecurityGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDbSecurityGroupInvokeArgs()
        {
        }
        public static new GetDbSecurityGroupInvokeArgs Empty => new GetDbSecurityGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetDbSecurityGroupResult
    {
        public readonly ImmutableArray<Outputs.DbSecurityGroupIngress> DbSecurityGroupIngress;
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.DbSecurityGroupTag> Tags;

        [OutputConstructor]
        private GetDbSecurityGroupResult(
            ImmutableArray<Outputs.DbSecurityGroupIngress> dbSecurityGroupIngress,

            string? id,

            ImmutableArray<Outputs.DbSecurityGroupTag> tags)
        {
            DbSecurityGroupIngress = dbSecurityGroupIngress;
            Id = id;
            Tags = tags;
        }
    }
}
