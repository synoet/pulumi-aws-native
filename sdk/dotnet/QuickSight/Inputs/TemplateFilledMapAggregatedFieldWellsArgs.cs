// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateFilledMapAggregatedFieldWellsArgs : global::Pulumi.ResourceArgs
    {
        [Input("geospatial")]
        private InputList<Inputs.TemplateDimensionFieldArgs>? _geospatial;
        public InputList<Inputs.TemplateDimensionFieldArgs> Geospatial
        {
            get => _geospatial ?? (_geospatial = new InputList<Inputs.TemplateDimensionFieldArgs>());
            set => _geospatial = value;
        }

        [Input("values")]
        private InputList<Inputs.TemplateMeasureFieldArgs>? _values;
        public InputList<Inputs.TemplateMeasureFieldArgs> Values
        {
            get => _values ?? (_values = new InputList<Inputs.TemplateMeasureFieldArgs>());
            set => _values = value;
        }

        public TemplateFilledMapAggregatedFieldWellsArgs()
        {
        }
        public static new TemplateFilledMapAggregatedFieldWellsArgs Empty => new TemplateFilledMapAggregatedFieldWellsArgs();
    }
}
