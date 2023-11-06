// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway.Outputs
{

    [OutputType]
    public sealed class StageTag
    {
        /// <summary>
        /// The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private StageTag(
            string key,

            string value)
        {
            Key = key;
            Value = value;
        }
    }
}
