// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Outputs
{

    [OutputType]
    public sealed class SegmentGpsPoint
    {
        public readonly Outputs.SegmentCoordinates Coordinates;
        public readonly double RangeInKilometers;

        [OutputConstructor]
        private SegmentGpsPoint(
            Outputs.SegmentCoordinates coordinates,

            double rangeInKilometers)
        {
            Coordinates = coordinates;
            RangeInKilometers = rangeInKilometers;
        }
    }
}
