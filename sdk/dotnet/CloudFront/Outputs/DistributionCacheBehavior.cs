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
    public sealed class DistributionCacheBehavior
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-allowedmethods
        /// </summary>
        public readonly ImmutableArray<string> AllowedMethods;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachepolicyid
        /// </summary>
        public readonly string? CachePolicyId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-cachedmethods
        /// </summary>
        public readonly ImmutableArray<string> CachedMethods;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-compress
        /// </summary>
        public readonly bool? Compress;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-defaultttl
        /// </summary>
        public readonly double? DefaultTTL;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-fieldlevelencryptionid
        /// </summary>
        public readonly string? FieldLevelEncryptionId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-forwardedvalues
        /// </summary>
        public readonly Outputs.DistributionForwardedValues? ForwardedValues;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-lambdafunctionassociations
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionLambdaFunctionAssociation> LambdaFunctionAssociations;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-maxttl
        /// </summary>
        public readonly double? MaxTTL;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-minttl
        /// </summary>
        public readonly double? MinTTL;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-originrequestpolicyid
        /// </summary>
        public readonly string? OriginRequestPolicyId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-pathpattern
        /// </summary>
        public readonly string PathPattern;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-realtimelogconfigarn
        /// </summary>
        public readonly string? RealtimeLogConfigArn;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-smoothstreaming
        /// </summary>
        public readonly bool? SmoothStreaming;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-targetoriginid
        /// </summary>
        public readonly string TargetOriginId;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedkeygroups
        /// </summary>
        public readonly ImmutableArray<string> TrustedKeyGroups;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-trustedsigners
        /// </summary>
        public readonly ImmutableArray<string> TrustedSigners;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-cloudfront-distribution-cachebehavior.html#cfn-cloudfront-distribution-cachebehavior-viewerprotocolpolicy
        /// </summary>
        public readonly string ViewerProtocolPolicy;

        [OutputConstructor]
        private DistributionCacheBehavior(
            ImmutableArray<string> AllowedMethods,

            string? CachePolicyId,

            ImmutableArray<string> CachedMethods,

            bool? Compress,

            double? DefaultTTL,

            string? FieldLevelEncryptionId,

            Outputs.DistributionForwardedValues? ForwardedValues,

            ImmutableArray<Outputs.DistributionLambdaFunctionAssociation> LambdaFunctionAssociations,

            double? MaxTTL,

            double? MinTTL,

            string? OriginRequestPolicyId,

            string PathPattern,

            string? RealtimeLogConfigArn,

            bool? SmoothStreaming,

            string TargetOriginId,

            ImmutableArray<string> TrustedKeyGroups,

            ImmutableArray<string> TrustedSigners,

            string ViewerProtocolPolicy)
        {
            this.AllowedMethods = AllowedMethods;
            this.CachePolicyId = CachePolicyId;
            this.CachedMethods = CachedMethods;
            this.Compress = Compress;
            this.DefaultTTL = DefaultTTL;
            this.FieldLevelEncryptionId = FieldLevelEncryptionId;
            this.ForwardedValues = ForwardedValues;
            this.LambdaFunctionAssociations = LambdaFunctionAssociations;
            this.MaxTTL = MaxTTL;
            this.MinTTL = MinTTL;
            this.OriginRequestPolicyId = OriginRequestPolicyId;
            this.PathPattern = PathPattern;
            this.RealtimeLogConfigArn = RealtimeLogConfigArn;
            this.SmoothStreaming = SmoothStreaming;
            this.TargetOriginId = TargetOriginId;
            this.TrustedKeyGroups = TrustedKeyGroups;
            this.TrustedSigners = TrustedSigners;
            this.ViewerProtocolPolicy = ViewerProtocolPolicy;
        }
    }
}