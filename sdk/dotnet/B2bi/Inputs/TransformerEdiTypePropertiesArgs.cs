// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.B2bi.Inputs
{

    public sealed class TransformerEdiTypePropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("x12Details", required: true)]
        public Input<Inputs.TransformerX12DetailsArgs> X12Details { get; set; } = null!;

        public TransformerEdiTypePropertiesArgs()
        {
        }
        public static new TransformerEdiTypePropertiesArgs Empty => new TransformerEdiTypePropertiesArgs();
    }
}
