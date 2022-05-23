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
    /// Describes the Docker container for the model package.
    /// </summary>
    public sealed class ModelPackageContainerDefinitionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The DNS host name for the Docker container.
        /// </summary>
        [Input("containerHostname")]
        public Input<string>? ContainerHostname { get; set; }

        [Input("environment")]
        public Input<Inputs.ModelPackageEnvironmentArgs>? Environment { get; set; }

        /// <summary>
        /// The machine learning framework of the model package container image.
        /// </summary>
        [Input("framework")]
        public Input<string>? Framework { get; set; }

        /// <summary>
        /// The framework version of the Model Package Container Image.
        /// </summary>
        [Input("frameworkVersion")]
        public Input<string>? FrameworkVersion { get; set; }

        /// <summary>
        /// The Amazon EC2 Container Registry (Amazon ECR) path where inference code is stored.
        /// </summary>
        [Input("image", required: true)]
        public Input<string> Image { get; set; } = null!;

        /// <summary>
        /// An MD5 hash of the training algorithm that identifies the Docker image used for training.
        /// </summary>
        [Input("imageDigest")]
        public Input<string>? ImageDigest { get; set; }

        /// <summary>
        /// A structure with Model Input details.
        /// </summary>
        [Input("modelDataUrl")]
        public Input<string>? ModelDataUrl { get; set; }

        [Input("modelInput")]
        public Input<Inputs.ModelPackageContainerDefinitionModelInputPropertiesArgs>? ModelInput { get; set; }

        /// <summary>
        /// The name of a pre-trained machine learning benchmarked by Amazon SageMaker Inference Recommender model that matches your model.
        /// </summary>
        [Input("nearestModelName")]
        public Input<string>? NearestModelName { get; set; }

        /// <summary>
        /// The AWS Marketplace product ID of the model package.
        /// </summary>
        [Input("productId")]
        public Input<string>? ProductId { get; set; }

        public ModelPackageContainerDefinitionArgs()
        {
        }
    }
}
