// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT.Inputs
{

    public sealed class TopicRuleHttpAuthorizationArgs : global::Pulumi.ResourceArgs
    {
        [Input("sigv4")]
        public Input<Inputs.TopicRuleSigV4AuthorizationArgs>? Sigv4 { get; set; }

        public TopicRuleHttpAuthorizationArgs()
        {
        }
        public static new TopicRuleHttpAuthorizationArgs Empty => new TopicRuleHttpAuthorizationArgs();
    }
}
