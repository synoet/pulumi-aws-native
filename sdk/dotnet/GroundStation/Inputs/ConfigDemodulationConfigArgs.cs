// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GroundStation.Inputs
{

    public sealed class ConfigDemodulationConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("unvalidatedJson")]
        public Input<string>? UnvalidatedJson { get; set; }

        public ConfigDemodulationConfigArgs()
        {
        }
        public static new ConfigDemodulationConfigArgs Empty => new ConfigDemodulationConfigArgs();
    }
}
