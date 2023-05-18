// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.FMS
{
    /// <summary>
    /// Creates an AWS Firewall Manager resource set.
    /// </summary>
    [AwsNativeResourceType("aws-native:fms:ResourceSet")]
    public partial class ResourceSet : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("resourceTypeList")]
        public Output<ImmutableArray<string>> ResourceTypeList { get; private set; } = null!;

        [Output("resources")]
        public Output<ImmutableArray<string>> Resources { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ResourceSetTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ResourceSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ResourceSet(string name, ResourceSetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:fms:ResourceSet", name, args ?? new ResourceSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ResourceSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:fms:ResourceSet", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ResourceSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ResourceSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ResourceSet(name, id, options);
        }
    }

    public sealed class ResourceSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resourceTypeList", required: true)]
        private InputList<string>? _resourceTypeList;
        public InputList<string> ResourceTypeList
        {
            get => _resourceTypeList ?? (_resourceTypeList = new InputList<string>());
            set => _resourceTypeList = value;
        }

        [Input("resources")]
        private InputList<string>? _resources;
        public InputList<string> Resources
        {
            get => _resources ?? (_resources = new InputList<string>());
            set => _resources = value;
        }

        [Input("tags")]
        private InputList<Inputs.ResourceSetTagArgs>? _tags;
        public InputList<Inputs.ResourceSetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ResourceSetTagArgs>());
            set => _tags = value;
        }

        public ResourceSetArgs()
        {
        }
        public static new ResourceSetArgs Empty => new ResourceSetArgs();
    }
}
