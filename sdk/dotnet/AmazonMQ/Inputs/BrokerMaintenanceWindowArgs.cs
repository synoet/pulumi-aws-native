// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.AmazonMQ.Inputs
{

    /// <summary>
    /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html
    /// </summary>
    public sealed class BrokerMaintenanceWindowArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-dayofweek
        /// </summary>
        [Input("DayOfWeek", required: true)]
        public Input<string> DayOfWeek { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timeofday
        /// </summary>
        [Input("TimeOfDay", required: true)]
        public Input<string> TimeOfDay { get; set; } = null!;

        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-amazonmq-broker-maintenancewindow.html#cfn-amazonmq-broker-maintenancewindow-timezone
        /// </summary>
        [Input("TimeZone", required: true)]
        public Input<string> TimeZone { get; set; } = null!;

        public BrokerMaintenanceWindowArgs()
        {
        }
    }
}