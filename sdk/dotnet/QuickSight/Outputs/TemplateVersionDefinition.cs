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
    public sealed class TemplateVersionDefinition
    {
        public readonly Outputs.TemplateAnalysisDefaults? AnalysisDefaults;
        public readonly ImmutableArray<Outputs.TemplateCalculatedField> CalculatedFields;
        public readonly ImmutableArray<Outputs.TemplateColumnConfiguration> ColumnConfigurations;
        public readonly ImmutableArray<Outputs.TemplateDataSetConfiguration> DataSetConfigurations;
        public readonly ImmutableArray<Outputs.TemplateFilterGroup> FilterGroups;
        public readonly Outputs.TemplateAssetOptions? Options;
        public readonly ImmutableArray<Outputs.TemplateParameterDeclaration> ParameterDeclarations;
        public readonly ImmutableArray<Outputs.TemplateSheetDefinition> Sheets;

        [OutputConstructor]
        private TemplateVersionDefinition(
            Outputs.TemplateAnalysisDefaults? analysisDefaults,

            ImmutableArray<Outputs.TemplateCalculatedField> calculatedFields,

            ImmutableArray<Outputs.TemplateColumnConfiguration> columnConfigurations,

            ImmutableArray<Outputs.TemplateDataSetConfiguration> dataSetConfigurations,

            ImmutableArray<Outputs.TemplateFilterGroup> filterGroups,

            Outputs.TemplateAssetOptions? options,

            ImmutableArray<Outputs.TemplateParameterDeclaration> parameterDeclarations,

            ImmutableArray<Outputs.TemplateSheetDefinition> sheets)
        {
            AnalysisDefaults = analysisDefaults;
            CalculatedFields = calculatedFields;
            ColumnConfigurations = columnConfigurations;
            DataSetConfigurations = dataSetConfigurations;
            FilterGroups = filterGroups;
            Options = options;
            ParameterDeclarations = parameterDeclarations;
            Sheets = sheets;
        }
    }
}
