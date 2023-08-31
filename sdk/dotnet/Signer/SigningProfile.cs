// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Signer
{
    /// <summary>
    /// A signing profile is a signing template that can be used to carry out a pre-defined signing job.
    /// </summary>
    [AwsNativeResourceType("aws-native:signer:SigningProfile")]
    public partial class SigningProfile : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the specified signing profile.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The ID of the target signing platform.
        /// </summary>
        [Output("platformId")]
        public Output<Pulumi.AwsNative.Signer.SigningProfilePlatformId> PlatformId { get; private set; } = null!;

        /// <summary>
        /// A name for the signing profile. AWS CloudFormation generates a unique physical ID and uses that ID for the signing profile name. 
        /// </summary>
        [Output("profileName")]
        public Output<string> ProfileName { get; private set; } = null!;

        /// <summary>
        /// A version for the signing profile. AWS Signer generates a unique version for each profile of the same profile name.
        /// </summary>
        [Output("profileVersion")]
        public Output<string> ProfileVersion { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the specified signing profile version.
        /// </summary>
        [Output("profileVersionArn")]
        public Output<string> ProfileVersionArn { get; private set; } = null!;

        /// <summary>
        /// Signature validity period of the profile.
        /// </summary>
        [Output("signatureValidityPeriod")]
        public Output<Outputs.SigningProfileSignatureValidityPeriod?> SignatureValidityPeriod { get; private set; } = null!;

        /// <summary>
        /// A list of tags associated with the signing profile.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.SigningProfileTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SigningProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SigningProfile(string name, SigningProfileArgs args, CustomResourceOptions? options = null)
            : base("aws-native:signer:SigningProfile", name, args ?? new SigningProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SigningProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:signer:SigningProfile", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "platformId",
                    "signatureValidityPeriod",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SigningProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SigningProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SigningProfile(name, id, options);
        }
    }

    public sealed class SigningProfileArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the target signing platform.
        /// </summary>
        [Input("platformId", required: true)]
        public Input<Pulumi.AwsNative.Signer.SigningProfilePlatformId> PlatformId { get; set; } = null!;

        /// <summary>
        /// Signature validity period of the profile.
        /// </summary>
        [Input("signatureValidityPeriod")]
        public Input<Inputs.SigningProfileSignatureValidityPeriodArgs>? SignatureValidityPeriod { get; set; }

        [Input("tags")]
        private InputList<Inputs.SigningProfileTagArgs>? _tags;

        /// <summary>
        /// A list of tags associated with the signing profile.
        /// </summary>
        public InputList<Inputs.SigningProfileTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SigningProfileTagArgs>());
            set => _tags = value;
        }

        public SigningProfileArgs()
        {
        }
        public static new SigningProfileArgs Empty => new SigningProfileArgs();
    }
}
