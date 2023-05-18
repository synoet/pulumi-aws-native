// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FSx.Inputs
{

    public sealed class VolumeClientConfigurationsArgs : global::Pulumi.ResourceArgs
    {
        [Input("clients", required: true)]
        public Input<string> Clients { get; set; } = null!;

        [Input("options", required: true)]
        private InputList<string>? _options;
        public InputList<string> Options
        {
            get => _options ?? (_options = new InputList<string>());
            set => _options = value;
        }

        public VolumeClientConfigurationsArgs()
        {
        }
        public static new VolumeClientConfigurationsArgs Empty => new VolumeClientConfigurationsArgs();
    }
}
