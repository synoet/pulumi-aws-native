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
    /// Includes headers of a web request.
    /// </summary>
    [OutputType]
    public sealed class WebAclCookies
    {
        public readonly Outputs.WebAclCookieMatchPattern MatchPattern;
        public readonly Pulumi.AwsNative.WaFv2.WebAclMapMatchScope MatchScope;
        public readonly Pulumi.AwsNative.WaFv2.WebAclOversizeHandling OversizeHandling;

        [OutputConstructor]
        private WebAclCookies(
            Outputs.WebAclCookieMatchPattern matchPattern,

            Pulumi.AwsNative.WaFv2.WebAclMapMatchScope matchScope,

            Pulumi.AwsNative.WaFv2.WebAclOversizeHandling oversizeHandling)
        {
            MatchPattern = matchPattern;
            MatchScope = matchScope;
            OversizeHandling = oversizeHandling;
        }
    }
}
