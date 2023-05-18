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
    /// Metadata information related to model package version
    /// </summary>
    public sealed class ModelCardModelPackageDetailsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description provided for the model approval
        /// </summary>
        [Input("approvalDescription")]
        public Input<string>? ApprovalDescription { get; set; }

        /// <summary>
        /// Information about the user who created model package.
        /// </summary>
        [Input("createdBy")]
        public Input<Inputs.ModelCardModelPackageCreatorArgs>? CreatedBy { get; set; }

        /// <summary>
        /// The machine learning domain of the model package you specified. Common machine learning domains include computer vision and natural language processing.
        /// </summary>
        [Input("domain")]
        public Input<string>? Domain { get; set; }

        /// <summary>
        /// Details about inference jobs that can be run with models based on this model package.
        /// </summary>
        [Input("inferenceSpecification")]
        public Input<Inputs.ModelCardInferenceSpecificationArgs>? InferenceSpecification { get; set; }

        /// <summary>
        /// Current approval status of model package
        /// </summary>
        [Input("modelApprovalStatus")]
        public Input<Pulumi.AwsNative.SageMaker.ModelCardModelPackageDetailsModelApprovalStatus>? ModelApprovalStatus { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the model package
        /// </summary>
        [Input("modelPackageArn")]
        public Input<string>? ModelPackageArn { get; set; }

        /// <summary>
        /// A brief summary of the model package
        /// </summary>
        [Input("modelPackageDescription")]
        public Input<string>? ModelPackageDescription { get; set; }

        /// <summary>
        /// If the model is a versioned model, the name of the model group that the versioned model belongs to.
        /// </summary>
        [Input("modelPackageGroupName")]
        public Input<string>? ModelPackageGroupName { get; set; }

        /// <summary>
        /// Name of the model package
        /// </summary>
        [Input("modelPackageName")]
        public Input<string>? ModelPackageName { get; set; }

        /// <summary>
        /// Current status of model package
        /// </summary>
        [Input("modelPackageStatus")]
        public Input<Pulumi.AwsNative.SageMaker.ModelCardModelPackageDetailsModelPackageStatus>? ModelPackageStatus { get; set; }

        /// <summary>
        /// Version of the model package
        /// </summary>
        [Input("modelPackageVersion")]
        public Input<double>? ModelPackageVersion { get; set; }

        [Input("sourceAlgorithms")]
        private InputList<Inputs.ModelCardSourceAlgorithmArgs>? _sourceAlgorithms;

        /// <summary>
        /// A list of algorithms that were used to create a model package.
        /// </summary>
        public InputList<Inputs.ModelCardSourceAlgorithmArgs> SourceAlgorithms
        {
            get => _sourceAlgorithms ?? (_sourceAlgorithms = new InputList<Inputs.ModelCardSourceAlgorithmArgs>());
            set => _sourceAlgorithms = value;
        }

        /// <summary>
        /// The machine learning task you specified that your model package accomplishes. Common machine learning tasks include object detection and image classification.
        /// </summary>
        [Input("task")]
        public Input<string>? Task { get; set; }

        public ModelCardModelPackageDetailsArgs()
        {
        }
        public static new ModelCardModelPackageDetailsArgs Empty => new ModelCardModelPackageDetailsArgs();
    }
}
