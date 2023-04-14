// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena.Inputs
{

    /// <summary>
    /// The configuration information that will be updated for this workgroup, which includes the location in Amazon S3 where query results are stored, the encryption option, if any, used for query results, whether the Amazon CloudWatch Metrics are enabled for the workgroup, whether the workgroup settings override the client-side settings, and the data usage limit for the amount of bytes scanned per query, if it is specified. 
    /// </summary>
    public sealed class WorkGroupConfigurationUpdatesArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalConfiguration")]
        public Input<string>? AdditionalConfiguration { get; set; }

        [Input("bytesScannedCutoffPerQuery")]
        public Input<int>? BytesScannedCutoffPerQuery { get; set; }

        [Input("customerContentEncryptionConfiguration")]
        public Input<Inputs.WorkGroupCustomerContentEncryptionConfigurationArgs>? CustomerContentEncryptionConfiguration { get; set; }

        [Input("enforceWorkGroupConfiguration")]
        public Input<bool>? EnforceWorkGroupConfiguration { get; set; }

        [Input("engineVersion")]
        public Input<Inputs.WorkGroupEngineVersionArgs>? EngineVersion { get; set; }

        [Input("executionRole")]
        public Input<string>? ExecutionRole { get; set; }

        [Input("publishCloudWatchMetricsEnabled")]
        public Input<bool>? PublishCloudWatchMetricsEnabled { get; set; }

        [Input("removeBytesScannedCutoffPerQuery")]
        public Input<bool>? RemoveBytesScannedCutoffPerQuery { get; set; }

        [Input("removeCustomerContentEncryptionConfiguration")]
        public Input<bool>? RemoveCustomerContentEncryptionConfiguration { get; set; }

        [Input("requesterPaysEnabled")]
        public Input<bool>? RequesterPaysEnabled { get; set; }

        [Input("resultConfigurationUpdates")]
        public Input<Inputs.WorkGroupResultConfigurationUpdatesArgs>? ResultConfigurationUpdates { get; set; }

        public WorkGroupConfigurationUpdatesArgs()
        {
        }
        public static new WorkGroupConfigurationUpdatesArgs Empty => new WorkGroupConfigurationUpdatesArgs();
    }
}
