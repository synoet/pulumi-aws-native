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
    public sealed class DashboardReferenceLine
    {
        public readonly Outputs.DashboardReferenceLineDataConfiguration DataConfiguration;
        public readonly Outputs.DashboardReferenceLineLabelConfiguration? LabelConfiguration;
        public readonly Pulumi.AwsNative.QuickSight.DashboardWidgetStatus? Status;
        public readonly Outputs.DashboardReferenceLineStyleConfiguration? StyleConfiguration;

        [OutputConstructor]
        private DashboardReferenceLine(
            Outputs.DashboardReferenceLineDataConfiguration dataConfiguration,

            Outputs.DashboardReferenceLineLabelConfiguration? labelConfiguration,

            Pulumi.AwsNative.QuickSight.DashboardWidgetStatus? status,

            Outputs.DashboardReferenceLineStyleConfiguration? styleConfiguration)
        {
            DataConfiguration = dataConfiguration;
            LabelConfiguration = labelConfiguration;
            Status = status;
            StyleConfiguration = styleConfiguration;
        }
    }
}
