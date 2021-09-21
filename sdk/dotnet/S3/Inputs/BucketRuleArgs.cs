// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    public sealed class BucketRuleArgs : Pulumi.ResourceArgs
    {
        [Input("abortIncompleteMultipartUpload")]
        public Input<Inputs.BucketAbortIncompleteMultipartUploadArgs>? AbortIncompleteMultipartUpload { get; set; }

        [Input("expirationDate")]
        public Input<string>? ExpirationDate { get; set; }

        [Input("expirationInDays")]
        public Input<int>? ExpirationInDays { get; set; }

        [Input("expiredObjectDeleteMarker")]
        public Input<bool>? ExpiredObjectDeleteMarker { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("noncurrentVersionExpirationInDays")]
        public Input<int>? NoncurrentVersionExpirationInDays { get; set; }

        [Input("noncurrentVersionTransition")]
        public Input<Inputs.BucketNoncurrentVersionTransitionArgs>? NoncurrentVersionTransition { get; set; }

        [Input("noncurrentVersionTransitions")]
        private InputList<Inputs.BucketNoncurrentVersionTransitionArgs>? _noncurrentVersionTransitions;
        public InputList<Inputs.BucketNoncurrentVersionTransitionArgs> NoncurrentVersionTransitions
        {
            get => _noncurrentVersionTransitions ?? (_noncurrentVersionTransitions = new InputList<Inputs.BucketNoncurrentVersionTransitionArgs>());
            set => _noncurrentVersionTransitions = value;
        }

        [Input("prefix")]
        public Input<string>? Prefix { get; set; }

        [Input("status", required: true)]
        public Input<string> Status { get; set; } = null!;

        [Input("tagFilters")]
        private InputList<Inputs.BucketTagFilterArgs>? _tagFilters;
        public InputList<Inputs.BucketTagFilterArgs> TagFilters
        {
            get => _tagFilters ?? (_tagFilters = new InputList<Inputs.BucketTagFilterArgs>());
            set => _tagFilters = value;
        }

        [Input("transition")]
        public Input<Inputs.BucketTransitionArgs>? Transition { get; set; }

        [Input("transitions")]
        private InputList<Inputs.BucketTransitionArgs>? _transitions;
        public InputList<Inputs.BucketTransitionArgs> Transitions
        {
            get => _transitions ?? (_transitions = new InputList<Inputs.BucketTransitionArgs>());
            set => _transitions = value;
        }

        public BucketRuleArgs()
        {
        }
    }
}
