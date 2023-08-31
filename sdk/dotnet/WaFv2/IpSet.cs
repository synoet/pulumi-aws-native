// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.WaFv2
{
    /// <summary>
    /// Contains a list of IP addresses. This can be either IPV4 or IPV6. The list will be mutually
    /// </summary>
    [AwsNativeResourceType("aws-native:wafv2:IpSet")]
    public partial class IpSet : global::Pulumi.CustomResource
    {
        /// <summary>
        /// List of IPAddresses.
        /// </summary>
        [Output("addresses")]
        public Output<ImmutableArray<string>> Addresses { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("ipAddressVersion")]
        public Output<Pulumi.AwsNative.WaFv2.IpSetIpAddressVersion> IpAddressVersion { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("scope")]
        public Output<Pulumi.AwsNative.WaFv2.IpSetScope> Scope { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.IpSetTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a IpSet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public IpSet(string name, IpSetArgs args, CustomResourceOptions? options = null)
            : base("aws-native:wafv2:IpSet", name, args ?? new IpSetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private IpSet(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:wafv2:IpSet", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                    "scope",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing IpSet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static IpSet Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new IpSet(name, id, options);
        }
    }

    public sealed class IpSetArgs : global::Pulumi.ResourceArgs
    {
        [Input("addresses", required: true)]
        private InputList<string>? _addresses;

        /// <summary>
        /// List of IPAddresses.
        /// </summary>
        public InputList<string> Addresses
        {
            get => _addresses ?? (_addresses = new InputList<string>());
            set => _addresses = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ipAddressVersion", required: true)]
        public Input<Pulumi.AwsNative.WaFv2.IpSetIpAddressVersion> IpAddressVersion { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("scope", required: true)]
        public Input<Pulumi.AwsNative.WaFv2.IpSetScope> Scope { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.IpSetTagArgs>? _tags;
        public InputList<Inputs.IpSetTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.IpSetTagArgs>());
            set => _tags = value;
        }

        public IpSetArgs()
        {
        }
        public static new IpSetArgs Empty => new IpSetArgs();
    }
}
