// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.StepFunctions
{
    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html
    /// </summary>
    [AwsNativeResourceType("aws-native:stepfunctions:StateMachine")]
    public partial class StateMachine : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition
        /// </summary>
        [Output("definition")]
        public Output<Outputs.StateMachineDefinition?> Definition { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
        /// </summary>
        [Output("definitionS3Location")]
        public Output<Outputs.StateMachineS3Location?> DefinitionS3Location { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        /// </summary>
        [Output("definitionString")]
        public Output<string?> DefinitionString { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
        /// </summary>
        [Output("definitionSubstitutions")]
        public Output<ImmutableDictionary<string, string>?> DefinitionSubstitutions { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
        /// </summary>
        [Output("loggingConfiguration")]
        public Output<Outputs.StateMachineLoggingConfiguration?> LoggingConfiguration { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        /// </summary>
        [Output("stateMachineName")]
        public Output<string?> StateMachineName { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
        /// </summary>
        [Output("stateMachineType")]
        public Output<string?> StateMachineType { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.StateMachineTagsEntry>> Tags { get; private set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
        /// </summary>
        [Output("tracingConfiguration")]
        public Output<Outputs.StateMachineTracingConfiguration?> TracingConfiguration { get; private set; } = null!;


        /// <summary>
        /// Create a StateMachine resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StateMachine(string name, StateMachineArgs args, CustomResourceOptions? options = null)
            : base("aws-native:stepfunctions:StateMachine", name, args ?? new StateMachineArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StateMachine(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:stepfunctions:StateMachine", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing StateMachine resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StateMachine Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new StateMachine(name, id, options);
        }
    }

    public sealed class StateMachineArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definition
        /// </summary>
        [Input("definition")]
        public Input<Inputs.StateMachineDefinitionArgs>? Definition { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitions3location
        /// </summary>
        [Input("definitionS3Location")]
        public Input<Inputs.StateMachineS3LocationArgs>? DefinitionS3Location { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionstring
        /// </summary>
        [Input("definitionString")]
        public Input<string>? DefinitionString { get; set; }

        [Input("definitionSubstitutions")]
        private InputMap<string>? _definitionSubstitutions;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-definitionsubstitutions
        /// </summary>
        public InputMap<string> DefinitionSubstitutions
        {
            get => _definitionSubstitutions ?? (_definitionSubstitutions = new InputMap<string>());
            set => _definitionSubstitutions = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-loggingconfiguration
        /// </summary>
        [Input("loggingConfiguration")]
        public Input<Inputs.StateMachineLoggingConfigurationArgs>? LoggingConfiguration { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-rolearn
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinename
        /// </summary>
        [Input("stateMachineName")]
        public Input<string>? StateMachineName { get; set; }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-statemachinetype
        /// </summary>
        [Input("stateMachineType")]
        public Input<string>? StateMachineType { get; set; }

        [Input("tags")]
        private InputList<Inputs.StateMachineTagsEntryArgs>? _tags;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tags
        /// </summary>
        public InputList<Inputs.StateMachineTagsEntryArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StateMachineTagsEntryArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-stepfunctions-statemachine.html#cfn-stepfunctions-statemachine-tracingconfiguration
        /// </summary>
        [Input("tracingConfiguration")]
        public Input<Inputs.StateMachineTracingConfigurationArgs>? TracingConfiguration { get; set; }

        public StateMachineArgs()
        {
        }
    }
}
