// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ManagedBlockchain
{
    /// <summary>
    /// Definition of AWS::ManagedBlockchain::com.amazonaws.taiga.webservice.api#Accessor Resource Type
    /// </summary>
    [Obsolete(@"Accessor is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:managedblockchain:Accessor")]
    public partial class Accessor : global::Pulumi.CustomResource
    {
        [Output("accessorType")]
        public Output<Pulumi.AwsNative.ManagedBlockchain.AccessorType> AccessorType { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("billingToken")]
        public Output<string> BillingToken { get; private set; } = null!;

        [Output("creationDate")]
        public Output<string> CreationDate { get; private set; } = null!;

        [Output("status")]
        public Output<Pulumi.AwsNative.ManagedBlockchain.AccessorStatus> Status { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.AccessorTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Accessor resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Accessor(string name, AccessorArgs args, CustomResourceOptions? options = null)
            : base("aws-native:managedblockchain:Accessor", name, args ?? new AccessorArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Accessor(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:managedblockchain:Accessor", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "accessorType",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Accessor resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Accessor Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Accessor(name, id, options);
        }
    }

    public sealed class AccessorArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessorType", required: true)]
        public Input<Pulumi.AwsNative.ManagedBlockchain.AccessorType> AccessorType { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.AccessorTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.AccessorTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AccessorTagArgs>());
            set => _tags = value;
        }

        public AccessorArgs()
        {
        }
        public static new AccessorArgs Empty => new AccessorArgs();
    }
}
