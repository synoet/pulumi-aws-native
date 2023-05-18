// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DynamoDB.Inputs
{

    public sealed class GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("contributorInsightsSpecification")]
        public Input<Inputs.GlobalTableContributorInsightsSpecificationArgs>? ContributorInsightsSpecification { get; set; }

        [Input("indexName", required: true)]
        public Input<string> IndexName { get; set; } = null!;

        [Input("readProvisionedThroughputSettings")]
        public Input<Inputs.GlobalTableReadProvisionedThroughputSettingsArgs>? ReadProvisionedThroughputSettings { get; set; }

        public GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs()
        {
        }
        public static new GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs Empty => new GlobalTableReplicaGlobalSecondaryIndexSpecificationArgs();
    }
}
