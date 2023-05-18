// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Inputs
{

    /// <summary>
    /// Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting
    /// </summary>
    public sealed class GameServerGroupAutoScalingPolicyArgs : global::Pulumi.ResourceArgs
    {
        [Input("estimatedInstanceWarmup")]
        public Input<double>? EstimatedInstanceWarmup { get; set; }

        [Input("targetTrackingConfiguration", required: true)]
        public Input<Inputs.GameServerGroupTargetTrackingConfigurationArgs> TargetTrackingConfiguration { get; set; } = null!;

        public GameServerGroupAutoScalingPolicyArgs()
        {
        }
        public static new GameServerGroupAutoScalingPolicyArgs Empty => new GameServerGroupAutoScalingPolicyArgs();
    }
}
