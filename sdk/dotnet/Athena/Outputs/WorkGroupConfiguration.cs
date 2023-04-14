// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena.Outputs
{

    [OutputType]
    public sealed class WorkGroupConfiguration
    {
        public readonly string? AdditionalConfiguration;
        public readonly int? BytesScannedCutoffPerQuery;
        public readonly Outputs.WorkGroupCustomerContentEncryptionConfiguration? CustomerContentEncryptionConfiguration;
        public readonly bool? EnforceWorkGroupConfiguration;
        public readonly Outputs.WorkGroupEngineVersion? EngineVersion;
        public readonly string? ExecutionRole;
        public readonly bool? PublishCloudWatchMetricsEnabled;
        public readonly bool? RequesterPaysEnabled;
        public readonly Outputs.WorkGroupResultConfiguration? ResultConfiguration;

        [OutputConstructor]
        private WorkGroupConfiguration(
            string? additionalConfiguration,

            int? bytesScannedCutoffPerQuery,

            Outputs.WorkGroupCustomerContentEncryptionConfiguration? customerContentEncryptionConfiguration,

            bool? enforceWorkGroupConfiguration,

            Outputs.WorkGroupEngineVersion? engineVersion,

            string? executionRole,

            bool? publishCloudWatchMetricsEnabled,

            bool? requesterPaysEnabled,

            Outputs.WorkGroupResultConfiguration? resultConfiguration)
        {
            AdditionalConfiguration = additionalConfiguration;
            BytesScannedCutoffPerQuery = bytesScannedCutoffPerQuery;
            CustomerContentEncryptionConfiguration = customerContentEncryptionConfiguration;
            EnforceWorkGroupConfiguration = enforceWorkGroupConfiguration;
            EngineVersion = engineVersion;
            ExecutionRole = executionRole;
            PublishCloudWatchMetricsEnabled = publishCloudWatchMetricsEnabled;
            RequesterPaysEnabled = requesterPaysEnabled;
            ResultConfiguration = resultConfiguration;
        }
    }
}
