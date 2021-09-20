// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kendra.Outputs
{

    [OutputType]
    public sealed class DataSourceSalesforceStandardObjectConfiguration
    {
        public readonly string DocumentDataFieldName;
        public readonly string? DocumentTitleFieldName;
        public readonly ImmutableArray<Outputs.DataSourceDataSourceToIndexFieldMapping> FieldMappings;
        public readonly Pulumi.AwsNative.Kendra.DataSourceSalesforceStandardObjectName Name;

        [OutputConstructor]
        private DataSourceSalesforceStandardObjectConfiguration(
            string documentDataFieldName,

            string? documentTitleFieldName,

            ImmutableArray<Outputs.DataSourceDataSourceToIndexFieldMapping> fieldMappings,

            Pulumi.AwsNative.Kendra.DataSourceSalesforceStandardObjectName name)
        {
            DocumentDataFieldName = documentDataFieldName;
            DocumentTitleFieldName = documentTitleFieldName;
            FieldMappings = fieldMappings;
            Name = name;
        }
    }
}
