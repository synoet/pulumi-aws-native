// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ElastiCache.Outputs
{

    [OutputType]
    public sealed class UserGroupReplicationGroupIdList
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticache-usergroup-replicationgroupidlist.html#cfn-elasticache-usergroup-replicationgroupidlist-replicationgroupidlist
        /// </summary>
        public readonly ImmutableArray<string> ReplicationGroupIdList;

        [OutputConstructor]
        private UserGroupReplicationGroupIdList(ImmutableArray<string> ReplicationGroupIdList)
        {
            this.ReplicationGroupIdList = ReplicationGroupIdList;
        }
    }
}