// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::EIPAssociation
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:EIPAssociation")]
    public partial class EIPAssociation : global::Pulumi.CustomResource
    {
        [Output("allocationId")]
        public Output<string?> AllocationId { get; private set; } = null!;

        [Output("eip")]
        public Output<string?> Eip { get; private set; } = null!;

        [Output("instanceId")]
        public Output<string?> InstanceId { get; private set; } = null!;

        [Output("networkInterfaceId")]
        public Output<string?> NetworkInterfaceId { get; private set; } = null!;

        [Output("privateIpAddress")]
        public Output<string?> PrivateIpAddress { get; private set; } = null!;


        /// <summary>
        /// Create a EIPAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public EIPAssociation(string name, EIPAssociationArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ec2:EIPAssociation", name, args ?? new EIPAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private EIPAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:EIPAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing EIPAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static EIPAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new EIPAssociation(name, id, options);
        }
    }

    public sealed class EIPAssociationArgs : global::Pulumi.ResourceArgs
    {
        [Input("allocationId")]
        public Input<string>? AllocationId { get; set; }

        [Input("eip")]
        public Input<string>? Eip { get; set; }

        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        [Input("privateIpAddress")]
        public Input<string>? PrivateIpAddress { get; set; }

        public EIPAssociationArgs()
        {
        }
        public static new EIPAssociationArgs Empty => new EIPAssociationArgs();
    }
}
