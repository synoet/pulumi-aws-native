// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CloudFront.Outputs
{

    [OutputType]
    public sealed class DistributionDistributionConfig
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-aliases
        /// </summary>
        public readonly ImmutableArray<string> Aliases;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-cachebehaviors
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionCacheBehavior> CacheBehaviors;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-comment
        /// </summary>
        public readonly string? Comment;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-customerrorresponses
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionCustomErrorResponse> CustomErrorResponses;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultcachebehavior
        /// </summary>
        public readonly Outputs.DistributionDefaultCacheBehavior? DefaultCacheBehavior;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-defaultrootobject
        /// </summary>
        public readonly string? DefaultRootObject;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-enabled
        /// </summary>
        public readonly bool Enabled;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-httpversion
        /// </summary>
        public readonly string? HttpVersion;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-ipv6enabled
        /// </summary>
        public readonly bool? IPV6Enabled;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-logging
        /// </summary>
        public readonly Outputs.DistributionLogging? Logging;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origingroups
        /// </summary>
        public readonly Outputs.DistributionOriginGroups? OriginGroups;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-origins
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionOrigin> Origins;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-priceclass
        /// </summary>
        public readonly string? PriceClass;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-restrictions
        /// </summary>
        public readonly Outputs.DistributionRestrictions? Restrictions;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-viewercertificate
        /// </summary>
        public readonly Outputs.DistributionViewerCertificate? ViewerCertificate;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-distributionconfig.html#cfn-cloudfront-distribution-distributionconfig-webaclid
        /// </summary>
        public readonly string? WebACLId;

        [OutputConstructor]
        private DistributionDistributionConfig(
            ImmutableArray<string> Aliases,

            ImmutableArray<Outputs.DistributionCacheBehavior> CacheBehaviors,

            string? Comment,

            ImmutableArray<Outputs.DistributionCustomErrorResponse> CustomErrorResponses,

            Outputs.DistributionDefaultCacheBehavior? DefaultCacheBehavior,

            string? DefaultRootObject,

            bool Enabled,

            string? HttpVersion,

            bool? IPV6Enabled,

            Outputs.DistributionLogging? Logging,

            Outputs.DistributionOriginGroups? OriginGroups,

            ImmutableArray<Outputs.DistributionOrigin> Origins,

            string? PriceClass,

            Outputs.DistributionRestrictions? Restrictions,

            Outputs.DistributionViewerCertificate? ViewerCertificate,

            string? WebACLId)
        {
            this.Aliases = Aliases;
            this.CacheBehaviors = CacheBehaviors;
            this.Comment = Comment;
            this.CustomErrorResponses = CustomErrorResponses;
            this.DefaultCacheBehavior = DefaultCacheBehavior;
            this.DefaultRootObject = DefaultRootObject;
            this.Enabled = Enabled;
            this.HttpVersion = HttpVersion;
            this.IPV6Enabled = IPV6Enabled;
            this.Logging = Logging;
            this.OriginGroups = OriginGroups;
            this.Origins = Origins;
            this.PriceClass = PriceClass;
            this.Restrictions = Restrictions;
            this.ViewerCertificate = ViewerCertificate;
            this.WebACLId = WebACLId;
        }
    }
}