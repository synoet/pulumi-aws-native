// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    public sealed class Ec2FleetTagSpecificationArgs : global::Pulumi.ResourceArgs
    {
        [Input("resourceType")]
        public Input<Pulumi.AwsNative.Ec2.Ec2FleetTagSpecificationResourceType>? ResourceType { get; set; }

        [Input("tags")]
        private InputList<Inputs.Ec2FleetTagArgs>? _tags;
        public InputList<Inputs.Ec2FleetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.Ec2FleetTagArgs>());
            set => _tags = value;
        }

        public Ec2FleetTagSpecificationArgs()
        {
        }
        public static new Ec2FleetTagSpecificationArgs Empty => new Ec2FleetTagSpecificationArgs();
    }
}
