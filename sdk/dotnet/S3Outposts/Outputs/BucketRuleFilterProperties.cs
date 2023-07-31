// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3Outposts.Outputs
{

    /// <summary>
    /// The container for the filter of the lifecycle rule.
    /// </summary>
    [OutputType]
    public sealed class BucketRuleFilterProperties
    {
        /// <summary>
        /// The container for the AND condition for the lifecycle rule. A combination of Prefix and 1 or more Tags OR a minimum of 2 or more tags.
        /// </summary>
        public readonly Outputs.FilterAndOperatorProperties? AndOperator;
        /// <summary>
        /// Object key prefix that identifies one or more objects to which this rule applies.
        /// </summary>
        public readonly string? Prefix;
        /// <summary>
        /// Specifies a tag used to identify a subset of objects for an Amazon S3Outposts bucket.
        /// </summary>
        public readonly Outputs.BucketFilterTag? Tag;

        [OutputConstructor]
        private BucketRuleFilterProperties(
            Outputs.FilterAndOperatorProperties? andOperator,

            string? prefix,

            Outputs.BucketFilterTag? tag)
        {
            AndOperator = andOperator;
            Prefix = prefix;
            Tag = tag;
        }
    }
}
