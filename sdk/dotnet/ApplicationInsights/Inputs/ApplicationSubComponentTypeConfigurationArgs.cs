// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApplicationInsights.Inputs
{

    /// <summary>
    /// One type sub component configurations for the component.
    /// </summary>
    public sealed class ApplicationSubComponentTypeConfigurationArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The configuration settings of sub components.
        /// </summary>
        [Input("subComponentConfigurationDetails", required: true)]
        public Input<Inputs.ApplicationSubComponentConfigurationDetailsArgs> SubComponentConfigurationDetails { get; set; } = null!;

        /// <summary>
        /// The sub component type.
        /// </summary>
        [Input("subComponentType", required: true)]
        public Input<Pulumi.AwsNative.ApplicationInsights.ApplicationSubComponentTypeConfigurationSubComponentType> SubComponentType { get; set; } = null!;

        public ApplicationSubComponentTypeConfigurationArgs()
        {
        }
    }
}
