// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TopicColumnArgs : global::Pulumi.ResourceArgs
    {
        [Input("aggregation")]
        public Input<Pulumi.AwsNative.QuickSight.TopicDefaultAggregation>? Aggregation { get; set; }

        [Input("allowedAggregations")]
        private InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation>? _allowedAggregations;
        public InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> AllowedAggregations
        {
            get => _allowedAggregations ?? (_allowedAggregations = new InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation>());
            set => _allowedAggregations = value;
        }

        [Input("cellValueSynonyms")]
        private InputList<Inputs.TopicCellValueSynonymArgs>? _cellValueSynonyms;
        public InputList<Inputs.TopicCellValueSynonymArgs> CellValueSynonyms
        {
            get => _cellValueSynonyms ?? (_cellValueSynonyms = new InputList<Inputs.TopicCellValueSynonymArgs>());
            set => _cellValueSynonyms = value;
        }

        [Input("columnDataRole")]
        public Input<Pulumi.AwsNative.QuickSight.TopicColumnDataRole>? ColumnDataRole { get; set; }

        [Input("columnDescription")]
        public Input<string>? ColumnDescription { get; set; }

        [Input("columnFriendlyName")]
        public Input<string>? ColumnFriendlyName { get; set; }

        [Input("columnName", required: true)]
        public Input<string> ColumnName { get; set; } = null!;

        [Input("columnSynonyms")]
        private InputList<string>? _columnSynonyms;
        public InputList<string> ColumnSynonyms
        {
            get => _columnSynonyms ?? (_columnSynonyms = new InputList<string>());
            set => _columnSynonyms = value;
        }

        [Input("comparativeOrder")]
        public Input<Inputs.TopicComparativeOrderArgs>? ComparativeOrder { get; set; }

        [Input("defaultFormatting")]
        public Input<Inputs.TopicDefaultFormattingArgs>? DefaultFormatting { get; set; }

        [Input("isIncludedInTopic")]
        public Input<bool>? IsIncludedInTopic { get; set; }

        [Input("neverAggregateInFilter")]
        public Input<bool>? NeverAggregateInFilter { get; set; }

        [Input("notAllowedAggregations")]
        private InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation>? _notAllowedAggregations;
        public InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> NotAllowedAggregations
        {
            get => _notAllowedAggregations ?? (_notAllowedAggregations = new InputList<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation>());
            set => _notAllowedAggregations = value;
        }

        [Input("semanticType")]
        public Input<Inputs.TopicSemanticTypeArgs>? SemanticType { get; set; }

        [Input("timeGranularity")]
        public Input<Pulumi.AwsNative.QuickSight.TopicTimeGranularity>? TimeGranularity { get; set; }

        public TopicColumnArgs()
        {
        }
        public static new TopicColumnArgs Empty => new TopicColumnArgs();
    }
}
