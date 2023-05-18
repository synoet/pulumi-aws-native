// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECS.Inputs
{

    /// <summary>
    /// An object representing the network configuration for a task or service.
    /// </summary>
    public sealed class TaskSetNetworkConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("awsVpcConfiguration")]
        public Input<Inputs.TaskSetAwsVpcConfigurationArgs>? AwsVpcConfiguration { get; set; }

        public TaskSetNetworkConfigurationArgs()
        {
        }
        public static new TaskSetNetworkConfigurationArgs Empty => new TaskSetNetworkConfigurationArgs();
    }
}
