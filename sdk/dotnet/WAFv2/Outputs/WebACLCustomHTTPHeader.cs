// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Outputs
{

    /// <summary>
    /// HTTP header.
    /// </summary>
    [OutputType]
    public sealed class WebACLCustomHTTPHeader
    {
        public readonly string Name;
        public readonly string Value;

        [OutputConstructor]
        private WebACLCustomHTTPHeader(
            string name,

            string value)
        {
            Name = name;
            Value = value;
        }
    }
}
