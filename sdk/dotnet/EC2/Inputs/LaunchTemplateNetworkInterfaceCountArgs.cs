// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    public sealed class LaunchTemplateNetworkInterfaceCountArgs : global::Pulumi.ResourceArgs
    {
        [Input("max")]
        public Input<int>? Max { get; set; }

        [Input("min")]
        public Input<int>? Min { get; set; }

        public LaunchTemplateNetworkInterfaceCountArgs()
        {
        }
        public static new LaunchTemplateNetworkInterfaceCountArgs Empty => new LaunchTemplateNetworkInterfaceCountArgs();
    }
}
