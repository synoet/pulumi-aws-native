// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    /// <summary>
    /// The baseline constraints resource for a monitoring job.
    /// </summary>
    public sealed class DataQualityJobDefinitionConstraintsResourceArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Amazon S3 URI for baseline constraint file in Amazon S3 that the current monitoring job should validated against.
        /// </summary>
        [Input("s3Uri")]
        public Input<string>? S3Uri { get; set; }

        public DataQualityJobDefinitionConstraintsResourceArgs()
        {
        }
        public static new DataQualityJobDefinitionConstraintsResourceArgs Empty => new DataQualityJobDefinitionConstraintsResourceArgs();
    }
}
