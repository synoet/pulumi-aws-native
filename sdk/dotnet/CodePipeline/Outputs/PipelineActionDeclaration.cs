// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline.Outputs
{

    [OutputType]
    public sealed class PipelineActionDeclaration
    {
        public readonly Outputs.PipelineActionTypeId ActionTypeId;
        public readonly object? Configuration;
        public readonly ImmutableArray<Outputs.PipelineInputArtifact> InputArtifacts;
        public readonly string Name;
        public readonly string? Namespace;
        public readonly ImmutableArray<Outputs.PipelineOutputArtifact> OutputArtifacts;
        public readonly string? Region;
        public readonly string? RoleArn;
        public readonly int? RunOrder;

        [OutputConstructor]
        private PipelineActionDeclaration(
            Outputs.PipelineActionTypeId actionTypeId,

            object? configuration,

            ImmutableArray<Outputs.PipelineInputArtifact> inputArtifacts,

            string name,

            string? @namespace,

            ImmutableArray<Outputs.PipelineOutputArtifact> outputArtifacts,

            string? region,

            string? roleArn,

            int? runOrder)
        {
            ActionTypeId = actionTypeId;
            Configuration = configuration;
            InputArtifacts = inputArtifacts;
            Name = name;
            Namespace = @namespace;
            OutputArtifacts = outputArtifacts;
            Region = region;
            RoleArn = roleArn;
            RunOrder = runOrder;
        }
    }
}
