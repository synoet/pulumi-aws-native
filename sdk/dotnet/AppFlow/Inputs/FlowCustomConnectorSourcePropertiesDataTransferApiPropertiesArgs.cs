// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.AppFlow.FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesType> Type { get; set; } = null!;

        public FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesArgs()
        {
        }
        public static new FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesArgs Empty => new FlowCustomConnectorSourcePropertiesDataTransferApiPropertiesArgs();
    }
}
