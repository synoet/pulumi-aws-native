// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NeptuneGraph
{
    /// <summary>
    /// The AWS::NeptuneGraph::PrivateGraphEndpoint resource creates an Amazon NeptuneGraph PrivateGraphEndpoint.
    /// </summary>
    [AwsNativeResourceType("aws-native:neptunegraph:PrivateGraphEndpoint")]
    public partial class PrivateGraphEndpoint : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The auto-generated Graph Id assigned by the service.
        /// </summary>
        [Output("graphIdentifier")]
        public Output<string> GraphIdentifier { get; private set; } = null!;

        /// <summary>
        /// PrivateGraphEndpoint resource identifier generated by concatenating the associated GraphIdentifier and VpcId with an underscore separator.
        /// 
        ///  For example, if GraphIdentifier is `g-12a3bcdef4` and VpcId is `vpc-0a12bc34567de8f90`, the generated PrivateGraphEndpointIdentifier will be `g-12a3bcdef4_vpc-0a12bc34567de8f90`
        /// </summary>
        [Output("privateGraphEndpointIdentifier")]
        public Output<string> PrivateGraphEndpointIdentifier { get; private set; } = null!;

        /// <summary>
        /// The security group Ids associated with the VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// The subnet Ids associated with the VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// VPC endpoint that provides a private connection between the Graph and specified VPC.
        /// </summary>
        [Output("vpcEndpointId")]
        public Output<string> VpcEndpointId { get; private set; } = null!;

        /// <summary>
        /// The VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a PrivateGraphEndpoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PrivateGraphEndpoint(string name, PrivateGraphEndpointArgs args, CustomResourceOptions? options = null)
            : base("aws-native:neptunegraph:PrivateGraphEndpoint", name, args ?? new PrivateGraphEndpointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PrivateGraphEndpoint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:neptunegraph:PrivateGraphEndpoint", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "graphIdentifier",
                    "securityGroupIds[*]",
                    "subnetIds[*]",
                    "vpcId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PrivateGraphEndpoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PrivateGraphEndpoint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PrivateGraphEndpoint(name, id, options);
        }
    }

    public sealed class PrivateGraphEndpointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The auto-generated Graph Id assigned by the service.
        /// </summary>
        [Input("graphIdentifier", required: true)]
        public Input<string> GraphIdentifier { get; set; } = null!;

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// The security group Ids associated with the VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// The subnet Ids associated with the VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        /// <summary>
        /// The VPC where you want the private graph endpoint to be created, ie, the graph will be reachable from within the VPC.
        /// </summary>
        [Input("vpcId", required: true)]
        public Input<string> VpcId { get; set; } = null!;

        public PrivateGraphEndpointArgs()
        {
        }
        public static new PrivateGraphEndpointArgs Empty => new PrivateGraphEndpointArgs();
    }
}
