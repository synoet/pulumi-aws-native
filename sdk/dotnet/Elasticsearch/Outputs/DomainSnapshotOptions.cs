// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Elasticsearch.Outputs
{

    [OutputType]
    public sealed class DomainSnapshotOptions
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-elasticsearch-domain-snapshotoptions.html#cfn-elasticsearch-domain-snapshotoptions-automatedsnapshotstarthour
        /// </summary>
        public readonly int? AutomatedSnapshotStartHour;

        [OutputConstructor]
        private DomainSnapshotOptions(int? AutomatedSnapshotStartHour)
        {
            this.AutomatedSnapshotStartHour = AutomatedSnapshotStartHour;
        }
    }
}