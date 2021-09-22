// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SecretsManager
{
    /// <summary>
    /// Resource Type definition for AWS::SecretsManager::Secret
    /// </summary>
    [Obsolete(@"Secret is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:secretsmanager:Secret")]
    public partial class Secret : Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("generateSecretString")]
        public Output<Outputs.SecretGenerateSecretString?> GenerateSecretString { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("replicaRegions")]
        public Output<ImmutableArray<Outputs.SecretReplicaRegion>> ReplicaRegions { get; private set; } = null!;

        [Output("secretString")]
        public Output<string?> SecretString { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.SecretTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Secret resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Secret(string name, SecretArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:secretsmanager:Secret", name, args ?? new SecretArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Secret(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:secretsmanager:Secret", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Secret resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Secret Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Secret(name, id, options);
        }
    }

    public sealed class SecretArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("generateSecretString")]
        public Input<Inputs.SecretGenerateSecretStringArgs>? GenerateSecretString { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("replicaRegions")]
        private InputList<Inputs.SecretReplicaRegionArgs>? _replicaRegions;
        public InputList<Inputs.SecretReplicaRegionArgs> ReplicaRegions
        {
            get => _replicaRegions ?? (_replicaRegions = new InputList<Inputs.SecretReplicaRegionArgs>());
            set => _replicaRegions = value;
        }

        [Input("secretString")]
        public Input<string>? SecretString { get; set; }

        [Input("tags")]
        private InputList<Inputs.SecretTagArgs>? _tags;
        public InputList<Inputs.SecretTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.SecretTagArgs>());
            set => _tags = value;
        }

        public SecretArgs()
        {
        }
    }
}
