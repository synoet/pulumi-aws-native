// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect
{
    public static class GetFlowVpcInterface
    {
        /// <summary>
        /// Resource schema for AWS::MediaConnect::FlowVpcInterface
        /// </summary>
        public static Task<GetFlowVpcInterfaceResult> InvokeAsync(GetFlowVpcInterfaceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFlowVpcInterfaceResult>("aws-native:mediaconnect:getFlowVpcInterface", args ?? new GetFlowVpcInterfaceArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::MediaConnect::FlowVpcInterface
        /// </summary>
        public static Output<GetFlowVpcInterfaceResult> Invoke(GetFlowVpcInterfaceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFlowVpcInterfaceResult>("aws-native:mediaconnect:getFlowVpcInterface", args ?? new GetFlowVpcInterfaceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFlowVpcInterfaceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
        /// </summary>
        [Input("flowArn", required: true)]
        public string FlowArn { get; set; } = null!;

        /// <summary>
        /// Immutable and has to be a unique against other VpcInterfaces in this Flow.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        public GetFlowVpcInterfaceArgs()
        {
        }
        public static new GetFlowVpcInterfaceArgs Empty => new GetFlowVpcInterfaceArgs();
    }

    public sealed class GetFlowVpcInterfaceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN), a unique identifier for any AWS resource, of the flow.
        /// </summary>
        [Input("flowArn", required: true)]
        public Input<string> FlowArn { get; set; } = null!;

        /// <summary>
        /// Immutable and has to be a unique against other VpcInterfaces in this Flow.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetFlowVpcInterfaceInvokeArgs()
        {
        }
        public static new GetFlowVpcInterfaceInvokeArgs Empty => new GetFlowVpcInterfaceInvokeArgs();
    }


    [OutputType]
    public sealed class GetFlowVpcInterfaceResult
    {
        /// <summary>
        /// IDs of the network interfaces created in customer's account by MediaConnect.
        /// </summary>
        public readonly ImmutableArray<string> NetworkInterfaceIds;
        /// <summary>
        /// Role Arn MediaConnect can assumes to create ENIs in customer's account.
        /// </summary>
        public readonly string? RoleArn;
        /// <summary>
        /// Security Group IDs to be used on ENI.
        /// </summary>
        public readonly ImmutableArray<string> SecurityGroupIds;
        /// <summary>
        /// Subnet must be in the AZ of the Flow
        /// </summary>
        public readonly string? SubnetId;

        [OutputConstructor]
        private GetFlowVpcInterfaceResult(
            ImmutableArray<string> networkInterfaceIds,

            string? roleArn,

            ImmutableArray<string> securityGroupIds,

            string? subnetId)
        {
            NetworkInterfaceIds = networkInterfaceIds;
            RoleArn = roleArn;
            SecurityGroupIds = securityGroupIds;
            SubnetId = subnetId;
        }
    }
}
