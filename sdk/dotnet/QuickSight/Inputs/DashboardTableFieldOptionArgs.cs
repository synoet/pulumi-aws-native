// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class DashboardTableFieldOptionArgs : global::Pulumi.ResourceArgs
    {
        [Input("customLabel")]
        public Input<string>? CustomLabel { get; set; }

        [Input("fieldId", required: true)]
        public Input<string> FieldId { get; set; } = null!;

        [Input("urlStyling")]
        public Input<Inputs.DashboardTableFieldUrlConfigurationArgs>? UrlStyling { get; set; }

        [Input("visibility")]
        public Input<Pulumi.AwsNative.QuickSight.DashboardVisibility>? Visibility { get; set; }

        /// <summary>
        /// String based length that is composed of value and unit in px
        /// </summary>
        [Input("width")]
        public Input<string>? Width { get; set; }

        public DashboardTableFieldOptionArgs()
        {
        }
        public static new DashboardTableFieldOptionArgs Empty => new DashboardTableFieldOptionArgs();
    }
}
