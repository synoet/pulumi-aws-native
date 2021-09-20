// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    /// <summary>
    /// Trigger settings of the flow.
    /// </summary>
    public sealed class FlowTriggerConfigArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Details required based on the type of trigger
        /// </summary>
        [Input("triggerProperties")]
        public Input<Inputs.FlowScheduledTriggerPropertiesArgs>? TriggerProperties { get; set; }

        /// <summary>
        /// Trigger type of the flow
        /// </summary>
        [Input("triggerType", required: true)]
        public Input<Pulumi.AwsNative.AppFlow.FlowTriggerType> TriggerType { get; set; } = null!;

        public FlowTriggerConfigArgs()
        {
        }
    }
}
