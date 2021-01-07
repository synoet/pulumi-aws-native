// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Cassandra.Outputs
{

    [OutputType]
    public sealed class TableProperties
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-billingmode
        /// </summary>
        public readonly Outputs.TableBillingMode? BillingMode;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-clusteringkeycolumns
        /// </summary>
        public readonly ImmutableArray<Outputs.TableClusteringKeyColumn> ClusteringKeyColumns;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-keyspacename
        /// </summary>
        public readonly string KeyspaceName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-partitionkeycolumns
        /// </summary>
        public readonly ImmutableArray<Outputs.TableColumn> PartitionKeyColumns;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-regularcolumns
        /// </summary>
        public readonly ImmutableArray<Outputs.TableColumn> RegularColumns;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-cassandra-table.html#cfn-cassandra-table-tablename
        /// </summary>
        public readonly string? TableName;

        [OutputConstructor]
        private TableProperties(
            Outputs.TableBillingMode? BillingMode,

            ImmutableArray<Outputs.TableClusteringKeyColumn> ClusteringKeyColumns,

            string KeyspaceName,

            ImmutableArray<Outputs.TableColumn> PartitionKeyColumns,

            ImmutableArray<Outputs.TableColumn> RegularColumns,

            string? TableName)
        {
            this.BillingMode = BillingMode;
            this.ClusteringKeyColumns = ClusteringKeyColumns;
            this.KeyspaceName = KeyspaceName;
            this.PartitionKeyColumns = PartitionKeyColumns;
            this.RegularColumns = RegularColumns;
            this.TableName = TableName;
        }
    }
}