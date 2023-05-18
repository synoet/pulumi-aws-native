// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DMS.Inputs
{

    public sealed class EndpointS3SettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("addColumnName")]
        public Input<bool>? AddColumnName { get; set; }

        [Input("bucketFolder")]
        public Input<string>? BucketFolder { get; set; }

        [Input("bucketName")]
        public Input<string>? BucketName { get; set; }

        [Input("cannedAclForObjects")]
        public Input<string>? CannedAclForObjects { get; set; }

        [Input("cdcInsertsAndUpdates")]
        public Input<bool>? CdcInsertsAndUpdates { get; set; }

        [Input("cdcInsertsOnly")]
        public Input<bool>? CdcInsertsOnly { get; set; }

        [Input("cdcMaxBatchInterval")]
        public Input<int>? CdcMaxBatchInterval { get; set; }

        [Input("cdcMinFileSize")]
        public Input<int>? CdcMinFileSize { get; set; }

        [Input("cdcPath")]
        public Input<string>? CdcPath { get; set; }

        [Input("compressionType")]
        public Input<string>? CompressionType { get; set; }

        [Input("csvDelimiter")]
        public Input<string>? CsvDelimiter { get; set; }

        [Input("csvNoSupValue")]
        public Input<string>? CsvNoSupValue { get; set; }

        [Input("csvNullValue")]
        public Input<string>? CsvNullValue { get; set; }

        [Input("csvRowDelimiter")]
        public Input<string>? CsvRowDelimiter { get; set; }

        [Input("dataFormat")]
        public Input<string>? DataFormat { get; set; }

        [Input("dataPageSize")]
        public Input<int>? DataPageSize { get; set; }

        [Input("datePartitionDelimiter")]
        public Input<string>? DatePartitionDelimiter { get; set; }

        [Input("datePartitionEnabled")]
        public Input<bool>? DatePartitionEnabled { get; set; }

        [Input("datePartitionSequence")]
        public Input<string>? DatePartitionSequence { get; set; }

        [Input("datePartitionTimezone")]
        public Input<string>? DatePartitionTimezone { get; set; }

        [Input("dictPageSizeLimit")]
        public Input<int>? DictPageSizeLimit { get; set; }

        [Input("enableStatistics")]
        public Input<bool>? EnableStatistics { get; set; }

        [Input("encodingType")]
        public Input<string>? EncodingType { get; set; }

        [Input("encryptionMode")]
        public Input<string>? EncryptionMode { get; set; }

        [Input("externalTableDefinition")]
        public Input<string>? ExternalTableDefinition { get; set; }

        [Input("ignoreHeaderRows")]
        public Input<int>? IgnoreHeaderRows { get; set; }

        [Input("includeOpForFullLoad")]
        public Input<bool>? IncludeOpForFullLoad { get; set; }

        [Input("maxFileSize")]
        public Input<int>? MaxFileSize { get; set; }

        [Input("parquetTimestampInMillisecond")]
        public Input<bool>? ParquetTimestampInMillisecond { get; set; }

        [Input("parquetVersion")]
        public Input<string>? ParquetVersion { get; set; }

        [Input("preserveTransactions")]
        public Input<bool>? PreserveTransactions { get; set; }

        [Input("rfc4180")]
        public Input<bool>? Rfc4180 { get; set; }

        [Input("rowGroupLength")]
        public Input<int>? RowGroupLength { get; set; }

        [Input("serverSideEncryptionKmsKeyId")]
        public Input<string>? ServerSideEncryptionKmsKeyId { get; set; }

        [Input("serviceAccessRoleArn")]
        public Input<string>? ServiceAccessRoleArn { get; set; }

        [Input("timestampColumnName")]
        public Input<string>? TimestampColumnName { get; set; }

        [Input("useCsvNoSupValue")]
        public Input<bool>? UseCsvNoSupValue { get; set; }

        [Input("useTaskStartTimeForFullLoadTimestamp")]
        public Input<bool>? UseTaskStartTimeForFullLoadTimestamp { get; set; }

        public EndpointS3SettingsArgs()
        {
        }
        public static new EndpointS3SettingsArgs Empty => new EndpointS3SettingsArgs();
    }
}
