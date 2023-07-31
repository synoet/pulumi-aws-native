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
    /// Details about inference jobs that can be run with models based on this model package.
    /// </summary>
    public sealed class ModelPackageInferenceSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("containers", required: true)]
        private InputList<Inputs.ModelPackageContainerDefinitionArgs>? _containers;

        /// <summary>
        /// The Amazon ECR registry path of the Docker image that contains the inference code.
        /// </summary>
        public InputList<Inputs.ModelPackageContainerDefinitionArgs> Containers
        {
            get => _containers ?? (_containers = new InputList<Inputs.ModelPackageContainerDefinitionArgs>());
            set => _containers = value;
        }

        [Input("supportedContentTypes", required: true)]
        private InputList<string>? _supportedContentTypes;

        /// <summary>
        /// The supported MIME types for the input data.
        /// </summary>
        public InputList<string> SupportedContentTypes
        {
            get => _supportedContentTypes ?? (_supportedContentTypes = new InputList<string>());
            set => _supportedContentTypes = value;
        }

        [Input("supportedRealtimeInferenceInstanceTypes")]
        private InputList<string>? _supportedRealtimeInferenceInstanceTypes;

        /// <summary>
        /// A list of the instance types that are used to generate inferences in real-time
        /// </summary>
        public InputList<string> SupportedRealtimeInferenceInstanceTypes
        {
            get => _supportedRealtimeInferenceInstanceTypes ?? (_supportedRealtimeInferenceInstanceTypes = new InputList<string>());
            set => _supportedRealtimeInferenceInstanceTypes = value;
        }

        [Input("supportedResponseMimeTypes", required: true)]
        private InputList<string>? _supportedResponseMimeTypes;

        /// <summary>
        /// The supported MIME types for the output data.
        /// </summary>
        public InputList<string> SupportedResponseMimeTypes
        {
            get => _supportedResponseMimeTypes ?? (_supportedResponseMimeTypes = new InputList<string>());
            set => _supportedResponseMimeTypes = value;
        }

        [Input("supportedTransformInstanceTypes")]
        private InputList<string>? _supportedTransformInstanceTypes;

        /// <summary>
        /// A list of the instance types on which a transformation job can be run or on which an endpoint can be deployed.
        /// </summary>
        public InputList<string> SupportedTransformInstanceTypes
        {
            get => _supportedTransformInstanceTypes ?? (_supportedTransformInstanceTypes = new InputList<string>());
            set => _supportedTransformInstanceTypes = value;
        }

        public ModelPackageInferenceSpecificationArgs()
        {
        }
        public static new ModelPackageInferenceSpecificationArgs Empty => new ModelPackageInferenceSpecificationArgs();
    }
}
