// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WAFRegional.Inputs
{

    public sealed class ByteMatchSetFieldToMatchArgs : global::Pulumi.ResourceArgs
    {
        [Input("data")]
        public Input<string>? Data { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public ByteMatchSetFieldToMatchArgs()
        {
        }
        public static new ByteMatchSetFieldToMatchArgs Empty => new ByteMatchSetFieldToMatchArgs();
    }
}
