// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Inputs
{

    public sealed class TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs : global::Pulumi.ResourceArgs
    {
        [Input("currentVersion")]
        public Input<Inputs.TaskDefinitionLoRaWanGatewayVersionArgs>? CurrentVersion { get; set; }

        [Input("updateVersion")]
        public Input<Inputs.TaskDefinitionLoRaWanGatewayVersionArgs>? UpdateVersion { get; set; }

        public TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs()
        {
        }
        public static new TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs Empty => new TaskDefinitionLoRaWanUpdateGatewayTaskEntryArgs();
    }
}
