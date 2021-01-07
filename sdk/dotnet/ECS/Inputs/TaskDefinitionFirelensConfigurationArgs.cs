// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.ECS.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html
    /// </summary>
    public sealed class TaskDefinitionFirelensConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("Options")]
        private InputMap<string>? _Options;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-options
        /// </summary>
        public InputMap<string> Options
        {
            get => _Options ?? (_Options = new InputMap<string>());
            set => _Options = value;
        }

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ecs-taskdefinition-firelensconfiguration.html#cfn-ecs-taskdefinition-firelensconfiguration-type
        /// </summary>
        [Input("Type")]
        public Input<string>? Type { get; set; }

        public TaskDefinitionFirelensConfigurationArgs()
        {
        }
    }
}