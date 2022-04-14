// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KMS
{
    /// <summary>
    /// The AWS::KMS::Key resource specifies an AWS KMS key in AWS Key Management Service (AWS KMS). Authorized users can use the AWS KMS key to encrypt and decrypt small amounts of data (up to 4096 bytes), but they are more commonly used to generate data keys. You can also use AWS KMS keys to encrypt data stored in AWS services that are integrated with AWS KMS or within their applications.
    /// </summary>
    [AwsNativeResourceType("aws-native:kms:Key")]
    public partial class Key : Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Enables automatic rotation of the key material for the specified AWS KMS key. By default, automation key rotation is not enabled.
        /// </summary>
        [Output("enableKeyRotation")]
        public Output<bool?> EnableKeyRotation { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("keyId")]
        public Output<string> KeyId { get; private set; } = null!;

        /// <summary>
        /// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
        /// </summary>
        [Output("keyPolicy")]
        public Output<object> KeyPolicy { get; private set; } = null!;

        /// <summary>
        /// Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
        /// </summary>
        [Output("keySpec")]
        public Output<Pulumi.AwsNative.KMS.KeySpec?> KeySpec { get; private set; } = null!;

        /// <summary>
        /// Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
        /// </summary>
        [Output("keyUsage")]
        public Output<Pulumi.AwsNative.KMS.KeyUsage?> KeyUsage { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the AWS KMS key should be Multi-Region. You can't change the MultiRegion value after the AWS KMS key is created.
        /// </summary>
        [Output("multiRegion")]
        public Output<bool?> MultiRegion { get; private set; } = null!;

        /// <summary>
        /// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        /// </summary>
        [Output("pendingWindowInDays")]
        public Output<int?> PendingWindowInDays { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.KeyTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Key resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Key(string name, KeyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:kms:Key", name, args ?? new KeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Key(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kms:Key", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Key resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Key Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Key(name, id, options);
        }
    }

    public sealed class KeyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Enables automatic rotation of the key material for the specified AWS KMS key. By default, automation key rotation is not enabled.
        /// </summary>
        [Input("enableKeyRotation")]
        public Input<bool>? EnableKeyRotation { get; set; }

        /// <summary>
        /// Specifies whether the AWS KMS key is enabled. Disabled AWS KMS keys cannot be used in cryptographic operations.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// The key policy that authorizes use of the AWS KMS key. The key policy must observe the following rules.
        /// </summary>
        [Input("keyPolicy", required: true)]
        public Input<object> KeyPolicy { get; set; } = null!;

        /// <summary>
        /// Specifies the type of AWS KMS key to create. The default value is SYMMETRIC_DEFAULT. This property is required only for asymmetric AWS KMS keys. You can't change the KeySpec value after the AWS KMS key is created.
        /// </summary>
        [Input("keySpec")]
        public Input<Pulumi.AwsNative.KMS.KeySpec>? KeySpec { get; set; }

        /// <summary>
        /// Determines the cryptographic operations for which you can use the AWS KMS key. The default value is ENCRYPT_DECRYPT. This property is required only for asymmetric AWS KMS keys. You can't change the KeyUsage value after the AWS KMS key is created.
        /// </summary>
        [Input("keyUsage")]
        public Input<Pulumi.AwsNative.KMS.KeyUsage>? KeyUsage { get; set; }

        /// <summary>
        /// Specifies whether the AWS KMS key should be Multi-Region. You can't change the MultiRegion value after the AWS KMS key is created.
        /// </summary>
        [Input("multiRegion")]
        public Input<bool>? MultiRegion { get; set; }

        /// <summary>
        /// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        /// </summary>
        [Input("pendingWindowInDays")]
        public Input<int>? PendingWindowInDays { get; set; }

        [Input("tags")]
        private InputList<Inputs.KeyTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.KeyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.KeyTagArgs>());
            set => _tags = value;
        }

        public KeyArgs()
        {
        }
    }
}
