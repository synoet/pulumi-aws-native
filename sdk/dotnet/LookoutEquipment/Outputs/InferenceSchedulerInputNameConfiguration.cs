// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.LookoutEquipment.Outputs
{

    /// <summary>
    /// Specifies configuration information for the input data for the inference, including timestamp format and delimiter.
    /// </summary>
    [OutputType]
    public sealed class InferenceSchedulerInputNameConfiguration
    {
        /// <summary>
        /// Indicates the delimiter character used between items in the data.
        /// </summary>
        public readonly string? ComponentTimestampDelimiter;
        /// <summary>
        /// The format of the timestamp, whether Epoch time, or standard, with or without hyphens (-).
        /// </summary>
        public readonly string? TimestampFormat;

        [OutputConstructor]
        private InferenceSchedulerInputNameConfiguration(
            string? componentTimestampDelimiter,

            string? timestampFormat)
        {
            ComponentTimestampDelimiter = componentTimestampDelimiter;
            TimestampFormat = timestampFormat;
        }
    }
}
