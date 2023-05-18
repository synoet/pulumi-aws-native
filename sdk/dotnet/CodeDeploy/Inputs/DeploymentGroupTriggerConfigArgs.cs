// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodeDeploy.Inputs
{

    public sealed class DeploymentGroupTriggerConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("triggerEvents")]
        private InputList<string>? _triggerEvents;
        public InputList<string> TriggerEvents
        {
            get => _triggerEvents ?? (_triggerEvents = new InputList<string>());
            set => _triggerEvents = value;
        }

        [Input("triggerName")]
        public Input<string>? TriggerName { get; set; }

        [Input("triggerTargetArn")]
        public Input<string>? TriggerTargetArn { get; set; }

        public DeploymentGroupTriggerConfigArgs()
        {
        }
        public static new DeploymentGroupTriggerConfigArgs Empty => new DeploymentGroupTriggerConfigArgs();
    }
}
