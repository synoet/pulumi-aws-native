// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.GroundStation.Outputs
{

    [OutputType]
    public sealed class DataflowEndpointGroupDataflowEndpoint
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-address
        /// </summary>
        public readonly Outputs.DataflowEndpointGroupSocketAddress? Address;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-mtu
        /// </summary>
        public readonly int? Mtu;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-name
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-dataflowendpointgroup-dataflowendpoint.html#cfn-groundstation-dataflowendpointgroup-dataflowendpoint-status
        /// </summary>
        public readonly string? Status;

        [OutputConstructor]
        private DataflowEndpointGroupDataflowEndpoint(
            Outputs.DataflowEndpointGroupSocketAddress? Address,

            int? Mtu,

            string? Name,

            string? Status)
        {
            this.Address = Address;
            this.Mtu = Mtu;
            this.Name = Name;
            this.Status = Status;
        }
    }
}