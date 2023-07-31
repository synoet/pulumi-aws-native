// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTWireless.Outputs
{

    [OutputType]
    public sealed class TaskDefinitionUpdateWirelessGatewayTaskCreate
    {
        public readonly Outputs.TaskDefinitionLoRaWANUpdateGatewayTaskCreate? LoRaWan;
        public readonly string? UpdateDataRole;
        public readonly string? UpdateDataSource;

        [OutputConstructor]
        private TaskDefinitionUpdateWirelessGatewayTaskCreate(
            Outputs.TaskDefinitionLoRaWANUpdateGatewayTaskCreate? loRaWan,

            string? updateDataRole,

            string? updateDataSource)
        {
            LoRaWan = loRaWan;
            UpdateDataRole = updateDataRole;
            UpdateDataSource = updateDataSource;
        }
    }
}
