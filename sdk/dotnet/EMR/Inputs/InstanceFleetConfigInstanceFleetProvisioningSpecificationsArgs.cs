// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Inputs
{

    public sealed class InstanceFleetConfigInstanceFleetProvisioningSpecificationsArgs : global::Pulumi.ResourceArgs
    {
        [Input("onDemandSpecification")]
        public Input<Inputs.InstanceFleetConfigOnDemandProvisioningSpecificationArgs>? OnDemandSpecification { get; set; }

        [Input("spotSpecification")]
        public Input<Inputs.InstanceFleetConfigSpotProvisioningSpecificationArgs>? SpotSpecification { get; set; }

        public InstanceFleetConfigInstanceFleetProvisioningSpecificationsArgs()
        {
        }
        public static new InstanceFleetConfigInstanceFleetProvisioningSpecificationsArgs Empty => new InstanceFleetConfigInstanceFleetProvisioningSpecificationsArgs();
    }
}
