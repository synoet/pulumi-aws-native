// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.Synthetics.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html
    /// </summary>
    public sealed class CanaryPropertiesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-artifacts3location
        /// </summary>
        [Input("ArtifactS3Location", required: true)]
        public Input<string> ArtifactS3Location { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-code
        /// </summary>
        [Input("Code", required: true)]
        public Input<Inputs.CanaryCodeArgs> Code { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
        /// </summary>
        [Input("ExecutionRoleArn", required: true)]
        public Input<string> ExecutionRoleArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-failureretentionperiod
        /// </summary>
        [Input("FailureRetentionPeriod")]
        public Input<int>? FailureRetentionPeriod { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-name
        /// </summary>
        [Input("Name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runconfig
        /// </summary>
        [Input("RunConfig")]
        public Input<Inputs.CanaryRunConfigArgs>? RunConfig { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-runtimeversion
        /// </summary>
        [Input("RuntimeVersion", required: true)]
        public Input<string> RuntimeVersion { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-schedule
        /// </summary>
        [Input("Schedule", required: true)]
        public Input<Inputs.CanaryScheduleArgs> Schedule { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-startcanaryaftercreation
        /// </summary>
        [Input("StartCanaryAfterCreation", required: true)]
        public Input<bool> StartCanaryAfterCreation { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-successretentionperiod
        /// </summary>
        [Input("SuccessRetentionPeriod")]
        public Input<int>? SuccessRetentionPeriod { get; set; }

        [Input("Tags")]
        private InputList<Pulumi.Cloudformation.Inputs.TagArgs>? _Tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-tags
        /// </summary>
        public InputList<Pulumi.Cloudformation.Inputs.TagArgs> Tags
        {
            get => _Tags ?? (_Tags = new InputList<Pulumi.Cloudformation.Inputs.TagArgs>());
            set => _Tags = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-vpcconfig
        /// </summary>
        [Input("VPCConfig")]
        public Input<Inputs.CanaryVPCConfigArgs>? VPCConfig { get; set; }

        public CanaryPropertiesArgs()
        {
        }
    }
}