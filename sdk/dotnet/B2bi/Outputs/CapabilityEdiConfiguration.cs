// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.B2bi.Outputs
{

    [OutputType]
    public sealed class CapabilityEdiConfiguration
    {
        public readonly Outputs.CapabilityS3Location InputLocation;
        public readonly Outputs.CapabilityS3Location OutputLocation;
        public readonly string TransformerId;
        public readonly Outputs.CapabilityEdiTypeProperties Type;

        [OutputConstructor]
        private CapabilityEdiConfiguration(
            Outputs.CapabilityS3Location inputLocation,

            Outputs.CapabilityS3Location outputLocation,

            string transformerId,

            Outputs.CapabilityEdiTypeProperties type)
        {
            InputLocation = inputLocation;
            OutputLocation = outputLocation;
            TransformerId = transformerId;
            Type = type;
        }
    }
}
