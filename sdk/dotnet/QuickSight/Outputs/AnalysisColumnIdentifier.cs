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
    public sealed class AnalysisColumnIdentifier
    {
        public readonly string ColumnName;
        public readonly string DataSetIdentifier;

        [OutputConstructor]
        private AnalysisColumnIdentifier(
            string columnName,

            string dataSetIdentifier)
        {
            ColumnName = columnName;
            DataSetIdentifier = dataSetIdentifier;
        }
    }
}
