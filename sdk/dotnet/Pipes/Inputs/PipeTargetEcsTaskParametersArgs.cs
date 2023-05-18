// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pipes.Inputs
{

    public sealed class PipeTargetEcsTaskParametersArgs : global::Pulumi.ResourceArgs
    {
        [Input("capacityProviderStrategy")]
        private InputList<Inputs.PipeCapacityProviderStrategyItemArgs>? _capacityProviderStrategy;
        public InputList<Inputs.PipeCapacityProviderStrategyItemArgs> CapacityProviderStrategy
        {
            get => _capacityProviderStrategy ?? (_capacityProviderStrategy = new InputList<Inputs.PipeCapacityProviderStrategyItemArgs>());
            set => _capacityProviderStrategy = value;
        }

        [Input("enableECSManagedTags")]
        public Input<bool>? EnableECSManagedTags { get; set; }

        [Input("enableExecuteCommand")]
        public Input<bool>? EnableExecuteCommand { get; set; }

        [Input("group")]
        public Input<string>? Group { get; set; }

        [Input("launchType")]
        public Input<Pulumi.AwsNative.Pipes.PipeLaunchType>? LaunchType { get; set; }

        [Input("networkConfiguration")]
        public Input<Inputs.PipeNetworkConfigurationArgs>? NetworkConfiguration { get; set; }

        [Input("overrides")]
        public Input<Inputs.PipeEcsTaskOverrideArgs>? Overrides { get; set; }

        [Input("placementConstraints")]
        private InputList<Inputs.PipePlacementConstraintArgs>? _placementConstraints;
        public InputList<Inputs.PipePlacementConstraintArgs> PlacementConstraints
        {
            get => _placementConstraints ?? (_placementConstraints = new InputList<Inputs.PipePlacementConstraintArgs>());
            set => _placementConstraints = value;
        }

        [Input("placementStrategy")]
        private InputList<Inputs.PipePlacementStrategyArgs>? _placementStrategy;
        public InputList<Inputs.PipePlacementStrategyArgs> PlacementStrategy
        {
            get => _placementStrategy ?? (_placementStrategy = new InputList<Inputs.PipePlacementStrategyArgs>());
            set => _placementStrategy = value;
        }

        [Input("platformVersion")]
        public Input<string>? PlatformVersion { get; set; }

        [Input("propagateTags")]
        public Input<Pulumi.AwsNative.Pipes.PipePropagateTags>? PropagateTags { get; set; }

        [Input("referenceId")]
        public Input<string>? ReferenceId { get; set; }

        [Input("tags")]
        private InputList<Inputs.PipeTagArgs>? _tags;
        public InputList<Inputs.PipeTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.PipeTagArgs>());
            set => _tags = value;
        }

        [Input("taskCount")]
        public Input<int>? TaskCount { get; set; }

        [Input("taskDefinitionArn", required: true)]
        public Input<string> TaskDefinitionArn { get; set; } = null!;

        public PipeTargetEcsTaskParametersArgs()
        {
        }
        public static new PipeTargetEcsTaskParametersArgs Empty => new PipeTargetEcsTaskParametersArgs();
    }
}
