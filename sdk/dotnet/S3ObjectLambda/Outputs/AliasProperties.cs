// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3ObjectLambda.Outputs
{

    [OutputType]
    public sealed class AliasProperties
    {
        /// <summary>
        /// The status of the Object Lambda alias.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// The value of the Object Lambda alias.
        /// </summary>
        public readonly string? Value;

        [OutputConstructor]
        private AliasProperties(
            string? status,

            string? value)
        {
            Status = status;
            Value = value;
        }
    }
}
