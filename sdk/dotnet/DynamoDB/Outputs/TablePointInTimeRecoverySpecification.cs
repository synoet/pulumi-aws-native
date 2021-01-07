// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.DynamoDB.Outputs
{

    [OutputType]
    public sealed class TablePointInTimeRecoverySpecification
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dynamodb-table-pointintimerecoveryspecification.html#cfn-dynamodb-table-pointintimerecoveryspecification-pointintimerecoveryenabled
        /// </summary>
        public readonly bool? PointInTimeRecoveryEnabled;

        [OutputConstructor]
        private TablePointInTimeRecoverySpecification(bool? PointInTimeRecoveryEnabled)
        {
            this.PointInTimeRecoveryEnabled = PointInTimeRecoveryEnabled;
        }
    }
}