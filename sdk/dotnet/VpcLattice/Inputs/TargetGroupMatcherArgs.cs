// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.VpcLattice.Inputs
{

    public sealed class TargetGroupMatcherArgs : global::Pulumi.ResourceArgs
    {
        [Input("httpCode", required: true)]
        public Input<string> HttpCode { get; set; } = null!;

        public TargetGroupMatcherArgs()
        {
        }
        public static new TargetGroupMatcherArgs Empty => new TargetGroupMatcherArgs();
    }
}
