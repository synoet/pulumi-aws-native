// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics
{
    public static class GetDatastore
    {
        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Datastore
        /// </summary>
        public static Task<GetDatastoreResult> InvokeAsync(GetDatastoreArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDatastoreResult>("aws-native:iotanalytics:getDatastore", args ?? new GetDatastoreArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Datastore
        /// </summary>
        public static Output<GetDatastoreResult> Invoke(GetDatastoreInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDatastoreResult>("aws-native:iotanalytics:getDatastore", args ?? new GetDatastoreInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDatastoreArgs : global::Pulumi.InvokeArgs
    {
        [Input("datastoreName", required: true)]
        public string DatastoreName { get; set; } = null!;

        public GetDatastoreArgs()
        {
        }
        public static new GetDatastoreArgs Empty => new GetDatastoreArgs();
    }

    public sealed class GetDatastoreInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("datastoreName", required: true)]
        public Input<string> DatastoreName { get; set; } = null!;

        public GetDatastoreInvokeArgs()
        {
        }
        public static new GetDatastoreInvokeArgs Empty => new GetDatastoreInvokeArgs();
    }


    [OutputType]
    public sealed class GetDatastoreResult
    {
        public readonly Outputs.DatastorePartitions? DatastorePartitions;
        public readonly Outputs.DatastoreStorage? DatastoreStorage;
        public readonly Outputs.DatastoreFileFormatConfiguration? FileFormatConfiguration;
        public readonly string? Id;
        public readonly Outputs.DatastoreRetentionPeriod? RetentionPeriod;
        public readonly ImmutableArray<Outputs.DatastoreTag> Tags;

        [OutputConstructor]
        private GetDatastoreResult(
            Outputs.DatastorePartitions? datastorePartitions,

            Outputs.DatastoreStorage? datastoreStorage,

            Outputs.DatastoreFileFormatConfiguration? fileFormatConfiguration,

            string? id,

            Outputs.DatastoreRetentionPeriod? retentionPeriod,

            ImmutableArray<Outputs.DatastoreTag> tags)
        {
            DatastorePartitions = datastorePartitions;
            DatastoreStorage = datastoreStorage;
            FileFormatConfiguration = fileFormatConfiguration;
            Id = id;
            RetentionPeriod = retentionPeriod;
            Tags = tags;
        }
    }
}
