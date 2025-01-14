// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetBillingGroup
    {
        /// <summary>
        /// Resource Type definition for AWS::IoT::BillingGroup
        /// </summary>
        public static Task<GetBillingGroupResult> InvokeAsync(GetBillingGroupArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetBillingGroupResult>("aws-native:iot:getBillingGroup", args ?? new GetBillingGroupArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoT::BillingGroup
        /// </summary>
        public static Output<GetBillingGroupResult> Invoke(GetBillingGroupInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetBillingGroupResult>("aws-native:iot:getBillingGroup", args ?? new GetBillingGroupInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetBillingGroupArgs : global::Pulumi.InvokeArgs
    {
        [Input("billingGroupName", required: true)]
        public string BillingGroupName { get; set; } = null!;

        public GetBillingGroupArgs()
        {
        }
        public static new GetBillingGroupArgs Empty => new GetBillingGroupArgs();
    }

    public sealed class GetBillingGroupInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("billingGroupName", required: true)]
        public Input<string> BillingGroupName { get; set; } = null!;

        public GetBillingGroupInvokeArgs()
        {
        }
        public static new GetBillingGroupInvokeArgs Empty => new GetBillingGroupInvokeArgs();
    }


    [OutputType]
    public sealed class GetBillingGroupResult
    {
        public readonly string? Arn;
        public readonly Outputs.BillingGroupPropertiesProperties? BillingGroupProperties;
        public readonly string? Id;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.BillingGroupTag> Tags;

        [OutputConstructor]
        private GetBillingGroupResult(
            string? arn,

            Outputs.BillingGroupPropertiesProperties? billingGroupProperties,

            string? id,

            ImmutableArray<Outputs.BillingGroupTag> tags)
        {
            Arn = arn;
            BillingGroupProperties = billingGroupProperties;
            Id = id;
            Tags = tags;
        }
    }
}
