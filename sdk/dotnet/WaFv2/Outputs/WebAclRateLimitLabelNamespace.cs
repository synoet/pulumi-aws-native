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
    /// Specifies a label namespace to use as an aggregate key for a rate-based rule.
    /// </summary>
    [OutputType]
    public sealed class WebAclRateLimitLabelNamespace
    {
        /// <summary>
        /// The namespace to use for aggregation.
        /// </summary>
        public readonly string Namespace;

        [OutputConstructor]
        private WebAclRateLimitLabelNamespace(string @namespace)
        {
            Namespace = @namespace;
        }
    }
}
