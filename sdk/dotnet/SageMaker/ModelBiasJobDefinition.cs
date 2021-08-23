// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html
    /// </summary>
    [AwsNativeResourceType("aws-native:sagemaker:ModelBiasJobDefinition")]
    public partial class ModelBiasJobDefinition : Pulumi.CustomResource
    {
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        [Output("jobDefinitionArn")]
        public Output<string> JobDefinitionArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        /// </summary>
        [Output("jobDefinitionName")]
        public Output<string?> JobDefinitionName { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        /// </summary>
        [Output("jobResources")]
        public Output<Outputs.ModelBiasJobDefinitionMonitoringResources> JobResources { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        /// </summary>
        [Output("modelBiasAppSpecification")]
        public Output<Outputs.ModelBiasJobDefinitionModelBiasAppSpecification> ModelBiasAppSpecification { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        /// </summary>
        [Output("modelBiasBaselineConfig")]
        public Output<Outputs.ModelBiasJobDefinitionModelBiasBaselineConfig?> ModelBiasBaselineConfig { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        /// </summary>
        [Output("modelBiasJobInput")]
        public Output<Outputs.ModelBiasJobDefinitionModelBiasJobInput> ModelBiasJobInput { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        /// </summary>
        [Output("modelBiasJobOutputConfig")]
        public Output<Outputs.ModelBiasJobDefinitionMonitoringOutputConfig> ModelBiasJobOutputConfig { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        /// </summary>
        [Output("networkConfig")]
        public Output<Outputs.ModelBiasJobDefinitionNetworkConfig?> NetworkConfig { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        /// </summary>
        [Output("stoppingCondition")]
        public Output<Outputs.ModelBiasJobDefinitionStoppingCondition?> StoppingCondition { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ModelBiasJobDefinition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ModelBiasJobDefinition(string name, ModelBiasJobDefinitionArgs args, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelBiasJobDefinition", name, args ?? new ModelBiasJobDefinitionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ModelBiasJobDefinition(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:sagemaker:ModelBiasJobDefinition", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ModelBiasJobDefinition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ModelBiasJobDefinition Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ModelBiasJobDefinition(name, id, options);
        }
    }

    public sealed class ModelBiasJobDefinitionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobdefinitionname
        /// </summary>
        [Input("jobDefinitionName")]
        public Input<string>? JobDefinitionName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-jobresources
        /// </summary>
        [Input("jobResources", required: true)]
        public Input<Inputs.ModelBiasJobDefinitionMonitoringResourcesArgs> JobResources { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasappspecification
        /// </summary>
        [Input("modelBiasAppSpecification", required: true)]
        public Input<Inputs.ModelBiasJobDefinitionModelBiasAppSpecificationArgs> ModelBiasAppSpecification { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasbaselineconfig
        /// </summary>
        [Input("modelBiasBaselineConfig")]
        public Input<Inputs.ModelBiasJobDefinitionModelBiasBaselineConfigArgs>? ModelBiasBaselineConfig { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjobinput
        /// </summary>
        [Input("modelBiasJobInput", required: true)]
        public Input<Inputs.ModelBiasJobDefinitionModelBiasJobInputArgs> ModelBiasJobInput { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-modelbiasjoboutputconfig
        /// </summary>
        [Input("modelBiasJobOutputConfig", required: true)]
        public Input<Inputs.ModelBiasJobDefinitionMonitoringOutputConfigArgs> ModelBiasJobOutputConfig { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-networkconfig
        /// </summary>
        [Input("networkConfig")]
        public Input<Inputs.ModelBiasJobDefinitionNetworkConfigArgs>? NetworkConfig { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-rolearn
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-stoppingcondition
        /// </summary>
        [Input("stoppingCondition")]
        public Input<Inputs.ModelBiasJobDefinitionStoppingConditionArgs>? StoppingCondition { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-sagemaker-modelbiasjobdefinition.html#cfn-sagemaker-modelbiasjobdefinition-tags
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ModelBiasJobDefinitionArgs()
        {
        }
    }
}
