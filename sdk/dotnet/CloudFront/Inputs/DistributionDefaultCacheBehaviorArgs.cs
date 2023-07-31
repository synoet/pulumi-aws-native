// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class DistributionDefaultCacheBehaviorArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedMethods")]
        private InputList<string>? _allowedMethods;
        public InputList<string> AllowedMethods
        {
            get => _allowedMethods ?? (_allowedMethods = new InputList<string>());
            set => _allowedMethods = value;
        }

        [Input("cachePolicyId")]
        public Input<string>? CachePolicyId { get; set; }

        [Input("cachedMethods")]
        private InputList<string>? _cachedMethods;
        public InputList<string> CachedMethods
        {
            get => _cachedMethods ?? (_cachedMethods = new InputList<string>());
            set => _cachedMethods = value;
        }

        [Input("compress")]
        public Input<bool>? Compress { get; set; }

        [Input("defaultTtl")]
        public Input<double>? DefaultTtl { get; set; }

        [Input("fieldLevelEncryptionId")]
        public Input<string>? FieldLevelEncryptionId { get; set; }

        [Input("forwardedValues")]
        public Input<Inputs.DistributionForwardedValuesArgs>? ForwardedValues { get; set; }

        [Input("functionAssociations")]
        private InputList<Inputs.DistributionFunctionAssociationArgs>? _functionAssociations;
        public InputList<Inputs.DistributionFunctionAssociationArgs> FunctionAssociations
        {
            get => _functionAssociations ?? (_functionAssociations = new InputList<Inputs.DistributionFunctionAssociationArgs>());
            set => _functionAssociations = value;
        }

        [Input("lambdaFunctionAssociations")]
        private InputList<Inputs.DistributionLambdaFunctionAssociationArgs>? _lambdaFunctionAssociations;
        public InputList<Inputs.DistributionLambdaFunctionAssociationArgs> LambdaFunctionAssociations
        {
            get => _lambdaFunctionAssociations ?? (_lambdaFunctionAssociations = new InputList<Inputs.DistributionLambdaFunctionAssociationArgs>());
            set => _lambdaFunctionAssociations = value;
        }

        [Input("maxTtl")]
        public Input<double>? MaxTtl { get; set; }

        [Input("minTtl")]
        public Input<double>? MinTtl { get; set; }

        [Input("originRequestPolicyId")]
        public Input<string>? OriginRequestPolicyId { get; set; }

        [Input("realtimeLogConfigArn")]
        public Input<string>? RealtimeLogConfigArn { get; set; }

        [Input("responseHeadersPolicyId")]
        public Input<string>? ResponseHeadersPolicyId { get; set; }

        [Input("smoothStreaming")]
        public Input<bool>? SmoothStreaming { get; set; }

        [Input("targetOriginId", required: true)]
        public Input<string> TargetOriginId { get; set; } = null!;

        [Input("trustedKeyGroups")]
        private InputList<string>? _trustedKeyGroups;
        public InputList<string> TrustedKeyGroups
        {
            get => _trustedKeyGroups ?? (_trustedKeyGroups = new InputList<string>());
            set => _trustedKeyGroups = value;
        }

        [Input("trustedSigners")]
        private InputList<string>? _trustedSigners;
        public InputList<string> TrustedSigners
        {
            get => _trustedSigners ?? (_trustedSigners = new InputList<string>());
            set => _trustedSigners = value;
        }

        [Input("viewerProtocolPolicy", required: true)]
        public Input<string> ViewerProtocolPolicy { get; set; } = null!;

        public DistributionDefaultCacheBehaviorArgs()
        {
        }
        public static new DistributionDefaultCacheBehaviorArgs Empty => new DistributionDefaultCacheBehaviorArgs();
    }
}
