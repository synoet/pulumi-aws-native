// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateNumericalMeasureFieldArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregationFunction")]
        public Input<Inputs.TemplateNumericalAggregationFunctionArgs>? AggregationFunction { get; set; }

        [Input("column", required: true)]
        public Input<Inputs.TemplateColumnIdentifierArgs> Column { get; set; } = null!;

        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        [Input("formatConfiguration")]
        public Input<Inputs.TemplateNumberFormatConfigurationArgs>? FormatConfiguration { get; set; }

        public TemplateNumericalMeasureFieldArgs()
        {
        }
        public static new TemplateNumericalMeasureFieldArgs Empty => new TemplateNumericalMeasureFieldArgs();
    }
}
