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
    /// The pattern to look for in the request cookies.
    /// </summary>
    [OutputType]
    public sealed class WebAclCookieMatchPattern
    {
        /// <summary>
        /// Inspect all parts of the web request cookies.
        /// </summary>
        public readonly object? All;
        public readonly ImmutableArray<string> ExcludedCookies;
        public readonly ImmutableArray<string> IncludedCookies;

        [OutputConstructor]
        private WebAclCookieMatchPattern(
            object? all,

            ImmutableArray<string> excludedCookies,

            ImmutableArray<string> includedCookies)
        {
            All = all;
            ExcludedCookies = excludedCookies;
            IncludedCookies = includedCookies;
        }
    }
}
