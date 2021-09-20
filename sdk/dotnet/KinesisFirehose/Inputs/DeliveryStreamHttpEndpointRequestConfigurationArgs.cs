// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamHttpEndpointRequestConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("commonAttributes")]
        private InputList<Inputs.DeliveryStreamHttpEndpointCommonAttributeArgs>? _commonAttributes;
        public InputList<Inputs.DeliveryStreamHttpEndpointCommonAttributeArgs> CommonAttributes
        {
            get => _commonAttributes ?? (_commonAttributes = new InputList<Inputs.DeliveryStreamHttpEndpointCommonAttributeArgs>());
            set => _commonAttributes = value;
        }

        [Input("contentEncoding")]
        public Input<Pulumi.AwsNative.KinesisFirehose.DeliveryStreamHttpEndpointRequestConfigurationContentEncoding>? ContentEncoding { get; set; }

        public DeliveryStreamHttpEndpointRequestConfigurationArgs()
        {
        }
    }
}
