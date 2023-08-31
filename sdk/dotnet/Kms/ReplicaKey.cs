// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Kms
{
    /// <summary>
    /// The AWS::KMS::ReplicaKey resource specifies a multi-region replica AWS KMS key in AWS Key Management Service (AWS KMS).
    /// </summary>
    [AwsNativeResourceType("aws-native:kms:ReplicaKey")]
    public partial class ReplicaKey : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

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
        /// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        /// </summary>
        [Output("pendingWindowInDays")]
        public Output<int?> PendingWindowInDays { get; private set; } = null!;

        /// <summary>
        /// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        /// </summary>
        [Output("primaryKeyArn")]
        public Output<string> PrimaryKeyArn { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ReplicaKeyTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ReplicaKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ReplicaKey(string name, ReplicaKeyArgs args, CustomResourceOptions? options = null)
            : base("aws-native:kms:ReplicaKey", name, args ?? new ReplicaKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ReplicaKey(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kms:ReplicaKey", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "primaryKeyArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ReplicaKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ReplicaKey Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ReplicaKey(name, id, options);
        }
    }

    public sealed class ReplicaKeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the AWS KMS key. Use a description that helps you to distinguish this AWS KMS key from others in the account, such as its intended use.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

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
        /// Specifies the number of days in the waiting period before AWS KMS deletes an AWS KMS key that has been removed from a CloudFormation stack. Enter a value between 7 and 30 days. The default value is 30 days.
        /// </summary>
        [Input("pendingWindowInDays")]
        public Input<int>? PendingWindowInDays { get; set; }

        /// <summary>
        /// Identifies the primary AWS KMS key to create a replica of. Specify the Amazon Resource Name (ARN) of the AWS KMS key. You cannot specify an alias or key ID. For help finding the ARN, see Finding the Key ID and ARN in the AWS Key Management Service Developer Guide.
        /// </summary>
        [Input("primaryKeyArn", required: true)]
        public Input<string> PrimaryKeyArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ReplicaKeyTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.ReplicaKeyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ReplicaKeyTagArgs>());
            set => _tags = value;
        }

        public ReplicaKeyArgs()
        {
        }
        public static new ReplicaKeyArgs Empty => new ReplicaKeyArgs();
    }
}
