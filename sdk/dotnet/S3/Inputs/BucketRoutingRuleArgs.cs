// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Inputs
{

    /// <summary>
    /// Specifies the redirect behavior and when a redirect is applied.
    /// </summary>
    public sealed class BucketRoutingRuleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Container for redirect information. You can redirect requests to another host, to another page, or with another protocol. In the event of an error, you can specify a different error code to return.
        /// </summary>
        [Input("redirectRule", required: true)]
        public Input<Inputs.BucketRedirectRuleArgs> RedirectRule { get; set; } = null!;

        [Input("routingRuleCondition")]
        public Input<Inputs.BucketRoutingRuleConditionArgs>? RoutingRuleCondition { get; set; }

        public BucketRoutingRuleArgs()
        {
        }
        public static new BucketRoutingRuleArgs Empty => new BucketRoutingRuleArgs();
    }
}
