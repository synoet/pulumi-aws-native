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
    public sealed class DataSourceConfluenceBlogToIndexFieldMapping
    {
        public readonly Pulumi.AwsNative.Kendra.DataSourceConfluenceBlogFieldName DataSourceFieldName;
        public readonly string? DateFieldFormat;
        public readonly string IndexFieldName;

        [OutputConstructor]
        private DataSourceConfluenceBlogToIndexFieldMapping(
            Pulumi.AwsNative.Kendra.DataSourceConfluenceBlogFieldName dataSourceFieldName,

            string? dateFieldFormat,

            string indexFieldName)
        {
            DataSourceFieldName = dataSourceFieldName;
            DateFieldFormat = dateFieldFormat;
            IndexFieldName = indexFieldName;
        }
    }
}
