// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFv2.Inputs
{

    /// <summary>
    /// The body of a web request. This immediately follows the request headers.
    /// </summary>
    public sealed class RuleGroupBodyArgs : global::Pulumi.ResourceArgs
    {
        [Input("oversizeHandling")]
        public Input<Pulumi.AwsNative.WAFv2.RuleGroupOversizeHandling>? OversizeHandling { get; set; }

        public RuleGroupBodyArgs()
        {
        }
        public static new RuleGroupBodyArgs Empty => new RuleGroupBodyArgs();
    }
}
