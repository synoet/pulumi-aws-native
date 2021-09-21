// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Batch.Outputs
{

    [OutputType]
    public sealed class JobDefinitionUlimit
    {
        public readonly int HardLimit;
        public readonly string Name;
        public readonly int SoftLimit;

        [OutputConstructor]
        private JobDefinitionUlimit(
            int hardLimit,

            string name,

            int softLimit)
        {
            HardLimit = hardLimit;
            Name = name;
            SoftLimit = softLimit;
        }
    }
}
