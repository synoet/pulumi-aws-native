// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    /// <summary>
    /// &lt;p&gt;The row-level security configuration for the dataset.&lt;/p&gt;
    /// </summary>
    [OutputType]
    public sealed class DataSetRowLevelPermissionDataSet
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the permission dataset.&lt;/p&gt;
        /// </summary>
        public readonly string Arn;
        public readonly Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionFormatVersion? FormatVersion;
        /// <summary>
        /// &lt;p&gt;The namespace associated with the row-level permissions dataset.&lt;/p&gt;
        /// </summary>
        public readonly string? Namespace;
        public readonly Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionPolicy PermissionPolicy;

        [OutputConstructor]
        private DataSetRowLevelPermissionDataSet(
            string arn,

            Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionFormatVersion? formatVersion,

            string? @namespace,

            Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionPolicy permissionPolicy)
        {
            Arn = arn;
            FormatVersion = formatVersion;
            Namespace = @namespace;
            PermissionPolicy = permissionPolicy;
        }
    }
}
