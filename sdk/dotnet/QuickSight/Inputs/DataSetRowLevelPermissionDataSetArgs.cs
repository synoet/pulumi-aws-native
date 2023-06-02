// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    /// <summary>
    /// &lt;p&gt;The row-level security configuration for the dataset.&lt;/p&gt;
    /// </summary>
    public sealed class DataSetRowLevelPermissionDataSetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// &lt;p&gt;The Amazon Resource Name (ARN) of the permission dataset.&lt;/p&gt;
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        [Input("formatVersion")]
        public Input<Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionFormatVersion>? FormatVersion { get; set; }

        /// <summary>
        /// &lt;p&gt;The namespace associated with the row-level permissions dataset.&lt;/p&gt;
        /// </summary>
        [Input("namespace")]
        public Input<string>? Namespace { get; set; }

        [Input("permissionPolicy", required: true)]
        public Input<Pulumi.AwsNative.QuickSight.DataSetRowLevelPermissionPolicy> PermissionPolicy { get; set; } = null!;

        [Input("status")]
        public Input<Pulumi.AwsNative.QuickSight.DataSetStatus>? Status { get; set; }

        public DataSetRowLevelPermissionDataSetArgs()
        {
        }
        public static new DataSetRowLevelPermissionDataSetArgs Empty => new DataSetRowLevelPermissionDataSetArgs();
    }
}
