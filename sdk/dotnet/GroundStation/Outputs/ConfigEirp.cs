// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GroundStation.Outputs
{

    [OutputType]
    public sealed class ConfigEirp
    {
        public readonly Pulumi.AwsNative.GroundStation.ConfigEirpUnits? Units;
        public readonly double? Value;

        [OutputConstructor]
        private ConfigEirp(
            Pulumi.AwsNative.GroundStation.ConfigEirpUnits? units,

            double? value)
        {
            Units = units;
            Value = value;
        }
    }
}
