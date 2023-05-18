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
    public sealed class AnalysisCalculatedField
    {
        public readonly string DataSetIdentifier;
        public readonly string Expression;
        public readonly string Name;

        [OutputConstructor]
        private AnalysisCalculatedField(
            string dataSetIdentifier,

            string expression,

            string name)
        {
            DataSetIdentifier = dataSetIdentifier;
            Expression = expression;
            Name = name;
        }
    }
}
