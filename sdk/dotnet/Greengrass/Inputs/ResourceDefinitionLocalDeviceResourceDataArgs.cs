// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Greengrass.Inputs
{

    public sealed class ResourceDefinitionLocalDeviceResourceDataArgs : global::Pulumi.ResourceArgs
    {
        [Input("groupOwnerSetting")]
        public Input<Inputs.ResourceDefinitionGroupOwnerSettingArgs>? GroupOwnerSetting { get; set; }

        [Input("sourcePath", required: true)]
        public Input<string> SourcePath { get; set; } = null!;

        public ResourceDefinitionLocalDeviceResourceDataArgs()
        {
        }
        public static new ResourceDefinitionLocalDeviceResourceDataArgs Empty => new ResourceDefinitionLocalDeviceResourceDataArgs();
    }
}
