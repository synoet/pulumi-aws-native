// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class DatastoreRetentionPeriodArgs : global::Pulumi.ResourceArgs
    {
        [Input("numberOfDays")]
        public Input<int>? NumberOfDays { get; set; }

        [Input("unlimited")]
        public Input<bool>? Unlimited { get; set; }

        public DatastoreRetentionPeriodArgs()
        {
        }
        public static new DatastoreRetentionPeriodArgs Empty => new DatastoreRetentionPeriodArgs();
    }
}
