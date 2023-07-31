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
    public sealed class FilterAndOperatorProperties
    {
        /// <summary>
        /// Prefix identifies one or more objects to which the rule applies.
        /// </summary>
        public readonly string? Prefix;
        /// <summary>
        /// All of these tags must exist in the object's tag set in order for the rule to apply.
        /// </summary>
        public readonly ImmutableArray<Outputs.BucketFilterTag> Tags;

        [OutputConstructor]
        private FilterAndOperatorProperties(
            string? prefix,

            ImmutableArray<Outputs.BucketFilterTag> tags)
        {
            Prefix = prefix;
            Tags = tags;
        }
    }
}
