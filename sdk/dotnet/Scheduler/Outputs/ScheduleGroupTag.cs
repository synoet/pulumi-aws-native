// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Scheduler.Outputs
{

    /// <summary>
    /// Tag to associate with the resource.
    /// </summary>
    [OutputType]
    public sealed class ScheduleGroupTag
    {
        /// <summary>
        /// Key for the tag
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// Value for the tag
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private ScheduleGroupTag(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
