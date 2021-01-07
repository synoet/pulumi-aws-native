// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Cloudformation.IoTAnalytics.Outputs
{

    [OutputType]
    public sealed class PipelineDatastore
    {
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-datastorename
        /// </summary>
        public readonly string? DatastoreName;
        /// <summary>
        /// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iotanalytics-pipeline-datastore.html#cfn-iotanalytics-pipeline-datastore-name
        /// </summary>
        public readonly string? Name;

        [OutputConstructor]
        private PipelineDatastore(
            string? DatastoreName,

            string? Name)
        {
            this.DatastoreName = DatastoreName;
            this.Name = Name;
        }
    }
}