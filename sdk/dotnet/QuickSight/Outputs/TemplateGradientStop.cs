// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TemplateGradientStop
    {
        public readonly string? Color;
        public readonly double? DataValue;
        public readonly double GradientOffset;

        [OutputConstructor]
        private TemplateGradientStop(
            string? color,

            double? dataValue,

            double gradientOffset)
        {
            Color = color;
            DataValue = dataValue;
            GradientOffset = gradientOffset;
        }
    }
}
