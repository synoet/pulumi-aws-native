// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Inputs
{

    public sealed class InstanceGroupConfigAutoScalingPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("constraints", required: true)]
        public Input<Inputs.InstanceGroupConfigScalingConstraintsArgs> Constraints { get; set; } = null!;

        [Input("rules", required: true)]
        private InputList<Inputs.InstanceGroupConfigScalingRuleArgs>? _rules;
        public InputList<Inputs.InstanceGroupConfigScalingRuleArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.InstanceGroupConfigScalingRuleArgs>());
            set => _rules = value;
        }

        public InstanceGroupConfigAutoScalingPolicyArgs()
        {
        }
    }
}
