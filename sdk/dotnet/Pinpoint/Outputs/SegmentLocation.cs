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
    public sealed class SegmentLocation
    {
        public readonly Outputs.SegmentSetDimension? Country;
        public readonly Outputs.SegmentGpsPoint? GpsPoint;

        [OutputConstructor]
        private SegmentLocation(
            Outputs.SegmentSetDimension? country,

            Outputs.SegmentGpsPoint? gpsPoint)
        {
            Country = country;
            GpsPoint = gpsPoint;
        }
    }
}
