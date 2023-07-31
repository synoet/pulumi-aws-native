// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lambda.Outputs
{

    /// <summary>
    /// The configuration used by AWS Lambda to access event source
    /// </summary>
    [OutputType]
    public sealed class EventSourceMappingSourceAccessConfiguration
    {
        /// <summary>
        /// The type of source access configuration.
        /// </summary>
        public readonly Pulumi.AwsNative.Lambda.EventSourceMappingSourceAccessConfigurationType? Type;
        /// <summary>
        /// The URI for the source access configuration resource.
        /// </summary>
        public readonly string? Uri;

        [OutputConstructor]
        private EventSourceMappingSourceAccessConfiguration(
            Pulumi.AwsNative.Lambda.EventSourceMappingSourceAccessConfigurationType? type,

            string? uri)
        {
            Type = type;
            Uri = uri;
        }
    }
}
