// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Elasticsearch.Outputs
{

    [OutputType]
    public sealed class DomainMasterUserOptions
    {
        public readonly string? MasterUserArn;
        public readonly string? MasterUserName;
        public readonly string? MasterUserPassword;

        [OutputConstructor]
        private DomainMasterUserOptions(
            string? masterUserArn,

            string? masterUserName,

            string? masterUserPassword)
        {
            MasterUserArn = masterUserArn;
            MasterUserName = masterUserName;
            MasterUserPassword = masterUserPassword;
        }
    }
}
