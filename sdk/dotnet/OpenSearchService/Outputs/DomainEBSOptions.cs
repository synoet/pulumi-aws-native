// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchService.Outputs
{

    [OutputType]
    public sealed class DomainEBSOptions
    {
        public readonly bool? EbsEnabled;
        public readonly int? Iops;
        public readonly int? Throughput;
        public readonly int? VolumeSize;
        public readonly string? VolumeType;

        [OutputConstructor]
        private DomainEBSOptions(
            bool? ebsEnabled,

            int? iops,

            int? throughput,

            int? volumeSize,

            string? volumeType)
        {
            EbsEnabled = ebsEnabled;
            Iops = iops;
            Throughput = throughput;
            VolumeSize = volumeSize;
            VolumeType = volumeType;
        }
    }
}
