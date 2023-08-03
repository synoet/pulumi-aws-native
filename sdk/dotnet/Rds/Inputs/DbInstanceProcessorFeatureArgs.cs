// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds.Inputs
{

    public sealed class DbInstanceProcessorFeatureArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the processor feature. Valid names are coreCount and threadsPerCore.
        /// </summary>
        [Input("name")]
        public Input<Pulumi.AwsNative.Rds.DbInstanceProcessorFeatureName>? Name { get; set; }

        /// <summary>
        /// The value of a processor feature name.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public DbInstanceProcessorFeatureArgs()
        {
        }
        public static new DbInstanceProcessorFeatureArgs Empty => new DbInstanceProcessorFeatureArgs();
    }
}
