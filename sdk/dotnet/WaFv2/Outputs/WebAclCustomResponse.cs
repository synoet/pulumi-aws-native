// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Outputs
{

    /// <summary>
    /// Custom response.
    /// </summary>
    [OutputType]
    public sealed class WebAclCustomResponse
    {
        /// <summary>
        /// Custom response body key.
        /// </summary>
        public readonly string? CustomResponseBodyKey;
        public readonly int ResponseCode;
        /// <summary>
        /// Collection of HTTP headers.
        /// </summary>
        public readonly ImmutableArray<Outputs.WebAclCustomHttpHeader> ResponseHeaders;

        [OutputConstructor]
        private WebAclCustomResponse(
            string? customResponseBodyKey,

            int responseCode,

            ImmutableArray<Outputs.WebAclCustomHttpHeader> responseHeaders)
        {
            CustomResponseBodyKey = customResponseBodyKey;
            ResponseCode = responseCode;
            ResponseHeaders = responseHeaders;
        }
    }
}
