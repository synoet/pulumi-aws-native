// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// Resource Type definition for AWS::SageMaker::ModelExplainabilityJobDefinition
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:ModelExplainabilityJobDefinition")]
    public partial class ModelExplainabilityJobDefinition : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The time at which the job definition was created.
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("endpointName")]
        public Output<string?> EndpointName { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of job definition.
        /// </summary>
        [Output("jobDefinitionArn")]
        public Output<string> JobDefinitionArn { get; private set; } = null!;

        [Output("jobDefinitionName")]
        public Output<string?> JobDefinitionName { get; private set; } = null!;

        [Output("jobResources")]
        public Output<Outputs.ModelExplainabilityJobDefinitionMonitoringResources> JobResources { get; private set; } = null!;

        [Output("modelExplainabilityAppSpecification")]
        public Output<Outputs.ModelExplainabilityJobDefinitionModelExplainabilityAppSpecification> ModelExplainabilityAppSpecification { get; private set; } = null!;

        [Output("modelExplainabilityBaselineConfig")]
        public Output<Outputs.ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfig?> ModelExplainabilityBaselineConfig { get; private set; } = null!;

        [Output("modelExplainabilityJobInput")]
        public Output<Outputs.ModelExplainabilityJobDefinitionModelExplainabilityJobInput> ModelExplainabilityJobInput { get; private set; } = null!;

        [Output("modelExplainabilityJobOutputConfig")]
        public Output<Outputs.ModelExplainabilityJobDefinitionMonitoringOutputConfig> ModelExplainabilityJobOutputConfig { get; private set; } = null!;

        [Output("networkConfig")]
        public Output<Outputs.ModelExplainabilityJobDefinitionNetworkConfig?> NetworkConfig { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        [Output("stoppingCondition")]
        public Output<Outputs.ModelExplainabilityJobDefinitionStoppingCondition?> StoppingCondition { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ModelExplainabilityJobDefinitionTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ModelExplainabilityJobDefinition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ModelExplainabilityJobDefinition(string name, ModelExplainabilityJobDefinitionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelExplainabilityJobDefinition", name, args ?? new ModelExplainabilityJobDefinitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ModelExplainabilityJobDefinition(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelExplainabilityJobDefinition", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ModelExplainabilityJobDefinition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ModelExplainabilityJobDefinition Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ModelExplainabilityJobDefinition(name, id, options);
        }
    }

    public sealed class ModelExplainabilityJobDefinitionArgs : global::Pulumi.ResourceArgs
    {
        [Input("endpointName")]
        public Input<string>? EndpointName { get; set; }

        [Input("jobDefinitionName")]
        public Input<string>? JobDefinitionName { get; set; }

        [Input("jobResources", required: true)]
        public Input<Inputs.ModelExplainabilityJobDefinitionMonitoringResourcesArgs> JobResources { get; set; } = null!;

        [Input("modelExplainabilityAppSpecification", required: true)]
        public Input<Inputs.ModelExplainabilityJobDefinitionModelExplainabilityAppSpecificationArgs> ModelExplainabilityAppSpecification { get; set; } = null!;

        [Input("modelExplainabilityBaselineConfig")]
        public Input<Inputs.ModelExplainabilityJobDefinitionModelExplainabilityBaselineConfigArgs>? ModelExplainabilityBaselineConfig { get; set; }

        [Input("modelExplainabilityJobInput", required: true)]
        public Input<Inputs.ModelExplainabilityJobDefinitionModelExplainabilityJobInputArgs> ModelExplainabilityJobInput { get; set; } = null!;

        [Input("modelExplainabilityJobOutputConfig", required: true)]
        public Input<Inputs.ModelExplainabilityJobDefinitionMonitoringOutputConfigArgs> ModelExplainabilityJobOutputConfig { get; set; } = null!;

        [Input("networkConfig")]
        public Input<Inputs.ModelExplainabilityJobDefinitionNetworkConfigArgs>? NetworkConfig { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of an IAM role that Amazon SageMaker can assume to perform tasks on your behalf.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        [Input("stoppingCondition")]
        public Input<Inputs.ModelExplainabilityJobDefinitionStoppingConditionArgs>? StoppingCondition { get; set; }

        [Input("tags")]
        private InputList<Inputs.ModelExplainabilityJobDefinitionTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ModelExplainabilityJobDefinitionTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ModelExplainabilityJobDefinitionTagArgs>());
            set => _tags = value;
        }

        public ModelExplainabilityJobDefinitionArgs()
        {
        }
        public static new ModelExplainabilityJobDefinitionArgs Empty => new ModelExplainabilityJobDefinitionArgs();
    }
}
