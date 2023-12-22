// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder.Outputs
{

    /// <summary>
    /// The workflow configuration of the image
    /// </summary>
    [OutputType]
    public sealed class ImageWorkflowConfiguration
    {
        /// <summary>
        /// Define execution decision in case of workflow failure
        /// </summary>
        public readonly Pulumi.AwsNative.ImageBuilder.ImageWorkflowConfigurationOnFailure? OnFailure;
        /// <summary>
        /// The parallel group name
        /// </summary>
        public readonly string? ParallelGroup;
        /// <summary>
        /// The parameters associated with the workflow
        /// </summary>
        public readonly ImmutableArray<Outputs.ImageWorkflowParameter> Parameters;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the workflow
        /// </summary>
        public readonly string? WorkflowArn;

        [OutputConstructor]
        private ImageWorkflowConfiguration(
            Pulumi.AwsNative.ImageBuilder.ImageWorkflowConfigurationOnFailure? onFailure,

            string? parallelGroup,

            ImmutableArray<Outputs.ImageWorkflowParameter> parameters,

            string? workflowArn)
        {
            OnFailure = onFailure;
            ParallelGroup = parallelGroup;
            Parameters = parameters;
            WorkflowArn = workflowArn;
        }
    }
}
