// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Inputs
{

    /// <summary>
    /// The definition for event bridge action.
    /// </summary>
    public sealed class RuleEventBridgeActionArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the event bridge action.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public RuleEventBridgeActionArgs()
        {
        }
        public static new RuleEventBridgeActionArgs Empty => new RuleEventBridgeActionArgs();
    }
}
