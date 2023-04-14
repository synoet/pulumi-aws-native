// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// Container image configuration object for the monitoring job.
    /// </summary>
    public sealed class DataQualityJobDefinitionDataQualityAppSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("containerArguments")]
        private InputList<string>? _containerArguments;

        /// <summary>
        /// An array of arguments for the container used to run the monitoring job.
        /// </summary>
        public InputList<string> ContainerArguments
        {
            get => _containerArguments ?? (_containerArguments = new InputList<string>());
            set => _containerArguments = value;
        }

        [Input("containerEntrypoint")]
        private InputList<string>? _containerEntrypoint;

        /// <summary>
        /// Specifies the entrypoint for a container used to run the monitoring job.
        /// </summary>
        public InputList<string> ContainerEntrypoint
        {
            get => _containerEntrypoint ?? (_containerEntrypoint = new InputList<string>());
            set => _containerEntrypoint = value;
        }

        /// <summary>
        /// Sets the environment variables in the Docker container
        /// </summary>
        [Input("environment")]
        public Input<object>? Environment { get; set; }

        /// <summary>
        /// The container image to be run by the monitoring job.
        /// </summary>
        [Input("imageUri", required: true)]
        public Input<string> ImageUri { get; set; } = null!;

        /// <summary>
        /// An Amazon S3 URI to a script that is called after analysis has been performed. Applicable only for the built-in (first party) containers.
        /// </summary>
        [Input("postAnalyticsProcessorSourceUri")]
        public Input<string>? PostAnalyticsProcessorSourceUri { get; set; }

        /// <summary>
        /// An Amazon S3 URI to a script that is called per row prior to running analysis. It can base64 decode the payload and convert it into a flatted json so that the built-in container can use the converted data. Applicable only for the built-in (first party) containers
        /// </summary>
        [Input("recordPreprocessorSourceUri")]
        public Input<string>? RecordPreprocessorSourceUri { get; set; }

        public DataQualityJobDefinitionDataQualityAppSpecificationArgs()
        {
        }
        public static new DataQualityJobDefinitionDataQualityAppSpecificationArgs Empty => new DataQualityJobDefinitionDataQualityAppSpecificationArgs();
    }
}
