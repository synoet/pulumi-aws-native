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
    public sealed class TemplateDestinationParameterValueConfiguration
    {
        public readonly Outputs.TemplateCustomValuesConfiguration? CustomValuesConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.TemplateSelectAllValueOptions? SelectAllValueOptions;
        public readonly string? SourceField;
        public readonly string? SourceParameterName;

        [OutputConstructor]
        private TemplateDestinationParameterValueConfiguration(
            Outputs.TemplateCustomValuesConfiguration? customValuesConfiguration,

            Pulumi.AwsNative.QuickSight.TemplateSelectAllValueOptions? selectAllValueOptions,

            string? sourceField,

            string? sourceParameterName)
        {
            CustomValuesConfiguration = customValuesConfiguration;
            SelectAllValueOptions = selectAllValueOptions;
            SourceField = sourceField;
            SourceParameterName = sourceParameterName;
        }
    }
}
