// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplatePivotTableSortConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("fieldSortOptions")]
        private InputList<Inputs.TemplatePivotFieldSortOptionsArgs>? _fieldSortOptions;
        public InputList<Inputs.TemplatePivotFieldSortOptionsArgs> FieldSortOptions
        {
            get => _fieldSortOptions ?? (_fieldSortOptions = new InputList<Inputs.TemplatePivotFieldSortOptionsArgs>());
            set => _fieldSortOptions = value;
        }

        public TemplatePivotTableSortConfigurationArgs()
        {
        }
        public static new TemplatePivotTableSortConfigurationArgs Empty => new TemplatePivotTableSortConfigurationArgs();
    }
}
