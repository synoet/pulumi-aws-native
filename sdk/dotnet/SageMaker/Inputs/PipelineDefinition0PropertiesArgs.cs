// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class PipelineDefinition0PropertiesArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A specification that defines the pipeline in JSON format.
        /// </summary>
        [Input("pipelineDefinitionBody", required: true)]
        public Input<string> PipelineDefinitionBody { get; set; } = null!;

        public PipelineDefinition0PropertiesArgs()
        {
        }
        public static new PipelineDefinition0PropertiesArgs Empty => new PipelineDefinition0PropertiesArgs();
    }
}
