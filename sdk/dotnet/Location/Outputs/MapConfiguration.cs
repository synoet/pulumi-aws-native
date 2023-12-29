// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Location.Outputs
{

    [OutputType]
    public sealed class MapConfiguration
    {
        public readonly string? PoliticalView;
        public readonly string Style;

        [OutputConstructor]
        private MapConfiguration(
            string? politicalView,

            string style)
        {
            PoliticalView = politicalView;
            Style = style;
        }
    }
}
