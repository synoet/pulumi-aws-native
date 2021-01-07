// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ManagedBlockchain.Outputs
{

    [OutputType]
    public sealed class NodeAttributes
    {
        public readonly string Arn;
        public readonly string MemberId;
        public readonly string NetworkId;
        public readonly string NodeId;

        [OutputConstructor]
        private NodeAttributes(
            string Arn,

            string MemberId,

            string NetworkId,

            string NodeId)
        {
            this.Arn = Arn;
            this.MemberId = MemberId;
            this.NetworkId = NetworkId;
            this.NodeId = NodeId;
        }
    }
}