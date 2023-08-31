// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Transfer
{
    /// <summary>
    /// Resource Type definition for AWS::Transfer::Agreement
    /// </summary>
    [AwsNativeResourceType("aws-native:transfer:Agreement")]
    public partial class Agreement : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Specifies the access role for the agreement.
        /// </summary>
        [Output("accessRole")]
        public Output<string> AccessRole { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the agreement.
        /// </summary>
        [Output("agreementId")]
        public Output<string> AgreementId { get; private set; } = null!;

        /// <summary>
        /// Specifies the unique Amazon Resource Name (ARN) for the agreement.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// Specifies the base directory for the agreement.
        /// </summary>
        [Output("baseDirectory")]
        public Output<string> BaseDirectory { get; private set; } = null!;

        /// <summary>
        /// A textual description for the agreement.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the local profile.
        /// </summary>
        [Output("localProfileId")]
        public Output<string> LocalProfileId { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the partner profile.
        /// </summary>
        [Output("partnerProfileId")]
        public Output<string> PartnerProfileId { get; private set; } = null!;

        /// <summary>
        /// A unique identifier for the server.
        /// </summary>
        [Output("serverId")]
        public Output<string> ServerId { get; private set; } = null!;

        /// <summary>
        /// Specifies the status of the agreement.
        /// </summary>
        [Output("status")]
        public Output<Pulumi.AwsNative.Transfer.AgreementStatus?> Status { get; private set; } = null!;

        /// <summary>
        /// Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.AgreementTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Agreement resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Agreement(string name, AgreementArgs args, CustomResourceOptions? options = null)
            : base("aws-native:transfer:Agreement", name, args ?? new AgreementArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Agreement(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:transfer:Agreement", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "serverId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Agreement resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Agreement Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Agreement(name, id, options);
        }
    }

    public sealed class AgreementArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specifies the access role for the agreement.
        /// </summary>
        [Input("accessRole", required: true)]
        public Input<string> AccessRole { get; set; } = null!;

        /// <summary>
        /// Specifies the base directory for the agreement.
        /// </summary>
        [Input("baseDirectory", required: true)]
        public Input<string> BaseDirectory { get; set; } = null!;

        /// <summary>
        /// A textual description for the agreement.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A unique identifier for the local profile.
        /// </summary>
        [Input("localProfileId", required: true)]
        public Input<string> LocalProfileId { get; set; } = null!;

        /// <summary>
        /// A unique identifier for the partner profile.
        /// </summary>
        [Input("partnerProfileId", required: true)]
        public Input<string> PartnerProfileId { get; set; } = null!;

        /// <summary>
        /// A unique identifier for the server.
        /// </summary>
        [Input("serverId", required: true)]
        public Input<string> ServerId { get; set; } = null!;

        /// <summary>
        /// Specifies the status of the agreement.
        /// </summary>
        [Input("status")]
        public Input<Pulumi.AwsNative.Transfer.AgreementStatus>? Status { get; set; }

        [Input("tags")]
        private InputList<Inputs.AgreementTagArgs>? _tags;

        /// <summary>
        /// Key-value pairs that can be used to group and search for agreements. Tags are metadata attached to agreements for any purpose.
        /// </summary>
        public InputList<Inputs.AgreementTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AgreementTagArgs>());
            set => _tags = value;
        }

        public AgreementArgs()
        {
        }
        public static new AgreementArgs Empty => new AgreementArgs();
    }
}
