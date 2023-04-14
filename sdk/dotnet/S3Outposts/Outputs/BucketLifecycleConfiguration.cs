// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3Outposts.Outputs
{

    [OutputType]
    public sealed class BucketLifecycleConfiguration
    {
        /// <summary>
        /// A list of lifecycle rules for individual objects in an Amazon S3Outposts bucket.
        /// </summary>
        public readonly ImmutableArray<Outputs.BucketRule> Rules;

        [OutputConstructor]
        private BucketLifecycleConfiguration(ImmutableArray<Outputs.BucketRule> rules)
        {
            Rules = rules;
        }
    }
}
