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
    public sealed class DashboardFilledMapConditionalFormattingOption
    {
        public readonly Outputs.DashboardFilledMapShapeConditionalFormatting Shape;

        [OutputConstructor]
        private DashboardFilledMapConditionalFormattingOption(Outputs.DashboardFilledMapShapeConditionalFormatting shape)
        {
            Shape = shape;
        }
    }
}
