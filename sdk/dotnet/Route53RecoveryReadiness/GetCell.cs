// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53RecoveryReadiness
{
    public static class GetCell
    {
        /// <summary>
        /// The API Schema for AWS Route53 Recovery Readiness Cells.
        /// </summary>
        public static Task<GetCellResult> InvokeAsync(GetCellArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCellResult>("aws-native:route53recoveryreadiness:getCell", args ?? new GetCellArgs(), options.WithDefaults());

        /// <summary>
        /// The API Schema for AWS Route53 Recovery Readiness Cells.
        /// </summary>
        public static Output<GetCellResult> Invoke(GetCellInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCellResult>("aws-native:route53recoveryreadiness:getCell", args ?? new GetCellInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCellArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the cell to create.
        /// </summary>
        [Input("cellName", required: true)]
        public string CellName { get; set; } = null!;

        public GetCellArgs()
        {
        }
        public static new GetCellArgs Empty => new GetCellArgs();
    }

    public sealed class GetCellInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the cell to create.
        /// </summary>
        [Input("cellName", required: true)]
        public Input<string> CellName { get; set; } = null!;

        public GetCellInvokeArgs()
        {
        }
        public static new GetCellInvokeArgs Empty => new GetCellInvokeArgs();
    }


    [OutputType]
    public sealed class GetCellResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the cell.
        /// </summary>
        public readonly string? CellArn;
        /// <summary>
        /// A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific Regions.
        /// </summary>
        public readonly ImmutableArray<string> Cells;
        /// <summary>
        /// The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element.
        /// </summary>
        public readonly ImmutableArray<string> ParentReadinessScopes;
        /// <summary>
        /// A collection of tags associated with a resource
        /// </summary>
        public readonly ImmutableArray<Outputs.CellTag> Tags;

        [OutputConstructor]
        private GetCellResult(
            string? cellArn,

            ImmutableArray<string> cells,

            ImmutableArray<string> parentReadinessScopes,

            ImmutableArray<Outputs.CellTag> tags)
        {
            CellArn = cellArn;
            Cells = cells;
            ParentReadinessScopes = parentReadinessScopes;
            Tags = tags;
        }
    }
}
