// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisAnalyticsV2.Outputs
{

    /// <summary>
    /// For a SQL-based Kinesis Data Analytics application, provides additional mapping information when the record format uses delimiters, such as CSV. For example, the following sample records use CSV format, where the records use the '\n' as the row delimiter and a comma (",") as the column delimiter:
    /// `"name1", "address1"`
    /// `"name2", "address2"`
    /// </summary>
    [OutputType]
    public sealed class ApplicationCSVMappingParameters
    {
        /// <summary>
        /// The column delimiter. For example, in a CSV format, a comma (",") is the typical column delimiter.
        /// </summary>
        public readonly string RecordColumnDelimiter;
        /// <summary>
        /// The row delimiter. For example, in a CSV format, '\n' is the typical row delimiter.
        /// </summary>
        public readonly string RecordRowDelimiter;

        [OutputConstructor]
        private ApplicationCSVMappingParameters(
            string recordColumnDelimiter,

            string recordRowDelimiter)
        {
            RecordColumnDelimiter = recordColumnDelimiter;
            RecordRowDelimiter = recordRowDelimiter;
        }
    }
}
