// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Inputs
{

    public sealed class LaunchTemplateEnclaveOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public LaunchTemplateEnclaveOptionsArgs()
        {
        }
        public static new LaunchTemplateEnclaveOptionsArgs Empty => new LaunchTemplateEnclaveOptionsArgs();
    }
}
