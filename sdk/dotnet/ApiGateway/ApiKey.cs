// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ApiGateway
{
    /// <summary>
    /// Resource Type definition for AWS::ApiGateway::ApiKey
    /// </summary>
    [AwsNativeResourceType("aws-native:apigateway:ApiKey")]
    public partial class ApiKey : global::Pulumi.CustomResource
    {
        /// <summary>
        /// A Unique Key ID which identifies the API Key. Generated by the Create API and returned by the Read and List APIs 
        /// </summary>
        [Output("apiKeyId")]
        public Output<string> ApiKeyId { get; private set; } = null!;

        /// <summary>
        /// An AWS Marketplace customer identifier to use when integrating with the AWS SaaS Marketplace.
        /// </summary>
        [Output("customerId")]
        public Output<string?> CustomerId { get; private set; } = null!;

        /// <summary>
        /// A description of the purpose of the API key.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the API key can be used by clients.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// Specifies whether the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.
        /// </summary>
        [Output("generateDistinctId")]
        public Output<bool?> GenerateDistinctId { get; private set; } = null!;

        /// <summary>
        /// A name for the API key. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the API key name.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// A list of stages to associate with this API key.
        /// </summary>
        [Output("stageKeys")]
        public Output<ImmutableArray<Outputs.ApiKeyStageKey>> StageKeys { get; private set; } = null!;

        /// <summary>
        /// An array of arbitrary tags (key-value pairs) to associate with the API key.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ApiKeyTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The value of the API key. Must be at least 20 characters long.
        /// </summary>
        [Output("value")]
        public Output<string?> Value { get; private set; } = null!;


        /// <summary>
        /// Create a ApiKey resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApiKey(string name, ApiKeyArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:ApiKey", name, args ?? new ApiKeyArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApiKey(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:apigateway:ApiKey", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "generateDistinctId",
                    "name",
                    "value",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ApiKey resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApiKey Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ApiKey(name, id, options);
        }
    }

    public sealed class ApiKeyArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// An AWS Marketplace customer identifier to use when integrating with the AWS SaaS Marketplace.
        /// </summary>
        [Input("customerId")]
        public Input<string>? CustomerId { get; set; }

        /// <summary>
        /// A description of the purpose of the API key.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Indicates whether the API key can be used by clients.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        /// <summary>
        /// Specifies whether the key identifier is distinct from the created API key value. This parameter is deprecated and should not be used.
        /// </summary>
        [Input("generateDistinctId")]
        public Input<bool>? GenerateDistinctId { get; set; }

        /// <summary>
        /// A name for the API key. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the API key name.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("stageKeys")]
        private InputList<Inputs.ApiKeyStageKeyArgs>? _stageKeys;

        /// <summary>
        /// A list of stages to associate with this API key.
        /// </summary>
        public InputList<Inputs.ApiKeyStageKeyArgs> StageKeys
        {
            get => _stageKeys ?? (_stageKeys = new InputList<Inputs.ApiKeyStageKeyArgs>());
            set => _stageKeys = value;
        }

        [Input("tags")]
        private InputList<Inputs.ApiKeyTagArgs>? _tags;

        /// <summary>
        /// An array of arbitrary tags (key-value pairs) to associate with the API key.
        /// </summary>
        public InputList<Inputs.ApiKeyTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ApiKeyTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The value of the API key. Must be at least 20 characters long.
        /// </summary>
        [Input("value")]
        public Input<string>? Value { get; set; }

        public ApiKeyArgs()
        {
        }
        public static new ApiKeyArgs Empty => new ApiKeyArgs();
    }
}
