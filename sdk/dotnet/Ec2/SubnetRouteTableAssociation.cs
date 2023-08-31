// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::SubnetRouteTableAssociation
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:SubnetRouteTableAssociation")]
    public partial class SubnetRouteTableAssociation : global::Pulumi.CustomResource
    {
        [Output("routeTableId")]
        public Output<string> RouteTableId { get; private set; } = null!;

        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a SubnetRouteTableAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SubnetRouteTableAssociation(string name, SubnetRouteTableAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:SubnetRouteTableAssociation", name, args ?? new SubnetRouteTableAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SubnetRouteTableAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:SubnetRouteTableAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "routeTableId",
                    "subnetId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SubnetRouteTableAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SubnetRouteTableAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SubnetRouteTableAssociation(name, id, options);
        }
    }

    public sealed class SubnetRouteTableAssociationArgs : global::Pulumi.ResourceArgs
    {
        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        public SubnetRouteTableAssociationArgs()
        {
        }
        public static new SubnetRouteTableAssociationArgs Empty => new SubnetRouteTableAssociationArgs();
    }
}
