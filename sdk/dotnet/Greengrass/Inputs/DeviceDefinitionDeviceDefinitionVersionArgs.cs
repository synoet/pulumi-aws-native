// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class DeviceDefinitionDeviceDefinitionVersionArgs : Pulumi.ResourceArgs
    {
        [Input("devices", required: true)]
        private InputList<Inputs.DeviceDefinitionDeviceArgs>? _devices;
        public InputList<Inputs.DeviceDefinitionDeviceArgs> Devices
        {
            get => _devices ?? (_devices = new InputList<Inputs.DeviceDefinitionDeviceArgs>());
            set => _devices = value;
        }

        public DeviceDefinitionDeviceDefinitionVersionArgs()
        {
        }
    }
}
