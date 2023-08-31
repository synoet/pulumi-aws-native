// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh
{
    /// <summary>
    /// Resource Type definition for AWS::AppMesh::Route
    /// </summary>
    [Obsolete(@"Route is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:appmesh:Route")]
    public partial class Route : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("meshName")]
        public Output<string> MeshName { get; private set; } = null!;

        [Output("meshOwner")]
        public Output<string?> MeshOwner { get; private set; } = null!;

        [Output("resourceOwner")]
        public Output<string> ResourceOwner { get; private set; } = null!;

        [Output("routeName")]
        public Output<string?> RouteName { get; private set; } = null!;

        [Output("spec")]
        public Output<Outputs.RouteSpec> Spec { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.RouteTag>> Tags { get; private set; } = null!;

        [Output("uid")]
        public Output<string> Uid { get; private set; } = null!;

        [Output("virtualRouterName")]
        public Output<string> VirtualRouterName { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:appmesh:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:appmesh:Route", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "meshName",
                    "meshOwner",
                    "routeName",
                    "virtualRouterName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Route(name, id, options);
        }
    }

    public sealed class RouteArgs : global::Pulumi.ResourceArgs
    {
        [Input("meshName", required: true)]
        public Input<string> MeshName { get; set; } = null!;

        [Input("meshOwner")]
        public Input<string>? MeshOwner { get; set; }

        [Input("routeName")]
        public Input<string>? RouteName { get; set; }

        [Input("spec", required: true)]
        public Input<Inputs.RouteSpecArgs> Spec { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.RouteTagArgs>? _tags;
        public InputList<Inputs.RouteTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.RouteTagArgs>());
            set => _tags = value;
        }

        [Input("virtualRouterName", required: true)]
        public Input<string> VirtualRouterName { get; set; } = null!;

        public RouteArgs()
        {
        }
        public static new RouteArgs Empty => new RouteArgs();
    }
}
