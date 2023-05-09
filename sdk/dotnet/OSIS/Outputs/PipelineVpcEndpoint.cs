// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OSIS.Outputs
{

    /// <summary>
    /// An OpenSearch Ingestion Service-managed VPC endpoint that will access one or more pipelines.
    /// </summary>
    [OutputType]
    public sealed class PipelineVpcEndpoint
    {
        /// <summary>
        /// The unique identifier of the endpoint.
        /// </summary>
        public readonly string? VpcEndpointId;
        /// <summary>
        /// The ID for your VPC. AWS Privatelink generates this value when you create a VPC.
        /// </summary>
        public readonly string? VpcId;
        public readonly Outputs.PipelineVpcOptions? VpcOptions;

        [OutputConstructor]
        private PipelineVpcEndpoint(
            string? vpcEndpointId,

            string? vpcId,

            Outputs.PipelineVpcOptions? vpcOptions)
        {
            VpcEndpointId = vpcEndpointId;
            VpcId = vpcId;
            VpcOptions = vpcOptions;
        }
    }
}
