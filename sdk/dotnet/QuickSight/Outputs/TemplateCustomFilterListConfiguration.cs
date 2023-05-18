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
    public sealed class TemplateCustomFilterListConfiguration
    {
        public readonly ImmutableArray<string> CategoryValues;
        public readonly Pulumi.AwsNative.QuickSight.TemplateCategoryFilterMatchOperator MatchOperator;
        public readonly Pulumi.AwsNative.QuickSight.TemplateFilterNullOption NullOption;
        public readonly Pulumi.AwsNative.QuickSight.TemplateCategoryFilterSelectAllOptions? SelectAllOptions;

        [OutputConstructor]
        private TemplateCustomFilterListConfiguration(
            ImmutableArray<string> categoryValues,

            Pulumi.AwsNative.QuickSight.TemplateCategoryFilterMatchOperator matchOperator,

            Pulumi.AwsNative.QuickSight.TemplateFilterNullOption nullOption,

            Pulumi.AwsNative.QuickSight.TemplateCategoryFilterSelectAllOptions? selectAllOptions)
        {
            CategoryValues = categoryValues;
            MatchOperator = matchOperator;
            NullOption = nullOption;
            SelectAllOptions = selectAllOptions;
        }
    }
}
