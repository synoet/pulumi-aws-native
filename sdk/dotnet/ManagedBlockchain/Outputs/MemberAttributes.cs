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
    public sealed class MemberAttributes
    {
        public readonly string MemberId;
        public readonly string NetworkId;

        [OutputConstructor]
        private MemberAttributes(
            string MemberId,

            string NetworkId)
        {
            this.MemberId = MemberId;
            this.NetworkId = NetworkId;
        }
    }
}