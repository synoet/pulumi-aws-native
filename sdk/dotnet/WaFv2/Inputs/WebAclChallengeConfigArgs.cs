// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2.Inputs
{

    public sealed class WebAclChallengeConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("immunityTimeProperty")]
        public Input<Inputs.WebAclImmunityTimePropertyArgs>? ImmunityTimeProperty { get; set; }

        public WebAclChallengeConfigArgs()
        {
        }
        public static new WebAclChallengeConfigArgs Empty => new WebAclChallengeConfigArgs();
    }
}
