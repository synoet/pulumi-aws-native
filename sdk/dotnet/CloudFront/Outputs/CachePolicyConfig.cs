// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Outputs
{

    [OutputType]
    public sealed class CachePolicyConfig
    {
        public readonly string? Comment;
        public readonly double DefaultTtl;
        public readonly double MaxTtl;
        public readonly double MinTtl;
        public readonly string Name;
        public readonly Outputs.CachePolicyParametersInCacheKeyAndForwardedToOrigin ParametersInCacheKeyAndForwardedToOrigin;

        [OutputConstructor]
        private CachePolicyConfig(
            string? comment,

            double defaultTtl,

            double maxTtl,

            double minTtl,

            string name,

            Outputs.CachePolicyParametersInCacheKeyAndForwardedToOrigin parametersInCacheKeyAndForwardedToOrigin)
        {
            Comment = comment;
            DefaultTtl = defaultTtl;
            MaxTtl = maxTtl;
            MinTtl = minTtl;
            Name = name;
            ParametersInCacheKeyAndForwardedToOrigin = parametersInCacheKeyAndForwardedToOrigin;
        }
    }
}
