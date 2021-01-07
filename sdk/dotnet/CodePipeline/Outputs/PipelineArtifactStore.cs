// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.CodePipeline.Outputs
{

    [OutputType]
    public sealed class PipelineArtifactStore
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-encryptionkey
        /// </summary>
        public readonly Outputs.PipelineEncryptionKey? EncryptionKey;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-location
        /// </summary>
        public readonly string Location;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codepipeline-pipeline-artifactstore.html#cfn-codepipeline-pipeline-artifactstore-type
        /// </summary>
        public readonly string Type;

        [OutputConstructor]
        private PipelineArtifactStore(
            Outputs.PipelineEncryptionKey? EncryptionKey,

            string Location,

            string Type)
        {
            this.EncryptionKey = EncryptionKey;
            this.Location = Location;
            this.Type = Type;
        }
    }
}